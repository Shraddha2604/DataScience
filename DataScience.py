import pandas as pd
import streamlit as st
import numpy as np

def content(df):
    for index, rows in df.iterrows():   
        expander = st.expander(rows['Question'])
        # expander.write(rows['Answer'])

        if '\n' in rows['Answer']:
            for i in list(rows['Answer'].split('\n')):
                expander.write(i)
        else:
            expander.write(rows['Answer'])

        if rows['Image'] != '':
            try:
                expander.image('D:\Interview\Preparation\images' + '\\' + rows['Image'] + '.jpg')
            except:
                expander.image('D:\Interview\Preparation\images' + '\\' + rows['Image'] + '.png')

st.set_page_config(layout="wide")
path = r'D:\Interview\Preparation'
print('--------------------------------------------------------------------------------------------------')
st.header('Interview Questions')
Python, ML, DL, NLP = st.tabs(['Python', 'Machine Learning', 'Deep Learning', 'Natural Language Processing'])

with ML:
    df = pd.read_excel(path + '\MachineLearning.xlsx')
    df = df.fillna('')
    content(df)

with DL:
    df = pd.read_excel(path + '\DeepLearning.xlsx')
    df = df.fillna('')
    content(df)
    

with NLP:
    df = pd.read_excel(path + '/NLP.xlsx')
    df = df.fillna('')
    content(df)

