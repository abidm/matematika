class hero:

    def __init__(self, name, health, power, armor) -> None:
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor

    def serang(self, lawan):
        print(self.name + " menyerang " + lawan.name)
        lawan.diserang(self, self.power)

    def diserang(self, lawan, powerLawan):
        print (self.name + " diserang " + lawan.name)
        damage = powerLawan - self.armor
        print ("serangan diterima : " + str(damage))
        self.health -= damage
        print ("Sisa Health " + self.name + " : " + str(self.health))

sniper = hero("sniper", 1400, 50, 3)
invoker = hero("invoker", 1500, 45, 4)


invoker.serang(sniper)
print ("\n")
sniper.serang(invoker)