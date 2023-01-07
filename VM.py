#a dictionary inside a list to call for in 'ordering()'
snacks = [
{'item_slot': 1, 
 'item_name': 'Lays', 
 'item_cost': 1,
 
 },

{'item_slot': 2, 
 'item_name': 'Doritos', 
 'item_cost': 1,
 
 },

{'item_slot': 3, 
 'item_name': 'Cheetos', 
 'item_cost': 1,
 
 },

{'item_slot': 4, 
 'item_name': 'Twix', 
 'item_cost': 3,
 'item_stock': 10,
 },

{'item_slot': 5, 
 'item_name': 'Kit-kat', 
 'item_cost': 3,
 
 },

{'item_slot': 6, 
 'item_name': 'Oreo', 
 'item_cost': 3,
 
 },


{'item_slot': 7, 
 'item_name': 'Pepsi', 
 'item_cost': 2.50,
 
 },

{'item_slot': 8, 
 'item_name': 'Mountain dew', 
 'item_cost': 2.50,
 
 },

{'item_slot': 9, 
 'item_name': 'Fanta', 
 'item_cost': 2.50,
 
 },

]



#prints the items in the vending machine
def menu():
  print("--------------MENU---------------")
   
  chips = {
      
    "01  Lays" : "$1", 
    "02  Doritos" : "$1",
    "03  Cheetos" : "$1",}
  
  chocolates = {
      
    "04  Twix" : "$3",
    "05  Kit-kat" : "$3",
    "06  Oreo" : "$3",
    }
  
  sodas = {
      
    "07  Pepsi" : "$2.50",
    "08  Mountain dew" : "$2.50",
    "09  Fanta" : "$2.50",
    }

  print("--------------CHIPS--------------")
  for key, value in chips.items():
      print(f" {key:25} {value}")
      print()
  print("-----------CHOCOLATES------------")
  for key, value in chocolates.items():
      print(f" {key:25} {value}")
      print()
  print("-------------SODAS---------------")
  for key, value in sodas.items():
      print(f" {key:25} {value}")
      print()

menu()

#ordering part
def ordering():
  on = True
  while on:
    #entering the money
    inserting_amount = int(input('Insert amount here:\n'))
    print('You entered $',inserting_amount, '\n')

    #if you entered 0 or less than 0 
    if inserting_amount <= 0:
      print('Invalid amount\n')
      ordering()
        
    #choosing an item 
    chosen_item = int(input('Input item slot number:\n'))

    #if slot number that doesnt exist is inputed, funds are given back the start over 
    if chosen_item >= 10 or chosen_item <= 0:
      print('Input a valid slot number\nfunds has been realsed\n')
      ordering()

    cost = []
    print_item = []
    for items in snacks:
      

        #not enough money
        if chosen_item == items['item_slot'] and inserting_amount < items['item_cost'] :
          print('not enough\n')

       

        #getting the item that's ordered
        if chosen_item == items['item_slot'] and inserting_amount >= items['item_cost']:
          print('Item being released\n')

          
          #add the total of all items
          print_item.append(items.get('item_name'))
          print(print_item,'\n')
          #print change
          cost.append(items.get('item_cost'))
          total_cost=sum(cost)
          change = inserting_amount - total_cost
          print("Your change is $",change,'\n')

          #asking the user if they want to buy more or are they finish
          more_items = input("do you want something else? type yes or no:\n")

          if more_items == 'no':
            on = False

          if more_items == 'yes':
            print('')
            
ordering()