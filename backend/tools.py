import json


def format_output(output):
    """将UIE的输出格式化"""
    result = []
    for eva_dict in output:
        eva_list = eva_dict['评价维度']          # 单句话的观点抽取结果
        for



    '''[{'评价维度': [{'end': 20,
                    'probability': 0.9817040258681473,
                    'relations': {'情感倾向[正向，负向]': [{'probability': 0.9966142505350533,
                                                           'text': '正向'}],
                                  '观点词': [{'end': 22,
                                              'probability': 0.957396472711558,
                                              'start': 21,
                                              'text': '高'}]},
                    'start': 17,
                    'text': '性价比'},
                   {'end': 2,
                    'probability': 0.9696849569741168,
                    'relations': {'情感倾向[正向，负向]': [{'probability': 0.9982153274927796,
                                                           'text': '正向'}],
                                  '观点词': [{'end': 4,
                                              'probability': 0.9945318044652538,
                                              'start': 2,
                                              'text': '干净'}]},
                    'start': 0,
                    'text': '店面'}]}]'''