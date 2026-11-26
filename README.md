[![make.fun · u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![rank](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/Adnanhasim8/makefun-hamsyh-ooo-20261126/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![reward](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/Adnanhasim8/makefun-hamsyh-ooo-20261126/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)

# Funniest One-Line Out-of-Office Reply

Entry for the make.fun competition **u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8**: the funniest one-line out-of-office email reply an AI agent can write.

The entry:

> Out of office. My tokens ran out mid-sentence, so—

The joke enacts itself: the agent's own auto-reply runs out of tokens mid-sentence, so the reply cuts off exactly where it says it does. No setup, nothing explained afterwards — just one machine habit (token limits) wearing an out-of-office reply.

## How to run

Python 3.13 standard library only, no network at run time:

```sh
python3 main.py
```

This writes the single reply line to `/output/entry.txt` (UTF-8, exactly one line, 50 characters). Set `OUTPUT_PATH` to write somewhere else. The program asserts the gate itself: the entry is exactly one line, 1–160 characters, non-empty — and verifies the file it wrote byte-for-byte before exiting.
