import pandas as pd
import glob

# edit this array to include all skipped lectures
skipped_lectures = [3, 5, 8]

# returns a string of the lecture number
# takes into account skipped numbers due to skipped lectures
def lec_num(index):
	index += 1
	for s in skipped_lectures:
		if index >= s:
			index += 1
	return str(index)

# returns the timestamp of the first reply
def csv_time(survey):
	return survey[1]['Timestamp'][0]

def main():
	path = "csv"
	files = glob.glob(path + '/*.csv')

	# surveys stored as (fileName, frame)
	surveys = []
	for f in files:
		surveys.append((f, pd.read_csv(f)))

	# sort surveys based on the timestamp of the first reply
	surveys.sort(key=csv_time)

	# print out surveys in order so you can make sure they are sorted correctly
	print("Read in", len(surveys), "participation surveys:")
	for i in range(len(surveys)):
		print("Lecture " + lec_num(i) + ":", end=" ")
		for s in range(5 - len(lec_num(i))):
			print(" ", end="")
		print(surveys[i][0])

	# get attendance
	attendance = []
	allStudents = set()
	for s in surveys:
		attendance.append(set())
		for u in s[1]['Username']:
			allStudents.add(u)
			attendance[-1].add(u)

	# create dataframe
	columns = ['Username']
	for i in range(len(attendance)):
		columns.append("Lecture " + lec_num(i))
	columns.append("Comment")
	columns.append("Total")
	data = []
	for s in allStudents:
		s_data = [s]
		total = 0
		comment = "Missed lecture: "
		for i in range(len(attendance)):
			if s in attendance[i]:
				s_data.append(1)
				total += 1
			else:
				s_data.append(0)
				comment = comment + lec_num(i) + ", "
		if total < len(attendance):
			s_data.append(comment[:-2])
		else:
			s_data.append("")
		s_data.append(total)
		data.append(s_data)
	df = pd.DataFrame(data, columns=columns)
	df.to_csv('out.csv')
	print("created out.csv for", len(allStudents), "students.")

if __name__ == '__main__':
    main()
