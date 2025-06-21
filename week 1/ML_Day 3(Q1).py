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

print("============ Q1 =============")
print("PART a")
Total_of_each=[]
for i in range(sales_data.shape[1]):#col
    Total =0;
    for j in range(sales_data.shape[0]):#row
          Total+= sales_data[j][i]

    print(f"Total of Product {i} = {Total}")
    Total_of_each.append(Total)


print("PART b")
average_daily_sales =[]
for i in range(sales_data.shape[0]):
    total=0;
    for j in range(sales_data.shape[1]):
        total+=sales_data[i][j]

    print(f"Average daily sale of Product {i} = {round(total/sales_data.shape[1],2)}")
    average_daily_sales.append(total/sales_data.shape[1])

print("PART c")
sales_data = np.add(0.05* sales_data,sales_data)
print(sales_data)

print("PART d")
sales_data = np.sqrt(sales_data)
print(sales_data)

