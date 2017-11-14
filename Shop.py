#Lemonade Stand Shop
Cash = 30.0
items_prices = {
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
  
  
Shop=True
while Shop:
  print ("The first thing you'll have to worry about is your recipe. At first, go with the default recipe, but try to experiment a little bit and see if you can find a better one. Make sure you buy enought of all your ingredients, or you won't be able to sell!")
  print ("\n Please choose one of the following ot purchase ingredients for your Lemonade Stand")
  for item in items_prices:
    print("Item Name: {0} Cost: {1}".format(item, items_prices[item]))
  requested_item = input("I would like ")
  if requested_item in items_prices:
    Cash = Cash - (items_prices[requested_item])
    print("This is your remaining dollar ammount {0}".format(Cash))
    print("would you like to coninue shopping? y for yes, n for no")
    contShop = input()
  else:
    print("Whoops, entered a value that doesn't exist")