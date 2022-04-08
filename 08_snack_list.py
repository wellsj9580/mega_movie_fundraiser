# initialise snack lists..... 

names = ["Rangi","Manaia", "Talia", "Arihi", "Fetu"]

popcorn = []
mms = []
pita_chips =[]
water = []
orange_juice = []

snack_lists = [popcorn,mms, pita_chips, water, orange_juice]

snack_menu_dict = {
  "Popcorn": popcorn,
  "Water": water, 
  "Pita Chips": pita_chips, 
  "M&Ms": mms,
  "Orange Juice": orange_juice
  }

test_data =[
  


  
]

count = 0 
for client_order in test_data: 

  # Assumes no snacks have been brought
  for item in snack_lists: 
    item.append(0)

  # print (snack_lists)

  # Get order (hard coded for easy testing)
  snack_order = test_data [count]
  count += 1 

  for item in snack_order: 
    to_find = (item[1])
    amount = (item[0])
    add_list = snack_menu_dict[to_find]
    add_list[-1] = amount 

print ()
print("Popcorn: ", snack_lists[0])
print("M&Ms:", snack_lists[1])
print("Pita Chips: ", snack_lists[2])
print("Water: ",snack_lists[3])
print("Orange Juice: ", snack_lists[4])
