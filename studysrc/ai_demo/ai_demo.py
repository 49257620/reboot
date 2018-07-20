"""
3.      实例一: 机器学习SVM分类器
1)       目标
用SVM分类器训练数据, 然后实现分类

2)       安装机器学习的相关库
$ sudo apt-get install python-sklearn

3)       代码
"""

from sklearn import svm
  
X = [[0, 0], [1, 1], [1, 0]]  # training samples   
y = [0, 1, 1]  # training target  
clf = svm.SVC()  # class   
clf.fit(X, y)  # training the svc model  
result = clf.predict([2, 2]) # predict the target of testing samples   
print result  # target 


"""
4.      实例二: 绘图
1)       目标
绘制饼图

2)       代码
"""

import matplotlib.pyplot as plt  
labels='frogs','hogs','dogs','logs'  
sizes=15,20,45,10  
colors='yellowgreen','gold','lightskyblue','lightcoral'  
explode=0,0.1,0,0  
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)  
plt.axis('equal')  
plt.show() 


"""
1)       目标
把一个中文句子分成单个词

2)       安装分词库
下载安装包jieba-0.38.zip
$ unzip jieba-0.38.zip
$ jieba-0.38
$ sudo python setup.py install

3)       代码
"""

#! -*- coding:utf-8 -*-
import jieba
seg_list = jieba.cut("北京野生动物园轿车遭黑熊围堵")
print "Default Mode:", ' '.join(seg_list)
