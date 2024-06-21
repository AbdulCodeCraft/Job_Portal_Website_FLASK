from flask import Flask , render_template ,jsonify

app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title' : 'Full Stack Web Developer',
        'location' : 'Chennai,INDIA',
        'Salary' : '20LPA'
    },
    {
        'id':2,
        'title' : 'Full Stack App Developer',
        'location' : 'Chennai,INDIA',
        'Salary' : '24LPA'
    },
    {
        'id':3,
        'title' : 'Dot Net Developer',
        'location' : 'kolakata,INDIA',
        'Salary' : '10LPA'
    },
    {
        'id':4,
        'title' : 'ML Engineer',
        'location' : 'Banglore,INDIA',
        'Salary' : '40LPA'
    },
]

@app.route("/")
def hello_abdul():
    return render_template("home.html",jobs = JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)