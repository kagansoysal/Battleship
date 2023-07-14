import sys

player1_txt = sys.argv[1]
player2_txt = sys.argv[2]
player1_in = sys.argv[3]
player2_in = sys.argv[4]

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
error_list = "IOError: input file(s) "

try:
    opening_the_file1 = open(player1_txt, "r")
except IOError:
    error_list = error_list + player1_txt
try:
    opening_the_file2 = open(player2_txt, "r")
except IOError:
    error_list = error_list + player2_txt + ", "
try:
    a = open(player1_in, "r").readlines()
except IOError:
    error_list = error_list + player1_in  + ", "
try:
    b = open(player2_in, "r").readlines()
except IOError:
    error_list = error_list + player2_in + ", "

# Executing this function to print our output to both terminal and file.
output = open("Battleship.out", "w")
def output_file(x):
    print(x)
    output.write(x + "\n")

# If the file names are wrong, it prints the error text and exits the code
if len(error_list) > 23:
    error_list = error_list + " is/are not reachable."
    print(error_list)
    error_list = error_list[:-24] + error_list[-22:]
    output_file(error_list)
    exit()

# We create the data structures that we will use while playing the game
map_player1 = {}
map_player2 = {}
hidden_player1 = {}
hidden_player2 = {}
ships_p1 = {"Carrier": {}, "Destroyer": {}, "Submarine": {}}
ships_p2 = {"Carrier": {}, "Destroyer": {}, "Submarine": {}}
optional_list1 = []
optional_list2 = []
command_list_p1 = []
command_list_p2 = []
ship_letter_list_C = []
ship_letter_list_D = []
ship_letter_list_S = []
player1loc_for_lenght = open(player1_txt, "r").readlines()
player2loc_for_lenght = open(player2_txt, "r").readlines()

# We add data to the data structures we will use for the tables
for numbers1p in range(len(player1loc_for_lenght)):
    map_player1[str(numbers1p + 1)] = {}
    hidden_player1[str(numbers1p + 1)] = {}
    for letters1p in range(len(player1loc_for_lenght)):
        letter = letters[letters1p]
        map_player1[str(numbers1p + 1)][letter] = ""
        hidden_player1[str(numbers1p + 1)][letter] = "-"

opening_the_file1 = open(player1_txt, "r")
for a in range(len(player1loc_for_lenght)):
    location1 = opening_the_file1.readline().rstrip().split(";")
    ship_letter_list_C = []
    ship_letter_list_D = []
    ship_letter_list_S = []

    for b in range(len(location1)):
        map_player1[str(a + 1)][letters[b]] = location1[b]
        try:
            if location1[b] == "C":
                ship_letter_list_C.append(letters[b])
                ships_p1["Carrier"][str(a + 1)] = ship_letter_list_C
            if location1[b] == "D":
                ship_letter_list_D.append(letters[b])
                ships_p1["Destroyer"][str(a + 1)] = ship_letter_list_D
            if location1[b] == "S":
                ship_letter_list_S.append(letters[b])
                ships_p1["Submarine"][str(a + 1)] = ship_letter_list_S
        except:
            continue

for numbers2p in range(len(player2loc_for_lenght)):
    map_player2[str(numbers2p + 1)] = {}
    hidden_player2[str(numbers2p + 1)] = {}
    for letters2p in range(len(player2loc_for_lenght)):
        letter = letters[letters2p]
        map_player2[str(numbers2p + 1)][letter] = ""
        hidden_player2[str(numbers2p + 1)][letter] = "-"

opening_the_file2 = open(player2_txt, "r")
for a in range(len(player2loc_for_lenght)):
    location2 = opening_the_file2.readline().rstrip().split(";")
    ship_letter_list_C = []
    ship_letter_list_D = []
    ship_letter_list_S = []

    for b in range(len(location2)):
        map_player2[str(a + 1)][letters[b]] = location2[b]
        try:
            if location2[b] == "C":
                ship_letter_list_C.append(letters[b])
                ships_p2["Carrier"][str(a + 1)] = ship_letter_list_C
            if location2[b] == "D":
                ship_letter_list_D.append(letters[b])
                ships_p2["Destroyer"][str(a + 1)] = ship_letter_list_D
            if location2[b] == "S":
                ship_letter_list_S.append(letters[b])
                ships_p2["Submarine"][str(a + 1)] = ship_letter_list_S
        except:
            continue

a = open(player1_in, "r").readlines()
b = open(player2_in, "r").readlines()

# We are editing our related data structure to distinguish ships of the same type from each other.
def ships():
    optional_player1 = open("OptionalPlayer1.txt", "r")
    optional_player2 = open("OptionalPlayer2.txt", "r")
    optionals1 = optional_player1.readlines()
    optionals2 = optional_player2.readlines()

    for info in optionals1:
        optional_list1.append(info.rstrip().split(";"))
    for info in optionals2:
        optional_list2.append(info.rstrip().split(";"))

    for i in optional_list1:
        colon_index = i[0].index(":")
        comma_index = i[0].index(",")
        if i[0][:colon_index][0] == "B":
            range_number = 4
        elif i[0][:colon_index][0] == "P":
            range_number = 2
        abcd = []
        turn = i[0][comma_index + 1:]
        turn2 = i[0][colon_index + 1:comma_index]
        ships_p1[i[0][:colon_index]] = {}
        if i[1] == "right" or i[1] == "left":
            for j in range(range_number):
                abcd.append(turn)
                ships_p1[i[0][:colon_index]][turn2] = abcd
                if i[1] == "right":
                    turn = letters[letters.index(turn) + 1]
                if i[1] == "left":
                    turn = letters[letters.index(turn) - 1]
        if i[1] == "down" or i[1] == "up":
            for j in range(range_number):
                ships_p1[i[0][:colon_index]][turn2] = []
                ships_p1[i[0][:colon_index]][turn2] = turn
                if i[1] == "down":
                    turn2 = str(int(turn2) + 1)
                if i[1] == "up":
                    turn2 = str(int(turn2) - 1)

    for i in optional_list2:
        colon_index = i[0].index(":")
        comma_index = i[0].index(",")
        if i[0][:colon_index][0] == "B":
            range_number = 4
        elif i[0][:colon_index][0] == "P":
            range_number = 2
        abcd = []
        turn = i[0][comma_index + 1:]
        turn2 = i[0][colon_index + 1:comma_index]
        ships_p2[i[0][:colon_index]] = {}
        if i[1] == "right" or i[1] == "left":
            for j in range(range_number):
                abcd.append(turn)
                ships_p2[i[0][:colon_index]][turn2] = abcd
                if i[1] == "right":
                    turn = letters[letters.index(turn) + 1]
                if i[1] == "left":
                    turn = letters[letters.index(turn) - 1]
        if i[1] == "down" or i[1] == "up":
            for j in range(range_number):
                ships_p2[i[0][:colon_index]][turn2] = []
                ships_p2[i[0][:colon_index]][turn2] = turn
                if i[1] == "down":
                    turn2 = str(int(turn2) + 1)
                if i[1] == "up":
                    turn2 = str(int(turn2) - 1)
ships()

# We build our lists to check the number of ships
ships_control1 = []
ships_control2 = []
for z in ships_p1:
    ships_control1.append(z[0])
for z in ships_p2:
    ships_control2.append(z[0])

# We create a list of players' commands
def commands():
    c = a[0].split(";")
    f = b[0].split(";")

    for d in c:
        command_list_p1.append(d.split(","))
    command_list_p1.pop()
    for e in f:
        command_list_p2.append((e.split(",")))
    command_list_p2.pop()
commands()

output_file("Battle of Ships Game\n")

# We create the tables that we will write for each round.
def drawing_table(command):
    output_file(f"Player{int(command) % 2 + 1}'s Move\n")
    print(f"Round: {int(command/2 + 1)}", end = "\t\t\t")
    output.write(f"Round : {int(command/2 + 1)}" + "\t\t\t\t\t")
    output_file(f"Grid Size: {len(player1loc_for_lenght)}X{len(player1loc_for_lenght)}\n")
    output_file("Player1's Hidden Board\t\tPlayer2's Hidden Board")
    print("  ",end="")
    output.write("  ")
    for number_p1 in hidden_player1:
        for letter_p1 in hidden_player1[number_p1]:
            print(letter_p1, end=" ")
            output.write(letter_p1 + " ")
        print("\t\t", end="  ")
        output.write("\t\t" + "  ")
        break

    for number_p2 in hidden_player2:
        for letter_p2 in hidden_player2[number_p2]:
            print(letter_p2, end=" ")
            output.write(letter_p2 + " ")
        output_file("")
        break

    def p1board(number_to_write_p1):
        if number_to_write_p1 < 10:
            print(number_to_write_p1, end=" ")
            output.write(str(number_to_write_p1) + " ")
        else:
            print(number_to_write_p1, end="")
            output.write(str(number_to_write_p1))
        for marks_p1 in hidden_player1[str(number_to_write_p1)]:
            if marks_p1 == "J":
                print(hidden_player1[str(number_to_write_p1)][marks_p1], end="")
                output.write(hidden_player1[str(number_to_write_p1)][marks_p1] + "")
            else:
                print(hidden_player1[str(number_to_write_p1)][marks_p1], end=" ")
                output.write(hidden_player1[str(number_to_write_p1)][marks_p1] + " ")
        p2board(number_to_write_p1)

    def p2board(number_to_write_p2):
        print("\t\t", end="")
        output.write("\t\t")
        if number_to_write_p2 < 10:
            print(number_to_write_p2, end=" ")
            output.write(str(number_to_write_p2) + " ")
        else:
            print(number_to_write_p2, end="")
            output.write(str(number_to_write_p2))
        for letter_to_write_p2 in hidden_player2[str(number_to_write_p2)]:
            print(hidden_player2[str(number_to_write_p2)][letter_to_write_p2], end=" ")
            output.write(hidden_player2[str(number_to_write_p2)][letter_to_write_p2] + " ")
        print()
        output.write("\n")
        if number_to_write_p2 < len(location1):
            p1board(number_to_write_p2 + 1)

    number_to_write_p1 = 1
    p1board(number_to_write_p1)
    print()
    output.write("\n")

# We are making changes to Player2 as a result of Player1's moves
def execute1():
    global number_target1, letter_target1
    if map_player2[number_target1][letter_target1] == "":
        hidden_player2[number_target1][letter_target1] = "O"
    else:
        hidden_player2[number_target1][letter_target1] = "X"

    for y in list(ships_p2):
        for v in list(ships_p2[y]):
            if type(ships_p2[y][v]) == list:
                if v == number_target1 and letter_target1 in ships_p2[y][v]:
                    if len(ships_p2[y][v]) > 1:
                        ships_p2[y][v].remove(letter_target1)
                    elif len(ships_p2[y][v]) == 1:
                        ships_p2[y].pop(v)
            else:
                if v == number_target1 and ships_p2[y][v] == letter_target1:
                    ships_p2[y].pop(v)

# We are making changes to Player1 as a result of Player2's moves
def execute2():
    global number_target2, letter_target2
    if map_player1[number_target2][letter_target2] == "":
        hidden_player1[number_target2][letter_target2] = "O"
    else:
        hidden_player1[number_target2][letter_target2] = "X"

    for y in list(ships_p1):
        for v in list(ships_p1[y]):
            try:
                if type(ships_p1[y][v]) == list:
                    if v == number_target2 and letter_target2 in ships_p1[y][v]:
                        if len(ships_p1[y][v]) > 1:
                            ships_p1[y][v].remove(letter_target2)
                        elif len(ships_p1[y][v]) == 1:
                            ships_p1[y].pop(v)
                else:
                    if v == number_target2 and ships_p1[y][v] == letter_target2:
                        ships_p1[y].pop(v)
            except:
                continue

# We check the number of ships and print how many are left.
def count_of_ships():
    for ships in ["Carrier", "Battleship", "Destroyer", "Submarine", "Patrol Boat"]:
        if ships == "Carrier":
            print(ships, end=" \t")
            output.write(ships + " \t")
        else:
            print(ships, end="\t")
            output.write(ships + "\t")

        t = ships_control1.count(ships[0])
        f = ships_control2.count(ships[0])
        if ships == "Carrier" or ships == "Destroyer" or ships == "Submarine":
            print((1-t)*"X " + t*"- ", end="\t\t")
            output.write((1-t)*"X " + t*"- " + "\t\t\t\t")
        elif ships == "Battleship":
            print((2-t)*"X " + t * "- ", end="\t\t")
            output.write((2 - t) * "X " + t * "- " + "\t\t\t")
        else:
            print((4-t) * "X " + t * "- ", end="\t")
            output.write((4 - t) * "X " + t * "- " + "\t\t")

        if ships == "Carrier":
            print(ships, end="\t\t")
            output.write(ships + "\t\t")
        else:
            print(ships, end="\t")
            output.write(ships + "\t")

        if ships == "Carrier" or ships == "Destroyer" or ships == "Submarine":
            output_file((1-f)*"X " + f*"- ")
        elif ships == "Battleship":
            output_file((2-f)*"X " + f * "- ")
        else:
            output_file((4-f) * "X " + f * "- ")

    output_file("")

# We remove the completely hit ships from the lists and print the next move.
def last_write(command):
    for inside1 in list(ships_p1):
        if len(ships_p1[inside1]) == 0:
            if inside1[0] in ships_control1:
                ships_control1.remove(inside1[0])
                ships_p1.pop(inside1)
        else:
            for inside2 in ships_p1[inside1]:
                if type(ships_p1[inside1][inside2]) == list:
                    if len(ships_p1[inside1][inside2]) == 0:
                        if inside1[0] in ships_control1:
                            ships_control1.remove(inside1[0])
                            ships_p1.pop(inside1)

    for inside1 in list(ships_p2):
        if len(ships_p2[inside1]) == 0:
            if inside1[0] in ships_control2:
                ships_control2.remove(inside1[0])
                ships_p2.pop(inside1)
        else:
            for inside2 in ships_p2[inside1]:
                if type(ships_p2[inside1][inside2]) == list:
                    if len(ships_p2[inside1][inside2]) == 0:
                        if inside1[0] in ships_control2:
                            ships_control2.remove(inside1[0])
                            ships_p2.pop(inside1)

    if command % 2 == 0:
        output_file(f"Enter your move: {number_target1},{letter_target1}\n")
    else:
        output_file(f"Enter your move: {number_target2},{letter_target2}\n")

# We create this function to print the final state of the game.
def final_statement():

    if number_x_p1 == 27 and number_x_p2 == 27:
        output_file("It is a Draw!\n")
    elif number_x_p1 == 27:
        output_file("Player2 Wins!\n")
    elif number_x_p2 == 27:
        output_file("Player1 Wins!\n")
    output_file("Final Information\n")

    output_file("Player1's Board\t\t\tPlayer2's Board")
    print("  ", end="")
    output.write("  ")
    for number_p1 in hidden_player1:
        for letter_p1 in hidden_player1[number_p1]:
            print(letter_p1, end=" ")
            output.write(letter_p1 + " ")
        print("\t\t", end="  ")
        output.write("\t\t" + "  ")
        break

    for number_p2 in hidden_player2:
        for letter_p2 in hidden_player2[number_p2]:
            print(letter_p2, end=" ")
            output.write(letter_p2 + " ")
        output_file("")
        break

    if number_x_p1 == 27:
        for inside1 in map_player2:
            for inside2 in map_player2[inside1]:
                if map_player2[inside1][inside2] != "" and hidden_player2[inside1][inside2] == "-":
                    hidden_player2[inside1][inside2] = map_player2[inside1][inside2]

    elif number_x_p2 == 27:
        for inside1 in map_player1:
            for inside2 in map_player1[inside1]:
                if map_player1[inside1][inside2] != "" and hidden_player1[inside1][inside2] == "-":
                    hidden_player1[inside1][inside2] = map_player1[inside1][inside2]
    count = 1

    def finalp1board(count):
        if count < 10:
            print(count, end=" ")
            output.write(str(count) + " ")
        else:
            print(count, end="")
            output.write(str(count))
        for marks_p1 in hidden_player1[str(count)]:
            print(hidden_player1[str(count)][marks_p1], end=" ")
            output.write(hidden_player1[str(count)][marks_p1] + " ")
        finalp2board(count)

    def finalp2board(number_to_write_p2):
        print("\t\t", end="")
        output.write("\t\t")
        if number_to_write_p2 < 10:
            print(number_to_write_p2, end=" ")
            output.write((str(number_to_write_p2) + " "))
        else:
            print(number_to_write_p2, end="")
            output.write(str(number_to_write_p2))
        for letter_to_write_p2 in hidden_player2[str(number_to_write_p2)]:
            print(hidden_player2[str(number_to_write_p2)][letter_to_write_p2], end=" ")
            output.write(hidden_player2[str(number_to_write_p2)][letter_to_write_p2] + " ")
        print()
        output.write("\n")
        if number_to_write_p2 < len(location1):
            finalp1board(number_to_write_p2 + 1)
        else:
            print()
            output.write("\n")
    finalp1board(count)
    count_of_ships()

# We use this loop to play the game sequentially.
for k in range(len(max(command_list_p1, command_list_p2))*2):
    try:
        drawing_table(k)

        if k % 2 == 0:
            try:
                number_target1 = command_list_p1[int(int(k) / 2)][0]
                letter_target1 = command_list_p1[int(int(k) / 2)][1]
                print(number_target1, letter_target1)

                if number_target1 == "" or letter_target1 == "":
                    raise IndexError
                if number_target1 in map_player1["1"] or letter_target1 in map_player1 or len(letter_target1) > 1:
                    raise ValueError

                assert int(number_target1) <= len(player1loc_for_lenght) and letter_target1 in map_player1["1"]
                execute1()

            except AssertionError:
                while number_target1 not in map_player1 or letter_target1 not in map_player1["1"]:
                    output_file(f"Enter your move: {number_target1},{letter_target1}")
                    k += 2
                    number_target1 = command_list_p1[int(int(k) / 2)][0]
                    letter_target1 = command_list_p1[int(int(k) / 2)][1]
                output_file("AssertionError: Invalid Operation.")
                execute1()
                command_list_p1.pop(int(k/2))
                last_write(k)
                continue

            except IndexError:
                while number_target1 == "" or letter_target1 == "":
                    try:
                        output_file(f"Enter your move: {number_target1},{letter_target1}")
                    except:
                        output_file(f"Enter your move: {number_target1}")
                    k+=2
                    number_target1 = command_list_p1[int(int(k) / 2)][0]
                    letter_target1 = command_list_p1[int(int(k) / 2)][1]
                output_file("IndexError: You must enter your commands in number comma letter semicolon order!")
                execute1()
                command_list_p1.pop(int(k / 2))
                last_write(k)
                continue

            except ValueError:
                while number_target1 in map_player1["1"] or letter_target1 in map_player1 or len(letter_target1) > 1:
                    output_file(f"Enter your move: {number_target1},{letter_target1}")
                    k+=2
                    number_target1 = command_list_p1[int(int(k) / 2)][0]
                    letter_target1 = command_list_p1[int(int(k) / 2)][1]
                output_file("ValueError: You must enter your commands in number comma letter semicolon order!")
                execute1()
                command_list_p1.pop(int(k / 2))
                last_write(k)
                continue
        else:
            try:
                number_target2 = command_list_p2[int(int(k) / 2)][0]
                letter_target2 = command_list_p2[int(int(k) / 2)][1]

                assert int(number_target2) <= len(player2loc_for_lenght)
                execute2()

                if number_target2 == "" or letter_target2 == "":
                    raise IndexError
                if number_target2 not in map_player2 or letter_target2 not in map_player2["1"]:
                    raise ValueError

            except AssertionError:
                output_file(f"Enter your move: {number_target2},{letter_target2}")
                while number_target2 not in map_player2 or letter_target2 not in map_player2["1"]:
                    k +=2
                    number_target2 = command_list_p2[int(int(k) / 2)][0]
                    letter_target2 = command_list_p2[int(int(k) / 2)][1]
                output_file("AssertionError: Invalid Operation.")
                execute2()
                command_list_p2.pop(int(k / 2))
                last_write(k)
                continue
            except IndexError:
                while number_target2 == "" or letter_target2 == "":
                    try:
                        output_file(f"Enter your move: {number_target2},{letter_target2}")
                    except:
                        output_file(f"Enter your move: {number_target2}")
                    k +=2
                    number_target2 = command_list_p2[int(int(k) / 2)][0]
                    letter_target2 = command_list_p2[int(int(k) / 2)][1]
                output_file("IndexError: You must enter your commands in number comma letter semicolon order!")
                execute2()
                command_list_p2.pop(int(k / 2))
                last_write(k)
                continue
            except ValueError:
                while number_target2 == "" or letter_target2 == "":
                    output_file(f"Enter your move: {number_target2},{letter_target2}")
                    k +=2
                    number_target2 = command_list_p2[int(int(k) / 2)][0]
                    letter_target2 = command_list_p2[int(int(k) / 2)][1]
                output_file("ValueError: You must enter your commands in number comma letter semicolon order!")
                execute2()
                command_list_p2.pop(int(k / 2))
                last_write(k)
                continue

        count_of_ships()
        last_write(k)
    except:
        output_file("kaBOOM: run for your life!")
        continue

    # We check if the game is over. We're also looking to see if there is a draw condition.
    check_list1 = []
    check_list2 = []
    for inside1 in hidden_player1:
        for inside2 in hidden_player1[inside1]:
            check_list1.append(hidden_player1[inside1][inside2])
    number_x_p1 = check_list1.count("X")

    for z in hidden_player2:
        for y in hidden_player2[z]:
            check_list2.append(hidden_player2[z][y])
    number_x_p2 = check_list2.count("X")

    if number_x_p1 == 27 or number_x_p2 == 27:
        if number_x_p1 == 27:
            final_statement()
            break
        elif number_x_p2 == 27 and len(ships_control1) == 1:
            continue
        elif number_x_p2 == 27 and len(ships_control1) > 1:
            final_statement()
            break