from model import Creature

dragon = Creature(
    name="dragon",
    description=["incorrect", "string", "list"], #this will cause an error for being a list[str] instead of str
    country="*" ,
    area="*",
    aka="firedrake")