#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Developer: fanchewang (sunmaxwell@outlook.com)
# Date: 2020.11
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import rospy
from std_msgs.msg import ColorRGBA

def main():
    rospy.init_node('tbm_blink_node',anonymous=False)
    pub = rospy.Publisher('tianbot_mini/led',ColorRGBA,queue_size=10)
    while not rospy.is_shutdown():
        led = ColorRGBA()
        led.r = 64
        led.g = 0
        led.b = 64
        led.a = 5
        pub.publish(led)
        rospy.sleep(1)
        led.r = 0
        led.g = 0
        led.b = 0
        pub.publish(led)
        rospy.sleep(1)
    pass

if __name__ == '__main__':
    main()
