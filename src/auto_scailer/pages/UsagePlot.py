import streamlit as st
from glob import glob
import pandas as pd
import matplotlib.pyplot as plt

from auto_scailer.utils import get_cpu_use, get_log_path

st.title("Usage log")

ops=[]
for i in glob(f"{get_log_path()}/usage/*.log"):
    ops.append(i.replace(f"{get_log_path()}/usage/",""))

ops.sort()

option = st.selectbox(
    "그래프 생성할 로그 파일 선택",
    ops,
)

filepath=f"{get_log_path()}/usage/{option}"

df = pd.read_csv(filepath)

usage = df["cpu_usage(%)"]
time = [10*i for i in range(len(usage))]

plt.subplots()
plt.plot(time, usage)

plt.xlabel("time (s)")
plt.ylabel("cpu_usage (%)")

st.pyplot(plt)

plt.subplots()
plt.bar(pd.DataFrame(df["cpu_use_status"].value_counts()).index, df["cpu_use_status"].value_counts())
plt.xlabel("status")
plt.ylabel("times")

st.pyplot(plt)