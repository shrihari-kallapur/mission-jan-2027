def get_marks():
	marks = []
	num_subjects = int(input("Enter the total nos of subjects you have"))

	for subject in range(num_subjects):
		mark = int(input(f"Enter marks for Subject {subject + 1}: "))
		marks.append(mark)
	return marks

def calculate_average(marks):
	avg = sum(marks) / len(marks)
	return avg

def assign_grade(avg):
	if avg >= 90:
		return "A"
	elif avg >= 75:
		return "B"
	elif avg >= 60:
		return "C"
	else:
		return "F"

def display_result(avg, grade):
	print(f"Average : {avg:.2f}")
	print(f"Grade   : {grade}")

marks = get_marks()

average = calculate_average(marks)

grade = assign_grade(average)

display_result(average, grade)
