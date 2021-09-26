from db.run_sql import run_sql

from models.fixture import Fixture
from models.team import Team
import repositories.team_repository as team_repository

def save(fixture):
    sql = "INSERT INTO fixtures (home_team, away_team, result, points, date, kick_off) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [fixture.team.id, fixture.team.id, fixture.result, fixture.points, fixture.date, fixture.kick_off]
    results = run_sql(sql, values)
    id = results[0]['id']
    fixture_id = id
    return fixture 
