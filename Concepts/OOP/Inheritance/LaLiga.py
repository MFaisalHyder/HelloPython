# I am learning Inheritance in Python using my favorite League and its Best Team


class SpanishLeague:
    matches_to_be_played = 720
    total_teams = 20
    matches_per_team = 38
    current_champions = 'Real Madrid'
    most_titles_holder = 'Real Madrid'
    biggest_stadium = 'Camp Nou, Barcelona'

    # Constructor
    def __init__(self, club_name, home_ground, home_ground_capacity, manager_name, asst_manager_name, total_players_in_squad):
        self.clubName = club_name
        self.homeGround = home_ground
        self.homeGroundCapacity = home_ground_capacity
        self.managerName = manager_name
        self.asstManagerName = asst_manager_name
        self.totalSquad = total_players_in_squad

    @classmethod
    def register_club(cls, comma_separated_club_info):
        club_name, home_ground, home_ground_capacity, manager_name, asst_manager_name, total_players_in_squad = comma_separated_club_info.split(",")
        return cls(club_name, home_ground, home_ground_capacity, manager_name, asst_manager_name, total_players_in_squad)
