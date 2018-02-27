"""
This is the way to import files(classes) in Python
There must be an empty __init__.py file in the same directory to enable importing across sibling files
"""""

from .LaLiga import SpanishLeague


class RealMadrid(SpanishLeague):
    pass
