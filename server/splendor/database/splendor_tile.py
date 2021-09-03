from dataclasses import dataclass
from typing import List

from splendor.database import get_database_connection


@dataclass
class SplendorTile:
    tile_id: int
    tile_score: int
    tile_illustration: str
    tile_cost_diamond: int
    tile_cost_sapphire: int
    tile_cost_emerald: int
    tile_cost_ruby: int
    tile_cost_onyx: int


def get_tile_by_id(tile_id: int) -> SplendorTile:
    with get_database_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
            SELECT
                tile_id,
                tile_score,
                tile_illustration,
                tile_cost_diamond,
                tile_cost_sapphire,
                tile_cost_emerald,
                tile_cost_ruby,
                tile_cost_onyx
            FROM
                SplendorTile
            WHERE
                tile_id=?
        """, (tile_id,))
        query_row = cursor.fetchone()

    if not query_row:
        print(f'Could not find tile with id "{tile_id}"')
        return None
    else:
        return SplendorTile(*query_row)


def get_random_tiles(n_tiles: int) -> List[SplendorTile]:
    with get_database_connection() as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT
                tile_id,
                tile_score,
                tile_illustration,
                tile_cost_diamond,
                tile_cost_sapphire,
                tile_cost_emerald,
                tile_cost_ruby,
                tile_cost_onyx
            FROM
                SplendorTile
            ORDER BY
                RANDOM()
            LIMIT
                ?
        """, (n_tiles,))
        query_rows = cursor.fetchall()
    return [SplendorTile(*row) for row in query_rows]
