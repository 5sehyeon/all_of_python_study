import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier,plot_tree
import graphviz
import pandas as pd
from sklearn.tree import export_graphviz
import seaborn as sns

def plot_tree(model, X, y):
    """This function takes a model and the X and y values for a datasetand plots a visualization of the decision tree"""
    dot_data = export_graphviz(model, out_file=None,feature_names=X.columns,class_names=y.unique(),filled=True, rounded=True,special_characters=True)
    return graphviz.Source(dot_data)


# iris는 데이터프레임
iris = sns.load_dataset("iris") # sns에서 제공하는 자료. 데이터 프레임 형태 !
print(iris)

# 데이터 전처리(분리해내야함)
X_feature = iris.loc[:,iris.columns != "species"] # 특성
Y_label = iris["species"] # 정답 


model = DecisionTreeClassifier()
model.fit(X_feature,Y_label)

plot_tree(model, X_feature, Y_label)
plt.show()


from sklearn.model_selection import train_test_split

titanic = sns.load_dataset("titanic")

# 타이타닉 데이터프레임에는 문자열과 NAN값이 있기에, 데이터 전처리 과정이 필요하다.

titanic = titanic.dropna() # NAN값 드롭
X_feature = titanic.loc[:,titanic.columns != "survived"] 
X_feature = pd.get_dummies(X_feature) # 문자열 값을 정수형으로,, 0 혹은 1 이진으로,,
Y_label = titanic["survived"]

# 랜덤하게, train할 자료와 test할 자료를 골라준다 !
X_train, X_test, y_train, y_test = train_test_split(X_feature,Y_label,test_size=0.2) # 0.8은 train , 0.2는 test
print(len(X_train),len(X_test))


model = DecisionTreeClassifier() # 머신러닝 객체 생성.

model.fit(X_train,y_train) # 학습데이터로 머신을 학습시키는 상황.

testing_train = model.predict(X_train)

testing_test = model.predict(X_test)


from sklearn.metrics import accuracy_score

print(accuracy_score(y_train, testing_train))

print(accuracy_score(y_test,testing_test))
