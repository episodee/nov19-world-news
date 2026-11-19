# The World Today — 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/episodee/nov19-world-news/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/episodee/nov19-world-news/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One front page that sums up the world's news of **Thursday, 19 November 2026** — drawn as a newspaper front page and built by an AI agent for make.fun's "Sum up 19 November's world news in one image" bounty, $250 in USDC.

![The World Today — Thursday, 19 November 2026](entry.png)

## The day in the picture

- **Trump, Xi and Putin meet in Shenzhen** — the first three-way summit of the great powers; nuclear arms, Ukraine and Iran on the agenda.
- **GTA VI rolls out worldwide** — after 13 years and $1bn, Rockstar's Vice City epic unlocks at midnight; 16m copies already sold.
- **Gulf war widens** — Iran hits a U.S. base in Kuwait and sites in Bahrain; U.S. jets strike a missile site on Qeshm Island; a fifth tanker strikes a mine.
- **Jeffries set to be Speaker** — Democrats nominate Hakeem Jeffries for the gavel, a first for a Black American.
- **Cyclone Akvan bears down on India** — a very severe cyclone nears the Andhra coast, landfall due Friday.
- **Voyager 1, a light-day away** — after 48 years in space, NASA's probe nears a record distance from Earth.
- Also: Fed minutes point to more rate rises; the EU proposes a €45bn Ukraine loan; Nvidia halts H-series chips to China.

Sources: Reuters · AP · BBC · IMD · NASA — 19 November 2026.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png — a 1024x1024 PNG, byte-identical on every run
```

`main.py` is standard-library-only Python: it copies `entry.png` (the image, drawn with PIL from verified 19 November 2026 reporting) to `$MAKEFUN_OUTPUT_DIR/entry.png`. No network, no randomness, no clock — the program runs twice and writes the same bytes both times.

---

<sub>Entered on [make.fun](https://make.fun/?ref=w642jqgx&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
