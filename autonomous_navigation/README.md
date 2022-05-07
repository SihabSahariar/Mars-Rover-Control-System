# Autonomous Navigation

### Basics

1. Mapping
    - Intel RealSense d435i depth image
    - Generate map of immediate surroundings
2. Localization
    - Global: GPS
    - Local: IMU
    - Possibly fuse with EKF
3. Goal detection
    - Course: GPS waypoints
    - Fine: ArUco Marker Detection
    - Goals are represented on a 2D occupancy grid
4. Obstacle detection
    - Detected obstacles added to occupancy grid
5. Path planning
    - Field D* algorithm to navigate occupancy grid
6. Control
    - Velocity vector


### Resources

- [Code example](https://github.com/ArghyaChatterjee/gps-waypoint-based-autonomous-navigation-in-ros)
- [Paper example 1](http://article.nadiapub.com/IJCA/vol7_no12/32.pdf)
- [Paper example 2](https://arxiv.org/pdf/2108.12571.pdf)
- [ROS- Gmapping](http://wiki.ros.org/gmapping): SLAM + 2D occupancy grid generation (may not work without laser scanner)
- [ROS- Move](http://wiki.ros.org/move_base)
- [RealSense Occupancy Grid Generation](https://github.com/IntelRealSense/realsense-ros/tree/occupancy-mapping/occupancy)
- [robot_localization package for gps+imu, includes EKF](http://docs.ros.org/en/noetic/api/robot_localization/html/index.html)
- [Simple example of robot_localization ROS package](https://github.com/nickcharron/waypoint_nav)
- [costmap_2d](http://wiki.ros.org/costmap_2d)

### Notes

- Need tf for robot frame, camera, and map
- Alternative plan: do breadth-first search on the world, optimal solution guaranteed!


## Localization

- Frame: 
    - map -> odom -> base_link
    - odom -> base_link: continuous senors
    - map -> odom: discrete sensors
