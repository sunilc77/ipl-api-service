from flask import Flask,jsonify,request
import ipl
from ipl import teamsAPI

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello Wolrd"


@app.route('/api/teams')
def teams():
    teams = ipl.teamsAPI()
    return jsonify(teams)

@app.route('/api/teamvteam')
def teamvteam():
    team1 = request.args.get('team1')
    print(team1)
    team2 = request.args.get('team2')
    print(team2)
    response = ipl.teamVteamAPI(team1,team2)
    print(response)
    return jsonify(response)


app.run(debug=True)
