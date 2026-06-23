import pytest

from randomizer import can_access


def test_nominal_case():
    assert can_access("Pond: Sunken T-Rex", ["Bone Dagger", "Bubble Helmet"])


def test_not_enough_case():
    assert not can_access("Pond: Sunken T-Rex", ["Bone Dagger"])


def test_no_items_pass():
    assert can_access("Grassland: Field Station 2", [])


def test_wrong_location():
    assert not can_access("European Parliament", ["Bone Dagger", "Bubble Helmet"])


def test_wrong_item_pass():
    assert can_access("Grassland: Field Station 2", ["Bone Dagger", "Cool Item", "Bubble Helmet"])


def test_wrong_item_fail():
    assert not can_access("Pond: Sunken T-Rex", ["Bone Dagger", "Cool Item", "Antlion Armor"])


def test_upper_tier_pass():
    assert can_access("Grassland: Field Station 1", ["Black Ox Hammer"])


def test_counter_pass():
    assert can_access("Embiggening Cell", ["Bone Dagger",
                                           "Black Anthill BURG.L Chip",
                                           "Haze BURG.L Chip",
                                           "Pond BURG.L Chip",
                                           "Woodpile BURG.L Chip"])


def test_counter_fail():
    assert not can_access("Embiggening Cell", ["Bone Dagger",
                                           "Black Anthill BURG.L Chip",
                                           "Woodpile BURG.L Chip"])


def test_counter_fail_no_chips():
    assert not can_access("Embiggening Cell", ["Bone Dagger"])
