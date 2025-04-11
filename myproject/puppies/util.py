from myproject import db
from myproject.models import Puppy

def Get_Puppies():
    print("Function Get_Puppies used")
    puppies = Puppy.query.all()
    return puppies