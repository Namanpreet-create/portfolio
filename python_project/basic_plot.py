import matplotlib.pyplot as plt

# This script creates a bar chart showing my interest in different programming languages.
languages = ['HTML', 'C', 'Python']
interest = [80, 70, 90]

plt.bar(languages, interest, color='lightcoral')
plt.title("My Interest in Programming Languages")
plt.xlabel("Languages")
plt.ylabel("Interest Level (%)")

plt.savefig("my_interest_chart.png")

plt.show()
