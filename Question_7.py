'''
Question7:
Write a python script to create a class named product that has a constructor to initialize the
product ID and a method named search product that will search the product name, type and
price based on the ID from products.txt file and print the values.
Suppose, products.txt contains the following values.
ID Name Type Price
3423 Samsung HDD 1TB HDD 6000
7856 Logitech Mouse 500
9856 Dell Monitor 15” Monitor 4500
'''

class Product:
    def __init__(self, id):
        self.id = id
    def search_product(self):
        file = open('Q7.txt',encoding='utf-8') 
        for x in file:
            value = x.split()
            if value[0] == self.id:
                print("ID    Name       Type                  Price")
                print(x) 
                break

        

product_id = input('Enter the product ID: ')
product = Product(product_id)
product.search_product()
