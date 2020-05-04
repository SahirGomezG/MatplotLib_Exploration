from matplotlib import pyplot as plt

plt.style.use('ggplot')

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Points by player on each minutes
player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

labels = ['Player1','Player2','Player3']
colors = ['#008fd5','#fc4f30','#6d904f']

plt.stackplot(minutes, player1, player2, player3, colors = colors, labels=labels,)

plt.legend(loc=(0.07, 0.65))

plt.title('My Awesome Stack Plot')
plt.xlabel("Hour")
plt.ylabel('Points')

plt.tight_layout()
plt.savefig('stack_plot.png')
plt.show()
