from subjects import ChineseExam, MathExam, EnglishExam,BaseExam
from grade_utils import *
import traceback


def safe_run(func):
    try:
        func()
    except Exception as e:
        print(f"错误：{e}")
        traceback.print_exc()




def test_basic():
    print("基础得分率")
    percent = calc_percentage(135, 150)
    print(f"得分率：{percent}%")



def test_file_io():
    print("\n成绩保存读取")
    save_record("测试记录：张三 语文 135")
    lines = read_all_records()
    print(f"共 {len(lines)} 条记录")




def test_thread():
    print("\n多线程录入")
    multi_thread_input_test()
    print("当前成绩：", student_records)
def test_chinese():
    print("\n语文测试")
    chinese = ChineseExam("张三", essay_score=55)
    chinese.input_score(138)
    print("等级：", chinese.get_grade(chinese.get_score()))
    chinese.print_report_card()
    save_record(f"语文成绩：{chinese.get_score()}")




def test_math():
    print("数学测试")
    math = MathExam("李四")
    math.input_score(148)
    math.set_bonus_points(5)
    print("加权分：", math.calc_weighted_score(0.7))
    save_record(f"数学成绩：{math.get_score()}")


def test_english():
    print("\n英语测试")
    english = EnglishExam("王五")
    english.input_score(92)
    english.print_report_card()
    print("等级：", english.get_grade(english.get_score()))
    save_record(f"英语成绩：{english.get_score()}")





def test_excellent():
    print("\n优秀学生筛选测试")
    scores = {"张三": 138, "李四": 148, "王五": 92}
    excellent = get_excellent_students(scores, 135)
    print("优秀学生：", excellent)



def test_generator():
    print("\n成绩单生成器测试")
    students = ["张三", "李四", "王五"]
    for card in report_card_generator(students):
        print(card)

def test_polymorphism():
    print("\n批量统计多态测试")
    exams = [
        ChineseExam("赵六"),
        MathExam("赵六"),
        EnglishExam("赵六"),
    ]
    exams[0].input_score(130)
    exams[1].input_score(142)
    exams[2].input_score(88)

    for exam in exams:
        print(
            f"{exam.subject_name} 加权分："
            f"{exam.calc_weighted_score(0.7)}"
        )





if __name__ == "__main__":
    BaseExam.set_passing_rate(0.65)

    safe_run(test_basic)
    safe_run(test_file_io)
    safe_run(test_thread)
    safe_run(test_chinese)
    safe_run(test_math)
    safe_run(test_english)
    safe_run(test_excellent)
    safe_run(test_generator)
    safe_run(test_polymorphism)

    print("所有测试完成")