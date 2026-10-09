import paho.mqtt.client as mqtt
import json

BROKER = "broker.emqx.io"
PORT = 1883
CMD_TOPIC = "iot/lab/light01/cmd"
STATUS_TOPIC = "iot/lab/light01/status"
DEVICE_ID = "light01"

# mặc định
current_status = "OFF"

def on_connect(client, userdata, flags, rc):
    print(f"[{DEVICE_ID}] Đã kết nối tới broker, đang lắng nghe lệnh")
    client.subscribe(CMD_TOPIC)

def on_message(client, userdata, msg):
    global current_status
    command = msg.payload.decode("utf-8").strip().upper()
    print(f"\n[{DEVICE_ID}] Nhận lệnh điều khiển: {command}")
    
    if command in ["ON", "OFF"]:
        current_status = command
        status_payload = {
            "device_id": DEVICE_ID,
            "status": current_status
        }
        client.publish(STATUS_TOPIC, json.dumps(status_payload))
        print(f"[{DEVICE_ID}] Đã cập nhật đèn thành {current_status} và gửi trạng thái phản hồi.")
    else:
        print(f"[{DEVICE_ID}] Lệnh không hợp lệ (Chỉ nhận ON/OFF).")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_forever()