# BAI THUC HANH PYTHON VOI GIAO THUC MQTT - BAI 1

## 1. Thong tin sinh vien
- Ho ten: Lê Trung Đức
- Ma sinh vien: B23DCCN171

## 2. Gioi thieu
Chuong trinh mo phong giao tiep MQTT co ban bang Python, gom Publisher gui thong diep va Subscriber nhan thong diep thong qua MQTT Broker.

## 3. Moi truong
- Python 3.x
- Thu vien paho-mqtt
- MQTT Broker: broker.mqtt.cool
- Port: 1883
- Topic: iot/lab/message

## 4. Cai dat
Mo terminal tai thu muc du an va chay:
python -m pip install paho-mqtt

## 5. Cau hinh
Trong hai file publisher_bai1.py va subscriber_bai1.py, su dung cung broker va port:
BROKER = "broker.mqtt.cool"
PORT = 1883
TOPIC = "iot/lab/message"
Trong file publisher_bai1.py, cap nhat FULL_NAME va STUDENT_ID theo thong tin sinh vien.

## 6. Cach chay
Buoc 1: Mo terminal thu nhat va chay:
python subscriber_bai1.py

Buoc 2: Mo terminal thu hai va chay:
python publisher_bai1.py

Buoc 3: Nhan Enter de Publisher gui thong diep. Kiem tra terminal Subscriber de xem ket qua.
Nhap q trong Publisher hoac nhan Ctrl+C de dung chuong trinh.

## 7. Ket qua
- Publisher ket noi MQTT Broker thanh cong.
- Publisher gui thong diep len topic iot/lab/message.
- Subscriber nhan va hien thi topic, payload va thoi diem nhan.
- Ho tro gui nhieu thong diep lien tiep.