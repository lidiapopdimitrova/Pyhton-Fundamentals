text = input()
doings = input()
while doings != "Finish":
    commands = doings.split()
    if commands[0] == "Replace":
        current_char = commands[1]
        new_char = commands[2]
        if current_char in text:
            text = text.replace(current_char, new_char)
        print(text)

    elif commands[0] == "Cut":
        start_index = int(commands[1])
        end_index = int(commands[2])
        is_valid = True
        if -1 < start_index <= end_index < len(text):
            front_text = text[:start_index]
            back_text = text[end_index + 1:]
            text = front_text + back_text
            print(text)

        else:
            print("Invalid indices!")

    elif commands[0] == "Make":
        up_low = commands[1]
        if up_low == "Upper":
            text = text.upper()
            print(text)
        else:
            text = text.lower()
            print(text)

    elif commands[0] == "Check":
        string = commands[1]
        if string in text:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")

    elif commands[0] == "Sum":
        start_index = int(commands[1])
        end_index = int(commands[2])
        if -1 < start_index <= end_index < len(text):

            cut = text[start_index:end_index+1]
            suma = 0
            for char in cut:
                suma += ord(char)
            print(suma)
        else:
            print("Invalid indices!")

    doings = input()



