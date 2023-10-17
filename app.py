from flask import Flask, render_template, jsonify

app = Flask(__name__)


JOBS = [
    {"id": 1, "title": "Data Analyst", "location": "RJ, Brazil", "salary": "R$4.000"},
    {"id": 2, "title": "Data Scientist", "location": "BH, Brazil", "salary": "R$5.000"},
    {"id": 3, "title": "Frontend Engineer", "location": "Remote", "salary": "R$10.000"},
    {
        "id": 4,
        "title": "Backend Engineer",
        "location": "SP, Brazil",
        "salary": "R$3.000",
    },
    {
        "id": 5,
        "title": "Fullstack Developer",
        "location": "SP, Brazil",
    },
]


@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS, company="Xaropinho")


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
