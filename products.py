#讀取檔案
products = []
with open('product.csv', 'r') as f:
	for line in f:
		name, price = line.strip().split(',')
		products.append([name, price])
		
print(products)


while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	if price == 'q':
		break 
	products.append([name, price])
print(products)	

for product in products:
	print(product[0], '的價格是', product[1])



with open('product.csv', 'w') as f:
	f.write('商品,價格\n')
	for product in products:
		f.write(product[0] + ',' + str(product[1]) + '\n')
