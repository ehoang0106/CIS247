from Player import Player


def main():
    name = input("Player's name: ")
    health = int(input("Player's Health: "))
    strength = int(input("Player's Strength: "))
    player = Player(name, health, strength)
    #player = Player("Khoa", 100, 80)
    
    #testing
    print(player)
    player.take_damage(80)
    print(f"Damage taken: {player.damage_taken}")
    player.heal()
    print(f"Health after healed: {player.health}")
    
    print(player)
    player.take_damage(70)
    print(f"Damage taken: {player.damage_taken}")
    player.heal()
    print(f"Health after healed: {player.health}")

    print(player)
    player.take_damage(70)
    print(f"Damage taken: {player.damage_taken}")
    player.heal()
    print(f"Health after healed: {player.health}")
    

    
    
main()