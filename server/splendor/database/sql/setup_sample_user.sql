DROP TABLE IF EXISTS User;
CREATE TABLE User (
    user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    user_name TEXT NOT NULL,
    user_password TEXT NOT NULL,
    user_is_online INTEGER DEFAULT 0,
    game_id INTEGER DEFAULT NULL
);
INSERT INTO User (user_name, user_password)
VALUES
    ('Hepheir', 'password'),
    ('cityboy_gimhae', 'password'),
    ('isuke12', 'password'),
    ('koreair', 'password'),
    ('Nangman', 'password'),
    ('skackdgus', 'password'),
    ('vmfoslkim', 'password'),
    ('whggf', 'password'),
    ('wjdwnsghks123', 'password'),
    ('zxxzx1515', 'password'),
    ('himkmk', 'password'),
    ('JayLoui', 'password'),
    ('OKHENRY2', 'password');
