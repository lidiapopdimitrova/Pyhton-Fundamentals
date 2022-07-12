text = input()

while text != "end":
    result = reversed(text)
    reversed_text = "".join(result)
    print(f"{text} = {reversed_text}")

    text = input()


