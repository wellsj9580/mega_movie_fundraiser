import re 

# Works out wether string has numbers and seperates string into amount and item

test_strings = [
  "Popcorn",
  "2 pc",
  "1.5OJ",
  "4OJ",
]

for item in test_strings:

  # Regural expression to find if item starts with a number
  number_regex = "^[1-9]"

  # If item has a number, seprate it into two (number / item)
  if re.match(number_regex, item) : 
    amount = int(item[0])
    desired_snack =item[1:]

  else: 
    amount = 1 
    desired_snack = item   

  # Remove white spaces around snack
  desired_snack = desired_snack.strip()

  # If the item does not have a number in front, set amount to 1 

  # Print order
  print ("Amount:", amount)
  print ("Snack: ", desired_snack)
  print ("Length of snack: ",len(desired_snack))
  