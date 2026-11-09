def reply(text):
    text = text.strip().lower()
    if text == "help":
        return "I can answer a few simple sentences."
    if text == "salam":
        return "Salam. Welcome. How may I assist you today?"
    return "Sorry, I do not understand yet."


if __name__ == "__main__":
    print(reply(input("You: ")))