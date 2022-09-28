from character import Character
class Pirate(Character):

    def __init__( self , name , strength = 14, speed = 2, health = 100):
        super().__init__( name, strength, speed, health)
        self.strength = strength
        self.speed = speed
        self.health = health

    # def show_stats( self ):
    #     print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    
    def attack ( self , pirate ):

        pirate.health -= self.strength
        return self
        
    def Heal ( self , pirate ):
        pirate.health += 1
        return self


