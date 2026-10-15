# w14 : Python - Data Visualization with Matplotlib
# line chart, bar chart, pie chart
import matplotlib.pyplot as plt

# Line chart
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 4, 10]
plt.plot(x, y, linestyle='--', marker='o')  # set line style and marker
plt.title("Simple Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

# Bar chart
products = ['Product A', 'Product B', 'Product C']
revenue = [45000, 78000, 32000]
plt.bar(products, revenue, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.ylabel('Revenue ($)')
plt.title('Product Performance')
plt.show()

# Pie chart
hobbies = ['Gaming', 'Reading', 'Exercise', 'Gardening']
hours = [10, 6, 5, 3]
plt.pie(hours, labels=hobbies)
plt.title('Weekly Time Spent on Hobbies')
plt.show()
