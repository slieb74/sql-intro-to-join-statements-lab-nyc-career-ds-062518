# Write your SQL queries inside the strings below.  If you choose to write your queries on multiple lines, make sure to wrap your query inside """triple quotes""".  Use "single quotes" if your query fits on one line.

def select_hero_names_and_squad_names_of_heroes_belonging_to_a_team():
    return """SELECT superheroes.name, squads.name as team FROM superheroes
              JOIN squads ON superheroes.squad_id = squads.id;"""

def reformatted_query():
    return """SELECT superheroes.name, squads.name as team FROM superheroes
              JOIN squads ON superheroes.squad_id = squads.id ORDER BY team;"""

def all_superheroes():
    return """SELECT superheroes.name, superpower, squads.name as team FROM superheroes
              LEFT JOIN squads ON superheroes.squad_id = squads.id ORDER BY team;"""

def all_squads():
    return """SELECT squads.name, COUNT(superheroes.name) as num_of_members FROM squads LEFT JOIN superheroes ON superheroes.squad_id = squads.id GROUP BY squads.name;"""
