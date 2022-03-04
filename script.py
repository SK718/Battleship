# from tabnanny import check


from unittest import skip


board_1 = {
    "1A":"_", "1B":"_", "1C":"_", "1D":"_", "1E":"_", "1F":"_", "1G":"_", "1H":"_", "1I":"_", "1J":"_",
    "2A":"_", "2B":"_", "2C":"_", "2D":"_", "2E":"_", "2F":"_", "2G":"_", "2H":"_", "2I":"_", "2J":"_",
    "3A":"_", "3B":"_", "3C":"_", "3D":"_", "3E":"_", "3F":"_", "3G":"_", "3H":"_", "3I":"_", "3J":"_",
    "4A":"_", "4B":"_", "4C":"_", "4D":"_", "4E":"_", "4F":"_", "4G":"_", "4H":"_", "4I":"_", "4J":"_",
    "5A":"_", "5B":"_", "5C":"_", "5D":"_", "5E":"_", "5F":"_", "5G":"_", "5H":"_", "5I":"_", "5J":"_",
    "6A":"_", "6B":"_", "6C":"_", "6D":"_", "6E":"_", "6F":"_", "6G":"_", "6H":"_", "6I":"_", "6J":"_",
    "7A":"_", "7B":"_", "7C":"_", "7D":"_", "7E":"_", "7F":"_", "7G":"_", "7H":"_", "7I":"_", "7J":"_",
    "8A":"_", "8B":"_", "8C":"_", "8D":"_", "8E":"_", "8F":"_", "8G":"_", "8H":"_", "8I":"_", "8J":"_",
    "9A":"_", "9B":"_", "9C":"_", "9D":"_", "9E":"_", "9F":"_", "9G":"_", "9H":"_", "9I":"_", "9J":"_",
    "10A":"_", "10B":"_", "10C":"_", "10D":"_", "10E":"_", "10F":"_", "10G":"_", "10H":"_", "10I":"_", "10J":"_"
}

board_2 = {
    "1A":"_", "1B":"_", "1C":"_", "1D":"_", "1E":"_", "1F":"_", "1G":"_", "1H":"_", "1I":"_", "1J":"_",
    "2A":"_", "2B":"_", "2C":"_", "2D":"_", "2E":"_", "2F":"_", "2G":"_", "2H":"_", "2I":"S", "2J":"_",
    "3A":"_", "3B":"S", "3C":"S", "3D":"_", "3E":"_", "3F":"S", "3G":"S", "3H":"S", "3I":"S", "3J":"_",
    "4A":"_", "4B":"_", "4C":"_", "4D":"_", "4E":"_", "4F":"_", "4G":"_", "4H":"_", "4I":"S", "4J":"_",
    "5A":"_", "5B":"_", "5C":"_", "5D":"_", "5E":"_", "5F":"_", "5G":"_", "5H":"_", "5I":"S", "5J":"_",
    "6A":"S", "6B":"_", "6C":"_", "6D":"_", "6E":"_", "6F":"_", "6G":"_", "6H":"_", "6I":"S", "6J":"_",
    "7A":"S", "7B":"_", "7C":"_", "7D":"_", "7E":"_", "7F":"_", "7G":"_", "7H":"_", "7I":"_", "7J":"_",
    "8A":"S", "8B":"_", "8C":"_", "8D":"_", "8E":"_", "8F":"_", "8G":"_", "8H":"_", "8I":"_", "8J":"_",
    "9A":"_", "9B":"_", "9C":"_", "9D":"_", "9E":"_", "9F":"_", "9G":"_", "9H":"_", "9I":"_", "9J":"_",
    "10A":"_", "10B":"_", "10C":"_", "10D":"S", "10E":"S", "10F":"S", "10G":"_", "10H":"_", "10I":"_", "10J":"_"
}


layout_basic = '''
|___||___||___||___||___||___||___||___||___||___|
|___||___||___||___||___||___||___||___||___||___|
|___||___||___||___||___||___||___||___||___||___|
|___||___||___||___||___||___||___||___||___||___|
|___||___||___||___||___||___||___||___||___||___|
|___||___||___||___||___||___||___||___||___||___|
|___||___||___||___||___||___||___||___||___||___|
|___||___||___||___||___||___||___||___||___||___|
|___||___||___||___||___||___||___||___||___||___|
|___||___||___||___||___||___||___||___||___||___|
'''


layout_positions = '''

|____||_A_||_B_||_C_||_D_||_E_||_F_||_G_||_H_||_I_||_J_|
|__1_||_{1A}_||_{1B}_||_{1C}_||_{1D}_||_{1E}_||_{1F}_||_{1G}_||_{1H}_||_{1I}_||_{1J}_|
|__2_||_{2A}_||_{2B}_||_{2C}_||_{2D}_||_{2E}_||_{2F}_||_{2G}_||_{2H}_||_{2I}_||_{2J}_|
|__3_||_{3A}_||_{3B}_||_{3C}_||_{3D}_||_{3E}_||_{3F}_||_{3G}_||_{3H}_||_{3I}_||_{3J}_|
|__4_||_{4A}_||_{4B}_||_{4C}_||_{4D}_||_{4E}_||_{4F}_||_{4G}_||_{4H}_||_{4I}_||_{4J}_|
|__5_||_{5A}_||_{5B}_||_{5C}_||_{5D}_||_{5E}_||_{5F}_||_{5G}_||_{5H}_||_{5I}_||_{5J}_|
|__6_||_{6A}_||_{6B}_||_{6C}_||_{6D}_||_{6E}_||_{6F}_||_{6G}_||_{6H}_||_{6I}_||_{6J}_|
|__7_||_{7A}_||_{7B}_||_{7C}_||_{7D}_||_{7E}_||_{7F}_||_{7G}_||_{7H}_||_{7I}_||_{7J}_|
|__8_||_{8A}_||_{8B}_||_{8C}_||_{8D}_||_{8E}_||_{8F}_||_{8G}_||_{8H}_||_{8I}_||_{8J}_|
|__9_||_{9A}_||_{9B}_||_{9C}_||_{9D}_||_{9E}_||_{9F}_||_{9G}_||_{9H}_||_{9I}_||_{9J}_|
|_10_||_{10A}_||_{10B}_||_{10C}_||_{10D}_||_{10E}_||_{10F}_||_{10G}_||_{10H}_||_{10I}_||_{10J}_|

'''

total_ships = 5

def welcome():
    print("")
    print("Welcome to BattleShip!")
    print("----------------------")
    print('''
    In this game you will need to determine where the enemy ships are.

    There are 5 enemy ships of various sizes.
        * Carrier - 5 Spaces
        * Battleship - 4 Spaces
        * Destroyer - 3 Spaces 
        * Submarine - 3 Spaces
        * Patrol Boat - 2 Spaces

    Each hit will be marked with an X.
    Each miss will be marked with a O.

    Good Luck!
    ''')

    start = input("Please hit Enter when you are ready to begin! ")
    if not start:

        begin_game()

def begin_game():
    print(layout_positions.format(**board_1))
    print("")
    print("Please enter the coordinates that you think a ship might be. (Example: 1A)")
    Input_Coordinate()

def Input_Coordinate():
    coordinate = input("").upper()
    guess(coordinate)


def guess(coordinate):
    if board_2[coordinate] == "S":
        board_1[coordinate] = "X"
        print(layout_positions.format(**board_1))
        print("Hit!!")
        check_ships()
        print("")
        print("Pick another spot.")
        Input_Coordinate()
    else:
        board_1[coordinate] = "O"
        print(layout_positions.format(**board_1))
        print("Miss")
        print("Try Again")
        Input_Coordinate()

class Ships:
    def __init__(self, name, spaces, board, count = 0):
        self.name = name
        self.spaces = spaces
        self.board = board
        self.count = count
        
    def grid_options(self):
        l = []
        if self.count == 0:
            for spot in self.board:
                if board_1[spot] == "X":
                    l.append(spot)
            if self.board == l:
                print("You Sunk The {}!!".format(self.name))
                self.count += 1
        else:
            pass
            


patrol_ship = Ships("Patrol Ship", 2, ["3B","3C"]) 
submarine = Ships("Submarine", 3, ["6A", "7A", "8A"])
destroyer = Ships("Destroyer", 3, ["10D", "10E", "10F"])
battleship = Ships("Battleship", 4,["3F", "3G", "3H", "3I"])
carrier = Ships("Carrier", 5, ["2I", "3I", "4I", "5I", "6I"])

def check_ships():
    patrol_ship.grid_options()
    submarine.grid_options()
    destroyer.grid_options()
    battleship.grid_options()
    carrier.grid_options()


welcome()

