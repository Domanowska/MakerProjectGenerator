import random
from typing import List

from src.materials import materials
from src.objects import objects


def generate_ideas(how_many: int) -> List[str]:
    ideas = []
    for i in range(how_many):
        ran_object = random.randint(0, len(objects) - 1)
        ran_material = random.randint(9, len(materials) - 1)
        ideas.append(f"Build {objects[ran_object]} out of {materials[ran_material]}.")
    return ideas


if __name__ == "__main__":
    num_of_ideas = input("How many ideas do you want to generate? ")
    list_of_ideas = generate_ideas(int(num_of_ideas))
    for idea in list_of_ideas:
        print(idea)
