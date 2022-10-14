import talib

funcs = talib.get_functions()
required =  [func for func in funcs if func.startswith('CDL')]
print(
    required[0].__doc__
)
import json
with open('assets.json','r') as file:
    assets = json.load(file)
    print(assets)