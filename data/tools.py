MELEE = "MELEE"
BUSTING = "BUSTING"
CHOPPING = "CHOPPING"
DIGGING = "DIGGING"
RANGED = "RANGED"
EXPLOSIVE = "EXPLOSIVE"
LIGHT = "LIGHT"
REPAIR = "REPAIR"
SHIELD = "SHIELD"
UNDERWATER = "UNDERWATER"
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
    "Mint Mace": {"Category": MELEE, "Tier": 3, "DAMAGE_TYPES": [FRESH]},
    "Club of the Mother Demon": {"Category": MELEE, "Tier": 3, "DAMAGE_TYPES": []},
    "Antlion Greatsword": {"Category": MELEE, "Tier": 3, "DAMAGE_TYPES": []},
    "Salt Morning Star": {"Category": MELEE, "Tier": 3, "DAMAGE_TYPES": [SALTY]},
    "Spicy Coaltana": {"Category": MELEE, "Tier": 3, "DAMAGE_TYPES": [SPICY]},
    "Fire Ant Club": {"Category": MELEE, "Tier": 3, "DAMAGE_TYPES": [CRIT_DAZE]},
    "Tick Macuahuitl": {"Category": MELEE, "Tier": 3, "DAMAGE_TYPES": [LIFE_STEAL]},
    "Scythe of Blossoms": {"Category": MELEE, "Tier": 3, "DAMAGE_TYPES": [YOKED_BLOWS]},
    "Toenail Scimitar": {"Category": MELEE, "Tier": 3, "DAMAGE_TYPES": [INFECTION]},
    "Widow Dagger": {"Category": MELEE, "Tier": 3, "DAMAGE_TYPES": [VENOM]},
    "Rusty Spear": {"Category": MELEE, "Tier": 3, "DAMAGE_TYPES": [INFECTION]},
    "Acid Edge": {"Category": MELEE, "Tier": 3, "DAMAGE_TYPES": [SOUR]},
    "Tiger Mosquito Rapier": {"Category": MELEE, "Tier": 3, "DAMAGE_TYPES": [LIFE_STEAL]},
    "Sizzle Striker": {"Category": MELEE, "Tier": 3, "DAMAGE_TYPES": [SPICY]},
    "Pucker Thumper": {"Category": MELEE, "Tier": 3, "DAMAGE_TYPES": [SOUR]},
    "Fresh Coldtana": {"Category": MELEE, "Tier": 3, "DAMAGE_TYPES": [FRESH]},
    "Sour Katanga": {"Category": MELEE, "Tier": 3, "DAMAGE_TYPES": [SOUR]},
    "Fresh Edge": {"Category": MELEE, "Tier": 3, "DAMAGE_TYPES": [FRESH]},
    "Blazing Edge": {"Category": MELEE, "Tier": 3, "DAMAGE_TYPES": [SPICY]},
    "Breathslayer": {"Category": MELEE, "Tier": 3, "DAMAGE_TYPES": [FRESH]},
    "Tingle Tongue": {"Category": MELEE, "Tier": 3, "DAMAGE_TYPES": [SOUR]},
    "Frosted Flake": {"Category": MELEE, "Tier": 3, "DAMAGE_TYPES": [FRESH]},
    "Pepper Flake": {"Category": MELEE, "Tier": 3, "DAMAGE_TYPES": [SPICY]},
    "Wallopeño": {"Category": MELEE, "Tier": 3, "DAMAGE_TYPES": [SPICY]},
    "Pickemaul": {"Category": MELEE, "Tier": 3, "DAMAGE_TYPES": [SOUR]},
    "Salt Chipper": {"Category": MELEE, "Tier": 3, "DAMAGE_TYPES": [SALTY]},
    "Fungnir": {"Category": MELEE, "Tier": 3, "DAMAGE_TYPES": []},
    "Stinger Spear": {"Category": MELEE, "Tier": 2, "DAMAGE_TYPES": [CRITICAL_HIT_CHANCE]},
    "Red Ant Club": {"Category": MELEE, "Tier": 2, "DAMAGE_TYPES": []},
    "Spider Fang Dagger": {"Category": MELEE, "Tier": 2, "DAMAGE_TYPES": [POISON]},
    "Mosquito Needle": {"Category": MELEE, "Tier": 2, "DAMAGE_TYPES": [LIFE_STEAL]},
    "Black Ant Sword": {"Category": MELEE, "Tier": 2, "DAMAGE_TYPES": []},
    "Ant Queen Scepter": {"Category": MELEE, "Tier": 2, "DAMAGE_TYPES": []},
    "Pebblet Spear": {"Category": MELEE, "Tier": 1, "DAMAGE_TYPES": []},
    "Spiky Sprig": {"Category": MELEE, "Tier": 1, "DAMAGE_TYPES": [BLEED]},
    "Larva Blade": {"Category": MELEE, "Tier": 1, "DAMAGE_TYPES": [POISON]},
    # Busting
    "Black Ox Hammer": {"Category": BUSTING, "Tier": 3, "DAMAGE_TYPES": []},
    "Insect Hammer": {"Category": BUSTING, "Tier": 2, "DAMAGE_TYPES": []},
    "Pebblet Hammer": {"Category": BUSTING, "Tier": 1, "DAMAGE_TYPES": []},
    # Chopping
    "Termite Axe": {"Category": CHOPPING, "Tier": 3, "DAMAGE_TYPES": []},
    "Insect Axe": {"Category": CHOPPING, "Tier": 2, "DAMAGE_TYPES": []},
    "Pebblet Axe": {"Category": CHOPPING, "Tier": 1, "DAMAGE_TYPES": []},
    # Digging
    "Black Ant Shovel": {"Category": DIGGING, "Tier": 2, "DAMAGE_TYPES": []},
    "Acorn Shovel": {"Category": DIGGING, "Tier": 1, "DAMAGE_TYPES": []},
    # Ranged
    "Splinter Arrow": {"Category": RANGED, "Tier": 3, "DAMAGE_TYPES": []},
    "Super Gas Arrow": {"Category": RANGED, "Tier": 3, "DAMAGE_TYPES": [GAS_HAZARD]},
    "Mint Staff": {"Category": RANGED, "Tier": 3, "DAMAGE_TYPES": [FRESH]},
    "Spicy Staff": {"Category": RANGED, "Tier": 3, "DAMAGE_TYPES": [SPICY]},
    "Sour Staff": {"Category": RANGED, "Tier": 3, "DAMAGE_TYPES": [SOUR]},
    "Super Venom Arrow": {"Category": RANGED, "Tier": 3, "DAMAGE_TYPES": [POISON]},
    "Bomb Arrow": {"Category": RANGED, "Tier": 3, "DAMAGE_TYPES": []},
    "Black Ox Crossbow": {"Category": RANGED, "Tier": 3, "DAMAGE_TYPES": [ROUGH_RELOAD]},
    "Sour Arrow": {"Category": RANGED, "Tier": 3, "DAMAGE_TYPES": [SOUR]},
    "Bard's Bow": {"Category": RANGED, "Tier": 3, "DAMAGE_TYPES": [MINOR_THREAT]},
    "Ant Queen Staff": {"Category": RANGED, "Tier": 3, "DAMAGE_TYPES": []},
    "Burny Rounds": {"Category": RANGED, "Tier": 3, "DAMAGE_TYPES": [MINUS_DAMAGE_RESIST]},
    "Splody Rounds": {"Category": RANGED, "Tier": 3, "DAMAGE_TYPES": []},
    "'Merica Rounds": {"Category": RANGED, "Tier": 3, "DAMAGE_TYPES": []},
    "Blaster of the Moldy Matriarch": {"Category": RANGED, "Tier": 3, "DAMAGE_TYPES": []},
    "Insect Bow": {"Category": RANGED, "Tier": 2, "DAMAGE_TYPES": []},
    "Crow Crossbow": {"Category": RANGED, "Tier": 2, "DAMAGE_TYPES": [ROUGH_RELOAD]},
    "Feather Arrow": {"Category": RANGED, "Tier": 2, "DAMAGE_TYPES": []},
    "Salt Arrow": {"Category": RANGED, "Tier": 2, "DAMAGE_TYPES": [SALTY]},
    "Mint Arrow": {"Category": RANGED, "Tier": 2, "DAMAGE_TYPES": [FRESH]},
    "Spicy Arrow": {"Category": RANGED, "Tier": 2, "DAMAGE_TYPES": [SPICY]},
    "Roman Candle": {"Category": RANGED, "Tier": 2, "DAMAGE_TYPES": []},
    "Pointy Rounds": {"Category": RANGED, "Tier": 2, "DAMAGE_TYPES": []},
    "Sappy Rounds": {"Category": RANGED, "Tier": 2, "DAMAGE_TYPES": [MINUS_MOVEMENT_SPEED]},
    "Sprig Bow": {"Category": RANGED, "Tier": 1, "DAMAGE_TYPES": []},
    "Arrow": {"Category": RANGED, "Tier": 1, "DAMAGE_TYPES": []},
    "Venom Arrow": {"Category": RANGED, "Tier": 1, "DAMAGE_TYPES": []},
    "Lure Arrow": {"Category": RANGED, "Tier": 1, "DAMAGE_TYPES": []},
    "Gas Arrow": {"Category": RANGED, "Tier": 1, "DAMAGE_TYPES": [GAS_HAZARD]},
    "Pollen Arrow": {"Category": RANGED, "Tier": 1, "DAMAGE_TYPES": [MINUS_MOVEMENT_SPEED, FLYERS_STUN]},
    "Rocky Rounds": {"Category": RANGED, "Tier": 1, "DAMAGE_TYPES": []},
    "Groundy Rounds": {"Category": RANGED, "Tier": 1, "DAMAGE_TYPES": []},
    # Explosive
    "Killbasa": {"Category": EXPLOSIVE, "Tier": 3, "DAMAGE_TYPES": []},
    "Splatburst": {"Category": EXPLOSIVE, "Tier": 2, "DAMAGE_TYPES": []},
    "Bratburst": {"Category": EXPLOSIVE, "Tier": 1, "DAMAGE_TYPES": []},
    # Light
    "EverChar Torch": {"Category": LIGHT, "Tier": 2, "DAMAGE_TYPES": []},
    "Torch": {"Category": LIGHT, "Tier": 1, "DAMAGE_TYPES": []},
    "Torch+": {"Category": LIGHT, "Tier": 1, "DAMAGE_TYPES": []},
    "Slime Mold Torch": {"Category": LIGHT, "Tier": 0, "DAMAGE_TYPES": []},
    # Repair
    "Ant Queen Repair Tool": {"Category": REPAIR, "Tier": 0, "DAMAGE_TYPES": []},
    "Repair Tool": {"Category": REPAIR, "Tier": 0, "DAMAGE_TYPES": []},
    # Shield
    "Fire Ant Shield": {"Category": SHIELD, "Tier": 3, "DAMAGE_TYPES": [DEFENSIVE_STANCE, BLOCK_CORROSION]},
    "Ladybird Shield": {"Category": SHIELD, "Tier": 3, "DAMAGE_TYPES": [DEFENSIVE_STANCE, BLOCK_CORROSION]},
    "Infected Ant Shield": {"Category": SHIELD, "Tier": 3, "DAMAGE_TYPES": [DEFENSIVE_STANCE, EXPLOSIVE_RESIST]},
    "Black Ant Shield": {"Category": SHIELD, "Tier": 2, "DAMAGE_TYPES": [DEFENSIVE_STANCE]},
    "Weevil Shield": {"Category": SHIELD, "Tier": 1, "DAMAGE_TYPES": [DEFENSIVE_STANCE]},
    # Underwater
    "Bone Dagger": {"Category": UNDERWATER, "Tier": 2, "DAMAGE_TYPES": []},
    "Bone Trident": {"Category": UNDERWATER, "Tier": 2, "DAMAGE_TYPES": []},
    "Pebblet Dagger": {"Category": UNDERWATER, "Tier": 1, "DAMAGE_TYPES": []},
    "Slime Lantern": {"Category": UNDERWATER, "Tier": 0, "DAMAGE_TYPES": []},
    "Slime Lantern+": {"Category": UNDERWATER, "Tier": 0, "DAMAGE_TYPES": []},
    # Misc
    "Decoy Bait": {"Category": MISC, "Tier": 0, "DAMAGE_TYPES": []},
    "Basketball": {"Category": MISC, "Tier": 0, "DAMAGE_TYPES": []},
    "Pupa Basketball": {"Category": MISC, "Tier": 0, "DAMAGE_TYPES": []},
    # Uncategorized
    "BURG.L's Old Flipper": {"Category": UNCATEGORIZED, "Tier": 3, "DAMAGE_TYPES": [VICTORY_FEAST]},
    "Infused Axe": {"Category": UNCATEGORIZED, "Tier": 4, "DAMAGE_TYPES": []},
    "Infused Blaster": {"Category": UNCATEGORIZED, "Tier": 4, "DAMAGE_TYPES": []},
    "Infused Bow": {"Category": UNCATEGORIZED, "Tier": 4, "DAMAGE_TYPES": []},
    "Infused Club": {"Category": UNCATEGORIZED, "Tier": 4, "DAMAGE_TYPES": []},
    "Infused Crossbow": {"Category": UNCATEGORIZED, "Tier": 4, "DAMAGE_TYPES": []},
    "Infused Dagger": {"Category": UNCATEGORIZED, "Tier": 4, "DAMAGE_TYPES": []},
    "Infused Greatsword": {"Category": UNCATEGORIZED, "Tier": 4, "DAMAGE_TYPES": []},
    "Infused Hammer": {"Category": UNCATEGORIZED, "Tier": 4, "DAMAGE_TYPES": []},
    "Infused Scythe": {"Category": UNCATEGORIZED, "Tier": 4, "DAMAGE_TYPES": []},
    "Infused Spear": {"Category": UNCATEGORIZED, "Tier": 4, "DAMAGE_TYPES": []},
    "Infused Sword": {"Category": UNCATEGORIZED, "Tier": 4, "DAMAGE_TYPES": []},
    "Pinch Whacker": {"Category": UNCATEGORIZED, "Tier": 3, "DAMAGE_TYPES": [SHORT_CIRCUIT]},
    "Prod Smacker": {"Category": UNCATEGORIZED, "Tier": 3, "DAMAGE_TYPES": [SHORT_CIRCUIT]},
}
