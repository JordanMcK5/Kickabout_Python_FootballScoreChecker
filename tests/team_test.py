import unittest
from models.team import Team

class TestTeam(unittest.TestCase):

    def setUp(self):
        self.team = Team("celtic")

    def test_team_has_name(self):
        self.assertEqual("celtic", self.team.name)