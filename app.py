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


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for object in data:
            if object["url"] == member_name:
                member = object
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/lvl-5-spells")
def lvl_5_spells():
    spellranges = []
    spellcasting = []
    with open("data/spellranges.json", "r") as json_data:
        spellranges = json.load(json_data)
    with open("data/spellcasting.json", "r") as json_data:
        spellcasting = json.load(json_data)
    return render_template("lvl-5-spells.html", page_title="Level 5 Spells", spellranges=spellranges, spellcasting=spellcasting)


@app.route("/lvl-4-spells")
def lvl_4_spells():
    return render_template("lvl-4-spells.html", page_title="Level 4 Spells")


@app.route("/lvl-3-spells")
def lvl_3_spells():
    return render_template("lvl-3-spells.html", page_title="Level 3 Spells")


@app.route("/lvl-2-spells")
def lvl_2_spells():
    return render_template("lvl-2-spells.html", page_title="Level 2 Spells")


@app.route("/lvl-1-spells")
def lvl_1_spells():
    return render_template("lvl-1-spells.html", page_title="Level 1 Spells")


@app.route("/lvl-0-spells")
def lvl_0_spells():
    return render_template("lvl-0-spells.html", page_title="Level 0 Spells")


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
