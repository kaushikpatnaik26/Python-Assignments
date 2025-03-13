from dataclasses import dataclass, field

@dataclass
class Employee:
    name: list= field(default_factory = list)
    salary : float = field(default=5000)
    department : str = field(default='IT' ,repr=True)
e1 = Employee()
# add Employee
e1.name.append("Ghays")
# e1.name.append("animesh")
print(e1)
e2 = Employee()
e2.name.append("shobii")
print(e2)