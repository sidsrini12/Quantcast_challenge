import unittest
import datetime
from src.most_active_cookie import find_cookie_count, most_active_cookie



class TestCookie(unittest.TestCase):
    def setUp(self):
        self.cookie_file = 'test/cookie_log.csv'
        self.test_date_1 = datetime.date.fromisoformat('2018-12-07')

    def test_find_cookie_count(self):
        self.assertEqual(find_cookie_count(self.cookie_file,
                                           self.test_date_1), [('4sMM2LxV07bPJzwf', 1)])

        with self.assertRaises(FileNotFoundError):
            find_cookie_count('cookielog.csv', self.test_date_1)

        with self.assertRaises(KeyError):
            find_cookie_count('test/bad_header.csv', self.test_date_1)

        with self.assertRaises(ValueError):
            find_cookie_count('test/bad_log.csv', self.test_date_1)

    def test_most_active_cookie(self):
        self.assertEqual(most_active_cookie(
            [('4sMM2LxV07bPJzwf', 2), ('5sfM2LxV07bPJzwf', 1)]), ['4sMM2LxV07bPJzwf'])
        self.assertEqual(most_active_cookie(
            [('AtY0laUfhglK3lC7', 2), ('SAZuXPGUrfbcn5UA', 2), ('5UAVanZf6UtGyKVS', 1)]), ['AtY0laUfhglK3lC7', 'SAZuXPGUrfbcn5UA'])

        with self.assertRaises(IndexError):
            most_active_cookie([])


