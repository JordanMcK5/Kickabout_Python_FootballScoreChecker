from db.run_sql import run_sql
from models.team import Team
from models.fixture import Fixture

def save(team):
    sql = "INSERT INTO teams (name) VALUES (%s) RETURNING *"
    values = [team.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    team_id = id
    return team 

def select_all():
    teams = []
    
    sql = "SELECT * FROM teams"
    results = run_sql(sql)

    for row in results:
        team = Team(row['name'], row['id'])
        teams.append(team)
    return teams

def select(id):
    team = None
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        team = Team(result['name'], result['id'] )
    return team


def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(team):
    sql = "UPDATE teams SET (name) = (%s) WHERE id = %s"
    values = [team.name, team.id]
    run_sql(sql, values)

def fixtures(team):
    fixtures = []

    sql = "SELECT * FROM fixtures WHERE team_id = %s"
    values = [team.id]
    results = run_sql(sql, values)

    for row in results:
        fixture = Fixture(team, row['home_score'], team, row['away_score'], row['id'] )
        fixtures.append(fixture)
    return fixtures