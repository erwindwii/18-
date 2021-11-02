#oop method python

class User():
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.__role = role
    
    def info(self):
        return f"{self.name}:{self.email}:{self.__role}"

    def update_role(self, new_role):
        if self.__role != "user":
            self.__role = new_role
    
    def getRole(self):
        return self.__role

loli = User("Loli","loli@anime.com","user")
loli.update_role("super_admin")
print(loli.info())

budi = User("Budi","budi@gaul.com","Admin")
budi.update_role("super_admin")
print(budi.info())
print(budi.getRole())
