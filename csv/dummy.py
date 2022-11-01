import pandas as pd
import random
from random_word import RandomWords

# create a random list of all students
r = RandomWords()
allStudents = set()
for s in range(70):
	allStudents.add(r.get_random_word() + '@' + r.get_random_word())
allStudents = list(allStudents)

# create 11 dummy csv files
for f in range(11):
	otherNum = random.randint(1, 5)
	columns = ['Timestamp', 'Username']
	for i in range(otherNum):
		columns.append("Other" + str(i+1))

	data = []
	for s in range(random.randint(20, 49)):
		s_data = ["2022/09/" + str(f+10) + " 6:59:" + str(s+10) + " PM MDT"]
		s_data.append(allStudents[random.randint(0, len(allStudents) - 1)])
		for i in range(otherNum):
			s_data.append(r.get_random_word())
		data.append(s_data)

	df = pd.DataFrame(data, columns=columns)
	df.to_csv('Survey' + str(f+1) + '.csv')
