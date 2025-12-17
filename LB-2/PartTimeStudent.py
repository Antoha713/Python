from Person import Person

class PartTimeStudent(Person):

    def __init__(self, name, age, prac_score, prac_count, exam_scr):
        super().__init__(name, age)
        self.prac_score = prac_score       # сумарний_бал_за_практичні
        self.prac_count = prac_count       # кількість_практичних
        self.exam_scr = exam_scr           # бал_за_іспит

    def avg_practice_score(self):
        if self.prac_count != 0:
            avg_prac = self.prac_score / self.prac_count
        else:
            avg_prac = 0
        return avg_prac

    def total_score(self):
        S_pr = self.avg_practice_score()
        S_ex = self.exam_scr
        return 0.7 * S_pr + 0.3 * S_ex

    def display_info(self):

        print("Форма навчання: заочна")
