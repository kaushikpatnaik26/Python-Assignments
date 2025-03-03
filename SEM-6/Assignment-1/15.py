from dataclasses import dataclass
from collections import namedtuple

PersonNT = namedtuple("Person", ["name", "age"])
p1 = PersonNT("Messi", 37)
print("NamedTuple:", p1)
@dataclass
class PersonDC:
    name: str
    age: int 
p2 = PersonDC("Kaushik", 21)
print("Dataclass:", p2)


