DROP TABLE IF EXISTS SplendorTile;
CREATE TABLE SplendorTile (
    tile_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    tile_score INTEGER,
    tile_illustration TEXT,
    tile_cost_diamond INTEGER,
    tile_cost_sapphire INTEGER,
    tile_cost_emerald INTEGER,
    tile_cost_ruby INTEGER,
    tile_cost_onyx INTEGER
);
INSERT INTO SplendorTile (tile_score, tile_illustration, tile_cost_diamond, tile_cost_sapphire, tile_cost_emerald, tile_cost_ruby, tile_cost_onyx)
VALUES
    (3, 'noble.mary_stuart', 0, 0, 4, 4, 0),
    (3, 'noble.soliman_the_magniflcent', 0, 4, 4, 0, 0),
    (3, 'noble.noble_macchiavelli', 4, 4, 0, 0, 0),
    (3, 'noble.isabel_of_castille', 4, 0, 0, 0, 4),
    (3, 'noble.henri_viii', 0, 0, 0, 4, 4),
    (3, 'noble.elisabeth_of_austria', 3, 3, 0, 0, 3),
    (3, 'noble.francis_i_of_france', 0, 0, 3, 3, 3),
    (3, 'noble.charles_quint', 3, 0, 0, 3, 3),
    (3, 'noble.catherine_of_medicis', 0, 3, 3, 3, 0),
    (3, 'noble.anne_of_brittany', 3, 3, 3, 0, 0);
