def change_reg(message: str) -> str:
    list_of_words = message.lower().split()
    list_of_words[0] = list_of_words[0].capitalize()
    list_of_words[-1] = list_of_words[-1].capitalize()
    return ' '.join(list_of_words)


if __name__ == '__main__':
    message = input("Input message: ")
    if len(message.split()) < 3:
        print("Condition not met")
    else:
        print(change_reg(message))
    