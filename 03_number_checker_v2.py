#function goes here


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

# main routine goes here 
age = int_check("Age: ")
print("Age: ", age)
