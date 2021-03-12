
shop={}
run = True
budget = int(input('Enter Your budget : '))
while run:
	print('1. Add an item')
	print('2. Exit')
	op = int(input('Enter you choice: '))
	if op == 1:
		product = input('Enter product: ')
		quantity = input('Enter quantity: ')
		price = int(input('Enter price: '))
		if price<budget:
			shop.update({product:(quantity,price)})
			budget = budget - price
		else:
			print("Can't Buy the product")
	if op ==2:
		for k,v in shop.items():
			if v[1] <=budget:
				print('Amount left can buy you '+k)
		print('GROCERY LIST is:')
		print('Product name \t Quantity \t Price')
		for k,v in shop.items():
			print(k+' \t\t '+v[0]+' \t\t '+str(v[1]))
		run = False




