import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/lvl-5-spells")
def lvl_5_spells():
    aenwyns_spellcasting = []
    with open("data/aenwyns_spellcasting.json", "r") as json_data:
        aenwyns_spellcasting = json.load(json_data)
    return render_template("lvl-5-spells.html", page_title="Level 5 Spells", aenwyns_spellcasting=aenwyns_spellcasting)


@app.route("/lvl-4-spells")
def lvl_4_spells():
    aenwyns_spellcasting = []
    with open("data/aenwyns_spellcasting.json", "r") as json_data:
        aenwyns_spellcasting = json.load(json_data)
    return render_template("lvl-4-spells.html", page_title="Level 4 Spells", aenwyns_spellcasting=aenwyns_spellcasting)


@app.route("/lvl-3-spells")
def lvl_3_spells():
    spellranges = []
    with open("data/spellranges.json", "r") as json_data:
        spellranges = json.load(json_data)
    return render_template("lvl-3-spells.html", page_title="Level 3 Spells", spellranges=spellranges)


@app.route("/lvl-2-spells")
def lvl_2_spells():
    spellranges = []
    with open("data/spellranges.json", "r") as json_data:
        spellranges = json.load(json_data)
    return render_template("lvl-2-spells.html", page_title="Level 2 Spells", spellranges=spellranges)


@app.route("/lvl-1-spells")
def lvl_1_spells():
    spellranges = []
    with open("data/spellranges.json", "r") as json_data:
        spellranges = json.load(json_data)
    return render_template("lvl-1-spells.html", page_title="Level 1 Spells", spellranges=spellranges)


@app.route("/lvl-0-spells")
def lvl_0_spells():
    spellranges = []
    with open("data/spellranges.json", "r") as json_data:
        spellranges = json.load(json_data)
    return render_template("lvl-0-spells.html", page_title="Level 0 Spells", spellranges=spellranges)


@app.route("/spelltactics")
def spelltactics():
    return render_template("spelltactics.html", page_title="Spell Tactics")


@app.route("/handy-haversack")
def handy_haversack():
    return render_template("handy-haversack.html", page_title="Handy Haversack")


@app.route("/magic-items")
def magic_items():
    return render_template("magic-items.html", page_title="Magic Items")


if __name__ == "__main__":
    app.run(
     host=os.environ.get("IP"),
     port=int(os.environ.get("PORT")),
     debug=True
    )
