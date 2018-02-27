"""
This is the way to import files(classes) in Python
There must be an empty __init__.py file in the same directory to enable importing across sibling files
"""""

from .LaLiga import SpanishLeague


class RealMadrid(SpanishLeague):
    # Every attribute and method available in SpanishLeague (parent class) is available to current class as well.

    def register_club(self, comma_separated_club_info_str):
        SpanishLeague.register_club(comma_separated_club_info_str)
