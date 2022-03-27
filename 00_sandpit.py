# play area

def numcheck(question):

    valid = False

    while not valid:
        try:
            response = int(input(question))

            return response
        
        except ValueError:
            print("whoops, that is not an integer")

number = numcheck("Number? ")

print("You chose {} and I like it".format(number))