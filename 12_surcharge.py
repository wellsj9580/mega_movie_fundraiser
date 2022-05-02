# Function goes here
def string_checker(choice, options):

    is_valid = ""
    chosen = ""

    for pay_method in options:

        #if the snack is in one of the lists, return the full name
        if choice in pay_method:

            # Get full name of the snack and put it in itle case so it looks nice when outputted
            chosen = pay_method[0].title()
            is_valid = "yes"
            break

            # if the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

    # is the snack is not OK - ask question again
    if is_valid == "yes":
        return chosen
    else:
        return "Invalid Choice"


# Main rotine
pay_method = [["Cash", "ca"], ["Credit", "cr"]]

# Loop until exit code...
name = ""
while name != "xxx":
    name = input("Name: ")
    if name == "xxx":
        break

    # Ask for payment method
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
      how_pay = input(
          "Please choose a payment method (cash / credit)? ").lower()
      how_pay = string_checker(how_pay, pay_method)
      
      print("You chose", how_pay)

        # Ask for subtotal (for testing purposes)
      subtotal = float(input("Sub total? $"))
      
      if how_pay == "Credit":
          surcharge = 0.05 * subtotal
      else:
          surcharge = 0
      
      total = subtotal + surcharge
      
      print(
          "Name: {} | Subtotal: ${:.2f} | Surcharge: ${:.2f} | Total Payable: ${:.2f}"
          .format(name, subtotal, surcharge, total))
