class Ship():
    size = none
    char = none

    def__init__(self):
        self.row = 0
        self.col = 0
        self.direction = none
        
class Carrier(ship):
    size = 5
    char = 'C'
class Battleship(ship):
    size = 4
    char = 'B'
class Destroyer(ship):
    size = 3
    char = 'D'
class Submarine(ship):
    size = 3
    char = 'S'
class Patrol(ship): 
    size = 2
    char = 'P'

    
my_carrier = Carrier()
my_battleship = Battleship()
my_destroyer = Destroyer()
my_submarine = Submarine()
my_patrol = Patrol()

x_carrier = Carrier()
x_battleship = Battleship()
x_destroyer = Destroyer()
x_submarine = Submarine()
x_patrol = Patrol()



print("welcome to battleship!")

w = '~'
hit = '*'
grid = [
    [' ',0,1,2,3,4,5,6,7,8,9],
    ['A',w,w,w,w,w,w,w,w,w,w],
    ['B',w,w,w,w,w,w,w,w,w,w],
    ['C',w,w,w,w,w,w,w,w,w,w],
    ['D',w,w,w,w,w,w,w,w,w,w],
    ['E',w,w,w,w,w,w,w,w,w,w],
    ['F',w,w,w,w,w,w,w,w,w,w],
    ['G',w,w,w,w,w,w,w,w,w,w],
    ['H',w,w,w,w,w,w,w,w,w,w],
    ['I',w,w,w,w,w,w,w,w,w,w],
    ['J',w,w,w,w,w,w,w,w,w,w]
]

def show_grid():
    for row in grid:
        for col in row:
            print(col, end=' ')
        print()
    

def shoot():

    target_row = input('target row: ').strip().lower()
    target_col = input('target col: ').strip()

        row = row_num[target_row]
    col = int(target_col) + 1
    grid [row] [col] = hit

def ask_coord():
     row_num = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10}

    row = input('row?').strip().lower()
    col = input('col?').strip
    print(row,col)
    return(row,col)

print(ask_coord())
def play():
    while true:
        show_grid()
        shoot()


print("Carrier first coord?") 
(my_carrier.row,my_carrier.col) = ask_coord()
print("horizontal or vertical? [h/v]")
my_carrier.direction = input('>').lower().strip()

if my_carrier.direction == 'h':
    for col in range (my_carrier.size):
        grid[my_carrier.row][my_carrier.col + col] = my_carrier.char

show_grid()
