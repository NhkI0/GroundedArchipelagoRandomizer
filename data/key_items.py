from data import MANAGER_AREA_ACCESS, SUPER_TECH, FINAL_ZONE_ACCESS, FINAL_EVENT_ACCESS
from data import MOSSY_KEY_REQUIRED, MINOTAUR_MAZE_KEY_REQUIRED, MELTED_MOAT_KEY_REQUIRED, STICKY_KEY_REQUIRED
from data import UNDERWATER, WATER_LIGHTING, WATER_BREATHING
from data import TIER_2_KNIFE_REQUIRED, TIER_3_HAMMER_REQUIRED, TIER_2_SHOVEL_REQUIRED

key_items = {
    "Asst Manager Keycard":
        {"REQUIREMENTS": [], "GRANTS": [MANAGER_AREA_ACCESS]},
    "ZIP.R":
        {"REQUIREMENTS": [MANAGER_AREA_ACCESS], "GRANTS": []},
    "SCA.B Replacement Fuse":
        {"REQUIREMENTS": [{"type": SUPER_TECH, "count": 4}, TIER_3_HAMMER_REQUIRED], "GRANTS": [FINAL_ZONE_ACCESS]},
    "Embiggening Cell":
        {"REQUIREMENTS": [{"type": SUPER_TECH, "count": 2}], "GRANTS": [FINAL_EVENT_ACCESS]},
    "Password Scribble: Y--":
        {"REQUIREMENTS": [], "GRANTS": []},
    "Password Scribble: -UR":
        {"REQUIREMENTS": [], "GRANTS": []},
    "Password Scribble: T19":
        {"REQUIREMENTS": [], "GRANTS": []},
    "Password Scribble: 58":
        {"REQUIREMENTS": [], "GRANTS": []},
    "Mossy Key":
        {"REQUIREMENTS": [UNDERWATER, WATER_LIGHTING, WATER_BREATHING], "GRANTS": [MOSSY_KEY_REQUIRED]},
    "Minotaur Maze Key":
        {"REQUIREMENTS": [TIER_2_KNIFE_REQUIRED], "GRANTS": [MINOTAUR_MAZE_KEY_REQUIRED]},
    "Melted Moat Key":
        {"REQUIREMENTS": [TIER_2_SHOVEL_REQUIRED], "GRANTS": [MELTED_MOAT_KEY_REQUIRED]},
    "Sticky Key":
        {"REQUIREMENTS": [TIER_2_SHOVEL_REQUIRED], "GRANTS": [STICKY_KEY_REQUIRED]},
}