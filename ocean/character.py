from ocean import sprite

class Character(sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 0

    def heal(health):
        self.health += health


    def damage(health):
        self.health -= health

    def is_dead():
        return self.health <= 0
