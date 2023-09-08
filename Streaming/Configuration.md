# Streaming
>카메라를 이용한 스트리밍

## infrared camera
야간용 적외선 카메라를 이용해 영상 촬영 후 실시간 스트리밍으로 서버에 전송한다. </br>
1. 카메라 연결 및 전원 연결 </br>
2. 옵션 설정 </br>
2-1. Preferences> Raspberry Pi Configuration 접속 > Camera enable </br>
2-2. sudo raspi-config 명령어 입력 > Interface Options > Camera > Yes >sudo reboot </br>
3. ifconfig로 라즈베리파이 ip 찾기 </br>
4. 코드 실행</br>
참고자료: https://stickode.tistory.com/825 </br>
