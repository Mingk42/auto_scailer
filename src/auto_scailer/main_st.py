import streamlit as st
import pandas as pd
from tz_kst import now

from auto_scailer.auto_scaler import do_scale, scale_log
from auto_scailer.utils import get_cpu_use, get_log_path, read_log


st.title("Usage Dashboard")

col = ["CPU사용량 (%)","컨테이너 수","상태","지속시간(s)"]
data= [[1,2,3,4]]
df = pd.DataFrame(data, columns=col)

p = st.empty()


###################################################################
l,m,r = st.columns([0.7,0.7,2])
if l.button("Scale out (+)"):
    cu, scale_cnt =get_cpu_use()
    nowTime=now()

    if scale_cnt:
        do_scale("out", scale_cnt+1)
        scale_log("out",None,scale_cnt,scale_cnt+1,cu)
    else:
        st.error("실행 중인 컨테이너가 없습니다.")

if m.button("Scale in (-)"):
    cu, scale_cnt =get_cpu_use()
    nowTime=now()

    if scale_cnt>1:
        do_scale("in", scale_cnt-1)
        scale_log("in",None,scale_cnt,scale_cnt-1,cu)
    elif scale_cnt==1:
        st.error("컨테이너의 수는 1보다 적을 수 없습니다.")
    else:
        st.error("실행 중인 컨테이너가 없습니다.")
###################################################################

while True:
    df = read_log()
    p.write(df.tail(1).style.hide(axis="index"))