#!/usr/bin/env python

```
파이썬에서는 #!으로 시작하는 라인을 Shebang 라인이라고 한다. Sharp(#) + Bang(!)의 합성어로 스크립트 파일의 첫줄에 사용되고 스크립트를 실행하는 데 사용되는 인터프리터를 지정한다. shebang이 들어가면 터미널에서 python을 붙이지 않고 바로 ./teacher.py 형태로 실행도 가능하다
```
import rospy
from std_msgs.msg import String

```
rospy 라이브러리를 import한다. rospy는 ROS에서 파이썬을 사용하기 위한 라이브러리이다.
std_msgs.msg 라는 ROS의 표준 패키지에서 String 부분을 가져와 사용하겠다는 의미이다. 더 여러개의 모듈을 가져올 수 있다

```

rospy.init_node('teacher')

#정수나 문자열을 선언하고 초기화하는 것 처럼 teacher라는 이름의 ROS노드를 선언하고 초기화

pub = rospy.Publisher('my_topic', String)

#my_topic 이라는 토픽에 string 메시지를 받아 발행하기 위해 Publisher 객체를 선언했다
#2번째 매개변수 String은 위에서 선언한 std_msgs.msg import String의 String이다

rate = rospy.Rate(2)

#발행 빈도를 2Hz로 설정하는 부분이다. 1초에 2번 반복할 수 있도록 rate 객체를 선언했다

while not rospy.is_shutdown(): #rospy가 종료되기 전까지 무한히 반복하면서
    pub.publish('call me please')
    rate.sleep()

#위에서 발행한 pub을 이용해 my_topic에 call me please 라는 문자열 메시지를 계속 발행한다
#위에서 호출한 rate 객체에 sleep()함수를 걸어줬다. 이는 while문이 종료되기 전까지 무한 반복되는 동안
#while 반복문 안에 rate.sleep()이 있기 때문에 0.5초에 한번씩 동작할 수 있도록 제어해주는 역할을 한다. 
