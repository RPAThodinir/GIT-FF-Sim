# Historical data for simulation (Weeks 1 to 9)
historical_data = {
    (1, "The Team With No Name", "Michael's Majestic Team"): (134.62, 92.22),
    (1, "Fantasy Wizard", "The Gibbly Plumps"): (80.66, 86.14),
    (1, "Teddy's Terrific Team", "Nightmare Tornado Supernova"): (108.52, 121.38),
    (1, "Steamrollers", "The Happy Pancakes"): (135.58, 120.76),
    (1, "Thor's Glass Hammer", "Ken's Impressive Team"): (83, 57.16),
    (2, "The Team With No Name", "The Gibbly Plumps"): (99.7, 111.14),
    (2, "Fantasy Wizard", "Nightmare Tornado Supernova"): (116, 150.94),
    (2, "Teddy's Terrific Team", "Steamrollers"): (98.58, 103.96),
    (2, "Thor's Glass Hammer", "The Happy Pancakes"): (125.34, 107.72),
    (2, "Ken's Impressive Team", "Michael's Majestic Team"): (119.74, 106.02),
    (3, "The Team With No Name", "Nightmare Tornado Supernova"): (78.72, 120.78),
    (3, "Fantasy Wizard", "Steamrollers"): (69.26, 123.72),
    (3, "Teddy's Terrific Team", "The Happy Pancakes"): (132.58, 92.46),
    (3, "Thor's Glass Hammer", "Michael's Majestic Team"): (123.42, 78.78),
    (3, "The Gibbly Plumps", "Ken's Impressive Team"): (67.48, 119.46),
    (4, "The Team With No Name", "Steamrollers"): (106.78, 108.7),
    (4, "Fantasy Wizard", "The Happy Pancakes"): (117.6, 87.64),
    (4, "Teddy's Terrific Team", "Thor's Glass Hammer"): (98.64, 106.22),
    (4, "Nightmare Tornado Supernova", "Ken's Impressive Team"): (117.48, 90.66),
    (4, "The Gibbly Plumps", "Michael's Majestic Team"): (82.4, 119.52),
    (5, "The Team With No Name", "The Happy Pancakes"): (139.44, 103.38),
    (5, "Fantasy Wizard", "Teddy's Terrific Team"): (72.74, 139.12),
    (5, "Steamrollers", "Ken's Impressive Team"): (83.54, 111.62),
    (5, "Thor's Glass Hammer", "The Gibbly Plumps"): (88.26, 95.84),
    (5, "Nightmare Tornado Supernova", "Michael's Majestic Team"): (121.3, 168.76),
    (6, "The Team With No Name", "Teddy's Terrific Team"): (133.54, 122.12),
    (6, "Fantasy Wizard", "Thor's Glass Hammer"): (75.08, 98.8),
    (6, "Steamrollers", "Michael's Majestic Team"): (120, 98.36),
    (6, "Nightmare Tornado Supernova", "The Gibbly Plumps"): (111.56, 112.9),
    (6, "The Happy Pancakes", "Ken's Impressive Team"): (82.02, 97.66),
    (7, "The Team With No Name", "Fantasy Wizard"): (118.28, 78.64),
    (7, "Teddy's Terrific Team", "Ken's Impressive Team"): (114.04, 103.44),
    (7, "Steamrollers", "The Gibbly Plumps"): (114.02, 72.5),
    (7, "Thor's Glass Hammer", "Nightmare Tornado Supernova"): (131.6, 113.26),
    (7, "The Happy Pancakes", "Michael's Majestic Team"): (83.26, 103.26),
    (8, "The Team With No Name", "Thor's Glass Hammer"): (111.46, 126.94),
    (8, "Fantasy Wizard", "Ken's Impressive Team"): (126.4, 79.06),
    (8, "Teddy's Terrific Team", "Michael's Majestic Team"): (102.56, 128.34),
    (8, "Steamrollers", "Nightmare Tornado Supernova"): (134.64, 126.38),
    (8, "The Gibbly Plumps", "The Happy Pancakes"): (103.88, 109.52),
    (9, "The Team With No Name", "Ken's Impressive Team"): (126.14, 104.64),
    (9, "Fantasy Wizard", "Michael's Majestic Team"): (133.04, 132.4),
    (9, "Teddy's Terrific Team", "The Gibbly Plumps"): (88.9, 156.34),
    (9, "Steamrollers", "Thor's Glass Hammer"): (123.88, 68.92),
    (9, "Nightmare Tornado Supernova", "The Happy Pancakes"): (89.36, 117.42)
}

def get_historical_data(week, team1, team2):
    """Retrieve the points scored in a specific week for a matchup"""
    if (week, team1, team2) in historical_data:
        return historical_data[(week, team1, team2)]
    else:
        return None
