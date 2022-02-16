import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = [1, 4, 9, 16, 25, 36, 49, 64, 81]
#plt.plot(squares)


plt.plot(squares, linewidth=2)
plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=10)
plt.ylabel("Square of Value", fontsize=10)
plt.tick_params(axis='both', labelsize=8)

plt.show()
