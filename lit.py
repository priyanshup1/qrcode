import streamlit as st
import pandas as pd
import numpy as np
from sklearn import datasets
import seaborn as sn 
import matplotlib as plt
import pyqrcode
import png
st.title("welcome to stream it")
st.title("GET YOUR QR_CODE")
urlink=st.text_input("enter the url",)
url = pyqrcode.create(urlink)
url.svg('uca-url.svg', scale=3)
url.eps('uca-url.eps', scale=2)
url.terminal(quiet_zone=1)
#print(url.terminal(quiet_zone=1))
url.png("myqrcode.png",scale=6)
st.image(url.png)
