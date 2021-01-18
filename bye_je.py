def does_jianne_give_a_fuck():
    message = input(str("Mel's Message: "))
    newMess = message.lower()
    if newMess != "bye":
        if "je" in newMess:
            print("Ji: blah blah blah")
            does_jianne_give_a_fuck()
        else:
            print("Ji: ok.. i'm listening")
            does_jianne_give_a_fuck()
    else:
        print("ok bye :)")
does_jianne_give_a_fuck()
