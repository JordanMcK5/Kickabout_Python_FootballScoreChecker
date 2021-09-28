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
team3 = Team("Burnbank")
team_repository.save(team3)
team4 = Team("Kilsyth Athletic")
team_repository.save(team4)
team5 = Team("Milton")
team_repository.save(team5)
team6 = Team("Stonehouse")
team_repository.save(team6)

team_repository.select_all()


fixture1 = Fixture(team1, 3, team2, 2)
fixture_repository.save(fixture1)

fixture2 = Fixture(team3, 7, team5, 1)
fixture_repository.save(fixture2)

fixture3 = Fixture(team4, 5, team5, 1)
fixture_repository.save(fixture3)

fixture4 = Fixture(team1, 6, team5, 2)
fixture_repository.save(fixture4)

pdb.set_trace()

