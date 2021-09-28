from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.team import Team
from models.fixture import Fixture
import repositories.team_repository as team_repository
import repositories.fixture_repository as fixture_repository


fixtures_blueprint = Blueprint("fixtures", __name__)

#Index
@fixtures_blueprint.route("/fixtures")
def fixtures():
    fixtures = fixture_repository.select_all()
    return render_template("fixtures/index.html", all_fixtures = fixtures)

# NEW
# GET
@fixtures_blueprint.route("/fixtures/new", methods=['GET'])
def new_fixture():
    teams = team_repository.select_all()
    fixtures = fixture_repository.select_all()
    return render_template("fixtures/new.html", all_fixtures = fixtures, all_teams = teams)

# CREATE
# POST
@fixtures_blueprint.route("/fixtures",  methods=['POST'])
def create_fixture():
    home_team = request.form['home_team']
    home_score = request.form['home_score']
    away_team = request.form['away_team']
    away_score = request.form['away_score']
    home_win = request.form['home_win']
    home_team = team_repository.select(home_team)
    away_team = team_repository.select(away_team)
    fixture = Fixture(home_team,home_score,away_team,away_score,home_win, id)
    fixture_repository.save(fixture)
    return redirect('/fixtures')


# SHOW
# GET
@fixtures_blueprint.route("/fixtures/<id>", methods=['GET'])
def show_fixtures(id):
    team = team_repository.select(id)
    fixture = fixture_repository.select()
    return render_template('fixtures/show.html', fixture = fixture, team = team)

# EDIT
# GET
@fixtures_blueprint.route("/fixtures/<id>/edit", methods=['GET'])
def edit_(id):
    fixture = fixture_repository.select(id)
    team = team_repository.select()
    return render_template('fixtures/edit.html', fixture = fixture, team = team)

# UPDATE
# POST
@fixtures_blueprint.route("/fixtures/<id>", methods=['POST'])
def update_fixture(id):
    home_team = request.form['home_team']
    home_score = request.form['home_score']
    away_team = request.form['away_team']
    away_score = request.form['away_score']
    home_win = request.form['home_win']
    home_team = team_repository.select(home_team)
    away_team = team_repository.select(away_team)
    fixture = Fixture(home_team,home_score,away_team,away_score,home_win)
    fixture_repository.update(fixture)
    return redirect('/fixtures')

# DELETE
# DELETE 
@fixtures_blueprint.route("/fixtures/<id>/delete", methods=['POST'])
def delete_fixture(id):
    fixture_repository.delete(id)
    return redirect('/fixtures')

