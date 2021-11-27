user_input = [15, 20, 0, 5]
tokens = user_input.split()
tokens = map(int, tokens)
nums = []
max_num = 0
total = 0


for token in tokens:
    nums.append(int(token))
    if token > max_num:
        max_num = token
    
avg = 0
for token in tokens:
    nums.append(int(token))
    total += token
    avg = total / len(token)
    
print(avg, max_num)