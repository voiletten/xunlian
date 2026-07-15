# 任务三代码
import time
import threading
from datetime import datetime

#1.模型类
class AIModel:
    def __init__(self, name, model_type):
        self.name = name
        self.model_type = model_type

    def predict(self, input_data):
        raise NotImplementedError("子类必须实现predict方法")

class TextModel(AIModel):
    def predict(self, input_data):
        # start = datetime.now()
        print(f"[{self.name}]正在生成文本：{input_data}")
        time.sleep(1)
        # end = datetime.now()
        # return {
        #     "output":f"《{input_data}》的生成结果",
        #     "cost":(end - start).totolseconds()
        # }
        return f"文本结果：{input_data}"

class ImageModel(AIModel):
    def predict(self, input_data):
        # start = datetime.now()
        print(f"[{self.name}]正在识别图像：{input_data}")
        time.sleep(1)
        # end = datetime.now()
        # return {
        #     "output":f"{input_data}的识别结果为：猫咪",
        #     "cost":(end - start).totolseconds()
        # }
        return f"图像结果：{input_data}"





class Scheduler:
    lock = threading.Lock()

    def __init__(self, tasks=None):
        self.tasks = tasks if tasks is not None else []
        self.records = []

    def _run_one(self):
        threads = [threading.Thread(target=self.user_request, args=t) for t in self.tasks]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        self.report()

    def run_serial(self):
        for user, model, data in self.tasks:
            self.user_request(user, model, data)
        self.report()

    def run_concurrent(self):
        threads = [threading.Thread(target=self.user_request, args=t) for t in self.tasks]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        self.report()

    def user_request(self, user_name, model, input_data):
        start = datetime.now()
        result = model.predict(input_data)
        cost = (datetime.now() - start).total_seconds()
        with self.lock:
            self.records.append({"user": user_name, "model": model.name, "cost": cost, "result": result})

    def report(self):
        for r in self.records:
            print(f"{r['user']}->{r['model']}，耗时{r['cost']}秒，结果：{r['result']}")





if __name__ == '__main__':
    all_start = datetime.now()

    text_model = TextModel("DB模型", "文本生成")
    image_model = ImageModel("DS模型", "图像识别")

    
    tasks = [
        ("用户A", text_model,  "今天天气真好"),
        ("用户B", image_model, "cat.jpg"),
        ("用户C", text_model,  "机器学习笔记"),
        ("用户D", image_model, "dog.png"),
        ("用户E", text_model,  "Python教程"),
        ("用户F", image_model, "bird.webp"),
    ]

    s1 = Scheduler(tasks)
    s2 = Scheduler(tasks)
    s3 = Scheduler(tasks)

    s1._run_one()
    s2.run_serial()
    s3.run_concurrent()

    print(f"总耗时：{(datetime.now() - all_start).total_seconds():.2f} 秒")
