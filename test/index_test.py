import unittest, sqlite3
import sys
sys.path.insert(0, '..')
from sql_queries import *

connection = sqlite3.connect('./superheroes.db')
cursor = connection.cursor()

class TestJoinStatements(unittest.TestCase):

    def test_select_hero_names_and_squad_names_of_heroes_belonging_to_a_team(self):
        result = [('Batman', 'Justice League'), ('Superman', 'Justice League'), ('Thor', 'Avengers'), ('Iron Man', 'Avengers'), ('Wonder Woman', 'Justice League'), ('Captain America', 'Avengers'), ('Aquaman', 'Justice League'), ('Black Panther', 'Avengers'), ('Black Widow', 'Avengers'), ('Hulk', 'Avengers'), ('Cyborg', 'Justice League'), ('Green Lantern', 'Justice League')]
        self.assertEqual(cursor.execute(select_hero_names_and_squad_names_of_heroes_belonging_to_a_team()).fetchall(), result)

    def test_reformatted_query(self):
        result = [('Thor', 'Avengers'), ('Iron Man', 'Avengers'), ('Captain America', 'Avengers'), ('Black Panther', 'Avengers'), ('Black Widow', 'Avengers'), ('Hulk', 'Avengers'), ('Batman', 'Justice League'), ('Superman', 'Justice League'), ('Wonder Woman', 'Justice League'), ('Aquaman', 'Justice League'), ('Cyborg', 'Justice League'), ('Green Lantern', 'Justice League')]
        self.assertEqual(cursor.execute(reformatted_query()).fetchall(), result)

    def test_all_superheroes(self):
        result = [('Megaman', 'elemental-mechanical physiology', None), ('StretcherFlex', 'enhanced flexibility', None), ('Goku', 'superstrength', None), ('Thor', 'summons lightning', 'Avengers'), ('Iron Man', 'ultra smart', 'Avengers'), ('Captain America', 'superstrength', 'Avengers'), ('Black Panther', 'speed and agility', 'Avengers'), ('Black Widow', 'expert martial artist', 'Avengers'), ('Hulk', 'rage', 'Avengers'), ('Batman', 'works hard', 'Justice League'), ('Superman', 'superstrength', 'Justice League'), ('Wonder Woman', 'superstrength', 'Justice League'), ('Aquaman', 'breaths underwater', 'Justice League'), ('Cyborg', 'technorganic physiology', 'Justice League'), ('Green Lantern', 'magic ring', 'Justice League')]
        self.assertEqual(cursor.execute(all_superheroes()).fetchall(), result)

    def test_all_squads(self):
        result = [('Avengers', 6), ('Justice League', 6), ('The Illuminati', 0)]
        self.assertEqual(cursor.execute(all_squads()).fetchall(), result)
