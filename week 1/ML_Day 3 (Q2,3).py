import numpy as np

sales_data = np.array([
    [200,220,250,210,180,190],
    [230,240,260,200,195,205],
    [210,215,255,220,185,200],
    [205,225,270,215,190,195],
    [215,230,265,225,200,210],
    [225,235,275,230,205,215],
    [235,245,280,240,210,220],
    [245,255,290,250,215,225],
    [255,265,300,260,220,230],
    [265,275,310,270,225,235]
])

# print("============ Q2 =============")
# print("PART a")
# bonus_array = np.array([10,20,15,25,30,5])
#
# sales_data = np.add(bonus_array,sales_data)
# print(sales_data)
#
# print("PART b")
# flat_bonus = np.add(50,sales_data)
# sales_data+=50
# print(flat_bonus)
# print(sales_data)

print("============ Q3 =============")
print("PART a")

mean = np.mean(sales_data)
print(round(mean,2))

median = np.median(sales_data)
print(round(median,2))

variance = np.var(sales_data)
print(round(variance,2))

std_deviation = np.std(sales_data)
print(round(std_deviation,2))

max = np.max(sales_data)
print(f"Maximum = {max}")

min = np.min(sales_data)
print(f"Minimum = {min}")

range = max-min
print(f"range = {range}")

arr = []


for i in range(sales_data.shape[0]):
    for j in range(sales_data.shape[1]):
        arr.append(sales_data[i][j])
arr.sort()
q1 = np.percentile(arr,25)
q3 = np.percentile(arr,75)

IQR = q3-q1
print(f"IQR = {IQR}")