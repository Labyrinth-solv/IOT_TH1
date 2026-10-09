
import time
import paho.mqtt.client as mqtt

BROKER = "broker.mqtt.cool"
PORT = 1883
TOPIC = "iot/lab/message"

FULL_NAME = "Le Trung Duc"  # Thay bằng họ tên của bạn
STUDENT_ID = "B23DCCN171"   # Thay bằng mã sinh viên của bạn


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Publisher da ket noi MQTT Broker")
    else:
        print(f"Ket noi that bai: {reason_code}")


client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="publisher_bai1"
)
client.on_connect = on_connect

try:
    client.connect(BROKER, PORT, 60)
    client.loop_start()

    # Cho den khi ket noi thanh cong
    for _ in range(50):
        if client.is_connected():
            break
        time.sleep(0.1)

    if not client.is_connected():
        raise TimeoutError("Khong the ket noi MQTT Broker")

    while True:
        message = f"Xin chao tu client Python MQTT - {STUDENT_ID} - {FULL_NAME}"
        info = client.publish(TOPIC, message, qos=1)
        info.wait_for_publish(timeout=5)

        if info.is_published():
            print(f"Da gui message: {message}")
        else:
            print("Chua xac nhan gui message thanh cong")

        choice = input("Nhan Enter de gui tiep, nhap q de thoat: ")
        if choice.strip().lower() == "q":
            break

except (OSError, TimeoutError) as e:
    print(f"Loi ket noi: {e}")
except KeyboardInterrupt:
    print("\nPublisher da dung.")
finally:
    client.loop_stop()
    client.disconnect()
