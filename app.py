from flask import Flask, render_template, jsonify

app = Flask(__name__)

MEETWAARDEN = [
  {
    'id': 1,
    'omschrijving': 'P-7301 A/B',
    'waarde': '3 bar',
  },
  {
    'id': 2,
    'omschrijving': 'P-7302 A/B',
    'waarde': '2,5 bar',
  },
  {
    'id': 3,
    'omschrijving': 'P-7303 A/B',
    'waarde': '3,5 bar',
  },
]

@app.route("/")
def hello_world():
  return render_template('home.html',
                        meetwaarden=MEETWAARDEN)
@app.route("/api/meetwaarden")
def list_meetwaarden():
  return jsonify(MEETWAARDEN)

print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)