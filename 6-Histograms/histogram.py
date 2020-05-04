from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('ggplot')

data = pd.read_csv('data.csv')
ids = data['Responder_id']
ages = data['Age']
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#plt.hist(ages, bins=bins, edgecolor='black')
# With logarithmic
plt.hist(ages, bins=bins, edgecolor='black', log = True)

median_age = 29
color = 'blue'

plt.axvline(median_age, color = color,label = 'Age Median' )
plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

# To save a file .png
plt.savefig('histogram_1.png')

plt.show()
