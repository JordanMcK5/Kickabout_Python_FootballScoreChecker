DROP TABLE IF EXISTS fixtures;
DROP TABLE IF EXISTS teams;

CREATE TABLE teams (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE fixtures (
  id SERIAL PRIMARY KEY,
  home_team INT REFERENCES teams(id) ON DELETE CASCADE,
  home_score INT,
  away_team INT REFERENCES teams(id) ON DELETE CASCADE,
  away_score INT,
  home_win BOOLEAN
);