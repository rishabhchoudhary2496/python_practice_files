# access specifiers
# public all can access
# protected  _ base class sub class access
# private __ name mangling __className__private inside class



#_protected is just a convention
class Game:
    __private = 40
    _protected = 10
    public = 50

    def __init__(self) -> None:
        pass





g = Game() # __ name mangling 
print(g._Game__private) #can only be access with this form obj._class__private
print(g._protected)