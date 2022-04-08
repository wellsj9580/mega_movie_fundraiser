import re

# checks that the ticket name is not blank 
def not_blank (question, error_message):
    valid = False

    while not valid:
        response = input (question)

        if response !="":
            return response
        else:
            print (error_message)

#checks fro an interger more than 0 
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

def get_snack():
  # Regural expression to find if item starts with a number
  number_regex = "^[1-9]"
  
  # Valid snacks holds list of all snacks each item in valid snakcs is a list with valid options for each 
  # Snack <full name, letter code(a-e), and possible abbreviations etc> 
  valid_snacks = [
      ["popcorn", "p", "corn", "a"],
      ["M&M's", "m&m's", "mms", "m", "b"],
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
    amount_snack = "{} {}".format(amount, snack_choice)

    # Check that snack is not the exit code before adding 
    if snack_choice != "xxx" and snack_choice != "Invalid Choice": 
      snack_order.append(amount_snack)
  

#valid options for yes / no questions  

      
# main routine goes here 

# intialise variables 
profit = 0 

# lists for error checking
yes_no = [ 
  ["yes", "y"],
  ["no", "n"], 
]

# Loop to get ticket and snack details (inc payment method)
name =""
while name != "xxx": 
  
  name = not_blank("Name: ",
  "Sorry - This can't be blank," " please enter your name")   

  # If name is exit code, break out of loop 
  if name == "xxx": 
    break 

  age = int_check("Age: ")

  if age < 12:
    print("sorry you are too young")
    continue
  elif age < 16: 
    ticket_price = 7.5 
  elif age <65: 
    ticket_price = 10.5
  elif age < 131: 
    ticket_price = 6.5 
  else:
    print("oops - this looks like an error")
    continue

  profit_made = ticket_price - 5 
  profit += profit_made 


# Function goes here 


  check_snack = "Invalid Choice"
  while check_snack == "Invalid Choice":
    want_snack = input ("Do you want to order snacks? ").lower()
    check_snack = string_checker(want_snack, yes_no) 
    if check_snack == "Invalid Choice":
      print("Please choose yes / no\n")
  
  # If they say yes, ask what snacks they wantr (and add to our snack list)
  if check_snack == "Yes":
    get_order = get_snack()
  
  else:
    get_order =[]
  # Show snack orders 
  print ()
  
  print(get_order)



print("we are done")