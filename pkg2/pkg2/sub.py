import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('detector_obstaculos')
        self.subscription = self.create_subscription(
            Float32,
            'distance',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        distancia = msg.data
        if distancia < 5.0:
            self.get_logger().warning(f'⚠ ALERTA! Obstáculo a {distancia:.2f} m')
        else:
            self.get_logger().info(f'Distancia segura: {distancia:.2f} m')

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()