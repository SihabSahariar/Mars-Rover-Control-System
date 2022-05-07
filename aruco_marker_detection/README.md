# ArUco Marker Detection

### Challenge Description
#### URC
- Autonomous Navigation Mission
- GNSS coordinates provided for vicinity of 4 posts/gates (Accurate GNSS coordinates provided for first 4 posts/gates without tags)
- Must autonomously find posts/gates
- Posts: stop within 2 m
- Gates: drive between 2 m opening
- Tag physical description
    - 3-sided
    - 20x20 cm faces
    - 30-100 cm off ground
    - 4x4_50 tag library
    - 1 cell white border, cells are 2.5 cm across

#### CIRC
- Not mission specific
- Each marker ID will only appear once
- 4x4_50 tag library (0-49 range)
- Minimum size 5x5 cm
- Be able to detect number

### General Goals
1. Detect marker in controlled environment
2. Use object detection to find approximate location of marker (may not be necessary)
3. Search plan to find marker
4. Calculate distance to marker
