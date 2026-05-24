from ament_index_python.packages import get_package_share_directory
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
import time
import os
import csv

TIME_FREQ = 10 # Hz
TIME_PERIOD = 1/TIME_FREQ

pkg_path = get_package_share_directory('task_5_csv_playback')

class ImuPub(Node):
    def __init__(self):
        super().__init__("imu_pub")
        self.imu_pub = self.create_publisher(Imu, "/imu/data", 10)
        self.timer = self.create_timer(TIME_PERIOD, self.timer_callback)
        self.file = os.path.join(pkg_path, 'data', 'imu_data.csv')
        # Read the CSV file and store the data in a list
        self.data = []
        with open(self.file, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                self.data.append(row)
        
    def timer_callback(self):
        msg = Imu()
        msg.header.stamp = self.get_clock().now().to_msg()
        if self.data:
            row = self.data.pop(0)
            msg.orientation.w = float(row['orient_w'])
            msg.orientation.x = float(row['orient_x'])
            msg.orientation.y = float(row['orient_y'])
            msg.orientation.z = float(row['orient_z'])
            msg.angular_velocity.x = float(row['ang_x'])
            msg.angular_velocity.y = float(row['ang_y'])
            msg.angular_velocity.z = float(row['ang_z'])
            msg.linear_acceleration.x = float(row['acc_x'])
            msg.linear_acceleration.y = float(row['acc_y'])
            msg.linear_acceleration.z = float(row['acc_z'])
            self.imu_pub.publish(msg)
        else:
            self.get_logger().info("No more data to publish.")

        self.get_logger().info(f"Publishing IMU data: {msg}")


def main(args=None):
    rclpy.init(args=args)
    node = ImuPub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()
