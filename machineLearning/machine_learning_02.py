from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd


def knn_iris():
    """
    用KNN算法对鸢尾花进行分类
    :return:
    """
    # 1、获取数据
    iris = load_iris()
    # 2、划分数据
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=6)
    # 3、特征工程：标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 4、KNN算法预估器
    estimator = KNeighborsClassifier(n_neighbors=3)
    estimator.fit(x_train, y_train)

    # 5、模型评估
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print('y_predict:\n', y_predict)
    print('直接对比真实值和预测值：\n', y_test == y_predict)

    # 方法2：计算准确率
    score = estimator.score(x_test, y_test)
    print('准确率：\n', score)


def knn_iris_gscv():
    """
    用KNN算法对鸢尾花进行分类，添加网格搜索和交叉验证
    :return:
    """
    # 1、获取数据
    iris = load_iris()
    # 2、划分数据
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=6)
    # 3、特征工程：标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 4、KNN算法预估器
    estimator = KNeighborsClassifier(n_neighbors=3)

    # 加入网格搜索和交叉验证
    # 参数准备
    param_dict = {'n_neighbors': [1, 3, 4, 5, 7, 9, 11]}
    estimator = GridSearchCV(estimator, param_grid=param_dict, cv=10)
    estimator.fit(x_train, y_train)

    # 5、模型评估
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print('y_predict:\n', y_predict)
    print('直接对比真实值和预测值：\n', y_test == y_predict)

    # 方法2：计算准确率
    score = estimator.score(x_test, y_test)
    print('准确率：\n', score)

    # 最佳参数：best_params_
    print("最佳参数：\n", estimator.best_params_)
    # 最佳结果：best_score_
    print("最佳结果：\n", estimator.best_score_)
    # 最佳估计器：best_estimator_
    print("最佳估计器:\n", estimator.best_estimator_)
    # 交叉验证结果：cv_results_
    print("交叉验证结果:\n", estimator.cv_results_)


def facebook():
    data = pd.read_csv('train.csv')
    data.head()
    # 1、缩小数据范围
    data = data.query('x<2.5 & x>2 & y<1.5 & y>1.0')
    # 2、处理时间特征
    time_value = pd.to_datetime(data['time'], unit='s')
    date = pd.DatetimeIndex(time_value)
    data['weekday'] = date.weekday
    data['day'] = date.day
    data['hour'] = date.hour
    # 3、过滤签到次数少的地点
    palce_count = data.groupby('place_id').count()['row_id']
    data_final = data[data['place_id'].isin(palce_count[palce_count > 3].index.values)]
    print(data_final)

    # 筛选特征值和目标值
    x = data_final[['x', 'y', 'accuracy', 'day', 'weekday', 'hour']]
    y = data_final['place_id']

    # 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(x, y)

    # 3、特征工程：标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 4、KNN算法预估器
    estimator = KNeighborsClassifier(n_neighbors=3)

    # 加入网格搜索和交叉验证
    # 参数准备
    param_dict = {'n_neighbors': [7, 9, 11]}
    estimator = GridSearchCV(estimator, param_grid=param_dict, cv=3)
    estimator.fit(x_train, y_train)

    # 5、模型评估
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print('y_predict:\n', y_predict)
    print('直接对比真实值和预测值：\n', y_test == y_predict)

    # 方法2：计算准确率
    score = estimator.score(x_test, y_test)
    print('准确率：\n', score)

    # 最佳参数：best_params_
    print("最佳参数：\n", estimator.best_params_)
    # 最佳结果：best_score_
    print("最佳结果：\n", estimator.best_score_)
    # 最佳估计器：best_estimator_
    print("最佳估计器:\n", estimator.best_estimator_)
    # 交叉验证结果：cv_results_
    print("交叉验证结果:\n", estimator.cv_results_)


def nb_new():
    """
    朴素贝叶斯算法对新闻进行分类
    :return:
    """
    # 1、获取数据
    news = fetch_20newsgroups(subset='all')
    # 2、划分数据集
    x_train, x_test, y_train, y_test = train_test_split(news.data, news.target)
    # 3、特征工程：文本特征抽取-tfidf
    transfer = TfidfVectorizer()
    x_train =transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 4、朴素贝叶斯算法预估器流程
    estimator = MultinomialNB()
    estimator.fit(x_train,y_train)
    # 5、模型评估
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print('y_predict:\n', y_predict)
    print('直接对比真实值和预测值：\n', y_test == y_predict)

    # 方法2：计算准确率
    score = estimator.score(x_test, y_test)
    print('准确率：\n', score)

    # 最佳参数：best_params_
    print("最佳参数：\n", estimator.best_params_)
    # 最佳结果：best_score_
    print("最佳结果：\n", estimator.best_score_)
    # 最佳估计器：best_estimator_
    print("最佳估计器:\n", estimator.best_estimator_)
    # 交叉验证结果：cv_results_
    print("交叉验证结果:\n", estimator.cv_results_)


if __name__ == '__main__':
    # knn_iris()
    # knn_iris_gscv()
    # facebook()
    nb_new()