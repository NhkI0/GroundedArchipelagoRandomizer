# LOCATIONS
from data.milk_molars import milk_molars
from data.chips import chips
from data.key_items import key_items
from data.landmarks import landmarks

# ITEMS
from data.mutations import mutations
from data.tools import tools
from data.milk_molars import augmentations


def expand_progressive(items_dict: dict) -> list:
    progressive_list = []
    for item in items_dict:
        if items_dict[item]["PHASES"] > 1:
            progressive_list.extend([f"Progressive {item}" for _ in range(items_dict[item]["PHASES"])])
        else:
            progressive_list.append(item)
    return progressive_list


def can_access(location: str, inventory: list) -> bool:
    # all_locations[location]["REQUIRED"]
    return True


def create_locations() -> tuple[dict, list]:
    locations_dict = dict(milk_molars)
    locations_dict.update(chips)
    locations_dict.update(key_items)
    locations_dict.update(landmarks)

    locations_list = list(milk_molars.keys()) + list(chips.keys()) + list(key_items.keys()) + list(landmarks.keys())

    print("Locations per category:")
    print(f"\tMilk molars: {len(milk_molars)}\n\tChips: {len(chips)}\n\tKey items: {len(key_items)}"
          f"\n\tLandmarks: {len(landmarks)}")
    return locations_dict, locations_list


def create_items() -> tuple[dict, list]:
    progressives_mutations = expand_progressive(mutations)
    progressives_augmentations = expand_progressive(augmentations)

    items_dict = dict(mutations)
    items_dict.update(tools)
    items_dict.update(chips)
    items_dict.update(key_items)
    items_dict.update(augmentations)

    items_list = (progressives_mutations
                  + list(tools.keys())
                  + list(chips.keys())
                  + list(key_items.keys())
                  + progressives_augmentations)
    return items_dict, items_list


all_locations_dict, all_locations_list = create_locations()
all_items_dict, all_items_list = create_items()

print("Items per category:")
print(f"\tMutations: {len(expand_progressive(mutations))}\n\tTools: {len(tools)}\n\tChips: {len(chips)}\n\tKey Items: "
      f"{len(key_items)}\n\tAugmentations: {len(expand_progressive(augmentations))}")
print(f"\nAll locations size: {len(all_locations_list)}\nAll items size: {len(all_items_list)}")
