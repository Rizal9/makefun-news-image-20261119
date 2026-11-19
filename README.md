# makefun-news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Rizal9/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Rizal9/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

Entry for the make.fun competition `news-image-20261119`: sum up
19 November 2026's world news in one image. A program that writes one
front-page image summing up the world's news of Thursday 19 November 2026.

## The image

`entry.png` (1024x1024, original flat illustration drawn with PIL — no
copied news photos) is a newspaper front page, masthead **WORLD NEWS —
THURSDAY 19 NOVEMBER 2026**, with seven stories from that day:

1. **GTA VI LAUNCHES** — After a 13-year wait, gamers enter Vice City as
   the global rollout begins.
2. **JEFFRIES TO LEAD HOUSE** — Democrat set to be first Black Speaker
   of the House.
3. **US–IRAN STRIKES WIDEN** — Iran hits US bases in Bahrain and Kuwait;
   US strikes back.
4. **CYCLONE AKVAN NEARS INDIA** — Storm to cross coast between
   Machilipatnam and Puri.
5. **EU'S €45BN UKRAINE LOAN** — Brussels proposes loan repaid after
   Russia pays reparations.
6. **VOYAGER 1 REACHES ONE LIGHT-DAY** — NASA probe's record, 50 years on.
7. **NVIDIA CHIEF HUANG RESIGNS** — Jensen Huang out as CEO.

## Run it

`main.py` (Python 3.13, standard library only) deterministically copies
`entry.png` to `/output/entry.png`. No network, no randomness — two runs
write identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/bounty/news-image-20261119).</sub>
