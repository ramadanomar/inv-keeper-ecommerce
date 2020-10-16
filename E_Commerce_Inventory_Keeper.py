class Customer: #Class for a customer ( Name, Email )
	def __init__(self,name,email):
		self.name = name
		self.email = email
		self.purchases = []

	def purchase(self, inventory, product): #Function for purchasing
		inventory_dict = inventory.inventory #Import the inventory
		if product in inventory_dict: # If product in inventory
			if inventory_dict[product] > 0: # Check if we have item in stock
				self.purchases.append(product) # Add product to customer purchased list
				inventory_dict[product] -= 1 # Decrease stock by one
			else: # Out of stock
				print("We are out of Stock") 
		else: # No such item
			print("We don't have that product :(")
			
	def print_purchases(self): # Function to print purchases
		print("The Customer has purchased:")
		for item in self.purchases:
			print(item.name)

class Product: # Class for product ( Name , Price )
	def __init__(self,name,price):
		self.name = name
		self.price = price

class Inventory: # Inventory Class
	def __init__(self):
		self.inventory = {} #Dictonary containing all of the inventories

	def add_product(self, product, quantity): #Function to add a product to the inventory ( or update stock )
		if product not in self.inventory:
			self.inventory[product] = quantity #Add a new product
		else:
			self.inventory[product] += quantity #Update Quantity

	def print_inventory(self): # Print all of the inventory
		for key, value in self.inventory.items():
			print(key.name + ' ' + str(value)) # Prints 'Product Name' with 'Product Quantity'
		print()


customer = Customer('Joe','joe@gmail.com')
#print(customer.name)
#print(customer.email)

apple_watch = Product('Apple Watch', 299)
#print(apple_watch.name)
#print(apple_watch.price)

mac = Product('Mac', 1999)
#print(mac.name)
#print(mac.price)

inventory = Inventory()
inventory.add_product(apple_watch, 100)
inventory.add_product(apple_watch, 13)

inventory.add_product(mac, 798)

inventory.print_inventory()

customer.purchase(inventory, apple_watch)

customer.purchase(inventory, mac)

inventory.print_inventory()
customer.print_purchases()