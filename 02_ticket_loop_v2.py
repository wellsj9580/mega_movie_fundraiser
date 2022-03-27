# start of loop 

#initialise loop so that it runs at least once 


who = "" 
count = 0
MAX_TICKETS = 5 

while who != "xxx" and count < MAX_TICKETS:
    print ("You have {} seats left".format(MAX_TICKETS - count) )

    #get details 
    who = input ("Name: ")

    if who == "xxx":
      break
  
    count += 1 
    print ()  

if count == MAX_TICKETS: 
    print ("You have sold all the available tickets!") 
else:
     print ("You have sold {} tickets. There are {} places still available"
     .format(count, MAX_TICKETS - count))   