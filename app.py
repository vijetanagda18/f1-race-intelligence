"""
Formula 1 Race Intelligence - Flask web integration
Embeds the published Tableau Public dashboard and story in a web page.

Run:
    pip install -r requirements.txt
    python app.py
Then open http://127.0.0.1:5000
"""
from flask import Flask, render_template

app = Flask(__name__)

# ---- Edit these if your workbook or sheet names differ -------------------
WORKBOOK = "F1_Race_Intelligence"
DASHBOARD_SHEET = "F1RaceIntelligenceDashboard"   # sheet name with spaces removed
STORY_SHEET = "F1RaceIntelligenceStory"           # check this in your story's link
PROFILE = "vijeta.nagda"
# --------------------------------------------------------------------------

EMBED_BASE = "https://public.tableau.com/views"
PUBLIC_BASE = "https://public.tableau.com/app/profile"


def embed_url(sheet):
    return f"{EMBED_BASE}/{WORKBOOK}/{sheet}"


def public_url(sheet):
    return f"{PUBLIC_BASE}/{PROFILE}/viz/{WORKBOOK}/{sheet}"


@app.route("/")
def dashboard():
    return render_template(
        "viz.html",
        page="dashboard",
        heading="Race Intelligence Dashboard",
        intro="Filter by DNF reason and race year, and set the Top N driver "
              "count. The charts update together.",
        src=embed_url(DASHBOARD_SHEET),
        height=1000,
        open_link=public_url(DASHBOARD_SHEET),
    )


@app.route("/story")
def story():
    return render_template(
        "viz.html",
        page="story",
        heading="Race Intelligence Story",
        intro="Nine scenes, from the global scale of Formula 1 to podium "
              "results. Use the captions to move between scenes.",
        src=embed_url(STORY_SHEET),
        height=1100,
        open_link=public_url(STORY_SHEET),
    )


if __name__ == "__main__":
    app.run(debug=True)
