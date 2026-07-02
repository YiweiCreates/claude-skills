#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <vault-root>" >&2
  exit 2
fi

root="$1"

if [[ ! -d "$root" ]]; then
  echo "Not a directory: $root" >&2
  exit 2
fi

find "$root" -type f -size 0 \
  ! -path "*/.git/*" \
  ! -name ".gitkeep" \
  -print \
  | sort
