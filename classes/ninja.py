from character import Character
class Ninja(Character):

    def __init__( self , name , strength = 12, speed = 2, health = 100):
        super().__init__( name, strength, speed, health)
        self.strength = strength
        self.speed = speed
        self.health = health
    # def show_stats( self ):
    #     print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")


    def attack ( self , ninja ):
        ninja.health -= self.strength
        return self

    def Heal ( self , ninja ):
        ninja.health += 1
        return self


