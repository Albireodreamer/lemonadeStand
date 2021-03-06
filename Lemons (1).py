#Lemonade Stand Shop
cashOnHand = 30.0
cupsOnHand = 0 
lemonsOnHand = 0 
sugarOnHand = 0 
iceOnHand = 0 

itemsPrices = {
    "25 cups": 0.85,
    "50 cups": 2.10,
    "100 cups": 3.85,
    "10 lemons": 1.25,
    "30 lemons": 2.50,
    "75 lemons": 4.50,
    "8 sugar": 1.25,
    "20 sugar": 2.25,
    "48 sugar": 4.25,
    "100 ice": 1.10,
    "250 ice": 2.20,
    "500 ice": 3.90
    }
  

inventoryCups = {
  "25 cups": 25,
  "50 cups": 50,
  "100 cups": 100
  }
  
inventoryLemons = {
  "10 lemons": 10,
  "30 lemons": 30,
  "75 lemons": 75
  }
inventorySugar = {
  "8 sugar": 8,
  "20 sugar": 20,
  "48 sugar": 48
  }
  
inventoryIce = {
  "100 ice": 100,
  "250 ice": 250,
  "500 ice": 500
  }




Shop=True
while Shop:
  print ("The first thing you'll have to worry about is your recipe. At first, go with the default recipe, but try to experiment a little bit and see if you can find a better one. Make sure you buy enought of all your ingredients, or you won't be able to sell!, you will be starting off with $30 to spend")
  print ("\n Please choose one of the following ot purchase ingredients for your Lemonade Stand")
  for item in itemsPrices:
    print("Item Name: {0} Cost: {1}".format(item, itemsPrices[item]))
  requested_item = input("I would like ")
  if requested_item in itemsPrices:
    cashOnHand = cashOnHand - (itemsPrices[requested_item])
    
  if requested_item in inventoryCups:
    cupsOnHand = cupsOnHand + (inventoryCups[requested_item])
    
  elif requested_item in inventoryIce:
    iceOnHand = iceOnHand + (inventoryIce[requested_item])
      
  elif requested_item in inventoryLemons:
    lemonsOnHand = lemonsOnHand + (inventoryLemons[requested_item])
      
  elif requested_item in inventorySugar:
      sugarOnHand = sugarOnHand + (inventorySugar[requested_item])
      
    
  print("\n This is your remaining dollar ammount $ {0}".format(cashOnHand))
  print("\n these are your remaining ingredients:")
  print("cups {0}".format(cupsOnHand)) 
  print ("lemons {0}".format(lemonsOnHand))
  print ("sugar {0}".format(sugarOnHand))
  print ("ice {0}".format(iceOnHand))
  print(" \n would you like to continue shopping? y for yes, n for no")
  contShop = input()
else:
  print("Whoops, entered a value that doesn't exist")