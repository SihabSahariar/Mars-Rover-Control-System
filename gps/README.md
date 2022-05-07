# GPS

- [Data Sheet](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-ultimate-gps.pdf)
- [ROS Diver](http://wiki.ros.org/nmea_navsat_driver)

### Connection:
| GPS | Jetson Nano |
|--|--|
|3.3 V | 3.3 V|
| GND | GND |
| TX | PIN 10 |
| RX | PIN 8 |

### Commands:

```
# install ROS driver
sudo apt install ros-melodic-nmea-navsat-driver

# temporarily allow r/w permissions to GPIO rx and tx pins on Jetson Nano
# more info: https://forums.developer.nvidia.com/t/read-write-permission-ttyths1/81623
sudo chmod 666 /dev/ttyTHS1

# run
rosrun nmea_navsat_driver nmea_serial_driver _port:=/dev/ttyTHS1 _baud:=9600
```

# IMU

- [Data Sheet](https://learn.adafruit.com/adafruit-bno055-absolute-orientation-sensor/overview)
- [ROS Driver](http://wiki.ros.org/ros_imu_bno055)
- [USB to UART TTL cable](https://www.amazon.com/PL2303-PL2303HX-Cable-Module-Converter/dp/B07ZCP3PPR)

### Connection:
| IMU | USB to UART TTL |
|--|--|
| Vin | Red |
| GND | Black |
| SDA/TX | White |
| SCL/RX | Green |

_for UART mode:_

| IMU | IMU |
|--|--|
| PS1 | Vin |

### Commands:

```
# install ROS driver and dependencies
# see: http://wiki.ros.org/ros_imu_bno055

# allow r/w for ttyUSB0 (restart after)
sudo usermod -a -G tty yourname
sudo usermod -a -G dialout yourname

# run
roslaunch ros_imu_bno055 view_imu.launch
```
