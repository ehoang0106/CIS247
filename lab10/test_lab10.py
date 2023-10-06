import random

class Player:
    #set damage block and taken  = 0
    damage_block = 0
    damage_taken = 0

    def __init__(self, name, health, strength):
        self.name = name
        self.valid_stat(health)
        self._health = health
        self.valid_stat(strength)
        self._strength = strength
       
        self._starting_health = health
        
    @property
    def health(self):
        return self._health
    @health.setter
    def health(self, new_val):
        self.valid_stat(new_val)
        self._health = new_val

    @property
    def strength(self):
        return self._strength
    @strength.setter
    def strength(self, new_val):
        self.valid_stat(new_val)
        self._strength = new_val

    def __str__(self):
        return f"Player's name: {self.name}\nCurrent health: {self._health}"
    

    def valid_stat(self, stat):
        if stat < 1 or stat > 100:
            raise ValueError(f"Invalid value. The value should be between 1 and 100")
        
    def attack(self):
        self.attack = random.randint(1, self.strength)
        return self.attack
        

    def take_damage(self, damage_amount):
        self.valid_stat(damage_amount)  #damage amount should be in range (1,100)
        self.damage_block = random.randint(1, damage_amount)
        #damage taken after enemy attacked and player blocked
        self.damage_taken = damage_amount - self.damage_block
        #player's health after taken damage
        self._health = self._health - self.damage_taken
        
        

        if self._health <= 0:
            return True
        else:
            return False
        
    

    def heal(self):
        
        #add 10 health to current health
        self._health += 10  

        if self._health > self._starting_health:
            self._health = self._starting_health
        
        return self._health

    