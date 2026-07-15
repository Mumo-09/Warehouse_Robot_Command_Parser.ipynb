import nltk
from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""

S -> COMMAND SEMI

COMMAND -> PICK
COMMAND -> MOVE
COMMAND -> DELIVER
COMMAND -> RETURN
COMMAND -> INSPECT

PICK -> 'pick' ITEM 'from' LOCATION

MOVE -> 'move' ITEM 'to' LOCATION

DELIVER -> 'deliver' PACKAGE 'to' LOCATION

RETURN -> 'return' ROBOT 'to' LOCATION

INSPECT -> 'inspect' ITEM
INSPECT -> 'inspect' LOCATION

ITEM -> 'item_45'
ITEM -> 'item_50'
ITEM -> 'item_70'

PACKAGE -> 'package_12'
PACKAGE -> 'package_20'

ROBOT -> 'robot_1'
ROBOT -> 'robot_2'

LOCATION -> 'shelf_A'
LOCATION -> 'shelf_B'
LOCATION -> 'packing_station'
LOCATION -> 'dispatch_area'
LOCATION -> 'charging_station'
LOCATION -> 'cold_room'

SEMI -> ';'

""")

parser = ChartParser(grammar)

commands = [

"pick item_45 from shelf_A ;",

"move item_45 to packing_station ;",

"deliver package_12 to dispatch_area ;",

"return robot_2 to charging_station ;",

"inspect shelf_A ;",

"inspect item_45 ;",

"pick from shelf_A item_45 ;",

"move packing_station item_45 ;"

]

for command in commands:

    print("\n------------------------------------")
    print("Command:", command)

    tokens = command.split()

    try:

        trees = list(parser.parse(tokens))

        if trees:

            print("VALID COMMAND")

            for tree in trees:

                print(tree)

                tree.pretty_print()

        else:

            print("INVALID COMMAND")

    except ValueError:

        print("INVALID COMMAND")