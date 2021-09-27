from models.fixture import Fixture
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.team import Team
import repositories.team_repository as team_repository
import repositories.fixture_repository as fixture_repository
import pdb


teams_blueprint = Blueprint("teams", __name__)

#Index
@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    return render_template("teams/index.html", all_teams = teams)

# NEW
# GET
@teams_blueprint.route("/teams/new", methods=['GET'])
def new_team():
    teams = team_repository.select_all()
    return render_template("teams/new.html", all_teams = teams)

# CREATE
# POST
@teams_blueprint.route("/teams",  methods=['POST'])
def create_team():
    name = request.form['name']
    new_team = Team(name)
    team_repository.save(new_team)
    return redirect('/teams')


# SHOW
# GET
@teams_blueprint.route("/teams/<id>", methods=['GET'])
def show_team(id):
    team = team_repository.select(id)
    all_fixtures = fixture_repository.select_all()
    fixtures_for_team = []
    for fixture in all_fixtures:
        if fixture.home_team.id == int(id) or fixture.away_team.id == int(id):
            fixtures_for_team.append(fixture)
    return render_template('teams/show.html', team = team, fixtures = fixtures_for_team)

# EDIT
# GET
@teams_blueprint.route("/teams/<id>/edit")
def edit_team(id):
    team = team_repository.select(id)
    return render_template('teams/edit.html', team = team)

# UPDATE
# POST
@teams_blueprint.route("/teams/<id>", methods=['POST'])
def update_team(id):
    name = request.form['update_name']
    team = Team(name, id)
    team_repository.update(team)
    return redirect('/teams')

# DELETE
# DELETE '/tasks/<id>'
@teams_blueprint.route("/teams/<id>/delete", methods=['POST'])
def delete_team(id):
    team_repository.delete(id)
    return redirect('/teams')