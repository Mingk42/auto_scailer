import streamlit as st
from glob import glob
import pandas as pd
import matplotlib.pyplot as plt

from auto_scailer.utils import get_cpu_use, get_log_path

st.title("Scale log")

ops=[]
for i in glob(f"{get_log_path()}/scale/*.log"):
    ops.append(i.replace(f"{get_log_path()}/scale/",""))

ops.sort()

option = st.selectbox(
    "그래프 생성할 로그 파일 선택",
    ops,
)

filepath=f"{get_log_path()}/scale/{option}"

df = pd.read_csv(filepath)

plt.bar(pd.DataFrame(df["method"].value_counts()).index, df["method"].value_counts())
plt.xlabel("method")
plt.ylabel("times")

st.pyplot(plt)