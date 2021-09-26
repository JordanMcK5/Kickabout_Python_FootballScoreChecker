from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.fixture import Fixture
import repositories.fixture_repository as fixture_repository
import repositories.team_repository as team_repository

fixtures_blueprint = Blueprint("fixtures", __name__)

#declaring route for all fixtures
@fixtures_blueprint.route("/fixtures")
def fixtures():
    return render_template("fixtures/index.html")