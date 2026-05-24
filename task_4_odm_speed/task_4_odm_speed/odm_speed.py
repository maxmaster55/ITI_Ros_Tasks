import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry


TIME_FREQ = 10 # Hz
TIME_PERIOD = 1/TIME_FREQ

class OdmSpeed(Node):
    def __init__(self):
        super().__init__("odm_speed")
        self.speed_pub = self.create_publisher(Odometry, "/odom", 10)
        self.timer = self.create_timer(TIME_PERIOD, self.timer_callback)
        self.x = 0.0
        self.msg = Odometry()
        self.msg.header.frame_id = "odom"
        self.msg.child_frame_id = "base_link"
        self.msg.pose.pose.orientation.w = 1.0
        self.msg.pose.pose.orientation.x = 0.0
        self.msg.pose.pose.orientation.y = 0.0
        self.msg.pose.pose.orientation.z = 0.0

    def timer_callback(self):
        msg = self.msg
        self.get_logger().info(f"speed: {msg.pose.pose.position.x}")
        msg.pose.pose.position.x = self.x
        self.x += 0.1
        self.speed_pub.publish(msg)
        self.msg.twist.twist.linear.x = TIME_FREQ * 0.1




def main(args=None):
    rclpy.init(args=args)
    node = OdmSpeed()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()
