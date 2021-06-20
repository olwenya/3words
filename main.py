with open('words.txt','r') as file:
  lines = file.readlines()

  print(lines)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
train = cv.fit_transform(lines)

import numpy as np
zipped = zip(cv.get_feature_names(), np.ravel(train.sum(axis=0)))

import csv
with open('output.csv', "w") as output:
        writer = csv.writer(output)
        writer.writerow(['word','count'])
        zip = [l for l in zipped]
        for l in zip:
            writer.writerow(l)
        print('Successful grab')