# function goes here

def int_check (question, low_num, high_num):

  error = "Please enter a whole number between {} and {}".format(low_num, high_num)
  
  vaild = False 
  while not vaild:

  # ask user for number and check it is valid 
    try: 
      response = int (input (question))
  
      if low_num <= response <= high_num:
         return response
      else:
         print(error) 
  
      # if an interger is not entered, display and error 
    except ValueError: 
      print (error)

# main routine goes here 
age = int_check("Age: ", 12, 130)
print("Age: ", age)
