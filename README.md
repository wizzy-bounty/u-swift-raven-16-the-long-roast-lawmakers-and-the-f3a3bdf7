# The Long Roast: Lawmakers and the File They Cannot Convert

[![make.fun](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![Rank](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/wizzy-bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![Reward](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/wizzy-bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)

A [make.fun](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7) program/v1 entry: one satirical sentence, at most 320 characters, roasting lawmakers who would regulate AI, crypto or the internet but cannot convert a file to PDF.

## The entry

> The senator who wrote the toughest AI law in the country has never once turned a .docx into a PDF — his staff does that for him, just like they write the laws he signs.

## How it works

`main.py` (Python standard library only, no network) writes the sentence to `/output/entry.txt`. It is deterministic — the same sentence on every run — and self-checks before writing: the output must be exactly one sentence of 1–320 characters, otherwise it exits 1 without writing anything.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
