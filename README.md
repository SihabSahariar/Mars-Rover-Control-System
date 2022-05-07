# Control & Software (BRACU MONGOL-TORI) Team Research

All software in development. See [main repo](https://github.com/BRACU-DICHARI) for code deployed on the rover.

### GUI
1. PyQt GUI with basic operations, camera feeds, and GPS with map readout
2. Record data from camera, GPS, and science system
3. Robot feedback

### GPS
1. Map GPS waypoints
2. "Implement differential GNSS for higher accuracy"?
3. Find direct route between waypoints

### Autonomous Navigation
1. Simple "wall detection" using depth camera
2. SLAM
3. SLAM with Extended Kalman Filter (EKF)
4. Online route modification given obstacle avoidance algorithm, detected marker location, and gps waypoint locations

### ArUco Marker Detection
1. Detect marker in controlled environment
2. Use object detection to find approximate location of marker (may not be necessary)
3. Calculate distance to marker

### ROS
1. Control structure with all data streams
