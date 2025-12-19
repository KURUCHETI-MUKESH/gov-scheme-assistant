from flask import Flask, render_template, request
import csv

app = Flask(__name__)

def load_schemes():
    schemes = []
    with open("schemes.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            schemes.append(row)
    return schemes

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        question = request.form["question"].lower()
        language = request.form["language"]

        schemes = load_schemes()
        for scheme in schemes:
            if (scheme["scheme"].lower() in question
                and scheme["language"].lower() == language.lower()):
                response = scheme["description"]
                break

        if response == "":
            response = "Scheme not found"

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
