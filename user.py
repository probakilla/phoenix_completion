import os
from file import add_character, check_file, complete_character, FILENAME
from file import flush_file, get_all_characters, get_todos, remove_from_file
from file import reset, format_name

MAX_LINE_LENGTH = 32

PROMPT = "> "
INPUT_ERROR = "Invalid input"

ADD_CHAR = "A"
DELETE = "D"
FLUSH = "F"
MARK = "M"
QUIT = "Q"
RESET = "R"
NO = "N"
EMPTY = ""
YES = "Y"
NO = "N"

LIST_CHOICES = [ADD_CHAR, DELETE, FLUSH,MARK, RESET, QUIT]
RESET_CHOICES = [EMPTY, YES, NO]
YES_CHOICE = [EMPTY, YES]


def correct_name(name):
    return " " not in name


def ask_char_name():
    print("Please enter a name for a new character :")
    print("(Naming it q or Q will quit)")
    while True:
        name = input(PROMPT)
        if correct_name(name):
            break
        print("No spaces in names")
    if name.upper() != QUIT:
        add_character(name)
    return name.upper()


def ask_for_reset():
    print("No character left, want to reset ? Y/n")
    while True:
        choice = input(PROMPT)
        if choice.upper() in RESET_CHOICES:
            break
        print(INPUT_ERROR + " : Enter y or n")
    if choice.upper() in YES_CHOICE:
        reset()
    elif choice.upper() == NO:
        return QUIT
    return QUIT


def ask_delete():
    print("Please select a character to delete :")
    list_char = get_all_characters()
    print(list_char[0])
    print("\t" + QUIT + ") Quit\n")
    while True:
        num = input(PROMPT)
        if not num.isdigit():
            if num.upper() == QUIT:
                break
        elif num.isdigit():
            if 0 <= int(num) < list_char[1]:
                break
        print(INPUT_ERROR + " : Enter the number of a character")
    if num.isdigit():
        name = clean_tab_char(list_char[0])
        remove_from_file(name[int(num)])
    return num


def ask_mark():
    characters = get_todos()
    print("Now choose one character :")
    print(characters[0])
    print("\t" + QUIT + ") Quit\n")
    while True:
        char = input(PROMPT)
        if char.upper() == QUIT or  0 <= int(char) < characters[1]:
            break
        print(INPUT_ERROR + " : Enter the number of a character")
    if char.isdigit():
        complete_character(clean_tab_char(characters[0])[int(char)])
    return char


def ask_action():
    print("Here is the list of remaining characters : ", end="")
    print(get_todos()[0] + "\n")
    print("What do you want to do ?")
    print(format_name("\t" + ADD_CHAR + ") Add a new character in file ",
        MAX_LINE_LENGTH), end="")
    print(format_name("\t" + DELETE + ") Delete a character", MAX_LINE_LENGTH),
        end="")
    print(format_name("\t" + FLUSH + ") Flush all characters", MAX_LINE_LENGTH))
    print(format_name("\t" + MARK + ") Mark a character as DONE",
        MAX_LINE_LENGTH), end="")
    print(format_name("\t" + RESET + ") Reset characters", MAX_LINE_LENGTH),
        end="")
    print(format_name("\t" + QUIT+  ") Quit", MAX_LINE_LENGTH))
    while True:
        choice = input(PROMPT)
        if choice.upper() in LIST_CHOICES:
            break
        error = INPUT_ERROR + " : Select a valid action : "
        for e in LIST_CHOICES:
            error += str(e) + " "
        print(error)
    if choice.upper() == ADD_CHAR:
        return ask_char_name()
    elif choice.upper() == FLUSH:
        flush_file()
        return choice
    elif choice.upper() == DELETE:
        return ask_delete()
    elif choice.upper() == MARK:
        return ask_mark()
    elif choice.upper() == RESET:
        reset()
        return choice
    return QUIT


def check_start():
    exit_var = EMPTY
    while exit_var != QUIT:
        check_file()
        if os.stat(FILENAME).st_size == 0:
            print("This file is empty please add a Character")
            exit_var = ask_char_name()
        elif get_todos()[1] == 0:
            exit_var = ask_for_reset()
        else:
            exit_var = ask_action()


def clean_tab_char(string):
    name = string.split()
    return [x for x in name if not any(c.isdigit() for c in x)]