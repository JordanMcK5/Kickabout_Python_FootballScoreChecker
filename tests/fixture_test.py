import unittest
from models.fixture import Fixture

class TestFixture(unittest.TestCase):

    def setUp(self):
        self.fixture = Fixture("celtic", 3, "rangers", 2)

    def test_fixture_has_home_team(self):
        self.assertEqual("celtic", self.fixture.home_team)

    def test_fixture_has_home_score(self):
        self.assertEqual(3, self.fixture.home_score)

    def test_fixture_has_away_team(self):
        self.assertEqual("rangers", self.fixture.away_team)

    def test_fixture_has_away_score(self):
        self.assertEqual(2, self.fixture.away_score)
        
        

    
       
        
    
    
    
   

    