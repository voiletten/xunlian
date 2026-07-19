from .base_exam import BaseExam


class EnglishExam(BaseExam):
    def __init__(self, student_name):
        super().__init__("英语", 100, student_name)



    def get_grade(self, score):
        if score >= 90:
            return "优秀"
        elif score >= 75:
            return "良好"
        elif score >= 60:
            return "及格"
        else:
            return "不及格"



    def print_report_card(self):
        print("成绩：")
        super().print_report_card()