# METHODOLOGY — how the sheep-to-regrets patch note was written and chosen

## The entry

> **v2.5.8: fixed a bug where the brain counted sheep until 4 a.m., then switched to counting regrets.**

98 characters, 98 bytes — under the bounty gate of 1–160 characters.
A software patch note for a bug in human biology: the brain's sleep
routine counts sheep until 4 a.m., then — with no setting changed —
switches to counting regrets.

## The judge this entry is built for

The bounty is judged pairwise by a model briefed as a comedy editor
who has read a thousand changelogs, weighing, most important first:
(1) a single-line patch note for a bug in real life or human biology
that reads as comedy; (2) genuinely funny, the joke landing on a
first read and resting on a real comedic idea, not just the word
"bug" dropped into a sentence; (3) reads like an actual release
note — a version number, a terse engineering register, a fix stated
as if it shipped; (4) a specific, recognisable bug of the body or of
daily life, so the reader winces and laughs at once; (5) uses its
160 characters well — no padding, no setup the punchline does not
need, every word working. A made-up version number and a dry
engineering tone are welcome; length for its own sake does not count.
Ties go to the smaller text (fewer bytes), then the earlier receipt.
The field at build time was 3,752 entries, and no competitor line is
visible (blind rounds), so this entry targets the published brief
directly. The brief's own example line (the left ear rendering audio
late) was not used, copied, or varied.

## Step 1 — 35 candidates

Each candidate was drafted fresh in this session, one line, each a
different bug, each in the terse release-note register ("vX.Y.Z:
fixed a bug where…") with a precise symptom, trigger, or number.
Lengths are characters; every candidate is under the 160 gate.

### Human biology

| # | Candidate | Chars |
| --- | --- | --- |
| 1 | v1.0.3: fixed a bug where sneezing closed both eyes, leaving users blind for 0.4s mid-conversation. | 99 |
| 2 | v2.1.0: fixed a bug where the left knee predicted rain 48 hours before the forecast did. | 88 |
| 3 | v3.2.1: fixed a bug where yawning was contagious across rooms with no line of sight. | 84 |
| 4 | v1.4.2: fixed a bug where the brain replayed your most embarrassing moment from 2011 at 3 a.m. on loop. | 103 |
| 5 | v2.0.7: fixed a bug where hiccups ignored the mute button and fired during silent prayers. | 90 |
| 6 | v1.9.4: fixed a bug where the stomach growled loudest in rooms that had just gone quiet. | 88 |
| 7 | v3.0.1: fixed a bug where walking into a room deleted the reason you went in there. | 83 |
| 8 | v2.3.5: fixed a bug where the nose itched only when both hands were covered in paint. | 85 |
| 9 | v1.2.8: fixed a bug where the eyelid twitched for 3 days after a single cup of coffee. | 86 |
| 10 | v4.1.0: fixed a bug where the body woke up 7 minutes before the alarm, every day, without exception. | 100 |
| 11 | v2.6.3: fixed a bug where the bladder sent its first alert 40 minutes after the last rest stop. | 95 |
| 12 | v1.7.2: fixed a bug where the tongue bit itself during meals it had already survived 10,000 times. | 98 |
| 22 | v1.6.1: fixed a bug where the memory of a password expired 12 seconds after it was created. | 91 |
| 23 | v2.7.0: fixed a bug where the body shivered in a 24C room but sweated in a 19C one. | 83 |
| 24 | v1.1.9: fixed a bug where the sneeze you felt coming for 20 seconds never actually arrived. | 91 |
| 25 | v3.5.2: fixed a bug where the foot fell asleep 4 minutes before you needed to stand up. | 87 |
| 28 | **v2.5.8: fixed a bug where the brain counted sheep until 4 a.m., then switched to counting regrets.** | **98** |
| 30 | v3.6.0: fixed a bug where the bladder low-battery warning arrived 2 minutes after the last toilet. | 98 |
| 31 | v2.1.9: fixed a bug where the knee cracked loudest in silent rooms, at 72 dB. | 77 |
| 32 | v1.2.4: fixed a bug where one cup of coffee made the eyelid twitch for 72 hours. | 80 |
| 33 | v4.2.0: fixed a bug where the body aged 1 year per birthday, regardless of user settings. | 89 |
| 34 | v1.4.7: fixed a bug where the hiccup module ignored all 14 documented home remedies. | 84 |
| 35 | v2.5.8: fixed a bug where the brain counted sheep until 4 a.m. and then switched to counting regrets. | 101 |

### Real life (objects, queues, machines)

| # | Candidate | Chars |
| --- | --- | --- |
| 13 | v3.4.0: fixed a bug where socks vanished in pairs of one from a closed drawer. | 78 |
| 14 | v2.2.9: fixed a bug where the umbrella inverted at wind speeds below the advertised 60 km/h. | 92 |
| 15 | v1.3.6: fixed a bug where the elevator doors closed on exactly the person running toward them. | 94 |
| 16 | v2.8.1: fixed a bug where the kettle boiled only after you walked away to check on it. | 86 |
| 17 | v1.5.0: fixed a bug where the phone battery dropped from 20% to 1% in under 90 seconds. | 87 |
| 18 | v3.1.4: fixed a bug where the queue you joined immediately became the slowest one in the store. | 95 |
| 19 | v2.4.6: fixed a bug where the toast landed butter-side down in 87% of drops. | 76 |
| 20 | v1.8.3: fixed a bug where the alarm snooze button added 9 minutes, never the requested 10. | 90 |
| 21 | v2.0.2: fixed a bug where the brain autocorrected their to there in every important email. | 90 |
| 26 | v2.9.4: fixed a bug where the Wi-Fi dropped only during the final 30 seconds of a video call. | 93 |
| 27 | v1.0.9: fixed a bug where the door you just locked needed checking three more times. | 84 |
| 29 | v3.0.5: fixed a bug where the nose ran in winter and the throat closed in summer, with no setting to change it. | 111 |

## Step 2 — scoring the top 10

Each of the ten strongest candidates was scored 1–10 on the judge's
five criteria in order: **register** (reads like a real release
note), **funny** (lands on first read, real comedic idea), **specific**
(a precise, recognisable bug), **tight** (every word working),
**fresh** (a twist the field is unlikely to have).

| # | Candidate (short name) | Register | Funny | Specific | Tight | Fresh | Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 28 | **sheep → regrets** | 10 | 10 | 9 | 9 | 10 | **48** |
| 12 | tongue, 10,000 meals | 10 | 9 | 9 | 9 | 9 | **46** |
| 30 | bladder low-battery | 10 | 9 | 9 | 9 | 8 | **45** |
| 20 | snooze adds 9, not 10 | 10 | 8 | 10 | 9 | 8 | **45** |
| 21 | brain autocorrects their | 10 | 9 | 8 | 9 | 9 | **45** |
| 31 | knee cracks at 72 dB | 10 | 8 | 9 | 10 | 8 | **45** |
| 22 | password memory, 12s | 10 | 8 | 9 | 9 | 8 | **44** |
| 4 | 3 a.m. replay of 2011 | 10 | 9 | 9 | 8 | 7 | **43** |
| 6 | stomach, quiet rooms | 10 | 8 | 8 | 9 | 8 | **43** |
| 24 | phantom sneeze, 20s | 10 | 8 | 9 | 9 | 7 | **43** |

Notes on the cuts: #7 (walking into a room deletes the reason) is
the most recognisable bug of all, but it is also the most obvious —
in a field of 3,752 the doorway effect is the line everyone writes
first, so it loses on freshness. #19 (toast, 87%) is a cliché with a
number glued on, not a joke. #4's "2011" is an arbitrary year that
adds nothing; the 3 a.m. replay is a strong image but a well-worn
one. #24's phantom sneeze is the same idea as a sneeze that builds
and vanishes, already a familiar coinage. #33 (aging 1 year per
birthday) is a tautology, not a bug report. #13 (socks vanish in
pairs of one) is neat but a one-liner the field will have in bulk.

## Step 3 — pairwise tournament (top 6)

Round-robin, 5 games each, decided on the judge's criteria in order
(register → funny → specific → tight → fresh).

| Place | Candidate | W–L | Deciding notes |
| --- | --- | --- | --- |
| 1 | **sheep → regrets** | **5–0** | Beats tongue: a two-beat joke (setup, then the switch) where tongue is one beat. Beats bladder: wit over bodily crudeness on criterion 2. Beats snooze: a bigger laugh, not just a true fact. Beats autocorrect: a more vivid image. Beats knee: universal (everyone has lain awake) where knee-cracking is niche. |
| 2 | tongue, 10,000 meals | 4–1 | Loses only the final to sheep; its "10,000 times" escalation is the second-best twist, and the body attacking itself is a perfect bug report. |
| 3 | bladder low-battery | 3–2 | Beats snooze and autocorrect on the wince (criterion 4); loses to the top two on criterion 2 — the laugh is visceral, not clever. |
| 4 | snooze adds 9, not 10 | 2–3 | Beats autocorrect on specificity (a real, checkable fact: the 9-minute snooze); loses to the top three on laugh size. |
| 5 | brain autocorrects their | 1–4 | Beats knee on freshness (the brain as a bad spellchecker); loses on specificity to the rest — no number, no trigger moment. |
| 6 | knee cracks at 72 dB | 0–5 | Tightest line (77 chars, 10 on tight) and the most precise number, but the smallest laugh: a crack is a sound, not a predicament. |

## Step 4 — refinement

The winning line was tried in two wordings:

- **Chosen (98 chars):** "v2.5.8: fixed a bug where the brain counted sheep until 4 a.m., then switched to counting regrets."
- Rejected variant (101 chars): "…until 4 a.m. and then switched to counting regrets." — the extra "and" adds a word and no laugh; the comma plus "then" is tighter and more changelog-like.

The version number v2.5.8 is invented (the brief welcomes a
made-up version number); a middle version reads like a real shipped
patch, where v1.0.0 would read like a launch and v9.9.9 like a joke
about the version itself.

## Why the winner wins

- **Register:** a version number, "fixed a bug where…", past-tense
  fix stated as shipped — it could sit in a real changelog.
- **Funny:** the joke is a two-beat structure inside one line. The
  first half is a familiar ritual (counting sheep); the second half
  swaps the object (regrets) with no warning, and the swap is the
  punchline. It lands on first read because the reader supplies the
  4 a.m. feeling themselves.
- **Specific:** one precise trigger, "until 4 a.m.", and one precise
  mechanism, the switch from sheep to regrets — a symptom, a time,
  and a twist, nothing vague.
- **Wince + laugh:** it names the exact moment insomnia turns from
  boring to miserable, which is criterion 4's "winces and laughs at
  once" in one image.
- **Tight:** 98 of 160 characters, every word working — no adjective
  could be cut, no clause added, without losing either the setup or
  the punchline. Shorter also helps the byte tie-break.

## The program

`main.py` writes the fixed entry literal to `/output/entry.txt`
(overridable with `MAKEFUN_OUTPUT_DIR` for local testing), chmod
0644 so the grader can collect it as another user. No network, no
randomness, no clock: two runs are byte-identical
(`test_determinism.sh` checks this, plus that the output matches
`entry.txt` and passes the 1–160 character gate). `entry.txt`
holds the same 98 bytes with no trailing newline, so the judged
text is exactly the patch note.
