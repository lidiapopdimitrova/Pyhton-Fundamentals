start_string = input()

command = input()
while command != "Generate":
    command_parts = command.split(">>>")
    if command_parts[0] == "Contains":
        substring = command_parts[1]
        if substring in start_string:
            print(f"{start_string} contains {substring}")
        else:
            print("Substring not found!")

    elif command_parts[0] == "Flip":
        up_or_low = command_parts[1]
        index_start = int(command_parts[2])
        end_index = int(command_parts[3])
        needed_piece = start_string[index_start:end_index]
        front_text = start_string[:index_start]
        back_text = start_string[end_index:]

        if up_or_low == "Upper":
            start_string = front_text + needed_piece.upper() + back_text

        else:
            start_string = front_text + needed_piece.lower() + back_text
        print(start_string)

    elif command_parts[0] == "Slice":
        index_start = int(command_parts[1])
        end_index = int(command_parts[2])
        front_text = start_string[:index_start]
        back_text = start_string[end_index:]
        start_string = front_text + back_text
        print(start_string)

    command = input()

print(f"Your activation key is: {start_string}")
