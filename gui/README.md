# GUI

### General Goals
1. PyQt GUI with basic operations, camera feeds, and GPS with map readout
2. Record data from camera, GPS, and science system
3. Robot feedback

### GUI Components
- [ ] Intel RealSense camera feed
- [ ] USB camera feed(s)
- [ ] Timer
- [ ] Mode selector (stop, auto, teleop, etc.)
- [ ] GPS readout with waypoint marking, rover location, and zoom
- [ ] Save camera photo/video and gps coordinate
- [ ] Science readout
- [ ] Robot systems feedback information
- [ ] Data stream low latency mode for poor connections

### ROS Communication
#### Subscribers
- RealSense camera (/realsense_camera_0/color/image_raw/compressed)
- USB camera (/usb_camera_0/image_raw/compressed)
- GPS
- Robot systems feedback?

#### Publishers
- Mode
