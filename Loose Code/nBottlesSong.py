# https://en.wikipedia.org/wiki/99_Bottles_of_Beer

def nBottlesSong(total_number_of_bottles):
    for bottles_left_on_wall in range(total_number_of_bottles, -1, -1):
        if bottles_left_on_wall > 0:
            print(str(bottles_left_on_wall) + " bottles of beer on the wall, " + str(bottles_left_on_wall) + " bottles of beer.")
            print("Take one down, pass it around, " + str(bottles_left_on_wall - 1) + " bottles of beer on the wall...")
        else:
            print("No more bottles of beer on the wall, no more bottles of beer.")

nBottlesSong(99)
