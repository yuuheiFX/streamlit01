import streamlit as st 

import time


st.title("Streamlit超超入門")

st.write("プログレスバー")
'Start!!'

latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)


'Done!!!!!!!!'




left_column,right_column=st.beta_columns(2)

button=left_column.button("右カラムに文字を表示")

if button:
    right_column.write("ここは右カラム")

expander1=st.beta_expander('問い合わせ')
expander1.write("内容を書く")
expander2=st.beta_expander('問い合わせ')
expander2.write("内容を書く")
expander3=st.beta_expander('問い合わせ')
expander3.write("内容を書く")
expander4=st.beta_expander('問い合わせ')
expander4.write("内容を書く")




# text = st.text_input('あなたの趣味は？')
# 'あなたの趣味は',text,"です。"

# condition=st.slider('あなたの調子は？',0.0,10.0,5.0)
# 'コンディション',condition
# option= st.selectbox(
#     'あなたが好きな数字を教えて',
#     list(range(1,11))
# )
# 'あなたの好きな数字は',option,'です。'

# if st.checkbox("Show Image"):
#     img=Image.open("sample.jpg")
#     st.image(img,caption="free",use_column_width=True)

# df=pd.DataFrame(
#    np.random.rand(100,2)+[35.69,139.70],
#    columns=["lat","lon"]
# )
# st.map(df)
#st.bar_chart(df)

#st.table(df)

