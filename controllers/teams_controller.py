from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.team import Team
import repositories.fixture_repository as fixture_repository
import repositories.team_repository as team_repository

teams_blueprint = Blueprint("teams", __name__)

@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    return render_template("teams/index.html", teams = teams)

@teams_blueprint.route("/teams/<id>")
def show(id):
    team = team_repository.select(id)
    fixtures = team_repository.fixtures(teams)
    return render_template("teams/show.html", team=team, fixtures=fixtures)