

# checks that the ticket name is not blank 
def not_blank (question):
    valid = False

    while not valid:
        response = input (question)

        if response !="":
            return response
        else:
            print ("Sorry,this can't be blank")

user_name = not_blank("Name: ")            
