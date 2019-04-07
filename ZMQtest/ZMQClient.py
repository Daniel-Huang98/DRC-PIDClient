import sys
import zmq
from simple_pid import PID

pid = PID(0.99, 1.3, 0, setpoint=5)
port = "8888"
speed = 90
steering = 60

def SendSpeed(steering, speed): #servo and motor interface
    checksum = (70+36+steering+speed)%256 #calc 8bit checksum 
    ser.write((('F${}{}{}').format(chr(speed),chr(steering),chr(checksum))).encode('utf-8'))

ser = serial.Serial('/dev/ttyACM0'
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("starting PID Client")
socket.connect ("tcp://localhost:%s" % port)

if len(sys.argv) > 2:
    socket.connect ("tcp://localhost:%s" % port1)

topicfilter = "PIDData"
socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

# Process 5 updates
total_value = 0
val = 0
flag = 1

while(flag):
    string = socket.recv()
    topic, angle, flag = string.split()
    val = int(angle)
    control = pid(val)
    SendSpeed(control, speed)
    print (topic, messagedata)

ser.close()
print ("end loop")
