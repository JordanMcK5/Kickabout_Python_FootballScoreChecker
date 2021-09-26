DROP TABLE IF EXISTS fixtures;
DROP TABLE IF EXISTS teams;

CREATE TABLE teams (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  points INT
);

CREATE TABLE fixtures (
  home_team_id INT REFERENCES teams (id) ON DELETE CASCADE,
  home_team_score INT,
  away_team_id INT REFERENCES teams (id) ON DELETE CASCADE,
  away_team_score INT,
  date DATE,
  kick off VARCHAR(100) 
  points INT REFERENCES teams (id) ON DELETE CASCADE
);