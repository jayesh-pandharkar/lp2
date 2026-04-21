while True:

    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("Bot: Hello, how can I help you?")

    elif user == "who are you":
        print("Bot: I am your virtual assistant.")

    elif user == "where do you operate":
        print("Bot: We operate from Singapore.")

    elif user == "payment methods":
        print("Bot: We accept debit cards and credit cards.")

    elif user == "customer service":
        print("Bot: Please call +65 3333 3333")

    elif user == "bye" or user == "ok":
        print("Bot: Bye")
        break

    else:
        print("Bot: Sorry, I did not understand.")