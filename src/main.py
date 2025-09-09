#!/usr/bin/env python3
# pylint: disable=import-error

"""
GPIO 과제
- gpiozero 라이브러리 사용

UART 과제
- pyserial 라이브러리 사용
- UART 통신: 115200 bps, 8N1, 플로우 제어 없음
- TXD3/RXD3을 활용
"""

import sys
import time

from gpiozero import LED, Button
from serial import Serial


def blink_led() -> None:
    """
    [문제 1] 18번 핀에 연결된 LED를 1초 간격으로 ON/OFF를 10번 반복
    - gpiozero.LED 사용
    - 종료시 LED는 OFF 상태
    """
    # TODO: blink_led 구현
    led = LED(18)
    try:
        for _ in range(10):
            led.on()
            time.sleep(1)
            led.off()
            time.sleep(1)
    finally:
        led.off()

    #raise NotImplementedError


def check_to_input_button() -> None:
    """
    [문제 2] 18번 핀 버튼 입력을 받아서
      - 눌렸을 때: 'pressed'
      - 뗐을 때:   'released'
    를 출력한다.
    - polling 방식으로 구현할 것.
    - 버튼 입력을 10번 받았으면 종료.
    """
    # TODO: check_to_input_button 구현
    button = Button(18)
    presses = 0
    last = button.is_pressed  # 시작 상태 기억
    try:
        while presses < 10:
            now = button.is_pressed
            if now != last:
                if now:
                    print("pressed")
                    presses += 1
                else:
                    print("released")
                last = now
            time.sleep(0.005)  # 가벼운 폴링 간격
    finally:
        button.close()


    
    



    #raise NotImplementedError


def blink_led_through_button() -> None:
    """
    [문제 3]
    - 12번: LED 출력
    - 13번: Button 입력
    - 버튼이 눌려 있는 동안에만 LED가 0.5초 간격으로 깜빡인다.
    - 버튼이 10번 눌려졌으면 종료.
    - 종료시 LED는 OFF 상태
    """
    # TODO: blink_led_through_button 구현
    

    try:
        led = LED(12)
        led.off()
    except Exception:
       
        pass
    return
    #led.on()

    #raise NotImplementedError


def transmit_msg() -> None:
    """
    [문제 1] UART3로 "Hello World! {i}" 문자열을 1초마다 전송
    - 총 10번 전송 후 종료
    - 개행을 붙여 전송 (수신/테스트 편의)
    """
    # TODO: blink_led_through_button 구현
    ser = Serial("/dev/ttyAMA3", baudrate=115200, bytesize=8, parity="N", stopbits=1, timeout=1)
    try:
        for i in range(10):
            msg = f"Hello World! {i}\n"
            ser.write(msg.encode())
            time.sleep(1.0)
    finally:
        try:
            ser.close()
        except Exception:
            pass

    #raise NotImplementedError


def receive_msg() -> None:
    """
    [문제 2] UART3에서 줄 단위로 읽어 화면에 출력.
    - 'exit' (대소문자 무시) 라인을 수신하면 함수 종료
    """
    # TODO: blink_led_through_button 구현
    ser = Serial("/dev/ttyAMA3", baudrate=115200, timeout=1)
    buf = bytearray()
    try:
        while True:
            b = ser.read(1)  # readline() 대신 1바이트씩 읽기
            if not b:
                # timeout 동안 데이터 없으면 계속 대기
                continue
            if b == b"\n":
                line = buf.decode(errors="ignore").strip()
                buf.clear()
                if line:
                    print(line)
                    if line.lower() == "exit":
                        break
            else:
                buf.extend(b)
    finally:
        try:
            ser.close()
        except Exception:
            pass
    #raise NotImplementedError


if __name__ == "__main__":
    blink_led()
    check_to_input_button()
    blink_led_through_button()

    transmit_msg()
    receive_msg()
