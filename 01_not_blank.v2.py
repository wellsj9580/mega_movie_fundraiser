def not_blank (question, error_message):
    valid = False

    while not valid:
        response = input (question)

        if response !="":
            return response
        else:
            print ("Sorry - This can't be blank," " please enter your name")
    
user_name = not_blank("Name: ")
