# claude-skills · Battle-tested Claude Code skills

[中文](README.md) | **English**

Every skill here was forged in real work — used repeatedly, refined through failures, and revised across multiple versions before being crystallized into methodology. Install them into Claude Code, say a trigger phrase, and Claude works by these playbooks.

> Note: the skill bodies are written in Chinese. **This does not affect usage** — Claude reads Chinese natively, and the workflows apply to projects in any language. This page tells you what each skill does; the frontmatter includes English triggers so you can invoke them in English.

## Catalog

| Skill | What it does | When to reach for it |
|---|---|---|
| [plain-write](plain-write/SKILL.md) | De-AI-ify writing so a real human can read it in one pass. Two opposite modes: documents get *more* explanation (cold-read by a stranger, forward-reference check); messages to people you know get *less* (cut parenthetical glosses, scaffolding, customer-service endings). Includes a structural-slop checklist and a 5-dimension pre-send score. | "This sounds so AI", "humanize this", "make it sound like a person wrote it" |
| [code-renew](code-renew/SKILL.md) | Renovation surgery for projects that "run but are full of problems". Backup first → three independent diagnostic tracks (line-by-line agent review + browser screenshot inspection + independent recomputation of key numbers) → staged construction with per-stage commits and real-machine verification. Never patch blindly. | "Full overhaul", "code health check", "I keep fixing this and it keeps breaking" |
| [oss-research](oss-research/SKILL.md) | Safely research any open-source project: profile the author, audit install hooks **before** installing (`--ignore-scripts`), grep for dangerous patterns, run it sandboxed (localhost-only, no real keys), verify at least one core mechanism hands-on, deliver a fixed-structure evidence-based report. | "Research this GitHub repo for me", "is this project worth learning from / safe?" |
| [oss-publish](oss-publish/SKILL.md) | Open-source a project safely and presentably: rewrite a de-personalized public version → pre-publish sensitive-info audit down to zero hits → fresh git history with noreply identity → post-publish re-scan from the remote. Core idea: a push is permanent — audit *before* publishing. | "Help me open-source this", "publish this to GitHub" |
| [vault-audit](vault-audit/SKILL.md) | Full-scale Obsidian vault inspection: structure / links / content / consistency, with a red-yellow-green graded report and confirm-before-fix repairs. Includes eight hard-won pitfalls from real audits. | "My vault is a mess", "do a full knowledge-base checkup" |
| [obsidian-link-guard](obsidian-link-guard/SKILL.md) | After renames/migrations: fix broken wikilinks, clean 0-byte ghost files, leave compatibility redirect pages, run a full-vault broken-link audit. Ships with two scripts (`audit_wikilinks.py`, `find_zero_byte_files.sh`) — the audit exits non-zero on findings, so it plugs into CI. | "All my links broke after renaming", "red links everywhere" |

The skills chain together: `oss-research` reads a project → `code-renew` renovates it → `oss-publish` ships your result → `plain-write` polishes anything meant for human eyes.

## Install (Claude Code)

```bash
git clone https://github.com/NovaKepler513/claude-skills.git
# install all (user-level, available in every project)
cp -r claude-skills/{plain-write,code-renew,oss-research,oss-publish,vault-audit,obsidian-link-guard} ~/.claude/skills/
# or just the ones you want
cp -r claude-skills/plain-write ~/.claude/skills/
```

Then just talk to Claude — "research this GitHub repo for me" or "humanize this email" will trigger the matching skill. You can also invoke explicitly: "use oss-research on X".

Not using Claude Code? Paste any `SKILL.md` into any AI assistant as an operating spec.

## Shared principles

- **Running it is the proof**: reading code isn't research, an untested fix isn't a fix, an unverified publish isn't done.
- **Claims carry evidence**: critiques cite file:line, numbers are cross-checked by independent implementation — "looks good to me" doesn't count.
- **Safety first**: check install hooks before installing strangers' code; audit to zero hits before publishing; a push is forever.
- **Look before you cut**: diagnosis is separated from treatment; confirm before repairing; never patch blindly.

## Credits

`plain-write`'s structural-slop taxonomy and 5-dimension scoring draw on several open-source anti-slop / humanizer projects — see the credits list at the end of that skill.

## License

MIT
