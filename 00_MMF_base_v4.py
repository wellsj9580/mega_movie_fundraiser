# Import statments 
import re
import pandas

'M&Ms'
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

def string_checker (choice, options): 

  for var_list in options:
  
    #if the snack is in one of the lists, return the full name 
    if choice in var_list: 
    
    # Get full name of the snack and put it in itle case so it looks nice when outputted 
      chosen = var_list[0].title()
      is_valid = "yes"
      break 
        
      # if the chosen option is not valid, set is_valid to no 
    else: 
      is_valid = "no"
  
  # is the snack is not OK - ask question again 
  if is_valid =="yes": 
    return chosen
  else: 
    return "Invalid Choice"

\

def get_snack():
  # Regural expression to find if item starts with a number
  number_regex = "^[1-9]"
  
  # Valid snacks holds list of all snacks each item in valid snakcs is a list with valid options for each 
  # Snack <full name, letter code(a-e), and possible abbreviations etc> 
  valid_snacks = [
      ["popcorn", "p", "corn", "a"],
      ["mms", "M&M's", "m&m's", "m", "b"],
      ["pita chips", "chips", "pc", "pita", "c"],
      ["water", "w", "d"],
      ["orange juice", "oj", "d", "juice"]
  ]

  # Holds snack order for single user
  snack_order = []

  desired_snack =""
  while desired_snack != "xxx":

    snack_row =[]
      
    # Ask user for desired snack and put it in lowercase 
    desired_snack = input("Snack: ").lower()
    if desired_snack == "xxx" : 
      return snack_order

        # If item has a number, seprate it into two (number / item)
    if re.match(number_regex, desired_snack) : 
      amount = int(desired_snack[0])
      desired_snack = desired_snack[1:]
  
    else: 
      amount = 1 
      desired_snack = desired_snack
    
    # Remove white spaces around snack
    desired_snack = desired_snack.strip()

     # Check if snack is valid 
    snack_choice = string_checker(desired_snack, valid_snacks)
    print ("Snack Choice: ", snack_choice)

    # Check snack amount is valid (less than 5)
    if amount >= 5:
      print ("Sorry - we have a four snack maximum")
      snack_choice = "Invalid Choice"

    # Add snack and amount to list
    snack_row.append(amount)
    snack_row.append(snack_choice)

    # Add snack AND amount to list 
    # amount_snack = "{} {}".format(amount, snack_choice)

    # Check that snack is not the exit code before adding 
    if snack_choice != "xxx" and snack_choice != "Invalid Choice": 
      snack_order.append(snack_row)

    if snack_order == "xxx":
      return snack_order
\

# main routine goes here 
#******* Main Routine *******

# Set up dictionaries/lists needed to hold data

#valid options for yes / no questions  
yes_no = [ 
  ["yes", "y"],
  ["no", "n"], 
]

# list of valid responses fo rpayment method 
pay_method = [
  ["Cash", "ca"], 
  ["Credit", "cr"]
]

# Initialise loop so that it runs at least once 
MAX_TICKETS = 5 

name = "" 
ticket_count  = 0
ticket_sales = 0

# Initialise lists (to make data-frame in due course)
all_names = []
all_tickets = []

popcorn = []
mms = []
pita_chips =[]
water = []
orange_juice = []

snack_lists = [popcorn,mms, pita_chips, water, orange_juice]

# Store surcharge multiplier 
surcharge_mult_list = []


# Data Frame Dictionary 
movie_data_dict = {
  'Name': all_names,
  'Ticket': all_tickets,
  'Popcorn': popcorn,
  'Water': water, 
  'Pita Chips': pita_chips, 
  'Mms': mms,
  'Orange Juice': orange_juice,
  'Surcharge_multiplier': surcharge_mult_list
}

# cost of each snack 
price_dict = {
  'Popcorn': 2.5,
  'Water': 2,
  'Pita Chips': 4.5,
  'Mms':3,
  'Orange Juice': 3.25
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

  # Get snacks 
  # If they say yes, ask what snacks they want (and add to our snack list)

  check_snack = "Invalid Choice"
  while check_snack == "Invalid Choice":
    want_snack = input ("Do you want to order snacks? ").lower()
    
    check_snack = string_checker(want_snack, yes_no) 
    if check_snack == "Invalid Choice":
      print("Please choose yes / no\n")
  
  # If they say yes, ask what snacks they wantr (and add to our snack list)
  if check_snack == "Yes":
    snack_order = get_snack()
  else:
    snack_order = []


  
  # Assumes no snacks have been brought
  for item in snack_lists: 
    item.append(0)

  # print (snack_lists)

  for item in snack_order:
    if len (item) > 0:
      to_find = (item[1])
      amount = (item[0])
      add_list = movie_data_dict[to_find]
      add_list[-1] = amount 

      
# Get payment method (ie: work out if surcharge is needed)
    
  #Ask for payment method
  how_pay = "invalid choice"
  while how_pay == "invalid choice":
    how_pay = input(
        "Please choose a payment method (cash / credit)? ").lower()
    how_pay = string_checker(how_pay, pay_method)

  if how_pay == "Credit":
      surcharge_multiplier = 0.05 
  else:
      surcharge_multiplier = 0

  surcharge_mult_list.append(surcharge_multiplier)

# End of tickets / snack / payment loop

# debugging print statements
print('Name', all_names)
print('Ticket', all_tickets)
print('Popcorn', popcorn)
print('Water', water) 
print('Pita Chips', pita_chips) 
print('Mms', mms)
print('Orange Juice', orange_juice)
print('Surcharge_multiplier', surcharge_mult_list)

# Print details... 
# Creat dataframe and set index to name column 
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

# Creates column called 'Sun Total' 
# Fill it price fro snacks and ticket 3

movie_frame["Snacks"] = \
    movie_frame['Popcorn']*price_dict['Popcorn'] + \
    movie_frame['Water']*price_dict['Water'] + \
    movie_frame['Pita Chips']*price_dict['Pita Chips'] + \
    movie_frame['Mms']*price_dict['Mms'] + \
    movie_frame['Orange Juice']*price_dict['Orange Juice']

movie_frame["Sub Total"] = \
    movie_frame['Ticket'] +\
    movie_frame['Snacks']

movie_frame["Surcharge"] = \
    movie_frame["Sub Total"] * movie_frame["Surcharge_multiplier"]

movie_frame["Total"] = movie_frame["Sub Total"] +\
    movie_frame['Surcharge']

# Shorten column names 
movie_frame = movie_frame.rename(columns = {'Orange Juice': 'OJ',
                                            'Pita Chips':'Chips',  
                                            'Surcharge_multiplier':'SM'})


# Set up colums to be printed... 
pandas.set_option('display.max_columns', None)

# Display numbers to 2 dp...
pandas.set_option('display.precision', 2)

print_all = input ("print all colums?? (y) for yes" )
if print_all == "y":
  print(movie_frame)
else:
  print(movie_frame[['Ticket', 'Sub Total', 'Surcharge', 'Total']])

print() 


# Calculate ticket profit 
ticket_profit = ticket_sales - (5* ticket_count)                         
print ("Ticket profit: ${:.2f}".format(ticket_profit))

# Tell user if they have unsold tickets...
if ticket_count == MAX_TICKETS: 
    print ("You have sold all the available tickets!") 
else:
     print ("You have sold {} tickets. \n"
            "There are {} places still available"
     .format(ticket_count, MAX_TICKETS - ticket_count)) 


