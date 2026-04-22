while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi there 👋")

    elif user == "hi":
        print("Bot: Hello!")

    elif user == "how are you":
        print("Bot: I'm doing great 😊")

    elif user == "what is your name":
        print("Bot: I'm a simple chatbot")

    elif user == "who created you":
        print("Bot: I was created using Python")

    elif user == "bye":
        print("Bot: Goodbye 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
        