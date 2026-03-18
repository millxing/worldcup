# BSC World Cup 2026

## Project Overview

A World Cup-themed league game for BSC soccer teams, running over 7 consecutive Mondays (April 20 – June 1, 2026). Teams are assigned World Cup countries and progress through group stages and knockout rounds.

## Key Documents

- `BSC_Mock_World_Cup_Event_Plan_7wk.pdf` — Current event plan (7-week version)
- `BSC_Mock_World_Cup_Event_Plan.pdf` — Original 8-week version (superseded)
- `information.xlsx` — Has 4 sheets of data:
  1. Actual Rankings — 48 World Cup countries with FIFA rankings
  2. Actual Groups — The real 2026 World Cup group draw (Groups A–L, 4 teams each)
  3. Actual Schedule — Full 104-game match schedule with dates, locations, and bracket
  4. BSC Teams — The 33 BSC team names with gender and grade

## Team Counts

| Grade | Girls | Boys | Total |
|-------|-------|------|-------|
| 3rd   | 3     | 4    | 7     |
| 4th   | 3     | 4    | 7     |
| 5th   | 2     | 3    | 5     |
| 6th   | 3     | 3    | 6     |
| 7th   | 2     | 2    | 4     |
| 8th   | 2     | 2    | 4     |
| **Total** | **15** | **18** | **33** |

Full participation (3rd–8th): 33 teams. If 7th/8th opt out: 25 teams. Design the apps to handle either scenario.

## Tournament Structure (7-week plan)

- **Week 1** (Apr 20): Opening launch + Group Stage Matchday 1
- **Week 2** (Apr 27): Group Stage Matchday 2
- **Week 3** (May 4): Group Stage Matchday 3 + final group rankings
- **Week 4** (May 11): Round of 16 + Scoring Title begins
- **Week 5** (May 18): Quarterfinals
- **Week 6** (May 25): Semifinals
- **Week 7** (Jun 1): Final, third-place, Scoring Title awards, ceremony

## Group Structure

- **33 teams**: 11 groups of 3 BSC teams + 1 challenge team each, plus Group G (challenge-only, 4 challenge teams)
- Each group plays a full round-robin over 3 weeks (pos1 vs pos2, pos1 vs pos3, pos2 vs pos3)
- Each BSC team plays 2 group matches + 1 challenge match = 3 matches total
- All 33 BSC teams play every week (no byes)

## Challenge Matches

- Each group's 4th member is a non-BSC "challenge" country from the real World Cup
- Challenge match results COUNT toward group standings
- The challenge team's score = rounded average of all 33 BSC teams' goals scored that week
- The organizer enters only the BSC team's score; the app computes the challenge team's score dynamically

## Advancement

- 11 group winners advance to R16 (if the challenge team tops a group, the runner-up advances instead)
- 5 best remaining BSC teams also advance (by points, then goals scored tiebreaker)
- Total: 16 teams in the knockout bracket

## Scoring Title (Weeks 4-7)

- All 33 teams get 1 score per week in weeks 4-7
- Bracket teams: goals scored in their knockout match
- Eliminated teams: goals scored in the weekly event/activity
- Top 3 total goals = Scoring Title 1st/2nd/3rd
- Replaces the old consolation format; keeps all teams engaged every week

## Digital Delivery

Two single-file, mobile-first web apps hosted on GitHub Pages:

- `index.html` — **Player app** (public): standings, schedule, bracket, results
- `coach.html` — **Coach app** (process-restricted): includes weekly instructions, Google Form link

No backend. Results submitted via Google Form → Google Sheet → organizer reviews → manually updates app data → republish.

## Technical Constraints

- Single-file HTML apps (embedded CSS/JS)
- GitHub Pages hosting, no server/backend
- Data stored as JS objects inside the HTML files
- Coach app republished weekly with current-week content only (no future week details embedded)
- Must work well on mobile

## Standings Rules

- Win = 3 pts, Draw = 1 pt, Loss = 0 pts
- Tiebreak: total points → goals scored → goals allowed → admin tiebreak
- Both group matches and challenge matches count toward standings
- Top 16 advance to knockout bracket after group stage (see Advancement above)

## Design & Branding

### Color Palette
| Color | Hex | Role |
|-------|-----|------|
| Dark Navy | `#34374C` | Header, nav, dark sections |
| Deep Navy | `#2C2E3E` | Secondary dark, countdown bg |
| Navy Light | `#3d4058` | Hover states, lighter dark |
| Vivid Red | `#EE2B47` | Primary accent, buttons, badges |
| Off-White | `#F6F6F6` | Page background |

CSS variables use semantic names: `--navy`, `--navy-deep`, `--navy-light`, `--red`, `--red-light`, `--red-dim`, `--off-white`. Legacy aliases (`--green-dark`, `--gold`, etc.) are preserved for JS inline style compatibility.

### Typography
- **Display/Headlines**: Oswald (700, uppercase, tight letter-spacing) — all headings, card titles, group headers, bracket rounds, countdown, club name
- **Body/Data**: Montserrat (400–800) — body text, tables, labels, nav tabs
- Google Fonts import includes both: `Montserrat:wght@400;500;600;700;800;900` + `Oswald:wght@400;500;600;700`

### Logo
- BSC Town Travel crest: `https://cdn2.sportngin.com/attachments/photo/bd06-216817597/BSC_TT_-_NBG_large.png`
- Transparent PNG, works on dark backgrounds
- Height: 180px mobile, 225px desktop
- Negative bottom margin (-30px) to close gap with "BROOKLINE SOCCER CLUB" text below

### Visual Identity
- **Aesthetic**: Sports broadcast editorial (think FIFA World Cup TV graphics)
- Cards have 3px solid red left border
- Group/week headers use full-width navy bars with Oswald uppercase text
- Bracket matches use navy-deep background with white text
- Countdown has subtle pulse animation
- Tab content fades in on switch (fadeIn animation)
- Footer: navy-deep background, Montserrat 0.65rem, white at 50% opacity
