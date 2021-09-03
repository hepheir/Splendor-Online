from dataclasses import asdict

from splendor.database import setup_sample_data
from splendor.database.splendor_card import get_all_cards_by_level, get_card_by_id, SplendorCard


setup_sample_data()


def test_get_non_existing_card():
    assert get_card_by_id(-1) is None


def test_get_an_existing_card():
    assert asdict(get_card_by_id(4)) == asdict(SplendorCard(
        card_id=4,
        card_level=1,
        card_score=1,
        card_bonus='onyx',
        card_illustration='onyx.mine',
        card_cost_diamond=0,
        card_cost_sapphire=4,
        card_cost_emerald=0,
        card_cost_ruby=0,
        card_cost_onyx=0
    ))


def test_number_of_splendor_components_cards():
    assert len(get_all_cards_by_level(1)) == 40
    assert len(get_all_cards_by_level(2)) == 30
    assert len(get_all_cards_by_level(3)) == 20
