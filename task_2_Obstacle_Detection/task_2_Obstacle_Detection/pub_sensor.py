import random
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


TIMER_FREQ = 10.0  # Hz
TIMER_PERIOD = 1.0 / TIMER_FREQ  # seconds

class PubSensor(Node):
    def __init__(self):
        super().__init__("PubSensor")
        self.get_logger().info("Publisher node has been started.")
        self.publisher_ = self.create_publisher(Float32, '/sensor/distance', 10)
        self.timer = self.create_timer(TIMER_PERIOD, self.publish_sensor_data)

    def publish_sensor_data(self):
        distance = random.uniform(0.03, 5.0)
        self.get_logger().info(f"Publishing sensor data: Distance to obstacle = {distance:.2f} meters")
        msg = Float32()
        msg.data = distance
        self.publisher_.publish(msg)



def main(args=None):
    rclpy.init(args=args)
    node = PubSensor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
