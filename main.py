import os

TODO = "todo"
DONE = "done"
PROMPT = ""
INPUT_ERROR = "Invalid input"

FILENAME = "data"

MARK = "M"
RESET = "R"
ADD_CHAR = "A"
DELETE = "D"
QUIT = "Q"
NO = "N"
EMPTY = ""
YES = "Y"
NO = "N"

NAME_COL = 0
SEP_COL = 1
VERB_COL = 2
LINE_LENGTH = 3

LIST_CHOICES = [ADD_CHAR, DELETE, MARK, RESET, QUIT]
RESET_CHOICES = [EMPTY, YES, NO]
YES_CHOICE = [EMPTY, YES]

def reset():
    string = open(FILENAME).read()
    string = string.replace(DONE, TODO)
    with open(FILENAME, "w") as file:
        file.write(string)

def remove_from_file(name):
    print(name)
    lines = open(FILENAME, "r").readlines()
    with open(FILENAME, "w") as outfile:
        for line in lines:
            if name not in line:
                outfile.write(line)

def ask_for_reset():
    print("No character left, want to reset ? Y/n")
    while True:
        choice = input(PROMPT)
        if choice.upper() in RESET_CHOICES:
            break
        print(INPUT_ERROR)
    if choice.upper() in YES_CHOICE:
        reset()
    elif choice.upper() == NO:
        return QUIT
    return QUIT

def add_character():
    print("Please enter a name for a new character :")
    print("\t(Naming it q or Q will quit)")
    name = input(PROMPT)
    if name.upper() != QUIT:
        with open(FILENAME, "a") as file:
            file.write(name + " : " + TODO + os.linesep)
    return name.upper()

def delete_character():
    print("Please select a character to delete :")
    list_char = get_all()
    print(list_char[0])
    print("\t" + QUIT + ") Quit")
    while True:
        num = input(PROMPT)
        if not num.isdigit():
            if num.upper() == QUIT:
                break
        elif num.isdigit():
            if 0 <= int(num) < list_char[1]:
                break
        print(INPUT_ERROR)
    if num.isdigit():
        name = list_char[0].split("\t")
        name = [x for x in name if x != ""]
        remove_from_file(name[int(num)].split()[1])
    return num

def sort_lines():
    lines = open(FILENAME, "r").readlines()
    with open(FILENAME, "w") as out_file:
        for line in sorted(lines, key=lambda line: line.split(" ")[NAME_COL], reverse=True):
            out_file.write(line + os.linesep)

def get_todos():
    cpt = 0
    lines = open(FILENAME, "r").readlines()
    output = EMPTY
    for line in lines:
        if TODO in line:
            output += "\t" + str(cpt) + ") " + line.split()[NAME_COL] + "\t"
            cpt += 1
    return (output.rstrip(), cpt)

def get_all():
    cpt = 0
    lines = open(FILENAME, "r").readlines()
    output = EMPTY
    for line in lines:
        if len(line.split()) == LINE_LENGTH:
            output += "\t" + str(cpt) + ") " + line.split()[NAME_COL] + "\t"
            cpt += 1
    return (output.rstrip(), cpt)

def complete_character(char_name):
    char_todo = char_name + " : " + TODO
    char_done = char_name + " : " + DONE
    string = open(FILENAME).read()
    string = string.replace(char_todo, char_done)
    with open(FILENAME, "w") as outfile:
        outfile.write(string)

def complete_char_from_num(number, string):
    lines = string.splitlines()
    for line in lines:
        if number in line:
            complete_character(line.split()[1])

def check_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w+"): pass
    lines = open(FILENAME).readlines()
    for line in lines:
        if len(line.split()) != LINE_LENGTH:
            print("FILE ILL FORMED\nPress any key...")
            input("")
            exit()
    file = open(FILENAME).read()
    with open(FILENAME, "w") as out:
        out.write(file.rstrip() + "\n")

def ask_complete():
    print("Here is the list of remaining characters : ")
    print(get_todos()[0])
    print("What do you want to do ?")
    print("\t" + ADD_CHAR + ") Add a new character in file", end="\t")
    print("\t" + DELETE + ") Delete a character", end="\t")
    print("\t" + MARK + ") Mark a character as DONE", end="\t")
    print("\t" + RESET + ") Reset characters", end="\t")
    print("\t" + QUIT+  ") Quit")
    while True:
        choice = input(PROMPT)
        if choice.upper() in LIST_CHOICES:
            break
        print(INPUT_ERROR)
    if choice.upper() == ADD_CHAR:
        return add_character()
    if choice.upper() == DELETE:
        return delete_character()
    elif choice.upper() == MARK:
        characters = get_todos()
        print(characters[0])
        print("\t" + QUIT + ") Quit")
        print("Now choose one character :")
        while True:
            char = input(PROMPT)
            if char.upper() == QUIT or  0 <= int(char) < characters[1]:
                break
            print(INPUT_ERROR)
        if char.isdigit():
            complete_char_from_num(char, characters[0])
            return char
    elif choice.upper() == RESET:
        reset()
        return choice
    return QUIT

if __name__ == "__main__":
    print("Hello ! This program is not case sensitive.")
    exit_var = EMPTY
    while exit_var != QUIT:
        check_file()
        if os.stat(FILENAME).st_size == 0:
            print("This file is empty please add a Character")
            exit_var = add_character()
        elif get_todos()[1] == 0:
            exit_var = ask_for_reset()
        else:
            exit_var = ask_complete()