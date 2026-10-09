import argparse
import json

import paho.mqtt.client as mqtt

TEMP_MAX = 35.0   # do C
HUMI_MIN = 40.0   # %


def make_client():
    try:
        return mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    except AttributeError:
        return mqtt.Client()


def main():
    parser = argparse.ArgumentParser(description="MQTT Monitoring Subscriber")
    parser.add_argument("--broker", default="localhost")
    parser.add_argument("--port", type=int, default=1883)
    parser.add_argument("--topic", default="iot/lab/sensor01/data")
    args = parser.parse_args()

    def on_connect(client, userdata, flags, rc, *extra):
        print(f"Da ket noi broker (rc={rc}). Subscribe: {args.topic}\n")
        client.subscribe(args.topic)  # subscribe lai neu bi mat ket noi

    def on_message(client, userdata, msg):
        try:
            data = json.loads(msg.payload.decode("utf-8"))
            device = data["device_id"]
            temp = float(data["temperature"])
            humi = float(data["humidity"])
        except (ValueError, KeyError, TypeError) as err:
            print(f"Payload khong hop le ({err}): {msg.payload!r}\n")
            return

        print(f"Device: {device}")
        print(f"Temperature: {temp:.1f} C")
        print(f"Humidity: {humi:.1f} %")
        if temp > TEMP_MAX:
            print("CANH BAO: Nhiet do cao")
        if humi < HUMI_MIN:
            print("CANH BAO: Do am thap")
        print("-" * 30)

    client = make_client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(args.broker, args.port, keepalive=60)

    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("\nDung subscriber.")
        client.disconnect()


if __name__ == "__main__":
    main()