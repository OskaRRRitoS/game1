print("Hello player!")
print("Welcome to the game.")
playername=input("What is your name? ")
class Player:
    def __init__(self, hp, mp, att, dfe, xp):
        self.hp=hp
        self.mp=mp
        self.att=att
        self.dfe=dfe
        self.xp=xp
playername=Player(15, 5, 5, 3, 0)
class Monster:
    def __init__(self, hp, mp, att, dfe):
        self.hp=hp
        self.mp=mp
        self.att=att
        self.dfe=dfe
Slime=Monster(5, 0, 2, 0)
prevmonhp=Slime.hp
def level():
    if playername.xp>=10:
        playername.hp=playername.hp+5
        playername.mp=playername.mp+5
        playername.att=playername.att+5
        playername.dfe=playername.dfe+3
        playername.xp=playername.xp-10
        print("you have leveled up!")
def action():
    actinput=input("\nHello, What will you do? type 'attack' or 'defend' ")
    if actinput=="attack":
        Slime.hp=Slime.hp-((playername.att/5)-Slime.dfe)
        print("You hit the Slime.")
        print("You dealt "+str(int((playername.att/5)-Slime.dfe))+" damage!")
        print("Slime has "+str(int(Slime.hp))+"hp left.")
        if Slime.hp<=0:
            print("You killed the slime.")
            playername.xp=playername.xp+15
            print("You gained 15 xp!")
            level()
        else:
            playername.hp=playername.hp-(Slime.att-(playername.dfe/3))
            print("You were hit!")
            print("You lost "+str(int(Slime.att-(playername.dfe/3)))+"hp!")
            print("You have "+str(int(playername.hp))+"hp left.")
    elif actinput=="defend":
        playername.dfe=playername.dfe*2
        playername.hp=playername.hp-(Slime.att/2-playername.dfe/3)
        print("You were hit!")
        print("You lost "+str(int(Slime.att/2-playername.dfe/3))+"hp!")
        print("You have "+str(int(playername.hp))+"hp left.")
    else:
        print("Unknown command.")
while True==True:
    action()
    if Slime.hp<=0:
        Slime.hp=prevmonhp+5
        prevmonhp=Slime.hp
        Slime.att=+2
        Slime.dfe=+1
        print("\nA new Slime spawned.")
        action()
        if Slime.hp<=0:
            break
        elif playername.hp<=0:
            print("Game over!")
            break
    elif playername.hp<=0:
        print("Game over!")
        break
    else:
        continue
