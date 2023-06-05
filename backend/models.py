from paddlenlp import Taskflow
import json
import paddle


class Models:
    """不同的任务：情感分析，信息抽取"""
    def __init__(self, data):
        self.data = data

    def sentiment_analysis(self):
        schema = '情感倾向[正向，负向]'
        ie = Taskflow('information_extraction', schema=schema)
        return ie(self.data)

    def entity_recognition(self):
        schema = ['时间', '地点', '人物']
        ie = Taskflow('information_extraction', schema=schema)
        return ie(self.data)

    def opinion_extraction(self):
        schema = {'评价维度': ['观点词', '情感倾向[正向，负向]']}
        ie = Taskflow('information_extraction', schema=schema)
        return ie(self.data)
