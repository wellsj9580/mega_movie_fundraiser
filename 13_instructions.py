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


def instructions(options): 
  show_help = "invalid choice"
  while show_help == "invalid choice":
    show_help = input ("Would you like to read the instructions: ")
    show_help = string_checker(show_help, options)

  if show_help == "yes":
    print ()
    print("**** Mega Movie Fundraiser Instructions ****")
    print()
    print("Instructions go here. They are brief but helpful")

  return 

# Main routine goes here 
# List of valid yes / no responses 
yes_no = [ 
  ["yes", "y"],
  ["no", "n"]
  ]

# Ask if instructions are needed 
instructions (yes_no)
print()
print ("Program Launches...")