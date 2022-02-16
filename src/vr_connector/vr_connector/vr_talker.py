import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import Twist


class VR_talker(Node):

    def __init__(self):
        super().__init__('VR_talker')
        self.publisher_ = self.create_publisher(Twist, 'VR_talker', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 0.0
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 0.0

        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg)



def main(args=None):
    rclpy.init(args=args)

    talker = VR_talker()

    rclpy.spin(talker)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    talker.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()