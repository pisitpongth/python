from student import Student


def main():
    students = []

    for i in range(3):
        students.append(Student())

        current_student = students[i]

        name = input("Enter student name: ").strip()

        id = input("Enter student id: ").strip()

        current_student.name = name
        current_student.id = id

        homework_score = int(input("Enter homework score: ").strip())
        current_student.do_homework(homework_score)

        exam_score = int(input("Enter exam score: ").strip())
        current_student.take_exam(exam_score)

        print()

    for i in range(len(students)):
        students[i].show_status()
        print("------------------------------")


if __name__ == "__main__":
    main()
