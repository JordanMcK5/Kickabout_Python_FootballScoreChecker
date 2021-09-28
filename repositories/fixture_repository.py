from db.run_sql import run_sql
from models.fixture import Fixture
from models.team import Team
import repositories.team_repository as team_repository

def save(fixture):
    sql = "INSERT INTO fixtures (home_team, home_score, away_team, away_score, home_win) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [fixture.home_team.id, fixture.home_score, fixture.away_team.id, fixture.away_score, fixture.home_win]
    results = run_sql(sql, values)
    id = results[0]['id']
    fixture.id = id
    return fixture


def select_all():
    fixtures = []
    sql = "SELECT * FROM fixtures"
    results = run_sql(sql)
    for row in results:
        home_team = team_repository.select(row['home_team'])
        away_team = team_repository.select(row['away_team'])
        fixture = Fixture(home_team, row['home_score'], away_team, row['away_score'],row['home_win'], row['id'] )
        fixtures.append(fixture)
    return fixtures

def select(id):
    fixture = None
    sql = "SELECT * FROM fixtures WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        team = team_repository.select(result['team_id'])
        fixture = Fixture(team, result['home_score'], team, result['away_score'], result['home_win'], result['id'])
    return fixture


def delete_all():
    sql = "DELETE  FROM fixtures"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM fixtures WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(fixture):
    sql = "UPDATE fixtures SET (home_team, home_score, away_team, away_score, home_win) VALUES (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [fixture.home_team.id, fixture.home_score, fixture.away_team.id, fixture.away_score, fixture.home_win]
    run_sql(sql, values)
    
