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







from ninja import Ninja
from pirate import Pirate
from character import Character

Bruce = Ninja("Bruce")

Black_Beard = Pirate("Black_Beard")


# Bruce.attack(Black_Beard)
# Black_Beard.show_stats()



while(Black_Beard.health > 0 and Bruce.health > 0):
    
    response=input("Bruce has ingaged in brutal combat, what will he do? \n 1: Attack \n 2: Heal")
    if (response=="1"):
        Bruce.attack(Black_Beard)
    elif(response=="2"):
        Bruce.Heal(Bruce)
        print(f"Bruce Heals: {Bruce.Heal}")
    else:
        print("Enter 1 or 2")
        response=input("Bruce has ingaged in brutal combat, what will he do? \n 1: Attack \n 2: Heal")
    
    