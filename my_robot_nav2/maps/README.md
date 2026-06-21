# Maps Directory

Place your saved maps here.

## How to save a map after SLAM

After driving the robot around and building a map with `slam.launch.py`, run:

```bash
ros2 run nav2_map_server map_saver_cli -f ~/my_map
```

This will create two files (`~/my_map.pgm` and `~/my_map.yaml`). 

To copy them to your package folder:
```bash
cp ~/my_map.* src/my_robot_nav2/maps/
```

Then rebuild the package so the map is installed:
```bash
colcon build --packages-select my_robot_nav2
source install/setup.bash
```

## Running navigation with the saved map

```bash
ros2 launch my_robot_nav2 nav2_simulation.launch.py map:=$(ros2 pkg prefix my_robot_nav2)/share/my_robot_nav2/maps/my_map.yaml
```
