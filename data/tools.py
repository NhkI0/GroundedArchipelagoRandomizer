from data import EXPLOSIVES_REQUIRED, UNDERWATER, TIER_2_KNIFE_REQUIRED
from data import TIER_1_SHOVEL_REQUIRED, TIER_2_SHOVEL_REQUIRED
from data import TIER_1_HAMMER_REQUIRED, TIER_2_HAMMER_REQUIRED, TIER_3_HAMMER_REQUIRED
from data import TIER_1_AXE_REQUIRED, TIER_2_AXE_REQUIRED, TIER_3_AXE_REQUIRED

MELEE = "MELEE"
BUSTING = "BUSTING"
CHOPPING = "CHOPPING"
DIGGING = "DIGGING"
RANGED = "RANGED"
EXPLOSIVE = "EXPLOSIVE"
LIGHT = "LIGHT"
REPAIR = "REPAIR"
SHIELD = "SHIELD"
MISC = "MISC"
UNCATEGORIZED = "UNCATEGORIZED"

# DAMAGE TYPES
FRESH = "FRESH"
SPICY = "SPICY"
SALTY = "SALTY"
SOUR = "SOUR"
CRIT_DAZE = "CRIT_DAZE"
LIFE_STEAL = "LIFE_STEAL"
YOKED_BLOWS = "YOKED_BLOWS"
INFECTION = "INFECTION"
VENOM = "VENOM"
POISON = "POISON"
CRITICAL_HIT_CHANCE = "CRITICAL_HIT_CHANCE"
BLEED = "BLEED"
GAS_HAZARD = "GAS_HAZARD"
ROUGH_RELOAD = "ROUGH_RELOAD"
MINOR_THREAT = "MINOR_THREAT"
MINUS_DAMAGE_RESIST = "MINUS_DAMAGE_RESIST"
MINUS_MOVEMENT_SPEED = "MINUS_MOVEMENT_SPEED"
FLYERS_STUN = "FLYERS_STUN"
DEFENSIVE_STANCE = "DEFENSIVE_STANCE"
BLOCK_CORROSION = "BLOCK_CORROSION"
EXPLOSIVE_RESIST = "EXPLOSIVE_RESIST"
VICTORY_FEAST = "VICTORY_FEAST"
SHORT_CIRCUIT = "SHORT_CIRCUIT"


tools = {
    # Melees weapon
    "Mint Mace": {"CATEGORY": MELEE, "TIER": 3, "DAMAGE_TYPES": [FRESH], "GRANTS": []},
    "Club of the Mother Demon": {"CATEGORY": MELEE, "TIER": 3, "DAMAGE_TYPES": [], "GRANTS": []},
    "Antlion Greatsword": {"CATEGORY": MELEE, "TIER": 3, "DAMAGE_TYPES": [], "GRANTS": []},
    "Salt Morning Star": {"CATEGORY": MELEE, "TIER": 3, "DAMAGE_TYPES": [SALTY], "GRANTS": []},
    "Spicy Coaltana": {"CATEGORY": MELEE, "TIER": 3, "DAMAGE_TYPES": [SPICY], "GRANTS": []},
    "Fire Ant Club": {"CATEGORY": MELEE, "TIER": 3, "DAMAGE_TYPES": [CRIT_DAZE], "GRANTS": []},
    "Tick Macuahuitl": {"CATEGORY": MELEE, "TIER": 3, "DAMAGE_TYPES": [LIFE_STEAL], "GRANTS": []},
    "Scythe of Blossoms": {"CATEGORY": MELEE, "TIER": 3, "DAMAGE_TYPES": [YOKED_BLOWS], "GRANTS": []},
    "Toenail Scimitar": {"CATEGORY": MELEE, "TIER": 3, "DAMAGE_TYPES": [INFECTION], "GRANTS": []},
    "Widow Dagger": {"CATEGORY": MELEE, "TIER": 3, "DAMAGE_TYPES": [VENOM], "GRANTS": [TIER_2_KNIFE_REQUIRED]},
    "Rusty Spear": {"CATEGORY": MELEE, "TIER": 3, "DAMAGE_TYPES": [INFECTION], "GRANTS": []},
    "Acid Edge": {"CATEGORY": MELEE, "TIER": 3, "DAMAGE_TYPES": [SOUR], "GRANTS": []},
    "Tiger Mosquito Rapier": {"CATEGORY": MELEE, "TIER": 3, "DAMAGE_TYPES": [LIFE_STEAL], "GRANTS": []},
    "Sizzle Striker": {"CATEGORY": MELEE, "TIER": 3, "DAMAGE_TYPES": [SPICY], "GRANTS": []},
    "Pucker Thumper": {"CATEGORY": MELEE, "TIER": 3, "DAMAGE_TYPES": [SOUR], "GRANTS": []},
    "Fresh Coldtana": {"CATEGORY": MELEE, "TIER": 3, "DAMAGE_TYPES": [FRESH], "GRANTS": []},
    "Sour Katanga": {"CATEGORY": MELEE, "TIER": 3, "DAMAGE_TYPES": [SOUR], "GRANTS": []},
    "Fresh Edge": {"CATEGORY": MELEE, "TIER": 3, "DAMAGE_TYPES": [FRESH], "GRANTS": []},
    "Blazing Edge": {"CATEGORY": MELEE, "TIER": 3, "DAMAGE_TYPES": [SPICY], "GRANTS": []},
    "Breathslayer": {"CATEGORY": MELEE, "TIER": 3, "DAMAGE_TYPES": [FRESH], "GRANTS": []},
    "Tingle Tongue": {"CATEGORY": MELEE, "TIER": 3, "DAMAGE_TYPES": [SOUR], "GRANTS": []},
    "Frosted Flake": {"CATEGORY": MELEE, "TIER": 3, "DAMAGE_TYPES": [FRESH], "GRANTS": []},
    "Pepper Flake": {"CATEGORY": MELEE, "TIER": 3, "DAMAGE_TYPES": [SPICY], "GRANTS": []},
    "Wallopeño": {"CATEGORY": MELEE, "TIER": 3, "DAMAGE_TYPES": [SPICY], "GRANTS": []},
    "Pickemaul": {"CATEGORY": MELEE, "TIER": 3, "DAMAGE_TYPES": [SOUR], "GRANTS": []},
    "Salt Chipper": {"CATEGORY": MELEE, "TIER": 3, "DAMAGE_TYPES": [SALTY], "GRANTS": []},
    "Fungnir": {"CATEGORY": MELEE, "TIER": 3, "DAMAGE_TYPES": [], "GRANTS": []},
    "Stinger Spear": {"CATEGORY": MELEE, "TIER": 2, "DAMAGE_TYPES": [CRITICAL_HIT_CHANCE], "GRANTS": []},
    "Red Ant Club": {"CATEGORY": MELEE, "TIER": 2, "DAMAGE_TYPES": [], "GRANTS": []},
    "Spider Fang Dagger": {"CATEGORY": MELEE, "TIER": 2, "DAMAGE_TYPES": [POISON], "GRANTS": [TIER_2_KNIFE_REQUIRED]},
    "Mosquito Needle": {"CATEGORY": MELEE, "TIER": 2, "DAMAGE_TYPES": [LIFE_STEAL], "GRANTS": []},
    "Black Ant Sword": {"CATEGORY": MELEE, "TIER": 2, "DAMAGE_TYPES": [], "GRANTS": []},
    "Ant Queen Scepter": {"CATEGORY": MELEE, "TIER": 2, "DAMAGE_TYPES": [], "GRANTS": []},
    "Pebblet Spear": {"CATEGORY": MELEE, "TIER": 1, "DAMAGE_TYPES": [], "GRANTS": []},
    "Spiky Sprig": {"CATEGORY": MELEE, "TIER": 1, "DAMAGE_TYPES": [BLEED], "GRANTS": []},
    "Larva Blade": {"CATEGORY": MELEE, "TIER": 1, "DAMAGE_TYPES": [POISON], "GRANTS": []},
    # Busting
    "Black Ox Hammer": {"CATEGORY": BUSTING, "TIER": 3, "DAMAGE_TYPES": [], "GRANTS": [TIER_3_HAMMER_REQUIRED]},
    "Insect Hammer": {"CATEGORY": BUSTING, "TIER": 2, "DAMAGE_TYPES": [], "GRANTS": [TIER_2_HAMMER_REQUIRED]},
    "Pebblet Hammer": {"CATEGORY": BUSTING, "TIER": 1, "DAMAGE_TYPES": [], "GRANTS": [TIER_1_HAMMER_REQUIRED]},
    # Chopping
    "Termite Axe": {"CATEGORY": CHOPPING, "TIER": 3, "DAMAGE_TYPES": [], "GRANTS": [TIER_3_AXE_REQUIRED]},
    "Insect Axe": {"CATEGORY": CHOPPING, "TIER": 2, "DAMAGE_TYPES": [], "GRANTS": [TIER_2_AXE_REQUIRED]},
    "Pebblet Axe": {"CATEGORY": CHOPPING, "TIER": 1, "DAMAGE_TYPES": [], "GRANTS": [TIER_1_AXE_REQUIRED]},
    # Digging
    "Black Ant Shovel": {"CATEGORY": DIGGING, "TIER": 2, "DAMAGE_TYPES": [], "GRANTS": [TIER_2_SHOVEL_REQUIRED]},
    "Acorn Shovel": {"CATEGORY": DIGGING, "TIER": 1, "DAMAGE_TYPES": [], "GRANTS": [TIER_1_SHOVEL_REQUIRED]},
    # Ranged
    "Splinter Arrow": {"CATEGORY": RANGED, "TIER": 3, "DAMAGE_TYPES": [], "GRANTS": []},
    "Super Gas Arrow": {"CATEGORY": RANGED, "TIER": 3, "DAMAGE_TYPES": [GAS_HAZARD], "GRANTS": []},
    "Mint Staff": {"CATEGORY": RANGED, "TIER": 3, "DAMAGE_TYPES": [FRESH], "GRANTS": []},
    "Spicy Staff": {"CATEGORY": RANGED, "TIER": 3, "DAMAGE_TYPES": [SPICY], "GRANTS": []},
    "Sour Staff": {"CATEGORY": RANGED, "TIER": 3, "DAMAGE_TYPES": [SOUR], "GRANTS": []},
    "Super Venom Arrow": {"CATEGORY": RANGED, "TIER": 3, "DAMAGE_TYPES": [POISON], "GRANTS": []},
    "Bomb Arrow": {"CATEGORY": RANGED, "TIER": 3, "DAMAGE_TYPES": [], "GRANTS": []},
    "Black Ox Crossbow": {"CATEGORY": RANGED, "TIER": 3, "DAMAGE_TYPES": [ROUGH_RELOAD], "GRANTS": []},
    "Sour Arrow": {"CATEGORY": RANGED, "TIER": 3, "DAMAGE_TYPES": [SOUR], "GRANTS": []},
    "Bard's Bow": {"CATEGORY": RANGED, "TIER": 3, "DAMAGE_TYPES": [MINOR_THREAT], "GRANTS": []},
    "Ant Queen Staff": {"CATEGORY": RANGED, "TIER": 3, "DAMAGE_TYPES": [], "GRANTS": []},
    "Burny Rounds": {"CATEGORY": RANGED, "TIER": 3, "DAMAGE_TYPES": [MINUS_DAMAGE_RESIST], "GRANTS": []},
    "Splody Rounds": {"CATEGORY": RANGED, "TIER": 3, "DAMAGE_TYPES": [], "GRANTS": []},
    "'Merica Rounds": {"CATEGORY": RANGED, "TIER": 3, "DAMAGE_TYPES": [], "GRANTS": []},
    "Blaster of the Moldy Matriarch": {"CATEGORY": RANGED, "TIER": 3, "DAMAGE_TYPES": [], "GRANTS": []},
    "Insect Bow": {"CATEGORY": RANGED, "TIER": 2, "DAMAGE_TYPES": [], "GRANTS": []},
    "Crow Crossbow": {"CATEGORY": RANGED, "TIER": 2, "DAMAGE_TYPES": [ROUGH_RELOAD], "GRANTS": []},
    "Feather Arrow": {"CATEGORY": RANGED, "TIER": 2, "DAMAGE_TYPES": [], "GRANTS": []},
    "Salt Arrow": {"CATEGORY": RANGED, "TIER": 2, "DAMAGE_TYPES": [SALTY], "GRANTS": []},
    "Mint Arrow": {"CATEGORY": RANGED, "TIER": 2, "DAMAGE_TYPES": [FRESH], "GRANTS": []},
    "Spicy Arrow": {"CATEGORY": RANGED, "TIER": 2, "DAMAGE_TYPES": [SPICY], "GRANTS": []},
    "Roman Candle": {"CATEGORY": RANGED, "TIER": 2, "DAMAGE_TYPES": [], "GRANTS": []},
    "Pointy Rounds": {"CATEGORY": RANGED, "TIER": 2, "DAMAGE_TYPES": [], "GRANTS": []},
    "Sappy Rounds": {"CATEGORY": RANGED, "TIER": 2, "DAMAGE_TYPES": [MINUS_MOVEMENT_SPEED], "GRANTS": []},
    "Sprig Bow": {"CATEGORY": RANGED, "TIER": 1, "DAMAGE_TYPES": [], "GRANTS": []},
    "Arrow": {"CATEGORY": RANGED, "TIER": 1, "DAMAGE_TYPES": [], "GRANTS": []},
    "Venom Arrow": {"CATEGORY": RANGED, "TIER": 1, "DAMAGE_TYPES": [], "GRANTS": []},
    "Lure Arrow": {"CATEGORY": RANGED, "TIER": 1, "DAMAGE_TYPES": [], "GRANTS": []},
    "Gas Arrow": {"CATEGORY": RANGED, "TIER": 1, "DAMAGE_TYPES": [GAS_HAZARD], "GRANTS": []},
    "Pollen Arrow": {"CATEGORY": RANGED, "TIER": 1, "DAMAGE_TYPES": [MINUS_MOVEMENT_SPEED, FLYERS_STUN], "GRANTS": []},
    "Rocky Rounds": {"CATEGORY": RANGED, "TIER": 1, "DAMAGE_TYPES": [], "GRANTS": []},
    "Groundy Rounds": {"CATEGORY": RANGED, "TIER": 1, "DAMAGE_TYPES": [], "GRANTS": []},
    # Explosive
    "Killbasa": {"CATEGORY": EXPLOSIVE, "TIER": 3, "DAMAGE_TYPES": [], "GRANTS": [EXPLOSIVES_REQUIRED]},
    "Splatburst": {"CATEGORY": EXPLOSIVE, "TIER": 2, "DAMAGE_TYPES": [], "GRANTS": [EXPLOSIVES_REQUIRED]},
    "Bratburst": {"CATEGORY": EXPLOSIVE, "TIER": 1, "DAMAGE_TYPES": [], "GRANTS": [EXPLOSIVES_REQUIRED]},
    # Light
    "EverChar Torch": {"CATEGORY": LIGHT, "TIER": 2, "DAMAGE_TYPES": [], "GRANTS": []},
    "Torch": {"CATEGORY": LIGHT, "TIER": 1, "DAMAGE_TYPES": [], "GRANTS": []},
    "Torch+": {"CATEGORY": LIGHT, "TIER": 1, "DAMAGE_TYPES": [], "GRANTS": []},
    "Slime Mold Torch": {"CATEGORY": LIGHT, "TIER": 0, "DAMAGE_TYPES": [], "GRANTS": []},
    # Repair
    "Ant Queen Repair Tool": {"CATEGORY": REPAIR, "TIER": 0, "DAMAGE_TYPES": [], "GRANTS": []},
    "Repair Tool": {"CATEGORY": REPAIR, "TIER": 0, "DAMAGE_TYPES": [], "GRANTS": []},
    # Shield
    "Fire Ant Shield": {"CATEGORY": SHIELD, "TIER": 3, "DAMAGE_TYPES": [DEFENSIVE_STANCE, BLOCK_CORROSION], "GRANTS": []},
    "Ladybird Shield": {"CATEGORY": SHIELD, "TIER": 3, "DAMAGE_TYPES": [DEFENSIVE_STANCE, BLOCK_CORROSION], "GRANTS": []},
    "Infected Ant Shield": {"CATEGORY": SHIELD, "TIER": 3, "DAMAGE_TYPES": [DEFENSIVE_STANCE, EXPLOSIVE_RESIST], "GRANTS": []},
    "Black Ant Shield": {"CATEGORY": SHIELD, "TIER": 2, "DAMAGE_TYPES": [DEFENSIVE_STANCE], "GRANTS": []},
    "Weevil Shield": {"CATEGORY": SHIELD, "TIER": 1, "DAMAGE_TYPES": [DEFENSIVE_STANCE], "GRANTS": []},
    # Underwater
    "Bone Dagger": {"CATEGORY": UNDERWATER, "TIER": 2, "DAMAGE_TYPES": [], "GRANTS": [UNDERWATER, TIER_2_KNIFE_REQUIRED]},
    "Bone Trident": {"CATEGORY": UNDERWATER, "TIER": 2, "DAMAGE_TYPES": [], "GRANTS": [UNDERWATER]},
    "Pebblet Dagger": {"CATEGORY": UNDERWATER, "TIER": 1, "DAMAGE_TYPES": [], "GRANTS": [UNDERWATER]},
    "Slime Lantern": {"CATEGORY": UNDERWATER, "TIER": 0, "DAMAGE_TYPES": [], "GRANTS": [UNDERWATER]},
    "Slime Lantern+": {"CATEGORY": UNDERWATER, "TIER": 0, "DAMAGE_TYPES": [], "GRANTS": [UNDERWATER]},
    # Misc
    "Decoy Bait": {"CATEGORY": MISC, "TIER": 0, "DAMAGE_TYPES": [], "GRANTS": []},
    "Basketball": {"CATEGORY": MISC, "TIER": 0, "DAMAGE_TYPES": [], "GRANTS": []},
    "Pupa Basketball": {"CATEGORY": MISC, "TIER": 0, "DAMAGE_TYPES": [], "GRANTS": []},
    # Uncategorized
    # "BURG.L's Old Flipper": {"CATEGORY": UNCATEGORIZED, "TIER": 3, "DAMAGE_TYPES": [VICTORY_FEAST], "GRANTS": []},
    # "Infused Axe": {"CATEGORY": UNCATEGORIZED, "TIER": 4, "DAMAGE_TYPES": [], "GRANTS": []},
    # "Infused Blaster": {"CATEGORY": UNCATEGORIZED, "TIER": 4, "DAMAGE_TYPES": [], "GRANTS": []},
    # "Infused Bow": {"CATEGORY": UNCATEGORIZED, "TIER": 4, "DAMAGE_TYPES": [], "GRANTS": []},
    # "Infused Club": {"CATEGORY": UNCATEGORIZED, "TIER": 4, "DAMAGE_TYPES": [], "GRANTS": []},
    # "Infused Crossbow": {"CATEGORY": UNCATEGORIZED, "TIER": 4, "DAMAGE_TYPES": [], "GRANTS": []},
    # "Infused Dagger": {"CATEGORY": UNCATEGORIZED, "TIER": 4, "DAMAGE_TYPES": [], "GRANTS": []},
    # "Infused Greatsword": {"CATEGORY": UNCATEGORIZED, "TIER": 4, "DAMAGE_TYPES": [], "GRANTS": []},
    # "Infused Hammer": {"CATEGORY": UNCATEGORIZED, "TIER": 4, "DAMAGE_TYPES": [], "GRANTS": []},
    # "Infused Scythe": {"CATEGORY": UNCATEGORIZED, "TIER": 4, "DAMAGE_TYPES": [], "GRANTS": []},
    # "Infused Spear": {"CATEGORY": UNCATEGORIZED, "TIER": 4, "DAMAGE_TYPES": [], "GRANTS": []},
    # "Infused Sword": {"CATEGORY": UNCATEGORIZED, "TIER": 4, "DAMAGE_TYPES": [], "GRANTS": []},
    # "Pinch Whacker": {"CATEGORY": UNCATEGORIZED, "TIER": 3, "DAMAGE_TYPES": [SHORT_CIRCUIT], "GRANTS": []},
    # "Prod Smacker": {"CATEGORY": UNCATEGORIZED, "TIER": 3, "DAMAGE_TYPES": [SHORT_CIRCUIT], "GRANTS": []},
}
