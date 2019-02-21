import os

TODO = "todo"
DONE = "done"
PROMPT = ""

FILENAME = "data"

MARK = "M"
RESET = "R"
ADD_CHAR = "A"
QUIT = "Q"
NO = "N"

LIST_CHOICES = [ADD_CHAR, MARK, RESET, QUIT]
RESET_CHOICES = ["", "Y", "N"]
YES_CHOICE = ["", "Y"]

def ask_for_reset():
    print("No character left, want to reset ? Y/n")
    while True:
        choice = input(PROMPT)
        if choice.upper() in RESET_CHOICES:
            break
    if choice.upper() in YES_CHOICE:
        print("OK")
    elif choice.upper() == NO:
        print("NO")

def add_character(name):
    with open(FILENAME, "w") as file:
        file.write(name + " : " + TODO)

def reset():
    string = open(FILENAME).read()
    string = string.replace(DONE, TODO)
    with open(FILENAME, "w") as file:
        file.write(string)

def sort_lines():
    lines = open(FILENAME, "r").readlines()
    with open(FILENAME, "w") as out_file:
        for line in sorted(lines, key=lambda line: line.split(" ")[0], reverse=True):
            out_file.write(line + os.linesep)

def get_todos():
    cpt = 0
    lines = open(FILENAME, "r").readlines()
    output = ""
    for line in lines:
        if TODO in line:
            output += "\t" + str(cpt) + ") " + line.split()[0] + os.linesep
            cpt += 1
    return (output, cpt)

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

def ask_complete():
    print("Here is the list of remaining characters : " + os.linesep)
    print(get_todos()[0])
    print("What do you want to do ?")
    print("\tD) Mark one as DONE")
    print("\tR) Reset characters")
    print("\tQ) Quit")
    while True:
        choice = input(PROMPT)
        if choice.upper() in LIST_CHOICES:
            break
    if choice.upper() == "D":
        characters = get_todos()
        print("\tQ) Quit")
        print(characters[0])
        print("Now choose one character :")
        while True:
            char = input(PROMPT)
            if char.upper() == "Q" or  0 <= int(char) < characters[1]:
                break
        if char.isdigit():
            complete_char_from_num(char, characters[0])

if __name__ == "__main__":
    if get_todos()[1] == 0:
        ask_for_reset()
    else:
        ask_complete()