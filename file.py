import os

TODO = "todo"
DONE = "done"

FILENAME = "data"
LINE_LENGTH = 3
MAX_IN_LINE = 4
MAX_NAME_LENGTH = 20
FILLER = " "

NAME_COL = 0
SEP_COL = 1
VERB_COL = 2


def format_name(name, length):
    string = name
    if len(name) > length:
        return string[:length]
    for _ in range(length - len(name)):
        string += FILLER
    return string


def check_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w+"): pass
        return
    file = open(FILENAME).read()
    filestr = open(FILENAME).read()
    if filestr == "":
        return
    with open(FILENAME, "w") as out:
        out.write(file.rstrip() + "\n")
    lines = open(FILENAME).readlines()
    for line in lines:
        if len(line.split()) != LINE_LENGTH:
            print("FILE ILL FORMED\nPress any key...")
            input("")
            exit()

def flush_file():
    with open(FILENAME, "w") as out:
        out.write("")

def complete_character(char_name):
    print(char_name)
    out = ""
    lines = open(FILENAME).readlines()
    for line in lines:
        if char_name not in line:
            out += line
        else:
            line = line.replace(TODO, DONE)
            out += line
    with open(FILENAME, "w") as outfile:
        outfile.write(out)


def reset():
    string = open(FILENAME).read()
    string = string.replace(DONE, TODO)
    with open(FILENAME, "w") as file:
        file.write(string)


def remove_from_file(name):
    lines = open(FILENAME, "r").readlines()
    with open(FILENAME, "w") as outfile:
        for line in lines:
            if name not in line:
                outfile.write(line)


def add_character(name):
    name = format_name(name, MAX_NAME_LENGTH)
    with open(FILENAME, "a") as file:
        file.write(name + " : " + TODO + os.linesep)


def get_todos():
    cpt = 0
    lines = open(FILENAME, "r").readlines()
    output = ""
    for line in lines:
        if TODO in line:
            if cpt % MAX_IN_LINE == 0:
                output += "\n\t"
            sup_char = len(str(cpt)) - 1
            output += str(cpt) + ") " + format_name(line.split(":")[0],
            MAX_NAME_LENGTH - sup_char)
            cpt += 1
    return (output.rstrip(), cpt)


def get_all_characters():
    cpt = 0
    lines = open(FILENAME, "r").readlines()
    output = ""
    for line in lines:
        if len(line.split()) == LINE_LENGTH:
            if cpt % MAX_IN_LINE == 0:
                output += "\n\t"
            sup_char = len(str(cpt)) - 1
            output += str(cpt) + ") " + format_name(line.split()[NAME_COL],
            MAX_NAME_LENGTH - sup_char) + " "
            cpt += 1
    return (output.rstrip(), cpt)