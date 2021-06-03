# ChainMap is used to combine several dictionaries or mappings. It returns a list of dictionaries.
from collections import ChainMap
dict1 = {'a':1,'b':2}
dict2 = (('c',1 ), ('d',2))
chain_map = ChainMap(dict1, dict2)
print(chain_map.maps)