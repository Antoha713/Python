from Person import Person

class FullTimeStudent(Person):

    def __init__(self, name, age, prac_score, prac_count, exam_scr, attend_pct):
        super().__init__(name, age)
        self.prac_score = prac_score       # сумарний_бал_за_практичні
        self.prac_count = prac_count       # кількість_практичних
        self.exam_scr = exam_scr           # бал_за_іспит
        self.attend_pct = attend_pct     # процент_відвідування
