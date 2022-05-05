# Import statments 
import re
import pandas


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

#checks number of tickets left and warns user if maxium is being approached 
def check_tickets(tickets_sold, ticket_limit):
  # Tells user how many seats are left 
  if ticket_count < MAX_TICKETS - 1:
      print ("You have {} seats left".format(MAX_TICKETS - ticket_count) )
  
  # Warns user that only one seat is left!
  else:
      print("*** There is ONE seat left!! ***")
  return ""
\

# Gets ticket price based on age 
def get_ticket_price ():
  
  # Get age (between 12 and 130) 
  age = int_check("Age: ")

  # Checks thta age is valid... 
  if age < 12:
    print ("Sorry you are too young for this movie")
    return "invalid ticket price" 
  elif age >130:
    print ("That is very old - it looks like a mistake!")
    return "invalid ticket price"  

  if age < 16: 
    ticket_price = 7.5 
  elif age <65: 
    ticket_price = 10.5
  else: 
    ticket_price = 6.5 

  return ticket_price 
\
  
# main routine goes here 
#******* Main Routine *******

# Set up dictionaries/lists needed to hold data

# Initialise loop so that it runs at least once 
MAX_TICKETS = 5 

name = "" 
ticket_count  = 0
ticket_sales = 0

# Initialise lists (to make data-frame in due course)
all_names = []
all_tickets = []

# Data Frame Dictionary 
movie_data_dict = {
  'Name': all_names,
  'Ticket': all_tickets

}




# Ask user if they have used the program before and show instructions

# Loop to get ticket details
while name != "xxx" and ticket_count < MAX_TICKETS:

  # Checks numbers of ticket limit has not been exceeded
  check_tickets(ticket_count, MAX_TICKETS)

  # **** Get details for each ticket...****

  # Get name (can't be blank)
  name = not_blank("Name: ", "Sorry - This can't be blank, please enter your name")
  
  # End the loop if the exit code is entered 
  if name == "xxx":
    break

  # get age (and ticket price)
  ticket_price = get_ticket_price()
  # If age is valid, restart loop (and get name again)
  if ticket_price == "invalid ticket price":
    continue 
    
  ticket_count += 1   
  ticket_sales += ticket_price 

  # Add name and ticket price to lists 
  all_names.append(name)
  all_tickets.append(ticket_price)

# End of tickets loop
# Calculate ticket profit 
ticket_profit = ticket_sales - (5* ticket_count)                         
print ("Ticket profit: ${:.2f}".format(ticket_profit))

if ticket_count == MAX_TICKETS: 
    print ("You have sold all the available tickets!") 
else:
     print ("You have sold {} tickets. \n"
            "There are {} places still available"
     .format(ticket_count, MAX_TICKETS - ticket_count)) 

  # Calculate ticket price 

  # Loop to ask for snacks 

  # Calculate snack price 






# Loop to get ticket details

# Start of loop 