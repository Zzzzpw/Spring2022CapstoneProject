import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import Twist


class VR_listener(Node):

    def __init__(self):
        super().__init__('VR_listener')
        self.subscription = self.create_subscription(
            Twist,
            'VR_talker',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg)


def main(args=None):
    rclpy.init(args=args)

    listener = VR_listener()

    rclpy.spin(listener)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    listener.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()