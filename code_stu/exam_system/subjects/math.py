from .base_exam import BaseExam


class MathExam(BaseExam):
    def __init__(self, student_name):
        super().__init__("数学", 150, student_name)
        self.__bonus_points = 0


    def get_bonus_points(self):
        return self.__bonus_points


    def set_bonus_points(self, points):
        if points < 0:
            raise ValueError("附加分错误")
        self.__bonus_points = points



    def get_grade(self, score):
        if score >= 140:
            return "优秀"
        elif score >= 120:
            return "良好"
        elif score >= 90:
            return "及格"
        else:
            return "不及格"



    def calc_weighted_score(self, weight):
        return (self.get_score() + self.__bonus_points) * weight