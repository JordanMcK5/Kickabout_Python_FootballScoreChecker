from db.run_sql import run_sql

from models.fixture import Fixture
from models.team import Team
import repositories.team_repository as team_repository

pass


def save(fixture):
    sql = "INSERT INTO fixtures (home_team_id, home_score, away_team_id, away_score) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [fixture.home_team.id, fixture.home_score, fixture.away_team.id, fixture.away_score]
    results = run_sql(sql, values)
    id = results[0]['id']
    fixture.id = id
    return fixture


def select_all():
    fixtures = []

    sql = "SELECT * FROM fixtures"
    results = run_sql(sql)

    for row in results:
        team = team_repository.select(row['team_id'])
        fixture = Fixture(team, row['home_score'], team, row['away_score'], row['id'] )
        fixtures.append(fixture)
    return fixtures



def select(id):
    fixture = None
    sql = "SELECT * FROM fixtures WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        team = team_repository.select(result['team_id'])
        fixture = Fixture(team, result['home_score'], team, result['away_score'], result['id'])
    return fixture


def delete_all():
    sql = "DELETE  FROM fixtures"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM fixtures WHERE id = %s"
    values = [id]
    run_sql(sql, values)