import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


st.title('Irisデータを用いた予測アプリ')

iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target, name='species')

st.write(iris.feature_names)
st.write(X)
# st.write(y)

# 学習データとテストデータに分割
X_train, X_test, y_train , y_test = train_test_split(X, y, test_size=0.3)

# モデルの学習
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# テストデータの予測
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
st.write(f'精度は{acc}です。')

# ユーザーが入力フォーム
st.header('好きな値を入力して下さい')
sepal_length = st.number_input('sepal length (cm)', min_value=0, value=3)
sepal_width = st.number_input('sepal width (cm)', min_value=0, value=3)
petal_length = st.number_input('petal length (cm)', min_value=0, value=3)
petal_width = st.number_input('petal width (cm)', min_value=0, value=3)

input_data = pd.DataFrame({
    "sepal length (cm)": [sepal_length],
    "sepal width (cm)": [sepal_width],
    "petal length (cm)": [petal_length],
    "petal width (cm)" : [petal_width] 
    }
)

if st.button('Predict'):
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)
    st.write(prediction)
    st.write(prediction_proba)
    species =iris.target_names[prediction][0]
    st.write(f'予測結果は {species} です')
    
    # データの可視化
    st.header('データの可視化')
    fig, ax = plt.subplots()
    scatter = ax.scatter(X['petal length (cm)'], X['petal width (cm)'], c=y, label=iris.target_names)
    ax.scatter(petal_length, petal_width, c='red')
    ax.set_xlabel('petal length (cm)')
    ax.set_ylabel('petal width (cm)')
    hanrei, _ = scatter.legend_elements(prop='colors')
    legend_labels = iris.target_names
    ax.legend(hanrei, legend_labels, title='Species')
    
    st.pyplot(fig)