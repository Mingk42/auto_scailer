from auto_scailer.utils import get_limit, get_cpu_use, send_line_noti, get_log_path, get_compose_file_path
import time
import os
from tz_kst import now

conti_high=0
conti_low=0
logging_time = now("%Y%m%d-%H%M%S")


def auto_scailer():
    global conti_high
    global conti_low

    scale_in_value, scale_out_value=map(float,get_limit())

    home_path=os.path.expanduser("~")
    cu, scale_cnt =get_cpu_use()

    while scale_cnt:
        cu=float(cu.replace("%",""))
        nowTime=now()

        usage_log_path=f"{get_log_path()}"
        os.makedirs(usage_log_path, exist_ok=True)
        with open(f"{usage_log_path}/usage_{logging_time}.log", "a") as f:
            data = {"cpu_usage(%)":cu, "time":nowTime, "scale_cnt":scale_cnt, "cpu_use_status": "high" if cu >scale_out_value else "low" if cu <scale_in_value else "stable"}
            f.write(str(data))
            f.write("\n")

        # print(f"[INFO] 현재 CPU사용량은 {cu}입니다.")
        # print(f"[INFO] 현재 container의 수는 {scale_cnt}개입니다.")
        #### CPU 사용량이 scale_out_value를 넘으면 scale out ####
        if cu >scale_out_value:
            conti_high+=10
            # print(f"[WARN] {conti_high}초 동안 과부하 상태...")
        else:
            conti_high=0

        if conti_high==60:
            print(f"[INFO] container의 수를 {scale_cnt+1}로 scale out 합니다.")
            #os.system(f"docker compose -f {home_path}/code/docker/k1s/docker-compose.yaml up -d --scale blog={scale_cnt+1}")
            os.system(f"docker compose -f {get_compose_file_path()} up -d --scale blog={scale_cnt+1}")

            conti_high=0
            code, msg = send_line_noti(f"[INFO] container의 수가 {scale_cnt+1}로 scale out 되었습니다.")


        ######################################################
        #### CPU 사용량이 scale_in_value보다 낮으면 scale in ####
        ##### 1개의 컨테이너는 남겨야 함 ########################
        if scale_cnt>1:
            if cu <scale_in_value:
                conti_low+=10
                # print(f"[INFO] {conti_low}초 동안 안정된 상태...")
            else:
                conti_low=0

            if conti_low==60:
                    print(f"[INFO] container의 수를 {scale_cnt-1}로 scale in 합니다.", end="\n\n")
                    #os.system(f"docker compose -f {home_path}/code/docker/k1s/docker-compose.yaml up -d --scale blog={scale_cnt-1}")
                    os.system(f"docker compose -f {get_compose_file_path()} up -d --scale blog={scale_cnt-1}")

                    conti_low=0
                    code, msg = send_line_noti(f"[INFO] container의 수가 {scale_cnt-1}로 scale in 되었습니다.")
        ######################################################
        if conti_high>0:
            status="High"
            conti_time=conti_high
        elif conti_low>0:
            status="Low"
            conti_time=conti_low
        else:
            status="Stable"
            conti_time="-"

        os.system("clear")
        print("+"+"-"*87+"+")
        print(f"|\tCPU사용량 (%)\t|\t컨테이너 수\t|\t상태\t|\t지속시간(s)\t|")
        print("-"*89)
        print(f"|\t\t{cu}\t|\t\t{scale_cnt}\t|\t{status}\t|\t\t{conti_time}\t|")
        print("+"+"-"*87+"+")

        print(f"마지막 확인시간 : {nowTime}")
        time.sleep(10)
        cu, scale_cnt =get_cpu_use()