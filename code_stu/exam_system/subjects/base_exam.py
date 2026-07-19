from abc import ABC, abstractmethod
import threading

record_lock = threading.Lock()


class BaseExam(ABC):
    passing_rate = 0.6



    def __init__(self, subject_name, max_score, student_name):
        self.subject_name = subject_name
        self.max_score = max_score
        self.student_name = student_name
        self.__score = 0.0



    def get_score(self):
        return self.__score



    def input_score(self, score):
        if not (0 <= score <= self.max_score):
            raise ValueError("成绩错误")
        self.__score = score



    @classmethod
    def set_passing_rate(cls, rate):
        cls.passing_rate = rate

    @staticmethod
    def check_student_name(name):
        return isinstance(name, str) and len(name) > 0


    @abstractmethod
    def get_grade(self, score):
        pass


    def calc_weighted_score(self, weight):

        return self.get_score() * weight

    def print_report_card(self):
        print(
            f"{self.student_name}-{self.subject_name} 成绩：{self.get_score()}"
        )