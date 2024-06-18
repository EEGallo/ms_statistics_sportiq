import unittest
from flask import current_app
from app import create_app, db
from ms_statistics_sportiq.app.models.statistic import Statistic
from app.services.statistic_services import StatisticService

service = StatisticService()

class StatisticsTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)

    def test_statistics(self):
        statistics = Statistic()
        statistics.events_participated = "10"
        statistics.wins = "10"
        statistics.losses = "10"
        statistics.goals_scored = "10"
        statistics.assists = "10"
        statistics.heights = "10"
        statistics.weight = "10"
        self.assertEqual(statistics.events_participated, "10")
        self.assertEqual(statistics.wins, "10")
        self.assertEqual(statistics.losses, "10")
        self.assertEqual(statistics.goals_scored, "10")
        self.assertEqual(statistics.assists, "10")
        self.assertEqual(statistics.heights, "10")
        self.assertEqual(statistics.weight, "10")


    def test_create_statistics(self):
        statistics = self.create_statistics()
        self.assertGreaterEqual(statistics.id, 1)

    def create_statistics(self):
        statistics = Statistic()
        statistics.events_participated = "10"
        statistics.wins = "10"
        statistics.losses = "10"
        statistics.goals_scored = "10"
        statistics.assists = "10"
        statistics.heights = "10"
        statistics.weight = "10"
        service.create(statistics)
        return statistics

    def test_find_by_id(self):
        _ = self.create_statistics()
        statistics = service.find_by_id(1)
        self.assertIsNotNone(statistics) 
        self.assertEqual(statistics.events_participated, "10")
        self.assertEqual(statistics.wins, "10")
        self.assertEqual(statistics.losses, "10")
        self.assertEqual(statistics.goals_scored, "10")
        self.assertEqual(statistics.assists, "10")
        self.assertEqual(statistics.heights, "10")
        self.assertEqual(statistics.weight, "10")
        

    def test_find_all(self):
        _ = self.create_statistics()
        statistics = service.find_all()
        self.assertGreaterEqual(len(statistics), 1)

    def test_update(self):
        statistics=self.create_statistics()
        statistics.events_participated = "10"
        statistics.wins = "10"
        statistics.losses = "10"
        statistics.goals_scored = "10"
        statistics.assists = "10"
        statistics.heights = "10"
        statistics.weight = "10"
        service.update(statistics, 1)
        result = service.find_by_id(1)
        self.assertEqual(statistics.events_participated, statistics.events_participated)
        self.assertEqual(statistics.wins, statistics.wins)
        self.assertEqual(statistics.losses, statistics.losses)
        self.assertEqual(statistics.goals_scored, statistics.goals_scored)
        self.assertEqual(statistics.assists, statistics.assists)
        self.assertEqual(statistics.heights, statistics.heights)
        self.assertEqual(statistics.weight, statistics.weight)

    def test_delete(self):
        _ = self.create_statistics()
        service.delete(1)
        statistics = service.find_all()
        self.assertEqual(len(statistics), 0)

if __name__ == '_main_':
    unittest.main()