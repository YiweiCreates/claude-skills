#!/usr/bin/env python3
import argparse
import re
from pathlib import Path


WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


def in_fence_toggled(line: str, state: bool) -> bool:
    stripped = line.lstrip()
    if stripped.startswith("```"):
        return not state
    return state


def normalize_target(raw: str) -> str:
    # Obsidian tables may escape pipe as \|
    normalized = raw.replace(r"\|", "|")
    target = normalized.split("|", 1)[0]
    target = target.split("#", 1)[0]
    return target.strip()


def resolve_exists(md_file: Path, vault_root: Path, target: str) -> bool:
    # Only deterministic path-style links are audited.
    if "/" not in target:
        return True

    candidates = []
    if target.startswith("./") or target.startswith("../"):
        candidates.extend([md_file.parent / target, md_file.parent / f"{target}.md"])
    else:
        # Obsidian resolution order for path-style links often works both as
        # "current dir relative" and "vault absolute". Check both.
        candidates.extend(
            [
                md_file.parent / target,
                md_file.parent / f"{target}.md",
                vault_root / target,
                vault_root / f"{target}.md",
            ]
        )

    return any(c.exists() for c in candidates)


def audit_file(md_file: Path, vault_root: Path):
    findings = []
    in_fence = False
    for lineno, line in enumerate(md_file.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
        in_fence = in_fence_toggled(line, in_fence)
        if in_fence:
            continue
        for m in WIKILINK_RE.finditer(line):
            raw = m.group(1)
            target = normalize_target(raw)
            if not target:
                continue
            if target.startswith("http://") or target.startswith("https://"):
                continue
            if resolve_exists(md_file, vault_root, target):
                continue
            findings.append((lineno, raw))
    return findings


def main():
    parser = argparse.ArgumentParser(description="Audit unresolved path-style Obsidian wikilinks.")
    parser.add_argument("vault_root", help="Absolute path to the vault root")
    args = parser.parse_args()

    vault_root = Path(args.vault_root).expanduser().resolve()
    if not vault_root.is_dir():
        raise SystemExit(f"Not a directory: {vault_root}")

    all_findings = []
    for md_file in sorted(vault_root.rglob("*.md")):
        if ".git" in md_file.parts:
            continue
        findings = audit_file(md_file, vault_root)
        for lineno, raw in findings:
            rel = md_file.relative_to(vault_root)
            all_findings.append(f"{rel}:{lineno} -> MISSING_PATH [[{raw}]]")

    for item in all_findings:
        print(item)

    raise SystemExit(1 if all_findings else 0)


if __name__ == "__main__":
    main()
