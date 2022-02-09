import streamlit as st
import pandas as pd
import datetime
import re
import csv
import zipfile
import io
from PIL import Image

st.title('研究紹介')

pass_st=1

if pass_st==1:
  st.sidebar.write('表示')
  slides_1 = st.sidebar.radio("テーマ",('1. 微細構造表面における凝縮水滴の凍結観察', '2. 機械学習を用いたPEFC触媒層の乾燥プロセス開発'))
  if str(slides_1[0])==str(1):
    slides_2 = st.sidebar.radio("スライド番号",('1. 背景・目的', '2. 背景・目的', '3. 実験方法(試料表面)','4. 実験方法(観察装置)',
                                          '5. 結果(観察)','6. 結果(成長分析)','7. 考察(仮説)','8. 考察(先行研究)','9. 考察(本研究)'))
  else:
    slides_2 = st.sidebar.radio("スライド番号",('1. 背景・目的', '2. 背景・目的', '3. 実験方法（操作）','4. 実験方法（センサ）','5. 実験結果','6. 考察'))
  
  filename = "./DATA.zip"
  view_name='DATA/'+str(str(slides_1[0]))+str(str(slides_2[0]))
  
  with zipfile.ZipFile(filename, "r") as zp:
    #画像表示
    with zp.open(view_name+'.JPG',pwd=pass_in.encode("utf-8")) as img_file:
      img_bin = io.BytesIO(img_file.read())
      img = Image.open(img_bin)
      st.image(img, caption='Sunrise by the mountains')
    #テキスト表示
    with zp.open(view_name+'.txt',pwd=pass_in.encode("utf-8")) as txt_file:
      txtdata = txt_file.read().decode('utf_8')
      #st.write(txtdata)
      txt_s=txtdata.split('\n')
      for i in range(len(txt_s)):
        st.write(txt_s[i])
