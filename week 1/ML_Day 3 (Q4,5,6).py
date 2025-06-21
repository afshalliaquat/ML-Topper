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
    [265,275,310,270,225,400]
])

print("========= Q4 ========")
print("part a")
greater =[]
greater.append(sales_data[sales_data>250])
print(f"Greater = {greater}")

print("part b")
sales_data[sales_data>300] = 300
print(sales_data)

print("part d")
mean = np.mean(sales_data)
belowthemean= sales_data[sales_data<mean]
print(belowthemean)

print("part c")
count = 0;
count= np.sum((sales_data>200) & (sales_data<250))
print(count)

print("================ Q5 =================")
print("Part a")
sor = np.sort(sales_data[5])
print(f"Sorted : {sor}")

print("part b")
highestvalue = 0;
index=0;
for i in range(sales_data.shape[0]):
    total=0;
    for j in range(sales_data.shape[1]):
        total+=sales_data[i][j]
    if total>highestvalue:
        highestvalue = total
        index = i

print(f"Highest Total Sales Row index = {index} with sales = {highestvalue}")

print("part c")
for i in range(sales_data.shape[1]):
    total=0;
    for j in range(sales_data.shape[0]):
        total+=sales_data[j][i]
    print(f"Column wise average of col {i} = {total/sales_data.shape[0]}")



print("part d")
for i in range(sales_data.shape[0]):
    total=0;
    for j in range(sales_data.shape[1]):
        total+=sales_data[i][j]

    print(f"Average daily sale of row {i} = {round(total/sales_data.shape[1],2)}")

print("part e")
overall_avg = np.mean(sales_data)
print(overall_avg)


print("========== Q6 ===========")
def highlight_outliers(data):
    mean = np.mean(data)

    above = data[data>mean]
    lower = data[data<mean]
    stand = np.std(above)
    stand2 = np.std(lower)
    return stand+stand2

print("Sum of std above and below mean:",highlight_outliers(sales_data))