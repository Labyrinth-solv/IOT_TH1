
from datetime import datetime
import paho.mqtt.client as mqtt

BROKER = "broker.mqtt.cool"
PORT = 1883
TOPIC = "iot/lab/message"


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Subscriber da ket noi MQTT Broker")
        client.subscribe(TOPIC, qos=1)
        print(f"Dang lang nghe topic: {TOPIC}")
    else:
        print(f"Ket noi that bai: {reason_code}")


def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    received_time = datetime.now().strftime("%H:%M:%S")

    print("\nNhan duoc message:")
    print(f"Topic: {msg.topic}")
    print(f"Payload: {payload}")
    print(f"Time: {received_time}")


client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="subscriber_bai1"
)
client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect(BROKER, PORT, 60)
    print("Dang ket noi va cho message...")
    client.loop_forever()
except (OSError, TimeoutError) as e:
    print(f"Loi ket noi: {e}")
except KeyboardInterrupt:
    print("\nSubscriber da dung.")
finally:
    client.disconnect()
