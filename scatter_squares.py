import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=5)


# Назначение заголовка диаграммы и меток осей.
plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=10)
plt.ylabel("Square of Value", fontsize=10)

# Назначение размера шрифта делений на осях.
plt.tick_params(axis='both', which='major', labelsize=10)

# Назначение диапазона для каждой оси.
plt.axis([0, 1100, 0, 1100000])

plt.show()
