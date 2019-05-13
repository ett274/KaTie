# --------OVERARCHING THINGS-----------
def NeedyInput(prompt, acceptable_responses):
    while True:
        response = raw_input(prompt).lower()
        if response in acceptable_responses:
            return response
        else:
            print "Invalid input."


def YesNo(prompt):
    answer = NeedyInput(prompt + " (y/n): ", ["y", "n"])
    if answer == "y":
        return True
    elif answer == "n":
        return False


def first_second_etc(number):
    if not isinstance(number, str):
        raise ValueError
    elif number[len(number) - 1] == "1":
        return "%sst" % number
    elif number[len(number) - 1] == "2":
        return "%snd" % number
    elif number[len(number) - 1] == "3":
        return "%srd" % number
    else:
        return "%sth" % number


class OverSightError(Exception):
    def __init__(self):
        Exception.__init__(self, "oh gosh, i missed something, didn't i")


color_dict = {"red": "red", "blu": "blue", "blue": "blue", "yel": "yellow", "yellow": "yellow", "gre": "green",
              "green": "green", "whi": "white", "white": "white", "bla": "black", "black": "black"}


# --------SPECIFIC MODULES-----------

def defuse_wires(wires, serial_odd):
    if len(wires) == 3:
        if "red" not in wires:
            return "Cut the second wire."
        elif wires[2] == "white":
            return "Cut the last wire."
        elif wires.count("blue") > 1:
            return "Cut the last blue wire."
        else:
            return "Cut the last wire."
    elif len(wires) == 4:
        if wires.count("red") > 1 and serial_odd is True:
            return "Cut the last red wire."
        elif wires[3] == "yellow" and "red" not in wires:
            return "Cut the first wire."
        elif wires.count("blue") == 1:
            return "Cut the first wire."
        elif wires.count("yellow") > 1:
            return "Cut the last wire."
        else:
            return "Cut the second wire."
    elif len(wires) == 5:
        if wires[4] == "black" and serial_odd is True:
            return "Cut the fourth wire."
        elif wires.count("red") == 1 and wires.count("yellow") > 1:
            return "Cut the first wire."
        elif "black" not in wires:
            return "Cut the second wire."
        else:
            return "Cut the first wire."
    elif len(wires) == 6:
        if "yellow" not in wires and serial_odd is True:
            return "Cut the third wire."
        elif wires.count("yellow") == 1 and wires.count("white") > 1:
            return "Cut the fourth wire."
        elif "red" not in wires:
            return "Cut the last wire."
        else:
            return "Cut the fourth wire."


def defuse_button(color, word, car_bool, frk_bool, bat_num):
    def hold():
        strip_color = color_dict[NeedyInput(
            "Hold down the button; a colored strip will light up next to the button. What color is it? ",
            ["white", "whi", "red", "blue", "blu", "yellow", "yel"])]
        if strip_color == "blue":
            return "Release the button when the timer has a 4 in any position."
        elif strip_color == "yellow":
            return "Release the button when the timer has a 5 in any position."
        else:
            return "Release the button when the timer has a 1 in any position."

    if color == "blue" and word == "abort":
        return hold()
    elif bat_num > 1 and word == "detonate":
        return "Press and immediately release the button."
    elif color == "white" and car_bool is True:
        return hold()
    elif bat_num > 2 and frk_bool is True:
        return "Press and immediately release the button."
    elif color == "yellow":
        return hold()
    elif color == "red" and word == "hold":
        return "Press and immediately release the button."
    else:
        return hold()


def defuse_symbols():
    while True:
        symbol_list = []
        answer_list = []
        crect_list = []
        symbols = ["q", "at", "lambda", "rest", "alien", "ge", "back c", "e", "swirl", "white star", "question",
                   "copyright", "w", "xi", "droop r", "6", "paragraph", "tb", "psi", "face", "bunny",
                   "black star", "!=", "ae", "n", "ohm", "c"]
        available_symbols = list(symbols)
        is_list = False
        for buttoning in range(4):
            symbul = NeedyInput("Input the symbols you see. Order doesn't matter: ", available_symbols)
            symbol_list.append(symbul)
            available_symbols.remove(symbul)
        lists = [["q", "at", "lambda", "rest", "alien", "ge", "back c"],
                 ["e", "q", "back c", "swirl", "white star", "ge", "question"],
                 ["copyright", "w", "swirl", "xi", "droop r", "lambda", "white star"],
                 ["6", "paragraph", "tb", "alien", "xi", "question", "face"],
                 ["psi", "face", "tb", "c", "paragraph", "bunny", "black star"],
                 ["6", "e", "!=", "ae", "psi", "n", "ohm"]]
        for lst in lists:
            if symbol_list[0] in lst and symbol_list[1] in lst and symbol_list[2] in lst and symbol_list[3] in lst:
                is_list = True
                crect_list = lst
                break
        if is_list is True:
            for wait in crect_list:
                if wait in symbol_list:
                    answer_list.append(wait)
            return "Press the symbols in this order: " + ", ".join(answer_list)
        else:
            print "Something went wrong. Did you input the correct symbols?"


def defuse_simon(vowel):
    step = 0
    color_list = []
    input_list = []
    no_strikes_vowel = {"red": "blue", "blue": "red", "green": "yellow", "yellow": "green"}
    one_strike_vowel = {"red": "yellow", "blue": "green", "green": "blue", "yellow": "red"}
    two_strikes_vowel = {"red": "green", "blue": "red", "green": "yellow", "yellow": "blue"}
    no_strikes_no_vowel = {"red": "blue", "blue": "yellow", "green": "green", "yellow": "red"}
    one_strike_no_vowel = {"red": "red", "blue": "blue", "green": "yellow", "yellow": "green"}
    while True:
        try:
            strikes = int(raw_input("How many strikes do we have? "))
        except ValueError:
            print "Invalid Input."
        else:
            if strikes > 2 or strikes < 0:
                print "Invalid Input."
            else:
                break
    colors_dict = {}
    if vowel is True:
        if strikes == 0:
            colors_dict = no_strikes_vowel
        elif strikes == 1:
            colors_dict = one_strike_vowel
        elif strikes == 2:
            colors_dict = two_strikes_vowel
    else:
        if strikes == 0:
            colors_dict = no_strikes_no_vowel
        elif strikes == 1:
            colors_dict = one_strike_no_vowel
        elif strikes == 2:
            colors_dict = one_strike_vowel
    while step < 5:
        color = NeedyInput("What is the last color that flashed? (or type 'done' if finished, or 's' if we got a strike): ",
                           ["red", "blue", "blu", "green", "gre", "yellow", "yel", "done", "s"])
        if color == "done":
            return
        elif color == 's':
            strikes += 1
            if strikes == 3:
                print "Oops. Sorry."
                return
            elif vowel is False:
                if strikes == 1:
                    colors_dict = one_strike_no_vowel
                elif strikes == 2:
                    colors_dict = one_strike_vowel
            elif vowel is True:
                if strikes == 1:
                    colors_dict = one_strike_vowel
                elif strikes == 2:
                    colors_dict = two_strikes_vowel
            color_list = []
            for incur in input_list:
                color_list.append(colors_dict[color_dict[incur]])
        else:
            input_list.append(color)
            color = color_dict[color]
            color_list.append(colors_dict[color])
            print "Press the buttons in this order: " + ", ".join(color_list)
            step += 1


def whos_on_first():
    for rum in range(3):
        display = NeedyInput("What is the word on display? (Type 'black' if there is nothing there): ",
                             ["yes", "first", "display", "okay", "says", "nothing", "black", "blank", "no", "led",
                              "lead", "read", "red", "reed", "leed", "hold on", "you", "you are", "your", "you're",
                              "ur", "there", "they're", "their", "they are", "see", "c", "cee"])
        if display == "ur":
            word = NeedyInput("What is the word on the top left? ",
                              ["ready", "first", "no", "blank", "nothing", "yes", "what", "uhhh", "left", "right",
                               'middle', 'okay', 'wait', 'press', 'you', 'you are', 'your', "you're", 'ur', 'u',
                               'uh huh', 'uh uh', 'what?', 'done', 'next', 'sure', 'like'])
        elif display == "first" or display == "okay" or display == "c":
            word = NeedyInput("What is the word on the top right? ",
                              ["ready", "first", "no", "blank", "nothing", "yes", "what", "uhhh", "left", "right",
                               'middle',
                               'okay', 'wait', 'press', 'you', 'you are', 'your', "you're", 'ur', 'u', 'uh huh',
                               'uh uh',
                               'what?', 'done', 'next', 'sure', 'like', 'hold'])
        elif display == "nothing" or display == "led" or display == "they are" or display == "yes":
            word = NeedyInput("What is the word on the middle left? ",
                              ["ready", "first", "no", "blank", "nothing", "yes", "what", "uhhh", "left", "right",
                               'middle',
                               'okay', 'wait', 'press', 'you', 'you are', 'your', "you're", 'ur', 'u', 'uh huh',
                               'uh uh',
                               'what?', 'done', 'next', 'sure', 'like', 'hold'])
        elif display == "red" or display == "read" or display == "you" or display == "their" or display == "you're" or display == "your" or display == "blank":
            word = NeedyInput("What is the word on the middle right? ",
                              ["ready", "first", "no", "blank", "nothing", "yes", "what", "uhhh", "left", "right",
                               'middle',
                               'okay', 'wait', 'press', 'you', 'you are', 'your', "you're", 'ur', 'u', 'uh huh',
                               'uh uh',
                               'what?', 'done', 'next', 'sure', 'like', 'hold'])
        elif display == "black" or display == "they're" or display == "reed" or display == "leed":
            word = NeedyInput("What is the word on the bottom left? ",
                              ["ready", "first", "no", "blank", "nothing", "yes", "what", "uhhh", "left", "right",
                               'middle',
                               'okay', 'wait', 'press', 'you', 'you are', 'your', "you're", 'ur', 'u', 'uh huh',
                               'uh uh',
                               'what?', 'done', 'next', 'sure', 'like', 'hold'])
        elif display == "see" or display == "cee" or display == "display" or display == "says" or display == "no" or display == "hold on" or display == "you are" or display == "there" or display == "lead" or display == "no":
            word = NeedyInput("What is the word on the bottom right? ",
                              ["ready", "first", "no", "blank", "nothing", "yes", "what", "uhhh", "left", "right",
                               'middle',
                               'okay', 'wait', 'press', 'you', 'you are', 'your', "you're", 'ur', 'u', 'uh huh',
                               'uh uh',
                               'what?', 'done', 'next', 'sure', 'like', 'hold'])
        else:
            raise OverSightError
        if word != "what" and word != "left" and word != "you're" and word != "uh huh":
            print "Push the first button that appears on this list:"
        if word == "ready":
            print "YES, OKAY, WHAT, MIDDLE, LEFT, PRESS, RIGHT, BLANK, READY"
        elif word == "first":
            print "LEFT, OKAY, YES, MIDDLE, NO, RIGHT, NOTHING, UHHH, WAIT, READY, BLANK, WHAT, PRESS, FIRST"
        elif word == "no":
            print "BLANK, UHHH, WAIT, FIRST, WHAT, READY, RIGHT, YES, NOTHING, LEFT, PRESS, OKAY, NO"
        elif word == "blank":
            print "WAIT, RIGHT, OKAY, MIDDLE, BLANK"
        elif word == "nothing":
            print "UHHH, RIGHT, OKAY, MIDDLE, YES, BLANK, NO, PRESS, LEFT, WHAT, WAIT, FIRST, NOTHING"
        elif word == "yes":
            print "OKAY, RIGHT, UHHH, MIDDLE, FIRST, WHAT, PRESS, READY, NOTHING, YES"
        elif word == "what":
            print "Press UHHH. If UHHH is not here, press WHAT."
        elif word == "uhhh":
            print "READY, NOTHING, LEFT, WHAT, OKAY, YES, RIGHT, NO, PRESS, BLANK, UHHH"
        elif word == "left":
            print "Press RIGHT. If RIGHT is not here, press LEFT."
        elif word == "right":
            print "YES, NOTHING, READY, PRESS, NO, WAIT, WHAT, RIGHT"
        elif word == "middle":
            print "BLANK, READY, OKAY, WHAT, NOTHING, PRESS, NO, WAIT, LEFT, MIDDLE"
        elif word == "okay":
            print "MIDDLE, NO, FIRST, YES, UHHH, NOTHING, WAIT, OKAY"
        elif word == "wait":
            print "UHHH, NO, BLANK, OKAY, YES, LEFT, FIRST, PRESS, WHAT, WAIT"
        elif word == "press":
            print "RIGHT, MIDDLE, YES, READY, PRESS"
        elif word == "you":
            print "SURE, YOU ARE, YOUR, YOU'RE, NEXT, UH HUH, UR, HOLD, WHAT?, YOU"
        elif word == "you are":
            print "YOUR, NEXT, LIKE, UH HUH, WHAT?, DONE, UH UH, HOLD, YOU, U, YOU'RE, SURE, UR, YOU ARE"
        elif word == "your":
            print "UH UH, YOU ARE, UH HUH, YOUR"
        elif word == "you're":
            print "Press YOU. If YOU is not here, press YOU'RE."
        elif word == "ur":
            print "DONE, U, UR"
        elif word == "u":
            print "UH HUH, SURE, NEXT, WHAT?, YOU'RE, UR, UH UH, DONE, U"
        elif word == "uh huh":
            print "Press UH HUH."
        elif word == "uh uh":
            print "UR, U, YOU ARE, YOU'RE, NEXT, UH UH"
        elif word == "what?":
            print "YOU, HOLD, YOU'RE, YOUR, U, DONE, UH UH, LIKE, YOU ARE, UH HUH, UR, NEXT, WHAT?"
        elif word == "done":
            print "SURE, UH HUH, NEXT, WHAT?, YOUR, UR, YOU'RE, HOLD, LIKE, YOU, U, YOU ARE, UH UH, DONE"
        elif word == "next":
            print "WHAT?, UH HUH, UH UH, YOUR, HOLD, SURE, NEXT"
        elif word == "hold":
            print "YOU ARE, U, DONE, UH UH, YOU, UR, SURE, WHAT?, YOU'RE, NEXT, HOLD"
        elif word == "sure":
            print "YOU ARE, DONE, LIKE, YOU'RE, YOU, HOLD, UH HUH, UR, SURE"
        elif word == "like":
            print "YOU'RE, NEXT, U, UR, HOLD, DONE, UH UH, WHAT?, UH HUH, YOU, LIKE"
        else:
            raise OverSightError


def defuse_complicated(digit_odd, parallel, bats):
    print "Instructions"
    print "---------------------------"
    print "For each wire, starting from the far left, input a series of letters based on its properties."
    print "Put 'l' if the light above the wire is on, put 'r' if the wire has red coloring, put 'b' if the wire has " \
          "blue coloring, and put 's' if there is a star beneath the wire. "
    print "Put 'n' if the wire has none of those traits."
    print "** IMPORTANT: A RED AND WHITE STRIPED WIRE IS CONSIDERED THE EXACT SAME AS A SOLID RED WIRE; DON'T WORRY " \
          "ABOUT WHITE STRIPES ** "
    print "Examples include: rb, ls, n, b, lbrs, lbs"
    print "Also, ignore blank spaces between wires."
    print "---------------------------"
    instruction_list = []
    for lumber in range(6):
        wire = NeedyInput("Describe the %s wire. (Put done if done): " % first_second_etc(str(lumber + 1)),
                          ["lrbs", "lrsb", "lbrs", "lbsr", "lsrb", "lsbr", "rlsb", "rlbs", "rbsl", "rbls", "rsbl",
                           "rslb", "blrs", "blsr", "brls", "brsl", "bslr", "bsrl", "slbr", "slrb", "srbl", "srlb",
                           "sbrl", "sblr", "lrb", "lrs", "lbr", "lbs", "lsr", "lsb", "rls", "rlb", "rbs", "rbl", "rsb",
                           "rsl", "blr", "bls", "brl", "brs", "bsl", "bsr", "slb", "slr", "srb", "srl", "sbr", "sbl",
                           "lr", "lb", "ls", "rl", "rb", "rs", "bl", "br", "bs", "sl", "sr",
                           "sb", "b", "l", "r", "s", "n", "done"])
        if wire == "done":
            return ", ".join(instruction_list)
        elif wire == "n":
            instruction_list.append("Cut")
        else:
            if "l" in wire:
                if "s" in wire:
                    if "r" in wire:
                        if "b" in wire:
                            instruction_list.append("Don't Cut")
                        else:
                            if bats >= 2:
                                instruction_list.append("Cut")
                            else:
                                instruction_list.append("Don't Cut")
                    else:
                        if "b" in wire:
                            if parallel is True:
                                instruction_list.append("Cut")
                            else:
                                instruction_list.append("Don't Cut")
                        else:
                            if bats >= 2:
                                instruction_list.append("Cut")
                            else:
                                instruction_list.append("Don't Cut")

                else:
                    if "r" in wire:
                        if "b" in wire:
                            if digit_odd is False:
                                instruction_list.append("Cut")
                            else:
                                instruction_list.append("Don't Cut")
                        else:
                            if bats >= 2:
                                instruction_list.append("Cut")
                            else:
                                instruction_list.append("Don't Cut")
                    else:
                        if "b" in wire:
                            if parallel is True:
                                instruction_list.append("Cut")
                            else:
                                instruction_list.append("Don't Cut")
                        else:
                            instruction_list.append("Don't Cut")
            else:
                if "s" in wire:
                    if "r" in wire:
                        if "b" in wire:
                            if parallel is True:
                                instruction_list.append("Cut")
                            else:
                                instruction_list.append("Don't Cut")
                        else:
                            instruction_list.append("Cut")
                    else:
                        if "b" in wire:
                            instruction_list.append("Don't Cut")
                        else:
                            instruction_list.append("Cut")
                else:
                    if "r" in wire:
                        if digit_odd is False:
                            instruction_list.append("Cut")
                        else:
                            instruction_list.append("Don't Cut")
                    else:
                        if "b" in wire:
                            if digit_odd is False:
                                instruction_list.append("Cut")
                            else:
                                instruction_list.append("Don't Cut")
                        else:
                            raise OverSightError
    return ", ".join(instruction_list)


def defuse_memory():
    stage1_label = None
    stage1_position = None
    stage2_label = None
    stage2_position = None
    stage3_label = None
    stage4_label = None
    keys = ":0"
    for stage in range(1, 6):
        display = NeedyInput("What is the number on display? ", ["1", "2", "3", "4"])
        if stage < 5:
            keys = NeedyInput("What are the numbers on the buttons? (In order): ",
                              ["1234", "1243", "1324", "1342", "1423", "1432", "2143", "2134", "2341", "2314", "2431",
                               "2413", "3124", "3142", "3214", "3241", "3412", "3421", "4132", "4123", "4231", "4213",
                               "4321", "4312"])
        if stage == 1:
            if display == "1" or display == "2":
                print("Press %s." % keys[1])
                stage1_label = keys[1]
                stage1_position = 1
            elif display == "3":
                print("Press %s." % keys[2])
                stage1_label = keys[2]
                stage1_position = 2
            elif display == "4":
                print("Press %s." % keys[3])
                stage1_label = keys[3]
                stage1_position = 3
        elif stage == 2:
            if display == "1":
                print "Press 4."
                stage2_label = "4"
                for zz in range(4):
                    if keys[zz] == "4":
                        stage2_position = zz
                        break
            elif display == "2" or display == "4":
                print("Press %s." % keys[stage1_position])
                stage2_position = stage1_position
                stage2_label = keys[stage1_position]
            elif display == "3":
                print("Press %s." % keys[0])
                stage2_label = keys[0]
                stage2_position = 0
        elif stage == 3:
            if display == "1":
                print("Press %s." % stage2_label)
                stage3_label = stage2_label
            elif display == "2":
                print("Press %s." % stage1_label)
                stage3_label = stage1_label
            elif display == "3":
                print("Press %s." % keys[2])
                stage3_label = keys[2]
            elif display == "4":
                print "Press 4."
                stage3_label = "4"
        elif stage == 4:
            if display == "1":
                print("Press %s." % keys[stage1_position])
                stage4_label = keys[stage1_position]
            elif display == "2":
                print("Press %s." % keys[0])
                stage4_label = keys[0]
            elif display == "3" or display == "4":
                print("Press %s." % keys[stage2_position])
                stage4_label = keys[stage2_position]
        elif stage == 5:
            if display == "1":
                print("Press %s." % stage1_label)
            elif display == "2":
                print("Press %s." % stage2_label)
            elif display == "3":
                print("Press %s." % stage4_label)
            elif display == "4":
                print("Press %s." % stage3_label)


def defuse_password():
    possible_passwords = ["about", "after", "again", "below", "could", "every", "first", "found", "great", "house",
                          "large", "learn", "never", "other", "place", "plant", "point", "right", "small", "sound",
                          "spell", "still", "study", "their", "there", "these", "thing", "think", "three", "water",
                          "where", "which", "world", "would", "write"]
    wanna_see = YesNo("Do you want to see the passwords left?")
    method = NeedyInput("Do you want to go straight, or back and forth? ", ["straight", "back"])
    for numb in range(5):
        if method == "back":
            if numb == 0:
                zyrm = 0
            elif numb == 1:
                zyrm = 4
            elif numb == 2:
                zyrm = 1
            elif numb == 3:
                zyrm = 3
            elif numb == 4:
                zyrm = 2
        else:
            zyrm = numb
        if wanna_see is True:
            print "These passwords are left: " + ", ".join(possible_passwords)
        while True:
            let = raw_input("Tell me each letter in the %s slot: " % first_second_etc(str(zyrm + 1))).lower()
            is_valid = True
            if not all(char.isalpha() for char in let):
                print "Invalid input."
            elif len(let) != 6:
                print "Invalid input."
            else:
                letters = []
                for lettin in let:
                    if lettin in letters:
                        print "Invalid input."
                        is_valid = False
                        break
                    else:
                        letters.append(lettin)
                if is_valid is True:
                    break
        still_included = []
        for password in possible_passwords:
            if password[zyrm] in let:
                still_included.append(password)
        if len(still_included) == 1:
            return "The password is " + still_included[0] + "."
        elif len(still_included) == 0:
            print "Uh oh. Something went wrong. Let's try that again."
            print "--------------------------------------------------------------------"
            return defuse_password()
        else:
            possible_passwords = still_included


def defuse_sequence():
    red = 1
    blue = 1
    black = 1
    # [color, letter]
    for numb in range(4):
        instructions = []
        wires = []
        for num in range(3):
            color = NeedyInput("What color is the %s wire? (or type 'done' if done): " % first_second_etc(str(num + 1)),
                               ["red", "blue", "blu", "black", "bla", "done", "stop"])
            if color == "stop":
                return
            elif color == "done":
                break
            else:
                color = color_dict[color]
            letter = NeedyInput("What letter is it connected to? ", ["a", "b", "c"])
            wires.append([color, letter])
        for wire in wires:
            if wire[0] == "red":
                if red == 1:
                    if wire[1] == "c":
                        instructions.append("Cut")
                    else:
                        instructions.append("Don't Cut")
                elif red == 2:
                    if wire[1] == "b":
                        instructions.append("Cut")
                    else:
                        instructions.append("Don't Cut")
                elif red == 3:
                    if wire[1] == "a":
                        instructions.append("Cut")
                    else:
                        instructions.append("Don't Cut")
                elif red == 4:
                    if wire[1] == "c" or wire[1] == "a":
                        instructions.append("Cut")
                    else:
                        instructions.append("Don't Cut")
                elif red == 5:
                    if wire[1] == "b":
                        instructions.append("Cut")
                    else:
                        instructions.append("Don't Cut")
                elif red == 6:
                    if wire[1] == "c" or wire[1] == "a":
                        instructions.append("Cut")
                    else:
                        instructions.append("Don't Cut")
                elif red == 7:
                    instructions.append("Cut")
                elif red == 8:
                    if wire[1] != "c":
                        instructions.append("Cut")
                    else:
                        instructions.append("Don't Cut")
                elif red == 9:
                    if wire[1] == "b":
                        instructions.append("Cut")
                    else:
                        instructions.append("Don't Cut")
                else:
                    raise OverSightError
                red += 1
            elif wire[0] == "blue":
                if blue == 1:
                    if wire[1] == "b":
                        instructions.append("Cut")
                    else:
                        instructions.append("Don't Cut")
                elif blue == 2:
                    if wire[1] != "b":
                        instructions.append("Cut")
                    else:
                        instructions.append("Don't Cut")
                elif blue == 3:
                    if wire[1] == "b":
                        instructions.append("Cut")
                    else:
                        instructions.append("Don't Cut")
                elif blue == 4:
                    if wire[1] == "a":
                        instructions.append("Cut")
                    else:
                        instructions.append("Don't Cut")
                elif blue == 5:
                    if wire[1] == "b":
                        instructions.append("Cut")
                    else:
                        instructions.append("Don't Cut")
                elif blue == 6:
                    if wire[1] == "c" or wire[1] == "b":
                        instructions.append("Cut")
                    else:
                        instructions.append("Don't Cut")
                elif blue == 7:
                    if wire[1] != "c":
                        instructions.append("Cut")
                    else:
                        instructions.append("Don't Cut")
                elif blue == 8:
                    if wire[1] == "c" or wire[1] == "a":
                        instructions.append("Cut")
                    else:
                        instructions.append("Don't Cut")
                elif blue == 9:
                    if wire[1] == "a":
                        instructions.append("Cut")
                    else:
                        instructions.append("Don't Cut")
                else:
                    raise OverSightError
                blue += 1
            elif wire[0] == "black":
                if black == 1:
                    instructions.append("Cut")
                elif black == 2:
                    if wire[1] != "b":
                        instructions.append("Cut")
                    else:
                        instructions.append("Don't Cut")
                elif black == 3:
                    if wire[1] == "b":
                        instructions.append("Cut")
                    else:
                        instructions.append("Don't Cut")
                elif black == 4:
                    if wire[1] == "a" or wire[1] == "c":
                        instructions.append("Cut")
                    else:
                        instructions.append("Don't Cut")
                elif black == 5:
                    if wire[1] == "b":
                        instructions.append("Cut")
                    else:
                        instructions.append("Don't Cut")
                elif black == 6:
                    if wire[1] == "c" or wire[1] == "b":
                        instructions.append("Cut")
                    else:
                        instructions.append("Don't Cut")
                elif black == 7:
                    if wire[1] != "c":
                        instructions.append("Cut")
                    else:
                        instructions.append("Don't Cut")
                elif black == 8:
                    if wire[1] == "c":
                        instructions.append("Cut")
                    else:
                        instructions.append("Don't Cut")
                elif black == 9:
                    if wire[1] == "c":
                        instructions.append("Cut")
                    else:
                        instructions.append("Don't Cut")
                else:
                    raise OverSightError
                black += 1
        print ", ".join(instructions)


def defuse_morse():
    print "Wait for a long pause between flashes, then begin inputting letters."
    morse_dict = {'.-': 'a', "-...": 'b', "-.-.": "c", "-..": "d", ".": 'e', "..-.": "f", "--.": "g",
                  "....": "h", "..": "i", "-.-": 'k', ".-..": 'l', "--": "m", "-.": "n",
                  "---": "o", ".-.": 'r', "...": "s", "-": "t",
                  "...-": "v", "-..-": "x"}
    code_dict = {"shell": "3.505", "halls": "3.515", "slick": "3.522", "trick": "3.532", "boxes": "3.535",
                 "leaks": "3.542", "strobe": "3.545", "bistro": "3.552", "flick": "3.555", "bombs": "3.565",
                 "break": "3.572", "brick": "3.575", "steak": "3.582", "sting": "3.592", "vector": "3.595",
                 "beats": "3.600"}
    possible_words = ["shell", "halls", "slick", "trick", "boxes", "leaks", "strobe", "bistro", "flick", "bombs",
                      "break", "brick", "steak", "sting", "vector", "beats"]
    for num in range(6):
        still_here = []
        inp = NeedyInput(("What is the %s letter? " % first_second_etc(str(num + 1))),
                         ['...', '...-', '-', '.-', '..', '-.-.', '..-.', '-.', '....', '.', '---', '--', '-..-',
                          '--.', '-...', '-..', '.-.', '.-..', '-.-'])
        pinp = morse_dict.get(inp)
        for word in possible_words:
            if word[num] == pinp:
                still_here.append(word)
        else:
            if len(still_here) == 0:
                print "There was an error. Try again."
                return defuse_morse()
            else:
                possible_words = list(still_here)
                if len(possible_words) == 1:
                    return "Respond at " + code_dict[possible_words[0]] + " mHz."


def defuse_maze():
    # ulrd
    maze_1 = [["rd", "lr", "ld", "rd", "lr", "l"],
              ["ud", "rd", "ul", "ur", "lr", "ld"],
              ["ud", "ur", "ld", "rd", "lr", "uld"],
              ["ud", "r", "ulr", "ul", "r", "uld"],
              ["urd", "lr", "ld", "rd", "l", "ud"],
              ["ur", "l", "ur", "ul", "r", "ul"]]

    maze_2 = [["r", "lrd", "l", "rd", "lrd", "l"],
              ["rd", "ul", "rd", "ul", "ur", "ld"],
              ["ud", "rd", "ul", "rd", "lr", "uld"],
              ["urd", "ul", "rd", "ul", "d", "ud"],
              ["ud", "d", "ud", "rd", "ul", "ud"],
              ["u", "ur", "ul", "ur", "lr", "ul"]]

    maze_3 = [["rd", "lr", "ld", "d", "rd", "ld"],
              ["u", "d", "ud", "ur", "ul", "ud"],
              ["rd", "uld", "ud", "rd", "ld", "ud"],
              ["ud", "ud", "ud", "ud", "ud", "ud"],
              ["ud", "ur", "ul", "ud", "ud", "ud"],
              ["ur", "lr", "lr", "ul", "ur", "ul"]]

    maze_4 = [["rd", "ld", "r", "lr", "lr", "ld"],
              ["ud", "ud", "rd", "lr", "lr", "uld"],
              ["ud", "ur", "ul", "rd", "l", "ud"],
              ["ud", "r", "lr", "ulr", "lr", "uld"],
              ["urd", "lr", "lr", "lr", "ld", "ud"],
              ["ur", "lr", "l", "r", "ul", "u"]]

    maze_5 = [["r", "lr", "lr", "lr", "lrd", "ld"],
              ["rd", "lr", "lr", "lrd", "ul", "u"],
              ["urd", "ld", "r", "ul", "rd", "ld"],
              ["ud", "ur", "lr", "ld", "u", "ud"],
              ["ud", "rd", "lr", "ulr", "l", "ud"],
              ["u", "ur", "lr", "lr", "lr", "ul"]]

    maze_6 = [["d", "rd", "ld", "r", "lrd", "ld"],
              ["ud", "ud", "ud", "rd", "ul", "ud"],
              ["urd", "ul", "u", "ud", "rd", "ul"],
              ["ur", "ld", "rd", "uld", "ud", "d"],
              ["rd", "ul", "u", "ud", "ur", "uld"],
              ["ur", "lr", "lr", "ul", "r", "ul"]]

    maze_7 = [["rd", "lr", "lr", "ld", "rd", "ld"],
              ["ud", "rd", "l", "ur", "ul", "ud"],
              ["ur", "ul", "rd", "l", "rd", "ul"],
              ["rd", "ld", "urd", "lr", "ul", "d"],
              ["ud", "u", "ur", "lr", "ld", "ud"],
              ["ur", "lr", "lr", "lr", "ulr", "ul"]]

    maze_8 = [["d", "rd", "lr", "ld", "rd", "ld"],
              ["urd", "ulr", "l", "ur", "ul", "ud"],
              ["ud", "rd", "lr", "lr", "ld", "ud"],
              ["ud", "ur", "ld", "r", "ulr", "ul"],
              ["ud", "d", "ur", "lr", "lr", "l"],
              ["ur", "ulr", "lr", "lr", "lr", "l"]]

    maze_9 = [["d", "rd", "lr", "lr", "lrd", "ld"],
              ["ud", "ud", "rd", "l", "ud", "ud"],
              ["urd", "ulr", "ul", "rd", "ul", "ud"],
              ["ud", "d", "rd", "ul", "r", "uld"],
              ["ud", "ud", "ud", "rd", "ld", "u"],
              ["ur", "ul", "ur", "ul", "ur", "l"]]
    print "Treat the coordinates like a graph. The bottom left corner is (1, 1)."
    while True:
        while True:
            try:
                circle_1_x = int(raw_input("What is the x-coordinate of one of the circles? "))
            except ValueError:
                print "Invalid Input."
            else:
                if circle_1_x > 6 or circle_1_x < 1:
                    print "Invalid input."
                else:
                    break
        while True:
            try:
                circle_1_y = int(raw_input("What is the y-coordinate of that same circle? "))
            except ValueError:
                print "Invalid Input."
            else:
                if circle_1_y > 6 or circle_1_y < 1:
                    print "Invalid input."
                else:
                    break
        while True:
            try:
                circle_2_x = int(raw_input("What is the x-coordinate of the other circle? "))
            except ValueError:
                print "Invalid Input."
            else:
                if circle_2_x > 6 or circle_2_x < 1:
                    print "Invalid input."
                else:
                    break
        while True:
            try:
                circle_2_y = int(raw_input("What is the y-coordinate of that same circle? "))
            except ValueError:
                print "Invalid Input."
            else:
                if circle_2_y > 6 or circle_2_y < 1:
                    print "Invalid input."
                else:
                    break

        circle_list = [(circle_1_x, circle_1_y), (circle_2_x, circle_2_y)]
        if (1, 5) in circle_list and (6, 4) in circle_list:
            maze = list(maze_1)
            break
        elif (2, 3) in circle_list and (5, 5) in circle_list:
            maze = list(maze_2)
            break
        elif (4, 3) in circle_list and (6, 3) in circle_list:
            maze = list(maze_3)
            break
        elif (1, 3) in circle_list and (1, 6) in circle_list:
            maze = list(maze_4)
            break
        elif (4, 1) in circle_list and (5, 4) in circle_list:
            maze = list(maze_5)
            break
        elif (3, 2) in circle_list and (5, 6) in circle_list:
            maze = list(maze_6)
            break
        elif (2, 1) in circle_list and (2, 6) in circle_list:
            maze = list(maze_7)
            break
        elif (3, 3) in circle_list and (4, 6) in circle_list:
            maze = list(maze_8)
            break
        elif (1, 2) in circle_list and (3, 5) in circle_list:
            maze = list(maze_9)
            break
        else:
            print "Error: You might have inputted the circles incorrectly."

    while True:
        try:
            start_x = int(raw_input("What is the x-coordinate of the white square? "))
        except ValueError:
            print "Invalid Input."
        else:
            if start_x > 6 or start_x < 1:
                print "Invalid input."
            else:
                break
    while True:
        try:
            start_y = int(raw_input("What is the y-coordinate of the white square? "))
        except ValueError:
            print "Invalid Input."
        else:
            if start_y > 6 or start_y < 1:
                print "Invalid input."
            else:
                break
    while True:
        try:
            goal_x = int(raw_input("What is the x-coordinate of the red triangle? "))
        except ValueError:
            print "Invalid Input."
        else:
            if goal_x > 6 or goal_x < 1:
                print "Invalid input."
            else:
                break
    while True:
        try:
            goal_y = int(raw_input("What is the y-coordinate of the red triangle? "))
        except ValueError:
            print "Invalid Input."
        else:
            if goal_y > 6 or goal_y < 1:
                print "Invalid input."
            else:
                break

    start_y = 6 - start_y
    start_x -= 1
    goal_y = 6 - goal_y
    goal_x -= 1

    def traverse(maza, current_x, current_y, golb_x, golb_y, path_list, previous_direction):
        if current_x == golb_x and current_y == golb_y:
            return path_list
        direction_list = None
        if previous_direction == "start":
            direction_list = [move_right(maza, current_x, current_y, golb_x, golb_y, path_list),
                              move_left(maza, current_x, current_y, golb_x, golb_y, path_list),
                              move_down(maza, current_x, current_y, golb_x, golb_y, path_list),
                              move_up(maza, current_x, current_y, golb_x, golb_y, path_list)]
        elif previous_direction == "left":
            direction_list = [move_left(maza, current_x, current_y, golb_x, golb_y, path_list),
                              move_down(maza, current_x, current_y, golb_x, golb_y, path_list),
                              move_up(maza, current_x, current_y, golb_x, golb_y, path_list)]
        elif previous_direction == "right":
            direction_list = [move_right(maza, current_x, current_y, golb_x, golb_y, path_list),
                              move_down(maza, current_x, current_y, golb_x, golb_y, path_list),
                              move_up(maza, current_x, current_y, golb_x, golb_y, path_list)]
        elif previous_direction == "up":
            direction_list = [move_left(maza, current_x, current_y, golb_x, golb_y, path_list),
                              move_right(maza, current_x, current_y, golb_x, golb_y, path_list),
                              move_up(maza, current_x, current_y, golb_x, golb_y, path_list)]
        elif previous_direction == "down":
            direction_list = [move_left(maza, current_x, current_y, golb_x, golb_y, path_list),
                              move_down(maza, current_x, current_y, golb_x, golb_y, path_list),
                              move_right(maza, current_x, current_y, golb_x, golb_y, path_list)]
        shortest_list = None
        if all(direction is None for direction in direction_list):
            return None
        for item in direction_list:
            if item is not None:
                shortest_list = item
                break
        if shortest_list is None:
            return None
        for blister in direction_list:
            if blister is not None:
                if len(direction_list) < len(shortest_list):
                    shortest_list = blister
        return shortest_list

    def move_right(mazi, current_x, current_y, glob_x, glob_y, path_list):
        if "r" not in mazi[current_y][current_x] or current_x + 1 > 5:
            return None
        else:
            return traverse(mazi, current_x + 1, current_y, glob_x, glob_y, path_list + ['right'], "right")

    def move_left(mazu, current_x, current_y, xx, yy, path_list):
        if "l" not in mazu[current_y][current_x] or current_x - 1 < 0:
            return None
        else:
            return traverse(mazu, current_x - 1, current_y, xx, yy, path_list + ['left'], "left")

    def move_up(mazo, current_x, current_y, xxx, yyy, path_list):
        if "u" not in mazo[current_y][current_x] or current_y - 1 < 0:
            return None
        else:
            return traverse(mazo, current_x, current_y - 1, xxx, yyy, path_list + ['up'], "up")

    def move_down(blaze, current_x, current_y, xxxx, yyyy, path_list):
        if "d" not in blaze[current_y][current_x] or current_y + 1 > 5:
            return None
        else:
            return traverse(blaze, current_x, current_y + 1, xxxx, yyyy, path_list + ['down'], "down")

    try:
        print "Input these directions using the arrows on the sides:"
        return ", ".join(traverse(maze, start_x, start_y, goal_x, goal_y, [], "start"))
    except TypeError:
        raise OverSightError


def defuse_knob():
    direction_dict = {}
    up = NeedyInput("Where is the UP label? ", ["up", "down", "left", "right"])
    print "Look only at the lights on the left side."
    if up == "up":
        direction_dict = {"up": "up", "down": "down", "right": "right", "left": "left"}
    elif up == "down":
        direction_dict = {"up": "down", "down": "up", "right": "left", "left": 'right'}
    elif up == "right":
        direction_dict = {"up": "right", "left": "up", "down": "left", "right": "down"}
    elif up == "left":
        direction_dict = {"up": "left", "left": "down", "right": "up", "down": "right"}
    question_1 = YesNo("Is the top left light on?")
    if question_1 is True:
        question_2 = YesNo("Is the bottom left light on?")
        if question_2 is True:
            return "Turn the knob to the " + direction_dict["right"] + " position."
        else:
            question_3 = YesNo("Is the bottom right light on?")
            if question_3 is True:
                return "Turn the knob to the " + direction_dict["up"] + " position."
            else:
                return "Turn the knob to the " + direction_dict["down"] + " position."
    else:
        question_2 = YesNo("Is the middle bottom light on?")
        if question_2 is False:
            return "Turn the knob to the " + direction_dict["left"] + " position."
        else:
            question_3 = YesNo("Is the light above that on too?")
            if question_3 is True:
                return "Turn the knob to the " + direction_dict["down"] + " position."
            else:
                return "Turn the knob to the " + direction_dict["up"] + " position."


# ----------CHECKING THE BOMB----------

print "Hi! My name is KaTie. Let's defuse a bomb!"
print "--------------------------------------------------------------------"
print "First, we need to check the bomb. Look at the sides."
car = NeedyInput("Is there a lit indicator with the word CAR? (y/n): ", ["y", "n", "skip"])
if car == "y":
    car = True
elif car == "n":
    car = False
elif car == "skip":
    frk = False
    batteries = 0
    cereal_num = False
    cereal_vow = False
    para = False
if car != "skip":
    frk = YesNo("Is there a lit indicator with the word FRK?")
    while True:
        try:
            batteries = int(raw_input("How many batteries are on the bomb? "))
        except ValueError:
            print "Invalid Input."
        else:
            break
    while True:
        try:
            cereal_num = int(raw_input("What is the last digit of the serial number? "))
        except ValueError:
            print "Invalid Input."
        else:
            if len(str(cereal_num)) - 2 > 1:
                print "Invalid Input."
            else:
                if cereal_num == 1 or cereal_num == 3 or cereal_num == 5 or cereal_num == 7 or cereal_num == 9:
                    cereal_num = True
                    break
                else:
                    cereal_num = False
                    break
    cereal_vow = YesNo("Is there a vowel in the serial number?")
    para = YesNo("Is there a long pink port on the bomb?")
else:
    car = False
print "Okay, let's get to it!"
print "--------------------------------------------------------------------"


# ---------------DUMBING IT DOWN------------------
def module_q_a():
    wire_question = YesNo("Are there wires?")
    if wire_question is True:
        specific_wires = YesNo("Are the wires vertical?")
        if specific_wires is True:
            print "Those are complicated wires. Input 'com' or 'complicated' the next time you see them."
            print "Don't worry, they won't be too complicated with me here. Let's disarm them!"
            print "--------------------------------------------------------------------"
            print defuse_complicated(cereal_num, para, batteries)
        else:
            sequence = YesNo("Are the wires in a small panel with numbers on the left and letters on the right?")
            if sequence is True:
                print "That is a wire sequence. Input 'seq' or 'sequence' the next time you see it."
                print "But for now, we need to disarm it."
                print "--------------------------------------------------------------------"
                defuse_sequence()
            else:
                print "Those are normal wires. Input 'wir' or 'wires' the next time you see them."
                print "But for now, we need to disarm them."
                print "--------------------------------------------------------------------"
                wi_list = []
                for yumm in range(6):
                    wi_input = NeedyInput(
                        "Input the %s wire color, or type 'done' when finished: " % first_second_etc(str(yumm + 1)),
                        ["red", "blue", "yellow", "white", "black", "done"])
                    if wi_input != "done":
                        wi_list.append(wi_input)
                    else:
                        break
                print defuse_wires(wi_list, cereal_num)
    else:
        memory_question = YesNo("Is there a screen with a big number on it, and four other numbered buttons below it?")
        if memory_question is True:
            print "That is the Memory module. Input 'mem' or 'memory' the next time you see it."
            print "Don't worry, you don't have to remember anything with me here. Let's disarm it!"
            print "--------------------------------------------------------------------"
            defuse_memory()
        else:
            simon_question = YesNo("Are there four colored buttons in a diamond shape?")
            if simon_question is True:
                print "That is Simon Says. Input 'sim' or 'simon' the next time you see it."
                print "I may not be Simon, but I say we need to disarm it!"
                print "--------------------------------------------------------------------"
                defuse_simon(cereal_vow)
            else:
                words_question = YesNo("Are there six buttons with different words on them?")
                if words_question is True:
                    print "That is Who's On First, but you should input 'wor' or 'words' the next time you see it."
                    print "This module is based around miscommunication, but here you can just type the words in! " \
                          "Isn't that great? "
                    print "--------------------------------------------------------------------"
                    whos_on_first()
                else:
                    symbols_question = YesNo("Are there four white buttons with symbols on them?")
                    if symbols_question is True:
                        print "That's the Symbols module. Input 'sym' or 'symbols' the next time you see it."
                        print "But for now, we need to disarm this."
                        print "--------------------------------------------------------------------"
                        print defuse_symbols()
                    else:
                        password_question = YesNo("Are there five letters on a green screen and a 'submit' button?")
                        if password_question is True:
                            print "That's the Password module. Input 'pas' or 'password' the next time you see it."
                            print "But for now, we need to find the password."
                            print "--------------------------------------------------------------------"
                            print defuse_password()
                        else:
                            morse_question = YesNo(
                                "Is there an orange light, a display that says 3.505 mHz, and a TX button?")
                            if morse_question is True:
                                print "That's Morse Code. Input 'mor' or 'morse' the next time you see it."
                                print ".-.. . - .----. ... / -.. .. ... .- .-. -- / - .... .. ... / -- --- -.. ..- " \
                                      ".-.. . -.-.-- "
                                print "--------------------------------------------------------------------"
                                print defuse_morse()
                            else:
                                maze_question = YesNo(
                                    "Is there a blue screen with dots, a red triangle, and a white square?")
                                if maze_question is True:
                                    print "That's the maze. Input 'maz' or 'maze' the next time you see it."
                                    print "Who's making these bombs anyway? Why put a maze? Whatever, let's disarm it."
                                    print "--------------------------------------------------------------------"
                                    print defuse_maze()
                                else:
                                    needy_question = YesNo("Is there a timer at the top of the module? (It should look like "
                                                           "a small black box if it's not activated)")
                                    if needy_question is False:
                                        print "Then I don't know what to tell you. Try again."
                                        print "---------------------------"
                                        return module_q_a()
                                    else:
                                        print "It seems like this is a needy module. Needy modules can never truly be " \
                                              "disarmed, but they can be stopped for a short amount of time. "
                                        knob_question = YesNo(
                                            "Is there a knob with an UP label (that might not necessarily be at the top) and lights below it?")
                                        if knob_question is True:
                                            print "That's the knob. Input 'kno' or 'knob' the next time you see it."
                                            print "We better hurry and defuse this thing."
                                            print "--------------------------------------------------------------------"
                                            print defuse_knob()
                                        else:
                                            hacking = YesNo("Is there a screen and two buttons that say 'Y' and 'N'?")
                                            if hacking is True:
                                                print "This one is the Venting Gas module. Just press Y if it asks to " \
                                                      "vent gas and N if it asks to detonate. "
                                            else:
                                                capacitor = YesNo("Is there a red lever you can pull down? (It's okay "
                                                                  "if you try it out; nothing bad will happen)")
                                                if capacitor is True:
                                                    print "That's the Capacitor. Hold the lever down and keep the red " \
                                                          "bar from reaching the top. "
                                                else:
                                                    print "Then I don't know what to tell you. Try again."
                                                    print "---------------------------"
                                                    return module_q_a()


# ---------------SELECTING A MODULE------------------
print "If you ever need a list of acceptable inputs, type 'list'."
print "If you still need help after that, type 'help'."
while True:
    module = NeedyInput("What module do we need to disarm? ",
                        ["wir", "wires", "but", "button", "sym", "symbols", "sim", "simon", "wor", "words", "com",
                         "complicated",
                         "mem", "memory", "pas", "password", "seq", "sequence", "mor", "morse", "kno", "knob", "maz",
                         "maze", "defused", "help", "list", "exploded"])
    print "---------------------------"
    if module == "but" or module == "button":
        but_color = color_dict[
            NeedyInput("What color is the button? ", ["blue", "blu", "red", "white", "whi", "yellow", "yel"])]
        but_word = NeedyInput("What word is written on the button? ", ["hold", "abort", "detonate", "press"])
        print defuse_button(but_color, but_word, car, frk, batteries)
    elif module == "wir" or module == "wires":
        print "Start from the top wire and go down. Ignore blank spaces."
        wire_list = []
        for x in range(6):
            wire_input = NeedyInput(
                "Input the %s wire color, or type 'done' when finished: " % first_second_etc(str(x + 1)),
                ["red", "blue", "blu", "yellow", "yel", "whi", "white", "bla", "black", "done"])
            if wire_input != "done":
                wire_list.append(color_dict[wire_input])
            else:
                break
        print defuse_wires(wire_list, cereal_num)
    elif module == "sym" or module == "symbols":
        print defuse_symbols()
    elif module == "sim" or module == "simon":
        defuse_simon(cereal_vow)
    elif module == "wor" or module == "words":
        whos_on_first()
    elif module == "com" or module == "complicated":
        print defuse_complicated(cereal_num, para, batteries)
    elif module == "mem" or module == "memory":
        defuse_memory()
    elif module == "pas" or module == "password":
        print defuse_password()
    elif module == "seq" or module == "sequence":
        defuse_sequence()
    elif module == "mor" or module == "morse":
        print defuse_morse()
    elif module == "maz" or module == "maze":
        print defuse_maze()
    elif module == "kno" or module == "knob":
        print defuse_knob()
    elif module == "list":
        print "Acceptable module inputs are: wir, but, sym, sim, wor, com, mem, pas, seq, mor, maz, and kno"
    elif module == "help":
        module_q_a()
    elif module == "defused":
        print "We did it!"
        break
    elif module == "exploded":
        print "Oh. Sorry."
        break
    else:
        raise OverSightError
    print "--------------------------------------------------------------------"
