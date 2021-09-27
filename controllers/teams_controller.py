from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.team import Team
import repositories.team_repository as team_repository
import repositories.fixture_repository as fixture_repository


teams_blueprint = Blueprint("teams", __name__)

@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    return render_template("teams/index.html", all_teams = teams)

@teams_blueprint.route("/teams/new", methods = ["GET"])
def add_team():
    teams = team_repository.select_all()
    return render_template("teams/new.html", teams = teams )
