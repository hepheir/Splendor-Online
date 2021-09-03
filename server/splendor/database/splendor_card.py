from dataclasses import dataclass
from typing import List, Union

from splendor.database import get_database_connection


@dataclass
class SplendorCard:
    card_id: int
    card_level: int
    card_score: int
    card_bonus: str
    card_illustration: str
    card_cost_diamond: int
    card_cost_sapphire: int
    card_cost_emerald: int
    card_cost_ruby: int
    card_cost_onyx: int


def get_card_by_id(card_id: int) -> Union[SplendorCard, None]:
    """데이터베이스로 부터 카드 데이터를 찾아 반환합니다.

    만약 데이터가 없다면 `None`을 반환합니다.
    """
    with get_database_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
            SELECT
                card_id,
                card_level,
                card_score,
                card_bonus,
                card_illustration,
                card_cost_diamond,
                card_cost_sapphire,
                card_cost_emerald,
                card_cost_ruby,
                card_cost_onyx
            FROM
                SplendorCard
            WHERE
                card_id=?
        """, (card_id,))
        query_row = cursor.fetchone()
    if not query_row:
        print(f'Could not find card with id "{card_id}"')
        return None
    else:
        return SplendorCard(*query_row)


def get_all_cards_by_level(card_level: int) -> List[SplendorCard]:
    """데이터 베이스로부터 특정 레벨에 해당하는 모든 카드들을 가져옵니다.
    """
    with get_database_connection() as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT
                card_id,
                card_level,
                card_score,
                card_bonus,
                card_illustration,
                card_cost_diamond,
                card_cost_sapphire,
                card_cost_emerald,
                card_cost_ruby,
                card_cost_onyx
            FROM
                SplendorCard
            WHERE
                card_level=?
        """, (card_level,))
        query_rows = cursor.fetchall()
    return [SplendorCard(*row) for row in query_rows]
