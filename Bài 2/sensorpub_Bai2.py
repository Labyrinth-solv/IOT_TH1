"""Chuong trinh 1: Sensor Publisher
Mo phong cam bien IoT gui du lieu moi 3 giay len MQTT broker.

Cai dat:  pip install paho-mqtt
Chay:     python sensor_publisher.py
          python sensor_publisher.py --device sensor02
"""
import argparse
import json
import random
import time

import paho.mqtt.client as mqtt


def make_client():
    # Tuong thich paho-mqtt 1.x va 2.x
    try:
        return mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    except AttributeError:
        return mqtt.Client()


def main():
    parser = argparse.ArgumentParser(description="MQTT Sensor Publisher")
    parser.add_argument("--broker", default="localhost")
    parser.add_argument("--port", type=int, default=1883)
    parser.add_argument("--device", default="sensor01")
    parser.add_argument("--interval", type=float, default=3.0)
    args = parser.parse_args()

    topic = f"iot/lab/{args.device}/data"

    client = make_client()
    client.connect(args.broker, args.port, keepalive=60)
    client.loop_start()

    print(f"[{args.device}] Ket noi {args.broker}:{args.port}, topic: {topic}")
    try:
        while True:
            payload = {
                "device_id": args.device,
                "temperature": round(random.uniform(25.0, 38.0), 1),
                "humidity": round(random.uniform(30.0, 80.0), 1),
            }
            message = json.dumps(payload)
            client.publish(topic, message, qos=0)
            print(f"Da gui: {message}")
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\nDung publisher.")
    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()
