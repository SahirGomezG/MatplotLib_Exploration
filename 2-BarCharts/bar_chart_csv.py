import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use('ggplot')

with open('data1.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    languages_counter = Counter()

    for row in csv_reader:
        languages_counter.update(row['LanguagesWorkedWith'].split(';'))

languages = []
popularity = []

for item in languages_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages,popularity)

plt.title("Most pupular languages")
plt.xlabel('# of Users')

plt.legend()

plt.tight_layout()
plt.savefig('plot2.png')
plt.show()
