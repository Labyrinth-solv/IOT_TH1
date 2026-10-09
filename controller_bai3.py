import paho.mqtt.client as mqtt
import time

BROKER = "broker.emqx.io"
PORT = 1883
CMD_TOPIC = "iot/lab/light01/cmd"
STATUS_TOPIC = "iot/lab/light01/status"

def on_connect(client, userdata, flags, rc):
    print("Đã kết nối thành công ứng dụng Controller.")
    client.subscribe(STATUS_TOPIC)

def on_message(client, userdata, msg):
    status = msg.payload.decode("utf-8")
    print(f"\nTrạng thái nhận được:\n{status}\n")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_start()
time.sleep(1)

print("ON: bật, OFF: tắt, EXIT: thoát")

while True:
    try:
        cmd = input("Nhập lệnh: ").strip().upper()
        
        if cmd == "EXIT":
            print("Đang thoát chương trình")
            break
        elif cmd in ["ON", "OFF"]:
            client.publish(CMD_TOPIC, cmd)
            print(f"Đã gửi lệnh {cmd} tới light01")
        else:
            print("Lệnh sai. Vui lòng chỉ nhập ON hoặc OFF.")
            
        time.sleep(0.5)
    except KeyboardInterrupt:
        break

client.loop_stop()
client.disconnect()