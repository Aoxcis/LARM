#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

print("test_move :: START...")


class ROSTalker:
    def __init__(self, rosNode):
        self._publisher= rosNode.create_publisher( String, 'testTopic', 10 )
        self._timer = rosNode.create_timer(0.5, self.timer_callback)
        self._i = 0

    def timer_callback(self):
        velocity = Twist()
        # Feed Twist velocity values
        velocity.linear.x = 0.5
        # Publish 
        self._publisher.publish(velocity)

def infiniteTalk():
    # Initialize ROS node with ROS client
    rclpy.init()
    aNode= Node( "avance" )
    talker= ROSTalker(aNode)
    # Start infinite loop
    rclpy.spin_once(aNode)
    # Clean everything and switch the light off
    aNode.destroy_node()
    rclpy.shutdown()
# Execute the function.
if __name__ == "__main__":
    infiniteTalk()
