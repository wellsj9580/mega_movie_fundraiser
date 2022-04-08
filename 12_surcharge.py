

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



# Main rotine 
pay_method =[
  ["Cash", "ca"],
  ["Credit", "cr"]
]

# Loop until exit code... 
name = ""
while name != "xxx":
  name = input ("Name: ")
  if name =="xxx":
    break

  # Ask for payment method 
  how_pay = "invalid choice"
  while how_pay == "invalid choice":
    how_pay = input ("Please choose a payment method (cash or credit)")
    how_pay = string_checker(how_pay, pay_method)
    