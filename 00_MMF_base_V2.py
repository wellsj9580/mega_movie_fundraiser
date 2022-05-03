# Import statments 

# Functions goes here 

# Checks that ticket name is not blank 
def not_blank (question, error_message):
    valid = False

    while not valid:
      response = input (question)

      # If the name is not blank, program continues 
      if response != "":
          return response
  
      # If name is blank, show error and repeat loop
      else:
          print (error_message)
  
\

# Checks for an interger more than 0 
def int_check(question): 

  error = "Please enter a whole number that is more than 12"

  valid = False 
  while not valid: 

    # ask user for number and check it is valid
    try: 
      response = int(input(question))

      if response <= 0 :
        print (error)
      else:
        return response 

 # if an interger is not entered, display and error 
    except ValueError: 
      print (error)
\

# main routine goes here 
#******* Main Routine *******

# Set up dictionaries/lists needed to hold data

# Ask user if they have used the program before and show 

# Loop to get ticket details

# Start of loop 

# Initialise loop so that it runs at least once 
MAX_TICKETS = 5 

name = "" 
ticket_count  = 0
ticket_sales = 0

while ticket_count < MAX_TICKETS:
    
  # Tells user how many seats are left 
  if ticket_count < ticket_count - 1:
      print ("You have {} seats left".format(MAX_TICKETS - ticket_count) )
  
  # Warns user that only one seat is left!
  else:
      print("*** There is ONE seat left!! ***")
  
  #get details 
  
  # Get name (can't be blank)
  name = not_blank("Name: ", "Sorry - This can't be blank, please enter your name")
  if name == "xxx":
    break

  # Get age (between 12 and 130) 
  age = int_check("Age: ")

  # Checks thta age is valid... 
  if age < 12:
    print ("Sorry you are too young for this movie")
    continue 
  elif age >130:
    print ("That is very old - it looks like a mistake!")
    continue 

  if age < 16: 
    ticket_price = 7.5 
  elif age <65: 
    ticket_price = 10.5
  else: 
    ticket_price = 6.5 

  ticket_count += 1   
  ticket_sales += ticket_price 

# End of tickets loop
# Calculate ticket profit 
ticket_profit = ticket_sales - (5* ticket_count)                         
print ("Ticket profit: ${:.2f".format(ticket_profit))

if ticket_count == MAX_TICKETS: 
    print ("You have sold all the available tickets!") 
else:
     print ("You have sold {} tickets. \n"
            "There are {} places still available"
     .format(ticket_count, MAX_TICKETS - ticket_count)) 

  # Calculate ticket price 

  # Loop to ask for snacks 

  # Calculate snack price 
