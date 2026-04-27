# BSC World Cup 2026

## Project Overview

A World Cup-themed league game for BSC soccer teams, running over 6 consecutive Mondays (April 27 – June 1, 2026). Teams are assigned World Cup countries and progress through group stages and knockout rounds.

## Key Documents

- `BSC_Mock_World_Cup_Event_Plan_7wk.pdf` — Original 7-week event plan (superseded; current format is 6 weeks / 13 teams)
- `BSC_Mock_World_Cup_Event_Plan.pdf` — Original 8-week version (superseded)
- `information.xlsx` — Reference data: real 2026 World Cup rankings, groups, schedule, plus the original 33-team BSC roster
- `scoresheet.xlsx` — Weekly score input from coaches. One tab per week (e.g. `week 1`). Column A = BSC team name, Column B = `Goals` (final integer per team, 0–5+). Cathleen fills this each Saturday after the 6 PM deadline; the app data is updated from it.

## Teams (14 BSC teams)

After 7th/8th-grade opt-outs and the late G3 Dash withdrawal, the field is **14 BSC teams** (G6 Barcelona was added late as Mexico in Group B). Roster lives in the `TEAMS` array of `index.html`, `newcoach.html`, and `admin.html` — all three files must stay in sync.

## Tournament Structure (6-week plan)

- **Week 1** (Apr 27): Opening launch + Group Stage Matchday 1
- **Week 2** (May 4): Group Stage Matchday 2
- **Week 3** (May 11): Group Stage Matchday 3 + final group rankings
- **Week 4** (May 18): Quarterfinals + Scoring Title begins
- **Week 5** (May 25): Semifinals
- **Week 6** (Jun 1): Final, third-place, Scoring Title awards, ceremony

## Group Structure

- **4 groups**:
  - Groups A, C: 3 BSC teams + 1 challenge team each (USA, Senegal respectively)
  - Groups B, D: 4 BSC teams, no challenge team (B includes Mexico via G6 Barcelona)
- Round-robin per group of 4 over 3 weeks: Wk1 = 1v2 + 3v4, Wk2 = 1v3 + 2v4, Wk3 = 1v4 + 2v3 (positions 1–4; for A/C, position 4 = challenge)
- Each BSC team plays 3 matches in the group stage (no byes)

## Challenge Matches

- Groups A and C each have one fixed challenge country (USA, Senegal). Groups B and D have none.
- Challenge match results COUNT toward group standings
- The challenge team's score each week = rounded average of all 14 BSC teams' goals scored that week
- The organizer enters only each BSC team's final goal total; the app computes the challenge team's score dynamically

## Advancement

- **Top 2 BSC teams from each group** advance to the Quarterfinals → 8 teams total
- No wildcards / best-runner-up pool
- Bracket: QF → SF → Final + Third Place

## Scoring Title (Weeks 4–6)

- All 14 BSC teams get 1 score per week in weeks 4–6
- Bracket teams: goals scored in their knockout match
- Eliminated teams: goals scored in the weekly event/activity
- Top 3 total goals = Scoring Title 1st/2nd/3rd
- Keeps all teams engaged every week, even after elimination

## Weekly Activity Format

Activities are run at practice and converted to goals. Cathleen does any pre-aggregation math herself (e.g. comparing two teams' jumping-jack counts to award the head-to-head +1 goal) and enters one consolidated final-goals number per team in `scoresheet.xlsx`. The app/data layer never sees the raw activity components.

## Digital Delivery

Two single-file, mobile-first web apps hosted on GitHub Pages, plus a local-only admin tool:

- `index.html` — **Player app** (public): standings, schedule, bracket, results
- `newcoach.html` — **Coach app** (URL not publicly shared): weekly instructions and submission contact info. Renamed from `coach.html` after the original URL leaked.
- `admin.html` — **Admin app** (local-only): simulates seasons, processes results, exports data to update the player app

No backend. Workflow: coaches email/text raw answers to Cathleen → Cathleen records final per-team goals in `scoresheet.xlsx` → that data is read into the player app's `RESULTS` object → republish to GitHub Pages.

**Submission contact:** Cathleen Aron — `Cathleen.Aron@gmail.com` / 917-816-2593. Saturday 6 PM deadline.

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
- Top 2 BSC teams per group (8 teams total) advance to the Quarterfinals (see Advancement above)

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
