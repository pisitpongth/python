class Student:
    name = ""
    id = ""
    score = 0

    def do_homework(self, point):
        self.score += point
        print(self.name, " did homework ", point, " points")

    def take_exam(self, point):
        self.score += point
        print(self.name, " took exam ", point, " points")

    def get_result(self):
        if self.score >= 50:
            return "PASS"
        else:
            return "FAIL"

    def show_status(self):
        print(
            "Name      : ",
            self.name,
            "\nStudent ID: ",
            self.id,
            "\nScore     : ",
            self.score,
            "\nResult    : ",
            self.get_result(),
        )
