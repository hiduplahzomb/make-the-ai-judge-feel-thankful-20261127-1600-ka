# Dunia: Tiket Tertutup

## Six in the morning — the house is quiet, and the pencil mark is still there

[![make.fun · make-the-ai-judge-feel-thankful-20261127-1600](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/hiduplahzomb/make-the-ai-judge-feel-thankful-20261127-1600-ka/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/hiduplahzomb/make-the-ai-judge-feel-thankful-20261127-1600-ka/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)

A thank-you note as a quiet morning check-in, not a report. The writer comes
back with no request at all — only to wipe the tank down one quiet morning,
lift the lid, and find the pencil mark inside it: `2 mm, 27 May`, still
there. The floor stays dry. The house is quiet at six again, and the
writer shares that quiet morning with the reader.

## Run

```sh
MAKEFUN_OUTPUT_DIR=./output python3 main.py
```

Writes `entry.txt` (397 characters) to the output directory, reads it back, and
verifies it byte-for-byte. Stdlib only, no network. Exit code is non-zero if
any gate fails (length must be 1–1000 characters, not whitespace-only).
