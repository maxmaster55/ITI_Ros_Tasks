# Session 11: Deep Dive into `nav2_params.yaml`

This document provides a line-by-line explanation of the `nav2_params.yaml` file used to configure the Nav2 stack for our TurtleBot3 (Waffle) simulation.

---

## 📍 1. AMCL Node (`amcl`)
The Adaptive Monte Carlo Localization node uses a particle filter to track the robot's pose on a 2D occupancy grid map.

| Parameter | Type | Default | Explanation |
| :--- | :--- | :--- | :--- |
| **`alpha1`** | float | `0.2` | Expected noise in odometry's rotation estimate from rotational motion. |
| **`alpha2`** | float | `0.2` | Expected noise in odometry's rotation estimate from translational motion. |
| **`alpha3`** | float | `0.2` | Expected noise in odometry's translation estimate from translational motion. |
| **`alpha4`** | float | `0.2` | Expected noise in odometry's translation estimate from rotational motion. |
| **`alpha5`** | float | `0.2` | Translation noise parameter (only used for omnidirectional robots). |
| **`base_frame_id`** | string | `"base_footprint"` | The coordinate frame of the robot's base. |
| **`beam_skip_distance`** | float | `0.5` | Distance threshold for ignoring range readings that don't match the map. |
| **`beam_skip_error_threshold`** | float | `0.9` | Ratio of beams that must fail match before we skip. |
| **`beam_skip_threshold`** | float | `0.3` | Minimum fraction of beams that must be skipped. |
| **`do_beamskip`** | bool | `false` | Enable/disable skipping laser beams that do not fit the map model. |
| **`global_frame_id`** | string | `"map"` | The frame published by the localization system. |
| **`lambda_short`** | float | `0.1` | Exponential decay parameter for the short-reading sensor model. |
| **`laser_likelihood_max_dist`** | float | `2.0` | Maximum distance to do obstacle lookup in likelihood field model. |
| **`laser_max_range`** | float | `100.0` | Maximum laser range to use; scan points beyond this are ignored. |
| **`laser_min_range`** | float | `-1.0` | Minimum laser range to use (negative value uses the scan message's minimum). |
| **`laser_model_type`** | string | `"likelihood_field"` | Laser sensor model algorithm: `"beam"` or `"likelihood_field"`. |
| **`max_beams`** | int | `60` | Number of evenly-spaced laser beams used to update the particle filter. |
| **`max_particles`** | int | `2000` | Maximum number of allowed particles in the filter. |
| **`min_particles`** | int | `500` | Minimum number of allowed particles in the filter. |
| **`odom_frame_id`** | string | `"odom"` | The coordinate frame of the odometry system. |
| **`pf_err`** | float | `0.05` | Target error between filter estimate and true distribution. |
| **`pf_z`** | float | `0.99` | Quantile probability of the target error. |
| **`recovery_alpha_fast`** | float | `0.0` | Exponential decay rate for the fast recovery average (helps recover from bad initialization). |
| **`recovery_alpha_slow`** | float | `0.0` | Exponential decay rate for the slow recovery average. |
| **`resample_interval`** | int | `1` | Number of filter updates before resampling the particles. |
| **`robot_model_type`** | string | `"nav2_amcl::DifferentialMotionModel"` | Motion model type: `"nav2_amcl::DifferentialMotionModel"` or `"nav2_amcl::OmniMotionModel"`. |
| **`save_pose_rate`** | float | `0.5` | Frequency (Hz) at which the last estimated pose is saved to parameters. |
| **`sigma_hit`** | float | `0.2` | Standard deviation for Gaussian model of hit laser beams. |
| **`tf_broadcast`** | bool | `true` | Whether to publish the transform between `map` and `odom`. |
| **`transform_tolerance`** | float | `1.0` | Time (seconds) to post-date published transforms to allow for lag. |
| **`update_min_a`** | float | `0.2` | Minimum rotational movement (radians) required before updating particles. |
| **`update_min_d`** | float | `0.25` | Minimum translational movement (meters) required before updating particles. |
| **`z_hit`** | float | `0.5` | Mixture weight of the standard hit distribution. |
| **`z_max`** | float | `0.05` | Mixture weight of the failed/out-of-range sensor readings. |
| **`z_rand`** | float | `0.5` | Mixture weight of random noise in the scan readings. |
| **`z_short`** | float | `0.05` | Mixture weight of short readings (e.g. dynamic obstacles). |
| **`scan_topic`** | string | `"scan"` | The topic from which laser scans are subscribed. |

---

## 🌲 2. BT Navigator Node (`bt_navigator`)
Orchestrates navigation tasks using Behavior Trees (BT).

| Parameter | Type | Default | Explanation |
| :--- | :--- | :--- | :--- |
| **`global_frame`** | string | `"map"` | The coordinate frame of the map coordinate system. |
| **`robot_base_frame`** | string | `"base_link"` | Base coordinate frame of the physical robot structure. |
| **`odom_topic`** | string | `"/odom"` | Topic name on which odometry information is published. |
| **`bt_loop_duration`** | int | `10` | Frequency limit (Hz) of Behavior Tree iterations. |
| **`default_server_timeout`** | int | `20` | Action server timeout limit in seconds. |
| **`wait_for_service_timeout`** | int | `1000` | Service call timeout in milliseconds. |
| **`action_server_result_timeout`** | float | `900.0` | Inactive action goal clean-up timeout. |
| **`navigators`** | list | `["navigate_to_pose", "navigate_through_poses"]` | Navigation tasks supported by this navigator node. |
| **`navigate_to_pose.plugin`** | string | `"nav2_bt_navigator::NavigateToPoseNavigator"` | Plugin class implementing single-goal pose routing. |
| **`navigate_through_poses.plugin`**| string | `"nav2_bt_navigator::NavigateThroughPosesNavigator"` | Plugin class implementing multi-waypoint navigation. |

---

## 🎮 3. Controller Server (`controller_server`)
Tracks the global path, running a local controller to compute velocity commands (`/cmd_vel`).

| Parameter | Type | Default | Explanation |
| :--- | :--- | :--- | :--- |
| **`controller_frequency`** | float | `20.0` | Execution rate (Hz) of the local controller loop. |
| **`costmap_update_timeout`** | float | `0.30` | Allowed latency (seconds) before costmap updates are considered stale. |
| **`min_x_velocity_threshold`** | float | `0.001` | Minimum X velocity below which the robot is considered stopped. |
| **`min_y_velocity_threshold`** | float | `0.5` | Minimum Y velocity threshold for holonomic robots. |
| **`min_theta_velocity_threshold`** | float | `0.001` | Minimum angular velocity below which the robot is considered stopped. |
| **`failure_tolerance`** | float | `0.3` | Allowed distance error before declaring controller failure. |
| **`progress_checker_plugins`** | list | `["progress_checker"]` | Array of progress checker plugin names. |
| **`goal_checker_plugins`** | list | `["general_goal_checker"]` | Array of goal checker plugin names. |
| **`controller_plugins`** | list | `["FollowPath"]` | Local planner plugins to follow. |
| **`use_realtime_priority`** | bool | `false` | Sets execution thread scheduling priority (POSIX RT). |

### 📈 MPPI Controller Plugin Parameters (`FollowPath`)
The MPPI (Model Predictive Path Integral) controller is the default local planner in Jazzy. It projects multiple possible trajectories using physics models to find the optimal velocity command.

| Parameter | Type | Default | Explanation |
| :--- | :--- | :--- | :--- |
| **`plugin`** | string | `"nav2_mppi_controller::MPPIController"` | Plugin class for path tracking controller. |
| **`time_steps`** | int | `56` | Simulation horizon steps for predictive planning. |
| **`model_dt`** | float | `0.05` | Time step duration (seconds) inside the simulation model. |
| **`batch_size`** | int | `2000` | Number of candidate trajectory samples evaluated in parallel. |
| **`ax_max` / `ax_min`** | float | `3.0` / `-3.0` | Maximum linear acceleration limits ($m/s^2$). |
| **`ay_max` / `ay_min`** | float | `3.0` / `-3.0` | Maximum lateral acceleration limits ($m/s^2$) for holonomic bases. |
| **`az_max`** | float | `3.5` | Maximum rotational acceleration limit ($rad/s^2$). |
| **`vx_std` / `vy_std` / `wz_std`** | float | `0.2` / `0.2` / `0.4` | Standard deviations for Gaussian velocity exploration. |
| **`vx_max` / `vx_min`** | float | `0.5` / `-0.35` | Velocity limits on the X axis ($m/s$). |
| **`vy_max`** | float | `0.5` | Lateral speed limit ($m/s$). |
| **`wz_max`** | float | `1.9` | Rotational speed limit ($rad/s$). |
| **`motion_model`** | string | `"DiffDrive"` | Robot chassis kinematics: `"DiffDrive"`, `"Omni"`, `"Ackermann"`. |
| **`critics`** | list | `[...]` | Evaluator functions used to score generated paths. |

---

## 🧱 4. Local Costmap (`local_costmap`)
Real-time cost representation in a rolling window around the robot.

| Parameter | Type | Default | Explanation |
| :--- | :--- | :--- | :--- |
| **`update_frequency`** | float | `5.0` | Rate (Hz) at which costmap cells are recalculated. |
| **`publish_frequency`** | float | `2.0` | Rate (Hz) at which visualization updates are published. |
| **`global_frame`** | string | `"odom"` | Coordinate reference frame of the costmap. |
| **`robot_base_frame`** | string | `"base_link"` | Origin coordinate frame of the robot's base. |
| **`rolling_window`** | bool | `true` | Moves the costmap grid as the robot moves. |
| **`width` / `height`** | int | `3` / `3` | Dimensions of the local costmap grid in meters. |
| **`resolution`** | float | `0.05` | Spatial resolution of costmap grid cell ($meters/cell$). |
| **`robot_radius`** | float | `0.22` | Collision bounding radius of circular robot structure (meters). |

---

## 🗺️ 5. Global Costmap (`global_costmap`)
Full environment cost representation computed using static maps and sensor layers.

| Parameter | Type | Default | Explanation |
| :--- | :--- | :--- | :--- |
| **`update_frequency`** | float | `1.0` | Cost recalculation frequency (Hz). |
| **`publish_frequency`** | float | `1.0` | Grid visualization message publish frequency (Hz). |
| **`global_frame`** | string | `"map"` | Coordinate frame of the global map structure. |
| **`track_unknown_space`** | bool | `true` | Dictates if unobserved cells are flagged as unknown or free space. |

---

## 🥞 5.1. Costmap Layers Explained
Nav2 uses a layered costmap system (derived from `costmap_2d`). Multiple layer plugins write values to a single master costmap.

### 💾 Static Layer (`nav2_costmap_2d::StaticLayer`)
- **Purpose**: Reads a pre-built static occupancy map (e.g. from the `/map` topic) and populates the master costmap with walls, furniture, and fixed structures.
- **Key attributes**: Static obstacles are represented with a cost value of `254` (Lethal).

### 📡 Obstacle Layer (`nav2_costmap_2d::ObstacleLayer`)
- **Purpose**: Subscribes to real-time 2D sensors (like `/scan` LaserScan) and writes new dynamic obstacles (people, boxes, chairs) into the costmap.
- **Clearing vs Marking**: 
  - **Marking**: If a laser beam hits something, it writes an obstacle at that cell.
  - **Clearing**: If a laser beam passes *through* a cell to hit something further away, the obstacle layer clears any previously marked obstacles in those intermediate cells (using ray tracing).
- **Parameters**:
  - `obstacle_max_range`: Distance limit within which the sensor can insert obstacles.
  - `raytrace_max_range`: Distance limit within which the sensor can clear obstacles.

### 📦 Voxel Layer (`nav2_costmap_2d::VoxelLayer`)
- **Purpose**: A 3D extension of the obstacle layer. Instead of a 2D grid, it maintains a 3D grid of voxels (volume pixels). Extremely useful when dealing with 3D LiDARs or RGB-D cameras to detect low obstacles (cables, table legs) or overhanging obstacles (tables).
- **Key attributes**: Automatically flattens the 3D voxel grid down to a 2D cost representation for the 2D path planner.

### 🎈 Inflation Layer (`nav2_costmap_2d::InflationLayer`)
- **Purpose**: Expands (inflates) the size of obstacles by a safety buffer to prevent the robot's physical chassis from hitting them. It translates the robot's footprint dimension into cost values.
- **Cost Falloff Profile**:
  - **Lethal Obstacle (254)**: The exact location of the obstacle.
  - **Inscribed Obstacle (253)**: Distance from obstacle is less than or equal to the robot's radius. The robot's center *cannot* enter this region without a collision.
  - **Inflated Cost (1-252)**: Distance is greater than the robot's radius but within the inflation buffer. Cost drops exponentially as distance increases, which encourages planners to stay in the center of corridors.
- **Parameters**:
  - `inflation_radius`: The distance threshold (meters) up to which obstacles are inflated.
  - `cost_scaling_factor`: Exponential decay factor. Increasing this makes the cost drop off *faster* (closer to obstacles), causing the robot to navigate closer to walls. Decreasing this makes cost drop off *slower*, keeping the robot strictly in the middle of open spaces.


---

## 🛣️ 6. Planner Server (`planner_server`)
Computes a global collision-free route using static costmaps.

| Parameter | Type | Default | Explanation |
| :--- | :--- | :--- | :--- |
| **`expected_planner_frequency`**| float | `20.0` | Expected rate (Hz) for planning requests. |
| **`planner_plugins`** | list | `["GridBased"]` | Array of path planner plugin names. |
| **`costmap_update_timeout`** | float | `1.0` | Timeout threshold for waiting on fresh costmap layers. |
| **`GridBased.plugin`** | string | `"nav2_navfn_planner::NavfnPlanner"` | Default Dijkstra/A* global path planner class. |
| **`GridBased.tolerance`** | float | `0.5` | Allowed destination target tolerance in meters if goal is blocked. |
| **`GridBased.use_astar`** | bool | `false` | If true, uses A* heuristics. If false, executes Dijkstra's search. |
| **`GridBased.allow_unknown`** | bool | `true` | If true, routes path through unmapped areas of the map. |

---

## 🌪️ 7. Recovery/Behavior Server (`behavior_server`)
Executes recovery behaviors (like clearing costmaps, backing up, spinning) when the robot gets stuck.

| Parameter | Type | Default | Explanation |
| :--- | :--- | :--- | :--- |
| **`local_costmap_topic`** | string | `"local_costmap/costmap_raw"`| Source topic for local grid queries. |
| **`global_costmap_topic`** | string | `"global_costmap/costmap_raw"`| Source topic for global grid queries. |
| **`cycle_frequency`** | float | `10.0` | Behavior control loop frequency (Hz). |
| **`behavior_plugins`** | list | `[...]` | Active recovery behavior plugins. |
| **`local_frame`** | string | `"odom"` | Odom coordinate frame for localized backup/spin movements. |
| **`global_frame`** | string | `"map"` | Global coordinate frame. |
| **`robot_base_frame`** | string | `"base_link"` | Frame ID of base link. |
| **`simulate_ahead_time`** | float | `2.0` | Time horizon (seconds) used to project safety of recovery motions. |
| **`max_rotational_vel`** | float | `1.0` | Speed ceiling ($rad/s$) during recovery rotations. |
| **`rotational_acc_lim`** | float | `3.2` | Angular acceleration limit ($rad/s^2$) during rotation. |

---

## 🚦 8. Waypoint Follower (`waypoint_follower`)
Manages the execution of a list of sequential navigation goals.

| Parameter | Type | Default | Explanation |
| :--- | :--- | :--- | :--- |
| **`loop_rate`** | int | `20` | Check rate (Hz) for evaluating waypoint completion status. |
| **`stop_on_failure`** | bool | `false` | Dictates if remaining waypoint list is aborted upon any waypoint failure. |
| **`action_server_result_timeout`**| float | `900.0` | Goal timeout before clearing server results. |
| **`waypoint_task_executor_plugin`**| string| `"wait_at_waypoint"` | Task execution class when arriving at a waypoint destination. |

---

## 🗺️ 9. Route Server (`route_server`)
Nav2 GPS-like routing node over spatial road network models.

| Parameter | Type | Default | Explanation |
| :--- | :--- | :--- | :--- |
| **`boundary_radius_to_achieve_node`**| float | `1.0` | Distance limit to mark spatial graph nodes as visited. |
| **`radius_to_achieve_node`** | float | `2.0` | Fallback radius threshold for routing logic. |
| **`smooth_corners`** | bool | `true` | Smooths sharp transitions between spatial graph route lines. |
| **`operations`** | list | `[...]` | Active plugins for route checking (speed limit overrides, collision checks). |

---

## 📊 10. Velocity Smoother (`velocity_smoother`)
Smooths velocity outputs from controllers to enforce physical robot dynamics and prevent jitter.

| Parameter | Type | Default | Explanation |
| :--- | :--- | :--- | :--- |
| **`smoothing_frequency`** | float | `20.0` | Interpolation loop frequency (Hz). |
| **`stamp_smoothed_velocity_with_smoothing_time`** | bool | `False` | Stamp `/cmd_vel` output header with calculation timestamp. |
| **`scale_velocities`** | bool | `False` | Scale translation/rotation proportionally if limits are hit. |
| **`feedback`** | string | `"OPEN_LOOP"` | Feedback system mechanism: `"OPEN_LOOP"`, `"CLOSED_LOOP"`. |
| **`max_velocity`** | list | `[0.5, 0.0, 2.0]` | Absolute speed limits: `[x_m_s, y_m_s, theta_rad_s]`. |
| **`min_velocity`** | list | `[-0.5, 0.0, -2.0]`| Reverse speed limits. |
| **`max_accel`** | list | `[2.5, 0.0, 3.2]` | Linear and angular acceleration limits. |
| **`max_decel`** | list | `[-2.5, 0.0, -3.2]`| Deceleration limit thresholds. |

---

## 🛡️ 11. Collision Monitor (`collision_monitor`)
Subscribes to `/cmd_vel` and uses laser scans to slow down or stop the robot if a crash is imminent.

| Parameter | Type | Default | Explanation |
| :--- | :--- | :--- | :--- |
| **`base_frame_id`** | string | `"base_footprint"` | The reference frame of the robot's base. |
| **`odom_frame_id`** | string | `"odom"` | Odometry coordinate frame. |
| **`cmd_vel_in_topic`** | string | `"cmd_vel_smoothed"` | Raw velocity input topic. |
| **`cmd_vel_out_topic`**| string | `"cmd_vel"` | Output topic passed to hardware or Gazebo simulator. |
| **`transform_tolerance`**| float | `0.2` | Frame transformation lookup tolerance (seconds). |
| **`source_timeout`** | float | `1.0` | Maximum sensor delay before declaring sensor data stale. |
| **`polygons`** | list | `["FootprintApproach"]` | Shapes used for boundary collision checks. |
| **`FootprintApproach.type`**| string| `"polygon"` | Zone geometric representation type. |
| **`FootprintApproach.action_type`**| string| `"approach"` | Action to take upon contact boundary overlap: `"stop"`, `"slowdown"`, `"approach"`. |
| **`FootprintApproach.time_before_collision`**| float| `1.2` | Projected time-to-collision window. |

---

## ⚓ 12. Docking Server (`docking_server`)
Handles automated charging station docking.

| Parameter | Type | Default | Explanation |
| :--- | :--- | :--- | :--- |
| **`controller_frequency`** | float | `50.0` | Control frequency during automated docking maneuvers. |
| **`initial_perception_timeout`**| float| `5.0` | Allowed search time for docking visual markers. |
| **`dock_approach_timeout`** | float | `30.0` | Timeout threshold for docking sequence completion. |
| **`dock_plugins`** | list | `['simple_charging_dock']` | Enabled docking mechanism plugins. |
| **`simple_charging_dock.staging_x_offset`**| float| `-0.7` | Staging position relative to docking frame origin. |

---

## 🔄 13. Lifecycle Manager (`lifecycle_manager`)
Orchestrates state transitions (Configure, Activate, Deactivate) of all Nav2 nodes to ensure safe startups.

| Parameter | Type | Default | Explanation |
| :--- | :--- | :--- | :--- |
| **`autostart`** | bool | `true` | Automatically configures and activates managed nodes on launch. |
| **`bond_timeout`** | float | `4.0` | Allowed delay (seconds) for node heartbeat signals before error. |
| **`node_names`** | list | `[...]` | Sequential ordered list of ROS 2 lifecycle nodes to be managed. |
