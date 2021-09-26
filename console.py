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

team_repository.select_all()

fixture = Fixture(team1, 2, team2, 1, team1)
fixture_repository.save(fixture)

pdb.set_trace()

