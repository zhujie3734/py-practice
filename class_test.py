user1 = {'name':'Tom', 'hp':'100'}
user2 = {'name':'jerry', 'hp':'100'}

def role(rolename):
    print ('name is %s, hp is %s' %(rolename['name'],rolename['hp']))

role(user1)

class Player():  #定义一个类
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
    def print_role(self):
        print('%s: %s' %(self.name,self.hp))

class Monster():
    def __init__(self,hp):
        self.hp = hp
    def run(self):
        print("移动到某个位置")

class Animal(Monster):
    def __init__(self, hp):
        super().__init__(hp)


a1 = Monster(100)
print(a1.hp)
a2 = Animal(200)
print(a2.hp)





#user1 = Player('tom',100)
#user2 = Player('jerry',90)

#user1.print_role()
#user2.print_role()