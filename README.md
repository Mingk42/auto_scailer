# auto_scailer
config.ini에 설정된 값에 따라 container의 수를 자동적으로 증감하는 프로그램으로, 원할한 시스템 운영에 기여합니다. 

### Usage
```bash
$ scailer-start   # auto scaler를 시작합니다.
$ get-log-path    # log file이 저장된 경로를 반환합니다.
$ usage-plot      # usage-time line plot을 출력합니다.
$ status-plot     # status-times bar plot을 출력합니다.
$ scale-plot      # scale in/out-times bar plot을 출력합니다.
```

### Dependency
![pandas](https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=FFFFFF)
![requests](https://img.shields.io/badge/requests-3776AB.svg?style=for-the-badge&logo=python&logoColor=FFFFFF)
![plotext](https://img.shields.io/badge/plotext-3776AB.svg?style=for-the-badge&logo=python&logoColor=FFFFFF)
![tz_kst](https://img.shields.io/badge/tz__kst-3776AB.svg?style=for-the-badge&logo=python&logoColor=FFFFFF)

### Versions
- `2.1.0` : log형식 변경 및 plot 추가
- `2.0.0` : 10초 마다 체크하는 로직 변경(sleep -> if), 해당 변경사항은 추후 수동으로 스케일을 조절할 수 있도록 하기 위한 조치
- `1.3.0` : stat display 변경 (미배포)
- `1.1.0` : CPU 사용량 log file 생성
- `1.0.1` : 실행중인 container가 없는 경우에 대한 처리 (프로그램 종료)
- `1.0.0` : 정식 배포, LINE NOTIFY 추가
- `0.5.0` : 데모

### Reference
- [configparser](https://docs.python.org/3/library/configparser.html)
- [패키징 가이드](https://packaging.python.org/en/latest/guides/packaging-namespace-packages/#native-namespace-packages)
