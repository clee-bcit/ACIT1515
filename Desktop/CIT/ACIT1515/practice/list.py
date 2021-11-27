li = [1,2,3,4,5]
li2 = ['a', 'b', 'c']
li3 = [1, 2.5 , 'a', True]

# Date Structure

amazon_cart = [
    'notebooks', 
    'sunglasses', 
    'speaker',
    'toys'
    ]
# Changeable

amazon_cart[0] = 'laptop'
newcart = amazon_cart[:]

newcart[0] = 'ABCABC'
print(newcart)
print(amazon_cart)

