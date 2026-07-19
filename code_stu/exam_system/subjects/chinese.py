from .base_exam import BaseExam


class ChineseExam(BaseExam):
    def __init__(self, student_name, essay_score=0):
        super().__init__("语文", 150, student_name)
        self.essay_score = essay_score



    def get_grade(self, score):
        if score >= 135:
            return "优秀"
        elif score >= 120:
            return "良好"
        elif score >= 90:
            return "及格"
        else:
            return "不及格"



    def print_report_card(self):
        super().print_report_card()
        print(f"作文：{self.essay_score}")