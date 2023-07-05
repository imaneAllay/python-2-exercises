import random
class Character:
    def __init__(self, hit_point):
        self.hit_point = hit_point

    def fight(self, character):
        random_number = random.randint(1, 20)
        character.hit_point -= random_number
        if character.hit_point < 0:
            character.hit_point = 0

    def __repr__(self):
        return f"{self.__class__.__name__}:{self.hit_point} hit point."


class Fighter(Character):
    pass


class Dwarf(Character):
    pass
