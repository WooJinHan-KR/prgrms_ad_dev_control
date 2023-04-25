#!/usr/bin/env python

import rospy
from std_msgs.msg import String

```
teacher.py에서 설명한 바와 같이 첫번째 줄은 스크립트가 파이썬 인터프리터를 사용해 실행할 수 있도록 하는
shebang라인이다. python을 붙이지 않고 ./student.py 와 같은 명령만으로도 실행시킬 수 있다
ROS 노드를 파이썬 코드로 생성하고 통신할 수 있도록 하는 라이브러리를 import하고
ROS 표준 메시지 패키지 std_mgms에서 문자열 타입인 String 메시지 타입을 가져오도록 하는 라인이다
```

def callback(msg):
    print msg.data

# def는 함수를 선언하고 정의할때 쓰는 용어다. callback이라는 함수를(msg)라는 매개변수를 가지고 있는 채로 선언했다
#이 함수는 callback(msg)형태로 사용하는데 msg에 들어온 값을 print(출력) 한다
    
rospy.init_node('student')

#teacher.py와 같이 student라는 이름의 ROS 노드를 선언하고 초기화 해준다. 다른 노드와 통신하기 위함이다

sub = rospy.Subscriber('my_topic', String, callback)

#my_topic에 대해서 구독자를 생성하고 String 타입의 메시지를 받아 callback 함수를 호출한다
#그리고 구독자의 인스턴스는 sub에 저장이 되며 토픽(메시지)를 받을 때 마다 callback함수가 호출된다

rospy.spin()

#rospy.spin()함수는 노드가 종료될 때까지 메시지를 계속 받고 callback 함수를 호출하는 무한 루프를 생성한다
#rospy.sleep()과 유사할 수 있는데 이 함수는 spin()과 다르게 특정한 시간동안만 동작한다는 부분이다
