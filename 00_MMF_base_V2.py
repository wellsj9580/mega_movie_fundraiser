# Import statments 

# Functions goes here 

# Checks that ticket name is not blank 
def not_blank (question, error_message):
    valid = False

    while not valid:
        response = input (question)

        # If the name is not blank, program continues 
        if response !="":
            return response

        # If name is blank, show error and repeat loop
        else:
            print ("Sorry - This can't be blank," " please enter your name")
    

#******* Main Routine *******

# Set up dictionaries/lists needed to hold data

# Ask user iif they have used the program before and show 

# Loop to get ticket details

  # Get name (can't be blank)
  name = not_blank("Name: ")

  # Get age (between 12 and 130)

  # Calculate ticket price 