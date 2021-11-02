# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 09:59:09 2021

@author: vincey
"""

import random
capitals = {
    '黑龙江': '哈尔滨', '吉林省': '长春', '辽宁省': '沈阳', '河北省': '石家庄', '甘肃省': '兰州', '青海省': '西宁', '陕西省': '西安', '河南省': '郑州', '山东省': '济南', '山西省': '太原', '安徽省': '合肥', '湖北省': '武汉', '湖南省': '长沙', '江苏省': '南京', '四川省': '成都', '贵州省': '贵阳', '云南省': '昆明', '浙江省': '杭州', '江西省': '南昌', '广东省': '广州', '福建省': '福州', '台湾省': '台北', '海南省': '海口', '新疆维吾尔自治区': '乌鲁木齐', '内蒙古自治区': '呼和浩特', '宁夏回族自治区': '银川', '广西壮族自治区': '南宁', '西藏自治区': '拉萨'
}
cptls = list(capitals.keys())
#wrongAnswers = list(capitals.values())

# To make four-choices answers and store to a dict
# params:num to make num
# return dict


def makeAnswers(num=3, excep=''):
    wrongAnswers = list(capitals.values())
    wrongAnswers.pop(wrongAnswers.index(excep))
    answers = random.sample(wrongAnswers, 3) + [excep]
    random.shuffle(answers)
    return dict(zip(answers, ['A', 'B', 'C', 'D']))


for quizNum in range(20):
    random.shuffle(cptls)
    quiz = open('test/test_'+str(quizNum+1)+'.txt', 'w')
    answer = open('test/answer_'+str(quizNum+1)+'.txt', 'w')
    quiz.write('Name:\t\t\tDate:\t\t\tQuiz_'+str(quizNum))
    quiz.write('\n'+'**'*20+'\n\n')
    answer.write('The Answers Of Quiz '+str(quizNum+1)+' Is:\n\n')
    for i in range(len(cptls)):
        an = makeAnswers(excep=capitals[cptls[i]])
        quiz.write(str(i+1)+'、 '+cptls[i]+'的省会是（ ）：\n')
        choice = ''
        for k, v in an.items():
            choice = choice + v+': '+k+'  '
        quiz.write(choice+'\n\n')
        answer.write(str(i+1)+'、'+an[capitals[cptls[i]]]+'\n')
    quiz.close()
    answer.close()
