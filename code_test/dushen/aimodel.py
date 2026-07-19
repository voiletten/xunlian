import time
import asyncio
from datetime import datetime
from tkinter import Image
from unittest import result


#====1.模型层（aimodel-textmodel/imagemodel)
class AIModel:
    """所有 AI 模型的父类，定义统一接口。"""
    def __init__(self, name, model_type):
        self.name = name
        self.model_type = model_type

    async def predict(self, input_data):
        # 父类只定义接口，具体实现交给子类
        raise NotImplementedError("子类必须实现 predict 方法")


class TextModel(AIModel):
    """文本生成模型。"""
    async def predict(self, input_data):
        print(f"  [{self.name}] 正在生成文本：{input_data}")
        await asyncio.sleep(1)
        return f"文本结果:{input_data}"

class ImageModel(AIModel):
    """图像识别模型。"""
    async def predict(self, input_data):
        print(f"  [{self.name}] 正在识别图像：{input_data}")
        await asyncio.sleep(2)
        return f"图像结果:{input_data}"


async def user_request(user, model, input_data):
    start = time.time()
    await model.predict(input_data)

    end = time.time()
    result = end - start

    return {
        "result": result,
        "user": user,
        "model": model,
        "input_data": input_data
    }

t1 = TextModel("豆包","文本")
t2 = TextModel("豆包","文本")
t3 = ImageModel("DS","图像")
t4 = ImageModel("DS","图像")

async def main():
    a = await asyncio.gather(user_request("alice",t1,"文本1"),user_request("bob",t2,"文本2"),user_request("candy",t3,"1.jpg"),user_request("david",t4,"2.jpg"))
    print(a)
asyncio.run(main())