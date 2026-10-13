"""Charts for the US data center water brief - Machine Readable brand palette.

Every value plotted here is transcribed from a primary source document and
recorded, with its unit as printed and a full citation, in data/sources.md.
The same values live in data/stats.json keyed to their source IDs.
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# Brand palette (same as the Denver 311 brief)
CHARCOAL = "#23221F"
PAPER = "#F1E7DA"
AMBER = "#E8A33D"
TEAL = "#2AA198"
AMBER_DIM = "#8A6420"
TEAL_DIM = "#1E6E68"
GRID = "#4A453C"
TEXT = "#F1E7DA"
TEXT_DIM = "#B8AE9C"
GRAY_BAR = "#6E675C"

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "charts")
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({
    "figure.facecolor": CHARCOAL,
    "axes.facecolor": CHARCOAL,
    "axes.edgecolor": GRID,
    "axes.labelcolor": TEXT,
    "text.color": TEXT,
    "xtick.color": TEXT_DIM,
    "ytick.color": TEXT_DIM,
    "grid.color": GRID,
    "grid.alpha": 0.5,
    "font.size": 11,
    "axes.titlesize": 14,
    "axes.titleweight": "bold",
    "axes.titlecolor": TEXT,
})


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, name), dpi=150, facecolor=CHARCOAL, bbox_inches="tight", pad_inches=0.25)
    plt.close(fig)
    print("saved", name)


# ---------------------------------------------------------------------------
# (a) US data center electricity (sources S1, S14)
# 2018: 76 TWh (1.9% of US electricity); 2023: 176 TWh (4.4%) - LBNL 2024
# report (S1). 2024: 192 TWh (4.7%) - LBNL 2025 Update, Jun 2026 (S14).
# 2030 (S14): Reference Case 649 TWh (11.8%); Compounded Uncertainty range
# 521 to 843 TWh (9.5% to 15.3%). Scenarios, not a forecast.
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8.6, 5.2))
years = ["2018", "2023", "2024", "2030 low", "2030 reference", "2030 high"]
vals = [76, 176, 192, 521, 649, 843]
colors = [TEAL, TEAL, TEAL, AMBER_DIM, AMBER, AMBER_DIM]
bars = ax.bar(years, vals, color=colors, width=0.62)
labels = ["76 TWh\n1.9% of US electricity",
          "176 TWh\n4.4% of US electricity",
          "192 TWh\n4.7% of US electricity",
          "521 TWh\n9.5% (scenario low)",
          "649 TWh\n11.8% (reference case)",
          "843 TWh\n15.3% (scenario high)"]
label_dy = [22, 22, 68, 22, 22, 22]  # 2024 label staggered above 2023's
for b, lab, dy in zip(bars, labels, label_dy):
    ax.annotate(lab, (b.get_x() + b.get_width() / 2, b.get_height() + dy),
                ha="center", va="bottom", fontsize=10.5, color=TEXT)
ax.annotate("", xy=(5.38, 962), xytext=(2.62, 962),
            arrowprops=dict(arrowstyle="-", color=TEXT_DIM, lw=1.2))
ax.text(4.0, 980, "2030 scenario range", ha="center", fontsize=10.5,
        color=TEXT_DIM)
ax.set_ylim(0, 1065)
ax.set_ylabel("Electricity use, TWh per year")
ax.set_title("US data center electricity use: growth through 2024, wide 2030 scenarios")
ax.grid(axis="y")
ax.set_axisbelow(True)
ax.text(0.0, -0.14,
        "Source: Lawrence Berkeley National Laboratory, 2024 United States Data Center\n"
        "Energy Usage Report (Dec 2024) for 2018 and 2023; 2025 Update (Jun 2026,\n"
        "LBNL-2001758) for 2024 and the 2030 scenarios. 2030 low and high are the\n"
        "update's compounded uncertainty bounds around its 649 TWh reference case.",
        transform=ax.transAxes, fontsize=9, color=TEXT_DIM, va="top")
save(fig, "energy_outlook.png")

# ---------------------------------------------------------------------------
# (b) Disclosed water consumption, company reports (sources S2, S3, S4)
# Normalized to billion liters. Boundaries differ by company; see chart note.
# Google: total water consumption, all operations (million gallons as printed):
#   2021 4,562 / 2022 5,565 / 2023 6,352 / 2024 8,135 / 2025 10,869
# Microsoft: total water consumed, all operations (cubic meters as printed):
#   FY20 4,196,000 / FY21 6,399,000 / FY22 8,068,000 / FY23 7,844,000 /
#   FY24 5,807,000 (estimation method changed in FY24; prior years not restated)
# Meta: total water consumption, all operations (megaliters as printed):
#   2020 2,202 / 2021 2,569 / 2022 2,638 / 2023 3,078 / 2024 3,123
# ---------------------------------------------------------------------------
GAL_TO_L = 3.78541
google_yrs = [2021, 2022, 2023, 2024, 2025]
google_bl = [v * 1e6 * GAL_TO_L / 1e9 for v in [4562, 5565, 6352, 8135, 10869]]
msft_yrs = [2020, 2021, 2022, 2023, 2024]
msft_bl = [v * 1e3 / 1e9 for v in [4196000, 6399000, 8068000, 7844000, 5807000]]
meta_yrs = [2020, 2021, 2022, 2023, 2024]
meta_bl = [v * 1e6 / 1e9 for v in [2202, 2569, 2638, 3078, 3123]]

fig, ax = plt.subplots(figsize=(8.6, 5.4))
ax.plot(google_yrs, google_bl, "-o", color=AMBER, lw=2.2, ms=5,
        label="Google, total consumption (CY)")
ax.plot(msft_yrs, msft_bl, "-s", color=TEAL, lw=2.2, ms=5,
        label="Microsoft, total consumed (FY, ends Jun 30)")
ax.plot(meta_yrs, meta_bl, "-^", color=PAPER, lw=2.0, ms=5,
        label="Meta, total consumption (CY)")
ax.annotate("41.1", (2025, 41.1), textcoords="offset points", xytext=(2, 6),
            fontsize=10, color=AMBER)
ax.annotate("5.8", (2024, 5.8), textcoords="offset points", xytext=(2, 6),
            fontsize=10, color=TEAL)
ax.annotate("3.1", (2024, 3.1), textcoords="offset points", xytext=(2, -14),
            fontsize=10, color=PAPER)
ax.set_ylabel("Water consumption, billion liters per year")
ax.set_title("What the hyperscalers disclose: water consumption is rising\n"
             "where it is reported at all")
ax.set_xticks([2020, 2021, 2022, 2023, 2024, 2025])
ax.grid(axis="y")
ax.set_axisbelow(True)
ax.legend(loc="upper left", frameon=False, fontsize=9.5)
ax.text(0.0, -0.13,
        "Company environmental reports; global totals for all operations, converted to liters.\n"
        "Boundaries and methods differ: Microsoft changed its estimation method in FY24 and did\n"
        "not restate prior years, so its FY24 drop is partly a method change. Amazon published no\n"
        "absolute total until June 2026 (2025 withdrawal, about 2.5 billion gallons, global).",
        transform=ax.transAxes, fontsize=9, color=TEXT_DIM, va="top")
save(fig, "disclosed_water.png")

# ---------------------------------------------------------------------------
# (c) National context (sources S1, S5)
# USGS 2015 (billion gallons per day as printed, converted to billion
# liters per year): irrigation withdrawals 118; thermoelectric withdrawals
# 133; public supply withdrawals 39; irrigation consumptive use 73.2;
# thermoelectric consumptive use 4.31.
# LBNL 2023: data center direct consumption 66 billion liters;
# direct plus indirect (electricity generation) about 866 billion liters.
# ---------------------------------------------------------------------------
BGAL_DAY_TO_BL_YR = 365 * GAL_TO_L  # billion gal/day -> billion liters/year
items = [
    ("Thermoelectric power withdrawals, 2015 (USGS)", 133 * BGAL_DAY_TO_BL_YR, AMBER_DIM, "withdrawal"),
    ("Irrigation withdrawals, 2015 (USGS)", 118 * BGAL_DAY_TO_BL_YR, AMBER_DIM, "withdrawal"),
    ("Irrigation consumption, 2015 (USGS)", 73.2 * BGAL_DAY_TO_BL_YR, AMBER, "consumption"),
    ("Public supply withdrawals, 2015 (USGS)", 39 * BGAL_DAY_TO_BL_YR, AMBER_DIM, "withdrawal"),
    ("Thermoelectric consumption, 2015 (USGS)", 4.31 * BGAL_DAY_TO_BL_YR, AMBER, "consumption"),
    ("Data centers, direct + indirect consumption, 2023 (LBNL)", 866, TEAL, "consumption"),
    ("Data centers, direct consumption only, 2023 (LBNL)", 66, TEAL, "consumption"),
]
items.sort(key=lambda t: t[1])
fig, ax = plt.subplots(figsize=(9.2, 5.6))
ypos = np.arange(len(items))
ax.barh(ypos, [i[1] for i in items], color=[i[2] for i in items], height=0.62)
ax.set_yticks(ypos)
ax.set_yticklabels([i[0] for i in items], fontsize=10)
for y, i in zip(ypos, items):
    ax.annotate(f"{i[1]:,.0f} B liters/yr ({i[3]})",
                (i[1] * 1.12, y), va="center", fontsize=9.5, color=TEXT)
ax.set_xscale("log")
ax.set_xlim(30, 3_000_000)
ax.set_xlabel("")
ax.text(0.5, -0.13, "Billion liters per year, log scale", transform=ax.transAxes, ha="center", fontsize=11, color=TEXT)
ax.set_title("National scale check: data centers vs. US water use")
ax.grid(axis="x")
ax.set_axisbelow(True)
fig.text(0.01, -0.02,
         "Withdrawal and consumption are different quantities and are labeled bar by bar;\n"
         "they are shown together only to fix orders of magnitude. USGS figures are 2015,\n"
         "the most recent USGS compilation that reports consumptive use.",
         fontsize=9, color=TEXT_DIM)
save(fig, "national_context.png")

# ---------------------------------------------------------------------------
# (d) Per-prompt water (sources S6, S7)
# Google (Aug 2025, median Gemini Apps text prompt, May 2025):
#   comprehensive method 0.26 mL (onsite consumption only, via WUE 1.15 L/kWh);
#   narrow method 0.12 mL.
# Altman (Jun 2025, as cited in the Google paper): about 0.000085 gallons
#   per query = 0.32 mL; no methodology published.
# Ren et al. (2023): 500 mL per roughly 10 to 50 requests, scope 1 + scope 2,
#   GPT-3-era inference, location and time dependent: 10 to 50 mL per request.
# The viral mutation: "500 mL per prompt" - no source states this.
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9.2, 5.4))
rows = [
    ("As repeated online: \"500 mL per prompt\"", 500, 500, GRAY_BAR,
     "no published source states this"),
    ("Ren et al. 2023, per request (range)", 10, 50, AMBER,
     "500 mL per 10 to 50 requests; incl. electricity water"),
    ("Altman 2025, per query", 0.32, 0.32, PAPER,
     "0.000085 gallons; no method published"),
    ("Google 2025, comprehensive method", 0.26, 0.26, TEAL,
     "median Gemini prompt; onsite water only"),
    ("Google 2025, narrow method", 0.12, 0.12, TEAL_DIM,
     "active machines only; onsite water only"),
]
ypos = np.arange(len(rows))[::-1]
for y, (label, lo, hi, color, note) in zip(ypos, rows):
    if lo == hi:
        ax.barh(y, hi, color=color, height=0.55)
        xlab = hi * 1.5
    else:
        ax.barh(y, hi - lo, left=lo, color=color, height=0.55)
        xlab = hi * 1.5
    ax.annotate(f"{label}: {note}", (xlab, y), va="center", fontsize=9.5,
                color=TEXT)
ax.set_yticks([])
ax.set_xscale("log")
ax.set_xlim(0.05, 200_000)
ax.set_xlabel("")
ax.text(0.5, -0.13, "Water per prompt or request, milliliters, log scale", transform=ax.transAxes, ha="center", fontsize=11, color=TEXT)
ax.set_title("One prompt, four numbers: the gap is method")
ax.grid(axis="x")
ax.set_axisbelow(True)
ax.text(0.0, -0.24,
        "The two families of numbers measure different things. Ren et al. average GPT-3-era\n"
        "inference over locations and include water consumed generating the electricity.\n"
        "Google measures a median 2025 Gemini prompt and counts onsite water only.",
        transform=ax.transAxes, fontsize=9, color=TEXT_DIM, va="top")
save(fig, "per_prompt.png")

# ---------------------------------------------------------------------------
# Hero: the most defensible striking contrast in the package.
# 0.26 mL measured (S7) vs 500 mL as the viral claim is usually told.
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10.67, 6.0))
ax.axis("off")
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.text(5, 5.55, "KNOWN VS. ASSERTED", ha="center", fontsize=15,
        color=TEXT_DIM, fontweight="bold")
ax.text(2.5, 4.35, "500 mL", ha="center", fontsize=54, color=GRAY_BAR,
        fontweight="bold")
ax.text(2.5, 3.55, "water per AI prompt,\nas the claim is usually told",
        ha="center", fontsize=13.5, color=TEXT_DIM)
ax.text(7.5, 4.35, "0.26 mL", ha="center", fontsize=54, color=TEAL,
        fontweight="bold")
ax.text(7.5, 3.55, "measured for a median Gemini\nprompt (Google, Aug 2025)",
        ha="center", fontsize=13.5, color=TEXT)
ax.text(5, 2.55, "No published source states 500 mL per prompt. The sourced figure is\n"
                 "500 mL per 10 to 50 requests (Ren et al. 2023), electricity water included.",
        ha="center", fontsize=13, color=TEXT)
ax.text(5, 1.45, "US data centers, direct water use 2023: 66 billion liters, about 0.015%\n"
                 "of total US withdrawals (LBNL 2024; USGS 2015). The honest story is the gap\n"
                 "between what is disclosed and what is claimed.",
        ha="center", fontsize=13, color=AMBER)
ax.text(5, 0.35, "MACHINE READABLE", ha="center", fontsize=12,
        color=TEXT_DIM, fontweight="bold")
save(fig, "hero.png")
print("done")
