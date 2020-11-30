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
from std_msgs.msg import String

def main():
    rospy.init_node('tbm_pub_msg_node',anonymous=False)
    pub = rospy.Publisher('tianbot_mini/pub_msg',String,queue_size=10)
    while not rospy.is_shutdown():
        pub.publish("Hello TianbotMini Robot.")
        rospy.sleep(1)
    pass

if __name__ == '__main__':
    main()
