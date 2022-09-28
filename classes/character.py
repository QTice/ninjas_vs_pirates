class Character:

    def __init__( self , name, strength, speed, health):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.health = health
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    # def attack( self , pirate ):
    #     # pirate.health -= self.strength
    #     print(f"Character does {self.strength} damage")
    #     return self



