#set contains immutable types but itself is not immutable so things can be added or 
# removed from it howerver frozen set is immutable set

x = frozenset(['as','this'])
#x.add() #throws error
print(x)

#if you want to define set of sets then you can because sets are immutable 
# so this can be done with frozenset
x1 = frozenset(['foo'])
x2 = frozenset(['bar'])
x3 = frozenset(['baz'])
x = {x1, x2, x3}