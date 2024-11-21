import os
import matplotlib.pyplot as plt

# Wherever you want to display the graph
#plt.hist(scores, bins=[0,25,50,75,100])

#OPTION 1:
#grade for entire course by student id
def get_final_grade(student_id):
    submissions = (os.listdir("data/submissions"))
    gross_points = 0
    max_points = 0
    for file in submissions:
        current_file = open(f'data/submissions/{file}')
        file_content = current_file.read()
        if str(student_id) in file_content[:3]:
            assignment_id = file_content[4:-3]
            assignment_grade = file_content[-2:]
            assignment_weight = get_assignment_weight(assignment_id)
            gross_points += int(assignment_grade) * int(assignment_weight)
            max_points += 100 * int(assignment_weight)
    final_grade = (gross_points/max_points) * 100
    current_file.close()
    return final_grade

#find student and print grade using previously defined function
def student_grade(student_name):
    #open file in read mode
    student_list = open("data/students.txt")
    student_found = False
    for student in student_list:
        if student_name in student:
            student_id = student[:3]
            print(f'{get_final_grade(student_id):.0f}%')
            student_found = True
    if not student_found:
        print("Student not found.")
        exit()
    student_list.close()
    exit()

#find assignment weight by assignment id, also technically serves as a dictionary containing every
#id as well as weight cause i overcomplicated :(
def get_assignment_weight(assignment_id):
    assignment_file = open('data/assignments.txt')
    assignment_file_content = assignment_file.readlines()
    weight_dict = {}
    for i in range(len(assignment_file_content)):
        if i%3 == 0:
            weight_dict[assignment_file_content[i+1]] = assignment_file_content[i + 2]

    assignment_id = str(assignment_id) + "\n"
    if assignment_id in weight_dict:
        return weight_dict[assignment_id]
    else:
        return None


#OPTION 2:
def get_assignment_id(assignment_name):
    assignment_file = open('data/assignments.txt')
    assignment_file_content = assignment_file.readlines()
    assignment_dict = {}
    for i in range(len(assignment_file_content)):
        if i%3 == 0:
            assignment_dict[assignment_file_content[i]] = assignment_file_content[i + 1]
    assignment_name = assignment_name + "\n"
    if assignment_name in assignment_dict:
        return assignment_dict[assignment_name]
    else:
        return None



def assignment_stats(assignment_name):
    assignment_id = get_assignment_id(assignment_name)
    assignment_found = True
    if assignment_id is None:
        print("Assignment not found.")
        assignment_found = False
        exit()
    if assignment_found:
        assignment_id = str(assignment_id)
        submissions = (os.listdir("data/submissions"))
        grade_list = []
        for file in submissions:
            current_file = open(f'data/submissions/{file}')
            file_content = current_file.read()
            file_assignment_id = str(file_content[4:9])
            if "|" in file_assignment_id:
                file_assignment_id = file_assignment_id[:-1]
            file_assignment_id = int(file_assignment_id)
            assignment_id = int(assignment_id)
            if assignment_id == file_assignment_id:
                grade_list.append(file_content[10:])
        grade_list.sort()
        minimum_score = grade_list[0]
        maximum_score = grade_list[-1]
        gross_score = 0
        for i in grade_list:
            gross_score += int(i)
        average_score = gross_score/(len(grade_list))
        print(f'Min: {minimum_score}%\nAvg: {maximum_score}%\nMax: {average_score:.0f}%')
        exit()

def assignment_scores(assignment_name):
    assignment_id = get_assignment_id(assignment_name)
    assignment_found = True
    if assignment_id is None:
        print("Assignment not found.")
        assignment_found = False
        exit()
    if assignment_found:
        assignment_id = str(assignment_id)
        submissions = (os.listdir("data/submissions"))
        grade_list = []
        for file in submissions:
            current_file = open(f'data/submissions/{file}')
            file_content = current_file.read()
            file_assignment_id = str(file_content[4:9])
            if "|" in file_assignment_id:
                file_assignment_id = file_assignment_id[:-1]
            file_assignment_id = int(file_assignment_id)
            assignment_id = int(assignment_id)
            if assignment_id == file_assignment_id:
                grade_list.append(file_content[10:])
        grade_list.sort()
        # convert list of strings into integers v
        grade_list = [int(i) for i in grade_list]
        plt.hist(grade_list)
        plt.show()
        exit()



def main():
    while True:
        print('''1. Student grade
2. Assignment statistics
3. Assignment graph 
''')
        selection = input('Enter your selection: ')
        try:
            selection = int(selection)
        except ValueError:
            exit()
        if selection == 1:
            s_name = input('''What is the student's name: ''')
            s_name = str(s_name)
            student_grade(s_name)

        if selection == 2:
            a_name = input('''What is the assignment name: ''')
            a_name = str(a_name)
            assignment_stats(a_name)

        if selection == 3:
            a_name = input('''What is the assignment name: ''')
            a_name = str(a_name)
            assignment_scores(a_name)
        else:
            exit()

if __name__ == "__main__":
    main()
