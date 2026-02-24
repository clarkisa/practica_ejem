import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32

import random
class My_publisher(Node):

    def __init__(self):
        super().__init__('ultrasonic_publisher')
        self.publisher_ = self.create_publisher(Float32, 'distance', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Float32()
        msg.data = random.uniform(0.0, 10.0) 
        self.publisher_.publish(msg)
        self.get_logger().info(f'Distancia publicada: {msg.data:.2f}')



def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = My_publisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()