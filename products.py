import os # 作業系統

# 讀取檔案
products = []
if os.path.isfile('product.csv'):
	print('yeah! 找到檔案了')
	with open('product.csv', 'r') as f:
		for line in f:
			if '商品,價格' in line:
				continue # 繼續
			name, price = line.strip().split(',')
			products.append([name, price])
else:
	print('找不到檔案.....')


print(products)		

# 讓使用者輸入
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

# 列出商品
for product in products:
	print(product[0], '的價格是', product[1])


# 寫入檔案
with open('product.csv', 'w') as f:
	f.write('商品,價格\n')
	for product in products:
		f.write(product[0] + ',' + str(product)[1] + '\n')
