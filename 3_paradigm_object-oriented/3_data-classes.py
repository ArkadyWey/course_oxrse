import dataclasses
import typing

# Data classes are where we don't need methods only attriibutes and their type
@dataclasses.dataclass
class Academic:
    name: str
    papers: list 

alice = Academic("Alice",[])
print(alice.papers)