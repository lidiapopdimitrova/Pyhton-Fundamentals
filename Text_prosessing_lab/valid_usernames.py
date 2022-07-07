
def length(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def text_type(username):
    for ch in username:
        if not (ch.isalnum() or ch == "-" or ch == "_"):
            return False
    return True


def redundant(username):
    for ch in username:
        if ch == " ":
            return False
    return True


def is_valid(username):
    if length(username) and redundant(username) and text_type(username):
        return True
    return False


usernames = input().split(", ")
for user in usernames:
    if is_valid(user):
        print(user)