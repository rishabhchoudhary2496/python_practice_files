class Enemy:
    Recovery = 2 #class variable
    def __init__(self,hp,mp,level):
        self.hp = hp
        self.mp = mp
        self.level = level
       

    def printdetails(self):
         print(f'Enemy HP {self.hp} MP {self.mp} Level {self.level}')


    def superSkill(self):
        print('Attacked with super skill')

    @classmethod
    def changeRecovery(cls,number): #can acesss class Variables 
        cls.Recovery = number
        print(cls)
        pass

    @classmethod  #class methods as alternative constructor
    def from_str(cls,str):
        return cls(*str.split('-'))



dark_elf = Enemy(400,300,4)
# print(dark_elf.Recovery) #class Variable access using instance
# dark_elf.Recovery = 4 #creates instance variable
# print(Enemy.Recovery) #class Variable access using instance
# print(dark_elf.__dict__) # object in dictionary form
# print(Enemy.__dict__)
dark_elf.printdetails()
dark_elf.superSkill()
dark_elf.changeRecovery(6)
ogre = Enemy.from_str('1000-500-10')
print(ogre.hp)

