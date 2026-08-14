# Write a program that takes a list of numbers and removes all duplicates using a set
def remove_duplicates(numbers):
    return list(set(numbers))
num=[12,23,45,67,78,89,90]
print(f"New list is {remove_duplicates(num)}")

# # Given a dictionary and their prices, find the product with the highest price
products = {
    "Laptop": 65000,
    "Mouse": 500,
    "Keyboard": 1200,
    "Monitor": 15000,
    "Headphones": 2500,
    "USB Drive": 800,
    "Printer": 9000,
    "Webcam": 2200,
    "Speaker": 1800,
    "Smartphone": 25000
}

# highest_product=max(products,key=products.get)
# print("The product with the highest price is:  ",highest_product)
# print("The price is: ",products[highest_product])
highest_product=max(products,key=products.get)
print("The product with the highest price is :\n ",highest_product)
print("The price of this product is:\n",products[highest_product])



# # To write a program to merge the two dictionaries
products_1 = {
    "Rice (5 kg)": 350,
    "Wheat Flour (10 kg)": 480,
    "Cooking Oil (1 L)": 180,
    "Sugar (1 kg)": 50,
    "Tea Powder (500 g)": 275,
    "Coffee (200 g)": 320,
    "Milk (1 L)": 65,
    "Eggs (12 pcs)": 90,
    "Toothpaste": 120,
    "Shampoo": 240,
    "Bath Soap": 45,
    "Detergent Powder (2 kg)": 390,
    "Biscuits": 30,
    "Chocolate": 80,
    "Notebook": 75
}


products.update(products_1)
print(products)


















# Different ways to solve the above problems



def remove_duplicates(numbers):
    return list(set(numbers))
nums=[1,2,3,42,1,34,5]
print("Original lists:",nums)
print("Without duplicates: ",remove_duplicates(nums))





def most_expensive_product(products):
    return max(products.items(),key=lambda x: x[1])
products = {
     "Laptop": 65000,
     "Mouse": 500,
     "Keyboard": 1200,
    "Monitor": 15000,
    "Headphones": 2500,
     "USB Drive": 800,
     "Printer": 9000,
     "Webcam": 2200,
    "Speaker": 1800,
    "Smartphone": 25000
}
product,price=most_expensive_product(products)

print(f"The most expensive product is '{product}' with price {price}")














def remove_duplicates(numbers):
    return list(set(numbers))
num=[1,2,3,4,5,6,7,8,9,90,99,1]
print("The original list is:  ",num)
print("The new list is:  ",remove_duplicates(num))