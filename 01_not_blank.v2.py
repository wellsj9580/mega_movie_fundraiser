def not_blank (question, error_message):
    valid = False

    while not valid:
        response = input (question)

        if response !="":
            return response
        else:
            print (error_message)
    
user_name = not_blank("Name: ",
"Sorry - This can't be blank," " please enter your name")            

