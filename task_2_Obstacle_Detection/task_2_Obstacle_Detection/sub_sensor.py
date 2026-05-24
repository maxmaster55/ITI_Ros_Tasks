import random
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Bool


class SubSensor(Node):
    def __init__(self):
        super().__init__("SubSensor")
        self.get_logger().info("Subscriber node has been started.")
        self.subscription_ = self.create_subscription(
            Float32,
            '/sensor/distance',
            self.sensor_callback,
            10
        )
        self.cmd_pub= self.create_publisher(Bool, '/cmd/stop', 10)

    def sensor_callback(self, msg):
        self.get_logger().info(f"Received sensor data: Distance to obstacle = {msg.data:.2f} meters")

        stop_msg = Bool()
        if msg.data < 2:
            stop_msg.data = True
            self.cmd_pub.publish(stop_msg)
            self.get_logger().info("Obstacle detected within 2 meters! Publishing stop command.")

        else:
            stop_msg.data = False
            self.cmd_pub.publish(stop_msg)

def main(args=None):
    rclpy.init(args=args)
    node = SubSensor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
