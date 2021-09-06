DROP TABLE IF EXISTS user; -- DEBUG
DROP TABLE IF EXISTS game; -- DEBUG
DROP TABLE IF EXISTS game_component; -- DEBUG


CREATE TABLE IF NOT EXISTS user (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT NOT NULL,
    game_id INTEGER DEFAULT NULL,
    FOREIGN KEY (game_id) REFERENCES game(game_id)
);


CREATE TABLE IF NOT EXISTS game (
    game_id INTEGER PRIMARY KEY,
    game_state INTEGER NOT NULL,
    game_turn INTEGER NOT NULL,
    FOREIGN KEY (game_id) REFERENCES user(user_id)
);


CREATE TABLE IF NOT EXISTS game_component (
    game_id INTEGER NOT NULL,
    component_id INTEGER NOT NULL,
    component_type INTEGER NOT NULL,
    owner_id INTEGER DEFAULT NULL,
    FOREIGN KEY (game_id) REFERENCES game(game_id),
    FOREIGN KEY (owner_id) REFERENCES user(user_id),
    PRIMARY KEY (game_id, component_id, component_type)
);
