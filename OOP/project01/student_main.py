from student import Student


def main():
    s1 = Student()
    s1.name = "Malee"
    s1.id = "25131110000"

    s1.show_status()
    print("------------------------------")

    s1.do_homework(15)
    s1.show_status()
    print("------------------------------")

    s1.take_exam(40)
    s1.show_status()
    print("------------------------------")

    s1.take_exam(30)
    s1.show_status()
    print("------------------------------")


if __name__ == "__main__":
    main()
