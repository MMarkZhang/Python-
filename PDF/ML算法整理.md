**无监督学习**
- [Apriori算法](#apriori算法)
- [K-Means（K平均值算法）](#k-means----k平均值算法)

**监督学习**
- [K-NN（K临近算法）](#k-nn---k临近算法)
- [Naive Bayesian Classifier(朴素贝叶斯算法)](#naive-bayesian-classifier朴素贝叶斯算法)
- [决策树算法](#决策树算法)
- [Logistic Regression逻辑回归](#logistic-regression逻辑回归)
 
# 无监督学习
# **Apriori算法**
## 主要功能：
是一种最有影响的挖掘布尔关联规则频繁项集的算法。其核心是基于两阶段频集思想的递推算法。该关联规则在分类上属于单维、单层、布尔关联规则。在这里，所有支持度大于最小支持度的项集称为频繁项集，简称频集。
## 使用方法：
第一步通过迭代，检索出事务数据库中的所有频繁项集，即支持度不低于用户设定的阈值的项集；
第二步利用频繁项集构造出满足用户最小信任度的规则。
## 用处：
通常用于找出各项之前的关联度，找到项集的支持度，以及条件概率的置信度
## 范例：
![图片](https://images-cdn.shimo.im/h6xmvrejc4o2INxf/屏幕快照_2018_06_21_下午3.11.04.png!thumbnail)
## 伪代码：
![图片](https://images-cdn.shimo.im/8z2aWf2cS3gKV5Of/屏幕快照_2018_06_21_下午2.23.57.png!thumbnail)
http://blog.51cto.com/wukong0716/1695849
https://blog.csdn.net/Bone_ACE/article/details/46660819 
https://blog.csdn.net/bone_ace/article/details/46648965
https://blog.csdn.net/u011067360/article/details/24810415

# **K-Means    K平均值算法**

## 主要功能：
k-means 所要优化的目标函数：设我们一共有 N 个数据点需要分为 K 个 cluster ，k-means 要做的就是最小化这个函数
## 使用方法：
![图片](https://images-cdn.shimo.im/imtxQCAixLoG37fL/image.png!thumbnail)
## 用处：
优点：
原理简单
速度快
对大数据集有比较好的伸缩性

缺点：
需要指定聚类 数量K
对异常值敏感
对初始值敏感
## 范例：
## ![图片](https://images-cdn.shimo.im/GZ0aRsz2jUcIuBdF/iter_00.png!thumbnail)![图片](https://images-cdn.shimo.im/QqwZmR2lvEwCfa2D/iter_01.png!thumbnail)![图片](https://images-cdn.shimo.im/KOkZhzHtI9gU3av8/iter_02.png!thumbnail)![图片](https://images-cdn.shimo.im/7sIiI4KArwkNZVpG/iter_04.png!thumbnail)
## 伪代码：
 创建k个点作为起始质心（经常是随机选择） 
 当任意一个点的蔟分配结果发生改变时 
 对数据集中的每个数据点 
 对每个质心 
 计算质心与数据点之间的距离 
将数据点分配到据其最近的蔟 
 对每一个蔟，计算蔟中所有点的均值并将其做为质心
[https://blog.csdn.net/hewei0241/article/details/8262768](https://blog.csdn.net/hewei0241/article/details/8262768)
# 监督学习
# **K-NN   K临近算法**

## 主要功能：
K近邻法是一个基本分类和回归方法，输入为实例的特征向量，对应于特征空间的点；输出为实例的类别，可以取多类。多组数据，多个维度
## 使用方法：
找到k范围内临近的object，然后根据多数服从原则，得到目标对应的object
## 用处：
![图片](https://images-cdn.shimo.im/h4VEt5VT8LMEOz6V/图片1.png!thumbnail)
## 范例：
## ![图片](https://images-cdn.shimo.im/c3NaGKKMAoIhftot/屏幕快照_2018_06_21_下午3.17.15.png!thumbnail)伪代码：
 计算训练集中到该点的距离 
 选择距离最小的k个点 
 返回k个点出现频率最高的类别作为当前点的预测分类
# **Naive Bayesian Classifier(朴素贝叶斯算法)**

## 主要功能：
贝叶斯分类算法是统计学的一种分类方法，它是一类利用概率统计知识进行分类的算法。在许多场合，朴素贝叶斯(Naïve Bayes，NB)分类算法可以与决策树和神经网络分类算法相媲美，该算法能运用到大型数据库中，而且方法简单、分类准确率高、速度快。
## 使用方法：
![图片](https://images-cdn.shimo.im/b5HssW6lyro5VolN/图片2.png!thumbnail)
## 用处：
根据已知，判断某事如何发生的概率问题。
![图片](https://images-cdn.shimo.im/OzlAHtbVJek9tinO/image.png!thumbnail)
## 范例：
[https://blog.csdn.net/zhaomengszu/article/details/54562026](https://blog.csdn.net/zhaomengszu/article/details/54562026)
## 伪代码：
多项式朴素贝叶斯算法伪代码
![图片](https://images-cdn.shimo.im/aS9xVI2IvSMsT0pl/22.png!thumbnail)

伯努利朴素贝叶斯算法伪代码
![图片](https://images-cdn.shimo.im/jDvafhDmA4wtz7Ic/23.png!thumbnail)

# **决策树算法**

## 主要功能：
决策树(Decision Tree）是在已知各种情况发生概率的基础上，通过构成决策树来求取净现值的期望值大于等于零的概率，评价项目风险，判断其可行性的决策分析方法，是直观运用概率分析的一种图解法。由于这种决策分支画成图形很像一棵树的枝干，故称决策树。
## 使用方法：
 	1创建节点N
	2如果训练集为空，在返回节点N标记为Failure
	3如果训练集中的所有记录都属于同一个类别，则以该类别标记节点N
	4如果候选属性为空，则返回N作为叶节点，标记为训练集中最普通的类；
	5for each 候选属性 attribute_list
	6if 候选属性是连续的then
	7对该属性进行离散化
	8选择候选属性attribute_list中具有最高信息增益率的属性D
	9标记节点N为属性D
	10for each 属性D的一致值d
	11由节点N长出一个条件为D=d的分支
	12设s是训练集中D=d的训练样本的集合
	13if s为空
	14加上一个树叶，标记为训练集中最普通的类
	15else加上一个有C4.5（R - {D},C，s）返回的点
## 用处：
根据练习集创造decision tree；然后用于决策之后的数据
创造decision tree时用到信息熵和信息增益
## 范例：
## ![图片](https://images-cdn.shimo.im/70pP0rlQmWwBqqLQ/屏幕快照_2018_06_22_下午4.58.26.png!thumbnail)
[https://blog.csdn.net/u012328159/article/details/70184415#commentBox](https://blog.csdn.net/u012328159/article/details/70184415#commentBox)
## 伪代码：
![图片](https://images-cdn.shimo.im/JJubyImEcBUfDM7Z/20171002112107949.png!thumbnail)

# **Logistic Regression逻辑回归**

## 主要功能：
LR回归是在线性回归模型的基础上，使用sigmoid函数得到的。
它的优点是，它是直接对分类的可能性进行建模的，无需事先假设数据分布，这样就避免了假设分布不准确所带来的问题，因为它是针对于分类的可能性进行建模的，所以它不仅能预测出类别，还可以得到属于该类别的概率。
## 使用方法：
	逻辑斯蒂回归是针对线性可分问题的一种易于实现而且性能优异的分类模型，是使用最为广泛的分类模型之一。假设某件事发生的概率为p，那么这件事不发生的概率为(1-p)，我们称p/(1-p)为这件事情发生的几率。取这件事情发生几率的对数，定义为logit(p)，所以logit(p)为
![图片](https://images-cdn.shimo.im/wzbUlmPnCmUZdBCL/图片3.png!thumbnail)
## 用处：
将特征回归，判断结果。
我们需要一个更好的映射函数，能够将分类的结果很好的映射成为[0,1]之间的概率，并且这个函数能够具有很好的可微分性。在这种需求下，人们找到了这个映射函数，即逻辑斯谛函数
## 范例：
输入 （分为练习和测试）：
![图片](https://images-cdn.shimo.im/ObmdrttXoKYfWps1/屏幕快照_2018_06_25_下午2.03.45.png!thumbnail)
![图片](https://images-cdn.shimo.im/Ef0ttZlpZ3svf8PO/屏幕快照_2018_06_25_下午2.04.00.png!thumbnail)

输出（测试准确率）：
![图片](https://images-cdn.shimo.im/gKiH7JrE4Qg8eKKJ/屏幕快照_2018_06_25_下午2.04.31.png!thumbnail)
## 伪代码：
随机梯度下降 伪代码(pseudo_code)：
每个回归系数初始化为1 
重复R次： 
计算整个数据集的梯度
使用a * gradient更新回归系数的向量
返回回归系数值

