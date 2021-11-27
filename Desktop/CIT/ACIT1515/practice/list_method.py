# List Methods
basket = [1,2,3,4,5]

# adding
new_list = basket.append(100)
# INSTEAD OF THIS #
basket.append(100) 
# insult
basket.insert(3, 2525)  # insult 2525 in [3]
# extend 
basket.extend([200, 202]) # extend end of the list
# remove
basket.pop() # removes the end of the list
basket.remove(2) # remove [4]
basket.clear # clear removes everything in the list

new_list = basket
print(basket)
print(new_list)
# index
alphabet = ['a','b','c','d','e']
alphabet.index('c') # returns the [n] of the (2)
print(alphabet.index('c'))
print(alphabet.index('c', 0, 4)) # is 'c' between [0] and [4]?
# is in
print('d' in alphabet) #True
print('x' in alphabet) #False
# count
print(alphabet.count('d')) # 1 - how many 'd' in the list?
# sort
alphabet.sort() # sort alphabetically
print(sorted(alphabet))

# reverse
alphabet.reverse()
print(alphabet)
