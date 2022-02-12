mean = np.mean(data)
std = np.std(data)
low = mean-std
high = mean+std
count = 0

for i in data:
    if low < i < high:
        count += 1

result = (count / len(data))*100

print(result)


"""
To calculate the percentage, divide the number of houses that satisfy the condition by the total number of houses, and multiply the result by 100.

""
