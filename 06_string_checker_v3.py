
# Function goes her 
def string_checker (choice, options): 

  for var_list in options:
  
    #if the snack is in one of the lists, return the full name 
    if choice in var_list: 
    
    # Get full name of the snack and put it in itle case so it looks nice when outputted 
      chosen = var_list[0].title()
      is_valid = "yes"
      break 
        
      # if the chosen option i snot valid, set is_valid to no 
    else: 
      is_valid = "no"
  
  # is the snack is not OK - asl question again 
  if is_valid =="yes": 
    return chosen
  else: 
    return "Invalid Choice"

# Valid snacks holds list of all snacks each item in valid snakcs is a list with valid options for each 
# Snack <full name, letter code(a-e), and possible abbreviations etc> 
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"],
    ["orange juice", "oj", "d"]
]

yes_no = [ 
  ["yes", "y"],
  ["no", "n"], 
]

check_snack = "invalid choice"
while check_snack == "invalid choice":
  want_snack = input ("Do you want to order snacks? ").lower()
  check_snack = string_checker(want_snack, yes_no) 

  
#loop six times to make testing quicker 
for item in range (0,6):

  # Ask user for desired snack and put it in lowercase 
  desired_snack = input("Snack: ").lower()

  # Check if the snack is valid 
  snack_choice = string_checker(desired_snack, valid_snacks)
  print ("Snack Choice: ", snack_choice)
