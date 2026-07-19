import threading
from datetime import datetime

# 全局共享数据
student_records = {}
record_lock = threading.Lock()



def check_valid_score(score, max_score):
    return 0 <= score <= max_score





def calc_percentage(score, max_score):
    return round(score / max_score * 100, 2)





def save_record(record_info):
    with open("exam_records.txt", "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {record_info}\n")




def read_all_records():
    with open("exam_records.txt", "r", encoding="utf-8") as f:
        return f.readlines()





def get_excellent_students(score_dict, threshold):
    return [name for name, score in score_dict.items() if score >= threshold]





def report_card_generator(student_list):
    for student in student_list:
        yield f"📄 成绩单：{student}"





def input_score_thread_safe(student_name, subject, score):
    with record_lock:
        if student_name not in student_records:
            student_records[student_name] = {}

        student_records[student_name][subject] = score
        save_record(f"{student_name} - {subject}: {score}")






def multi_thread_input_test():
    t1 = threading.Thread(
        target=input_score_thread_safe, args=("张三", "语文", 130)
    )
    t2 = threading.Thread(
        target=input_score_thread_safe, args=("李四", "数学", 145)
    )

    t1.start()
    t2.start()
    t1.join()
    t2.join()