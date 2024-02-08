import streamlit as st
import pandas as pd
import time

st.title('Streamlit 超入門')
st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [1, 2, 3, 4]
})

df2 = pd.DataFrame({
    'lat':[35.69],
    'lon':[139.70]
    })


st.dataframe(df, width = 100, height=100)
st.table(df)
st.line_chart(df)

if st.checkbox('map'):
    st.map(df2)

num1 = st.sidebar.selectbox(
    'select num',
    list(range(1, 11))
)
'選んだ数字は', num1, 'です。'

txt1 = st.sidebar.text_input('文字列を入力してください')
'入力した文字列は', txt1, 'です。'

num2 = st.sidebar.slider('スライダー', 0, 100, 50)
'入力した値は', num2, 'です。'

st.write('プログレスバー')

lt = st.empty()
bar = st.progress(0)

for i in range(100):
    lt.text(f'{i+1} %')
    bar.progress(i+1)
    time.sleep(0.01)


""""
# 章
## 節
### 項目
"""