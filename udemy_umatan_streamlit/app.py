import streamlit as st
import pandas as pd

# テキスト記載
st.write("Hello World")

# テキストの色を変える
st.write("Hello :blue[World]")

# タイトル
st.title("Hello World")

# 絵文字
st.title("Hello World:sunglasses:")

# データフレーム挿入
st.write(
    pd.DataFrame(
     {
         "first column" : [1, 2, 3, 4],
         "second column" : [10, 20, 30, 40]
     }   
    )
)

# リンクボタン
st.link_button("Click here", "https://docs.streamlit.io/develop/api-reference")

# ヘッダーに虹色のラインをつける
st.header("Hello world", divider="rainbow")

# コード挿入
code = '''print(hello)'''
st.code(code, language='python')

# チェックボックス
agree = st.checkbox('I agree')
if agree:
    st.write('OK!')
    
# マルチセレクトチェックボックス
options = st.multiselect(
    "好きな色はなんですか？",
    ['赤', '緑', '青', '黄']
)
st.write("あなたが選んだ色は：", options)

#　ラジオボタン（単一セレクト）
options = st.radio(
    "好きな色はなんですか？",
    ['赤', '緑', '青', '黄']
)
st.write("あなたが選んだ色は：", options)

# 修正できるデータフレーム
df = pd.DataFrame(
    [
        {"colors": "赤", "rating": 5, "mark": True},
        {"colors": "緑", "rating": 4, "mark": True},
        {"colors": "青", "rating": 3, "mark": True},
    ]
)

# dfからmarkがTrueのものでその中の最大値のratingをとる色を取得
edited_df = st.data_editor(df)
edited_df = edited_df[edited_df['mark'] == True]
st.write(edited_df.loc[edited_df['rating'].idxmax()]['colors'])

# ダウンロードボタン
csv = edited_df.to_csv().encode('utf-8')

st.download_button(
    label='csvをダウンロード',
    data=csv,
    file_name='sample.csv',
    mime='text/csv'
)

# プログレスバー表示
df = pd.DataFrame(
    {
        'sales': [20, 55, 100, 10],
        'progress_sales': [20, 55, 100, 10]
    }
)
st.data_editor(
    df,
    column_config={
        'progress_sales': st.column_config.ProgressColumn(
            min_value=0,
            max_value=100
        )
    }
)

# 時系列バー表示
df = pd.DataFrame({
    'sales': [
        [0, 4, 26, 30, 50],
        [3, 50, 20, 70, 100],
    ],
})
st.write(df)

st.data_editor(
    df,
    column_config={
        'sales': st.column_config.BarChartColumn(
            y_min=0,
            y_max=100
        )
    }
)

# 棒グラフ
df = pd.DataFrame({
    'sales': [
        [0, 4, 26, 30, 50],
        [3, 50, 20, 70, 100],
    ],
})
st.write(df)

# 棒グラフ
st.data_editor(
    df,
    column_config={
        'sales': st.column_config.BarChartColumn(
            y_min=0,
            y_max=100
        )
    },
    key="bar_chart"
)

# 折れ線グラフ
st.data_editor(
    df,
    column_config={
        'sales': st.column_config.LineChartColumn(
            y_min=0,
            y_max=100
        )
    },
    key="line_chart"
)

# スライダー
age = st.slider('あなたは何歳ですか？', 0, 130, 40)
st.write(f'私は{age}です。')

# 日付選択
import datetime 
date = st.date_input('あなたが生まれたのはいつですか？', datetime.date(2000, 1, 1))
st.write(f'私は{date}に生まれました。')

# ユーザーの自由記述
text = st.text_input('入力してください', 'xxxx')
st.write(text)

# カラムを分ける
col1, col2 = st.columns(2)
with col1:
    st.title('Column1')
    st.write('これはカラム1です。')
with col2:
    st.title('Column2')
    st.write('これはカラム2です。')
    
    
# タブを分ける
tab1, tab2 = st.tabs(["tab1", "tab2"])
with tab1:
    st.title('Tab1')
    st.write('これはタブ1です。')
with tab2:
    st.title('Tab2')
    st.write('これはタブ2です。')

# アコーディオン表示
with st.expander('もっと詳しく見る'):
    st.write('xxxxxxx')
    
# ポップアップ表示
with st.popover('もっと詳しく見る'):
    st.write('xxxxxxx')
    
# サイドバー
with st.sidebar:
    st.title('xxxxxxxxxxxx')
    st.write('xxxx')
    
# nortification
aeree = st.checkbox('同意しますか？')
if agree:
    st.toast('Thank You!', icon="🚨" )
    
# エフェクト
birthday = st.checkbox("今日はあなたの誕生日ですか？")
if birthday:
    st.balloons()
    

# 複数ページにする
st.page_link('app.py', label='Home', icon="🏠")
st.page_link('pages/page1.py', label='Page1')
st.page_link('pages/page2.py', label='Page2')
st.page_link('https://docs.streamlit.io/develop/api-reference', label='StreamlitのAPIドキュメント')

