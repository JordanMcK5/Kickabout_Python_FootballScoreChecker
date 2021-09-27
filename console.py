import pdb
from models.team import Team
from models.fixture import Fixture
import repositories.team_repository as team_repository
import repositories.fixture_repository as fixture_repository

team_repository.delete_all()
fixture_repository.delete_all()

team1 = Team("Mill United")
team_repository.save(team1)
team2 = Team("Campsie")
team_repository.save(team2)
team3 = Team("Celtic")
team_repository.save(team3)
team4 = Team("Aberdeen")
team_repository.save(team4)
team5 = Team("Rangers")
team_repository.save(team5)

fixture1 = Fixture(team1, 3, team2, 2)
fixture_repository.save(fixture1)

fixture2 = Fixture(team1, 3, team5, 0)
fixture_repository.save(fixture2)

fixture3 = Fixture(team3, 5, team4, 0)
fixture_repository.save(fixture3)

pdb.set_trace()

