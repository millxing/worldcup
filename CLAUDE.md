# BSC World Cup 2026

## Project Overview

A World Cup-themed league game for BSC soccer teams, running over 7 consecutive Mondays (April 20 – June 1, 2026). Teams are assigned World Cup countries and progress through group stages and knockout rounds.

## Key Documents

- `BSC_Mock_World_Cup_Event_Plan_7wk.pdf` — Current event plan (7-week version)
- `BSC_Mock_World_Cup_Event_Plan.pdf` — Original 8-week version (superseded)

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
- **Week 4** (May 11): Round of 16; consolation begins
- **Week 5** (May 18): Quarterfinals
- **Week 6** (May 25): Semifinals
- **Week 7** (Jun 1): Final, third-place, consolation closeout, awards

## Group Structure

- **33 teams**: 9 groups of 3 + 3 groups of 2 (12 groups)
- **25 teams**: Likely 4 groups of 4 + 3 groups of 3 (7 groups). Top-8 bracket becomes an option (frees a week).

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
- Tiebreak: total points → point differential → total points scored → admin tiebreak
- Top 16 (or top 8 if 25 teams) advance to knockout bracket after group stage
- Remaining teams enter consolation standings (table-based, not bracket)

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
