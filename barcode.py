import RPi.GPIO as GPIO
import time

# GPIOピンの設定
GPIO.setmode(GPIO.BOARD)

SENSOR1 = 11
SENSOR2 = 13
GPIO.setup(SENSOR1, GPIO.IN)  # IRセンサー1の入力ピン
GPIO.setup(SENSOR2, GPIO.IN)  # IRセンサー2の入力ピン

def linetrace():
    while True:
        if GPIO.input(SENSOR1) == GPIO.LOW and GPIO.input(SENSOR2) == GPIO.LOW:
            # 両方のセンサーでラインが検出された場合、適切な処理を行う
            print("両方のセンサーでラインが検出されました")
            # ロボットの動作を制御するためのコードを追加する

        elif GPIO.input(SENSOR1) == GPIO.LOW:
            # センサー1でラインが検出された場合、適切な処理を行う
            print("センサー1でラインが検出されました")
            # ロボットの動作を制御するためのコードを追加する

        elif GPIO.input(SENSOR2) == GPIO.LOW:
            # センサー2でラインが検出された場合、適切な処理を行う
            print("センサー2でラインが検出されました")
            # ロボットの動作を制御するためのコードを追加する

        else:
            # ラインが検出されなかった場合、適切な処理を行う
            print("ラインが検出されませんでした")
            # ロボットの動作を制御するためのコードを追加する

        time.sleep(0.1)  # 安定のための遅延

linetrace()

# GPIOピンのクリーンアップ
GPIO.cleanup()
