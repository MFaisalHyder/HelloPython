"""
This is the way to import files(classes) in Python
There must be an empty __init__.py file in the same directory to enable importing across sibling files
"""""

from .LaLiga import SpanishLeague


class RealMadrid(SpanishLeague):
    # Every attribute and method available in SpanishLeague (parent class) is available to current class as well.

    LaLiga = 'La_liga'
    Copa_Del_Rey = 'copa_del_rey'

    def register_club(self, comma_separated_club_info_str):
        SpanishLeague.register_club(comma_separated_club_info_str)

    def la_liga_schedule(self):
        pass

    def copa_del_rey_schedule(self):
        pass

    def champions_league_schedule(self):
        pass

    def match_schedule(self, specific_league):
        if (specific_league == RealMadrid.LaLiga):
            RealMadrid.la_liga_schedule()
        elif (specific_league == RealMadrid.Copa_Del_Rey):
            RealMadrid.copa_del_rey_schedule()
        else:
            RealMadrid.champions_league_schedule()


# This functions helps to visualize easily the hierarchy of inherited class and Method resolution order
print(help(RealMadrid))
