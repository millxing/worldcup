#!/usr/bin/env python3
"""Generate the 7-week BSC Mock World Cup Event Plan PDF."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, ListFlowable, ListItem
)

OUTPUT = "/Users/robschoen/Dropbox/CC/worldcup/BSC_Mock_World_Cup_Event_Plan_7wk.pdf"

BLUE = HexColor("#1a5276")
LIGHT_BLUE_BG = HexColor("#eaf2f8")
BORDER_BLUE = HexColor("#2980b9")
WHITE = HexColor("#ffffff")
BLACK = HexColor("#000000")
GREY = HexColor("#666666")
LIGHT_GREY = HexColor("#f2f2f2")
HEADER_BG = HexColor("#2c3e50")

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "DocTitle", parent=styles["Title"],
    fontSize=22, leading=26, textColor=BLACK,
    fontName="Helvetica-Bold", spaceAfter=2, alignment=TA_LEFT,
)
subtitle_style = ParagraphStyle(
    "Subtitle", parent=styles["Normal"],
    fontSize=9.5, leading=12, textColor=GREY,
    fontName="Helvetica", spaceAfter=6,
)
heading_style = ParagraphStyle(
    "SectionHead", parent=styles["Heading1"],
    fontSize=14, leading=18, textColor=BLUE,
    fontName="Helvetica-Bold", spaceBefore=16, spaceAfter=8,
)
body_style = ParagraphStyle(
    "Body", parent=styles["Normal"],
    fontSize=10, leading=14, textColor=BLACK,
    fontName="Helvetica", spaceAfter=8,
)
bold_body = ParagraphStyle(
    "BoldBody", parent=body_style,
    fontName="Helvetica-Bold",
)
callout_style = ParagraphStyle(
    "Callout", parent=body_style,
    fontSize=10, leading=14,
    leftIndent=12, rightIndent=12,
    spaceBefore=4, spaceAfter=4,
)
bullet_style = ParagraphStyle(
    "Bullet", parent=body_style,
    leftIndent=24, bulletIndent=12, spaceAfter=4,
)
table_header_style = ParagraphStyle(
    "TblHead", parent=body_style,
    fontSize=9.5, fontName="Helvetica-Bold", textColor=WHITE,
)
table_cell_style = ParagraphStyle(
    "TblCell", parent=body_style,
    fontSize=9.5, spaceAfter=2, spaceBefore=2,
)
numbered_style = ParagraphStyle(
    "Numbered", parent=body_style,
    leftIndent=24, spaceAfter=4,
)
italic_style = ParagraphStyle(
    "Italic", parent=body_style,
    fontName="Helvetica-Oblique", textColor=GREY, fontSize=9.5,
    spaceBefore=12,
)


def make_callout_box(text):
    """Create the planning-basis callout box."""
    inner = Paragraph(text, callout_style)
    t = Table([[inner]], colWidths=[6.3 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LIGHT_BLUE_BG),
        ("BOX", (0, 0), (-1, -1), 1.5, BORDER_BLUE),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
    ]))
    return t


def make_table(headers, rows, col_widths=None):
    """Generic bordered table with header row."""
    header_cells = [Paragraph(h, table_header_style) for h in headers]
    data = [header_cells]
    for row in rows:
        data.append([Paragraph(cell, table_cell_style) for cell in row])

    if col_widths is None:
        col_widths = [6.3 * inch / len(headers)] * len(headers)

    t = Table(data, colWidths=col_widths, repeatRows=1)
    style_cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), HEADER_BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 9.5),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
        ("TOPPADDING", (0, 0), (-1, 0), 8),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#cccccc")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 1), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]
    # Alternate row shading
    for i in range(1, len(data)):
        if i % 2 == 0:
            style_cmds.append(("BACKGROUND", (0, i), (-1, i), LIGHT_GREY))
    t.setStyle(TableStyle(style_cmds))
    return t


def build():
    doc = SimpleDocTemplate(
        OUTPUT, pagesize=letter,
        leftMargin=0.85 * inch, rightMargin=0.85 * inch,
        topMargin=0.75 * inch, bottomMargin=0.75 * inch,
    )
    story = []

    # ── Title block ──
    story.append(Paragraph("BSC Mock World Cup Event Plan", title_style))
    story.append(Paragraph(
        "Event window: April 20, 2026 to June 1, 2026 | Scope: competition format, "
        "operating plan, and digital delivery model", subtitle_style))
    story.append(HRFlowable(
        width="100%", thickness=2, color=BORDER_BLUE,
        spaceAfter=12, spaceBefore=4))

    # ── Callout box ──
    story.append(make_callout_box(
        "<b>Planning basis.</b> This version replaces the earlier backend/frontend concept. "
        "The event will use <b>two single-file, mobile-friendly web apps hosted on GitHub Pages</b>, "
        "plus a <b>Google Form and Google Sheet</b> for weekly result submission and review. "
        "Detailed event activities are intentionally left out for now."
    ))
    story.append(Spacer(1, 10))

    # ── 1. Event Purpose and Scope ──
    story.append(Paragraph("1. Event Purpose and Scope", heading_style))
    story.append(Paragraph(
        "The goal is to run a World Cup-themed league game across 33 BSC soccer teams from "
        "3rd through 8th grade over seven Mondays, beginning on April 20, 2026 and ending on "
        "June 1, 2026. Each BSC team will be assigned a World Cup country and will progress "
        "through a tournament structure that feels like a World Cup without attempting to copy "
        "the full 48-team format literally.", body_style))
    story.append(Paragraph(
        "The plan must work within three practical constraints. First, the league has 33 teams, "
        "not 48. Second, the season window is fixed at seven weeks. Third, the digital tools "
        "must be lightweight enough to run on GitHub Pages without a custom backend.", body_style))

    # ── 2. Tournament Format ──
    story.append(Paragraph("2. Tournament Format", heading_style))
    story.append(Paragraph(
        "Each BSC team will be randomly assigned a World Cup country. The 33 assigned teams "
        "will then be placed into the World Cup-style group structure in a scaled format: nine "
        "groups will contain three active BSC teams and three groups will contain two active BSC "
        "teams. Any unassigned countries function as scheduled challenge opponents rather than "
        "live teams.", body_style))
    story.append(Paragraph(
        "Week 1 combines the opening launch with the first official group match. Country reveals, "
        "group releases, schedule launches, and app orientation all happen at the start of Week 1, "
        "followed immediately by Group Stage Matchday 1. Weeks 2 and 3 complete the group stage. "
        "After group play, all 33 teams are ranked in one overall table using total match points "
        "first, then point differential, then total points scored, with a final admin tiebreak "
        "if required.", body_style))
    story.append(Paragraph(
        "The top 16 teams advance to the championship bracket. The remaining 17 teams stay active "
        "through the end of the event in a consolation or plate standings race so that every team "
        "has something meaningful to follow through June 1.", body_style))

    # Schedule table
    schedule_rows = [
        ["Week 1", "Monday, April 20",
         "Opening week launch (country reveal, group release, schedule launch, "
         "app orientation) and Group Stage Matchday 1"],
        ["Week 2", "Monday, April 27", "Group Stage Matchday 2"],
        ["Week 3", "Monday, May 4", "Group Stage Matchday 3 and final group rankings"],
        ["Week 4", "Monday, May 11", "Round of 16; consolation standings begin"],
        ["Week 5", "Monday, May 18", "Quarterfinals; consolation standings continue"],
        ["Week 6", "Monday, May 25", "Semifinals; consolation standings continue"],
        ["Week 7", "Monday, June 1", "Final, third-place finish, consolation closeout, awards"],
    ]
    story.append(make_table(
        ["Week", "Date", "Competition Focus"], schedule_rows,
        col_widths=[0.8 * inch, 1.4 * inch, 4.1 * inch]))
    story.append(Spacer(1, 6))

    # ── 3. Standings and Advancement Rules ──
    story.append(Paragraph("3. Standings and Advancement Rules", heading_style))
    story.append(Paragraph(
        "Each week, every team receives one scheduled matchup: either a head-to-head matchup "
        "against another active BSC team or a benchmark challenge against an unassigned country. "
        "Official standings should use the same table structure throughout the event so the player "
        "experience remains simple and consistent.", body_style))

    for bullet_text in [
        "Win = 3 points",
        "Draw = 1 point",
        "Loss = 0 points",
        "Tiebreak order after group play: table points, point differential, total points scored, admin tiebreak",
    ]:
        story.append(Paragraph(f"\u2022  {bullet_text}", bullet_style))

    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "After Week 3, the overall rankings seed the championship bracket as 1 vs 16, 2 vs 15, "
        "and so on. The consolation track can remain table-based rather than bracket-based to "
        "reduce administrative overhead during the second half of the event.", body_style))

    # ── 4. Digital Delivery Model ──
    story.append(Paragraph("4. Digital Delivery Model", heading_style))
    story.append(Paragraph(
        "The event will use two separate single-file web apps, both mobile-friendly and both "
        "hosted on GitHub Pages. Each app should be delivered as a self-contained HTML file with "
        "embedded CSS and JavaScript so the system can be hosted cheaply and managed without "
        "server infrastructure.", body_style))
    story.append(Paragraph(
        "A static GitHub Pages site cannot securely hide future coach-only content. For that reason, "
        "the operating rule should be simple: the coach app must only contain the current week\u2019s "
        "details. Future weeks should never be embedded in the file ahead of time. The organizer "
        "updates and republishes coach.html each week so players cannot inspect the page source and "
        "discover future activities early.", body_style))

    # Apps comparison table
    app_rows = [
        ["\u2022 Country assignment and team identity\n"
         "\u2022 Group tables and overall standings\n"
         "\u2022 Weekly schedule and completed results\n"
         "\u2022 Knockout bracket and consolation table\n"
         "\u2022 League announcements and current week label\n"
         "\u2022 Recommended file: <b>index.html</b>",
         "\u2022 Everything shown in the player app\n"
         "\u2022 Current week event instructions\n"
         "\u2022 Coach reminders, deadlines, and scoring notes\n"
         "\u2022 Link to the weekly Google Form for result submission\n"
         "\u2022 Recommended file: <b>coach.html</b>"],
    ]
    app_table_data = [
        [Paragraph("Player App (public)", table_header_style),
         Paragraph("Coach App (restricted by process, not true security)", table_header_style)],
        [Paragraph(app_rows[0][0].replace("\n", "<br/>"), table_cell_style),
         Paragraph(app_rows[0][1].replace("\n", "<br/>"), table_cell_style)],
    ]
    t = Table(app_table_data, colWidths=[3.15 * inch, 3.15 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), HEADER_BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#cccccc")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(t)
    story.append(Spacer(1, 6))

    # ── 5. Results Collection ──
    story.append(Paragraph("5. Results Collection: Google Form and Google Sheet", heading_style))
    story.append(Paragraph(
        "Because the apps are static and have no backend, coaches will not submit results directly "
        "into the GitHub Pages site. Instead, coaches will use a Google Form on mobile. Every form "
        "submission feeds a Google Sheet that becomes the official intake and review log for weekly "
        "results.", body_style))
    story.append(Paragraph(
        "The form should capture the minimum information needed to verify a result cleanly: week "
        "number, team name, opponent or challenge country, result, score or points earned, coach "
        "name, and any notes needed for review. A proof field can be added later if the league "
        "decides it wants a photo or other confirmation, but that is optional for version 1.",
        body_style))
    story.append(Paragraph(
        "For the first release, the safest operating model is review first, then publish. The "
        "organizer reviews the Google Sheet, confirms any conflicts, and then updates the static "
        "app data with the approved results. This avoids incorrect standings going live immediately "
        "from an unverified submission.", body_style))

    # Tool table
    story.append(make_table(
        ["Tool", "Role in the workflow"],
        [
            ["Google Form", "Coach-facing mobile submission form for weekly results"],
            ["Google Sheet", "Automatic collection point for submissions, review notes, and approval status"],
            ["GitHub Pages apps", "Public display of official schedule, standings, bracket, and published results"],
        ],
        col_widths=[1.6 * inch, 4.7 * inch]))
    story.append(Spacer(1, 6))

    # ── 6. Weekly Operating Workflow ──
    story.append(Paragraph("6. Weekly Operating Workflow", heading_style))
    story.append(Paragraph(
        "The event should run on a predictable weekly cycle so coaches know exactly where to look "
        "and when to submit. This makes one organizer the scorekeeper and publisher, which is "
        "realistic for a static-site setup and is much simpler than trying to simulate live "
        "multi-user entry without a backend.", body_style))

    for i, step in enumerate([
        "At the start of each week, the organizer updates coach.html with that week\u2019s instructions and publishes the live Google Form link.",
        "Teams complete the weekly event and coaches submit results through the form on mobile.",
        "All submissions land in the Google Sheet, where the organizer reviews, verifies, and marks results as approved.",
        "The organizer updates the JavaScript data inside the single-file apps with the official results.",
        "The GitHub Pages site is republished so players and coaches see the updated standings, scores, and bracket.",
    ], 1):
        story.append(Paragraph(f"<b>{i}.</b>  {step}", numbered_style))

    # ── 7. Build Requirements ──
    story.append(Paragraph("7. Build Requirements for the GitHub Pages Apps", heading_style))
    story.append(Paragraph(
        "Version 1 should stay narrow. The apps do not need logins, accounts, chat, notifications, "
        "or live database writes. They only need to present the tournament clearly on a phone and "
        "be simple to update every week.", body_style))
    story.append(Paragraph(
        "The player app should remain fully public. The coach app should be distributed only to "
        "coaches, but it should still be treated as a process-controlled page rather than a secure "
        "private application. The weekly publishing rule is what protects future event details, "
        "not the code itself.", body_style))

    for b in [
        "Responsive layout that works on mobile first",
        "Embedded HTML, CSS, and JavaScript in each file",
        "Data objects for teams, countries, groups, schedule, results, standings, bracket, and announcements",
        "Automatic standings calculation from approved results",
        "A visible current-week indicator",
        "A clean method for swapping in updated results each week",
    ]:
        story.append(Paragraph(f"\u2022  {b}", bullet_style))

    # ── 8. Organizer Responsibilities ──
    story.append(Paragraph("8. Organizer Responsibilities", heading_style))
    story.append(Paragraph(
        "One person or a very small admin group should own the tournament data throughout the "
        "season. The job is manageable because the system is intentionally simple and all official "
        "data changes happen on a weekly cadence.", body_style))

    for b in [
        "Assign countries and groups before kickoff",
        "Publish the full seven-week schedule",
        "Create and maintain the Google Form and Google Sheet",
        "Update coach.html weekly with current instructions only",
        "Review submissions and approve official results",
        "Update standings, bracket, and announcements in the app files",
        "Republish GitHub Pages after each update cycle",
    ]:
        story.append(Paragraph(f"\u2022  {b}", bullet_style))

    # ── 9. Pre-Launch Checklist ──
    story.append(Paragraph("9. Pre-Launch Checklist", heading_style))
    story.append(Paragraph(
        "Before April 20, the league should finalize the tournament structure, assign countries, "
        "finish the schedule, and complete a dry run of the digital workflow from submission to "
        "publication.", body_style))

    for b in [
        "Finalize team list and country assignments",
        "Place all 33 teams into the scaled group structure",
        "Build the seven-week calendar and knockout seeding rules",
        "Create the initial index.html and coach.html files",
        "Create the Google Form and linked Google Sheet",
        "Test one full result cycle on a phone: submit form, review sheet, update apps, republish GitHub Pages",
        "Freeze Week 1 content and publish the launch version by Friday, April 17",
    ]:
        story.append(Paragraph(f"\u2022  {b}", bullet_style))

    # ── 10. Final Recommendation ──
    story.append(Paragraph("10. Final Recommendation", heading_style))
    story.append(Paragraph(
        "The most practical version of this event is a scaled World Cup competition with three "
        "group-stage weeks and four knockout weeks, supported by two single-file GitHub Pages apps "
        "and a Google Form/Google Sheet results workflow. This structure fits the seven-week "
        "calendar, respects the no-backend requirement, keeps players from seeing future event "
        "details, and gives the league a realistic weekly operating process.", body_style))
    story.append(Paragraph(
        "The key rule is to separate published standings and schedule from coach-only weekly "
        "instructions. The public app can carry the full season structure from day one, while the "
        "coach app should be refreshed weekly and never include future event details in advance.",
        body_style))
    story.append(Paragraph(
        "This plan intentionally excludes the design of the weekly activities themselves so the "
        "league can finalize the operating model and digital workflow first.", italic_style))

    doc.build(story)
    print(f"PDF created: {OUTPUT}")


if __name__ == "__main__":
    build()
