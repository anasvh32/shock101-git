def reply(text):
    text = text.strip().lower()
    if text == "help":
        return "I can answer a few simple sentences."
    if text == "salam":
        return "Salam, khoobi?"
    return "Sorry, I do not understand yet."


if __name__ == "__main__":
    print(reply(input("You: ")))