import random
class Player:
    def __init__(self, name):  
      self.name=name
      self.hp=100
      self.inventory=[]
    
    def display_inventory(self):
        if self.inventory:
          print("Inventory" , ", ".join(self.inventory))
        else:
          print("Inventory is empty.")
      
    def display_hp(self):
      print(f"Health Points: {self.hp}")
    
class Riddle:
    def __init__ (self,question,answer):
      self.question=question
      self.answer=answer
      
    def askToUser(self):
      print("Riddle:" , self.question)
      user_answer = input("Answer: ").strip().lower()
      return user_answer==self.answer
 

class Event:
    def __init__ (self, description, effect, value):
      self.description=description
      self.effect=effect
      self.value=value
      
    def trigger(self,player):
        print(self.description)
        if self.effect== "heal":
          player.hp+=self.value
          print(f"You gain {self.value} HP")
        elif self.effect == "damage":
          player.hp-=self.value
          print(f"You lose {self.value} HP")
        elif self.effect == "item":
          player.inventory.append(self.value)
          print(f"You add a {self.value} to your inventory")
        
class Game:
    def __init__ (self,player):
      self.player=player
      self.riddles=[
        Riddle("I’m tall when I’m young, and I’m short when I’m old. What am I?", "a candle"),
        Riddle("What kind of ship has two mates but no captain?", "a relationship"),
        Riddle("What month of the year has 28 days?", "all months"),
        Riddle("If you drop a yellow hat in the Red Sea, what does it become?", "wet"),
        Riddle("What goes up but never comes down?","your age"),
        Riddle("What gets wet while drying?","towel")
      ]
      self.events = [
            Event("You find a healing potion!", "heal", 30),
            Event("A wild boar attacks you!", "damage", 15),
            Event("You find a shiny sword!", "item", "sword")
        ]
      
    def display_Intro(self):
      print("Welcome to the adventure world")
      user_name=input("Enter your name:").capitalize()
      print(f"Hello {user_name}!! You find yourself in a dark forest and you have to choose paths to the north/south/east/west")
      print("Solve riddles and collect your rewards!!!")
      # print("\n")
    
    def g_choice(self):
      return input("Which direction do you want to go?(north/south/west/east)").strip().lower()
    
    
    def random_event(self):
      event =random.choice(self.events)
      event.trigger(self.player)
      
    def for_north(self):
      print("\n")
      print("Let's GO North")
      print("--->")
      print("Stop...")
      print("There is HELL DRAGON")
      if random.choice(self.riddles).askToUser():
        print("You solved the riddle and hell dragon let you pass")
      else:
        print("Wrong answer! The dragon roars and you run back to the starting point.")
        self.random_event()
        
    def for_south(self): 
      print("\n")
      print("You go south but nothing interesting happens. Try another direction.")
        
    def for_east(self):
      print("\n")
      print("You go east and discover a hidden treasure chest!")
      if(random.choice(self.riddles)).askToUser():
          print("You solved the riddle and open the chest to find gold and jewels")
      else:
          print("Wrong answer! The chest is locked tight and you return to the forest.")
          
    def for_west(self):
      print("\n")
      print("You go west and fall into a deep ravine.")
      if random.choice(self.riddles).askToUser():
          print("You solved the riddles and find a secret passage out of the ravine!")
      else:
          print("Wrong answer! You remain stuck and have to climb back up to the forest.")
          self.random_event()
    
    def start(self):
      self.display_Intro()
      while True:
          self.player.display_hp()
          self.player.display_inventory()
          choice=self.g_choice()
          if choice == "north":
           self.for_north()
          elif choice == "south":
           self.for_south()
          elif choice == "east":
           self.for_east()
          elif choice == "west":
           self.for_west()
          else:
           print("Invalid choice.Try again.")
          if self.player.hp <=0:
            print("You have run out of HP. Game Over!")
            break
        
#main game loop
if __name__ == "__main__":
    player = Player(name="hero")
    game = Game(player)
    game.start()