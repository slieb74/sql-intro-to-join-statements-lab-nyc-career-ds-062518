CREATE TABLE superheroes (
  id INTEGER PRIMARY KEY,
  name TEXT,
  real_identity TEXT,
  superpower TEXT,
  weakness TEXT,
  squad_id INTEGER
);

CREATE TABLE squads (
  id INTEGER PRIMARY KEY,
  name TEXT
);
