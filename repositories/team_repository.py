from db.run_sql import run_sql

from models.team import Team
from models.fixture import Fixture

def save(team):
    sql = "INSERT INTO teams (name, points) VALUES (%s, %s) RETURNING *"
    values = [team.name, team.points]
    results = run_sql(sql, values)
    id = results[0]['id']
    team_id = id
    return team 