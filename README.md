# THE WORLD TODAY — Monday 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/akbare12/news-23-b51-front-page-dense/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/akbare12/news-23-b51-front-page-dense/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A one-page front page summing up 23 November 2026's world news in a single image:
AI rout hits Asia (Kospi −3.3%), Guterres urges AI rules at Bridgetown, and the US lead
over China hits a record low — plus 10 more stories, a world map with 13 pins, and an
18-item "Also on Monday" list. 31 stories, 6 regions.

## Run

```sh
python3 draw.py            # regenerates entry.png (1024x1024, < 1 MiB)
python3 main.py            # copies entry.png to $MAKEFUN_OUTPUT_DIR/entry.png
```

`main.py` is stdlib-only: it parses the PNG header by hand and never writes next
to itself, so it also runs from a read-only copy of this repo.

## Layout

Masthead → kicker → number strip → region bar → THE DAY IN UTC → 3 hero scenes
(Kospi chart, Guterres framework, Asia Power Index bars) → 10 story cards →
world map + ALSO list → DATE CHECK (stories dated other days are left out) →
sources + chip legend.

Scenes are drawn illustrations, not photographs. Chips: REPORTED = confirmed by
wires; CLAIM = one side's claim, not independently confirmed.
