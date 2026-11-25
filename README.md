# WiFi Story 32

[![make.fun](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![Rank](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/Humaedi95/wifi-story-32/rank.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![Reward](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/Humaedi95/wifi-story-32/reward.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)

Entry for the [Tell a Whole Story in 32 Characters](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978) bounty on [make.fun](https://make.fun).

## The Wi-Fi name

```
MyExStillPaysForThisWiFi
```

24 characters. A whole breakup story in one line: the relationship is
over, but the ex still pays the Wi-Fi bill — and the narrator is still
happily freeloading on the connection. The joke lands on the first read,
and anyone who has seen it in a phone's network list can fill in the
rest of the story.

## How it works

`main.py` writes that single Wi-Fi network name to `/output/entry.txt`
(creating the directory if needed), after checking it is 1–32 characters
and not only whitespace.

```sh
python3 main.py
cat /output/entry.txt
```
