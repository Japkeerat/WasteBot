from picamera import PiCamera
import RPi.GPIO as GPIO
from time import sleep
import os
import socket
from PIL import Image


def server_connectivity(image_address):
	
	s = socket.socket()
	HOST = '192.168.43.254'
	port = 8000
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	client_socket.connect((HOST, port))
	
	file1 = open(image_address, 'rb')
	i=Image.open(image_address)
	i=i.resize((224,224))
	
	i.save("1.jpg")
	
	file1 = open("1.jpg", 'rb')
	
	#client.send(file1)
	fsize=os.stat("1.jpg").st_size
	print(fsize)
	client_socket.send(str(fsize).encode())
	l = file1.read(fsize)
	'''while (fsize>=1024):
		client_socket.send(l)
		fsize=fsize-1024
		l = file1.read(1024)
		print(".")
		
	print("sending")
	
	if(fsize<1024 and fsize>0):	
		l = file1.read(fsize)
		client_socket.send(l)'''
	client_socket.sendall(l)	
	'''while(l):
		
		l=file1.read(1024)
		print(".")'''
		
	print("Sent")
	prediction = client_socket.recv(1024).decode()
	print (prediction)
	client_socket.close()
	return prediction

def motor_controller(GPIO, classifier, angle=90, servoPIN=17, angle2 = 90, servoPIN2 = 18):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(servoPIN, GPIO.OUT)
	GPIO.setup(servoPIN2, GPIO.OUT)
	
	# elbow motor
	p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
	q = GPIO.PWM(servoPIN2, 50) # GPIO 17 for PWM with 50Hz
	p.start(0)
	q.start(0)
	duty = angle / 18
	duty += 2.5
	duty2 = angle2 / 18
	duty2 += 2.5
	if classifier is 1:
		while duty >= 5.0:
			duty -= 0.1
			p.ChangeDutyCycle(duty)
			sleep(0.05)
		sleep(0.5)
		
		while duty2 >= 2.5:
			duty2 -= 0.1
			q.ChangeDutyCycle(duty2)
			sleep(0.001)
		sleep(0.5)
		
		while duty2 <= 7.2:
			duty2 += 0.1
			q.ChangeDutyCycle(duty2)
			sleep(0.001)
		sleep(0.5)
		
		while duty <= 7.0:
			duty += 0.1
			p.ChangeDutyCycle(duty)
			sleep(0.05)
		
	elif classifier is 2:
		while duty <= 7.0:
			duty += 0.1
			p.ChangeDutyCycle(duty)
			sleep(0.05)
		sleep(0.5)
		
		while duty2 >= 2.5:
			duty2 -= 0.1
			q.ChangeDutyCycle(duty2)
			sleep(0.001)
		sleep(0.5)
		
		while duty2 <= 7.2:
			duty2 += 0.1
			q.ChangeDutyCycle(duty2)
			sleep(0.001)
		sleep(0.5)
	
	else:	
		while duty <= 9.0:
			duty += 0.1
			p.ChangeDutyCycle(duty)
			sleep(0.05)
		sleep(0.5)
		
		while duty2 >= 2.5:
			duty2 -= 0.1
			q.ChangeDutyCycle(duty2)
			sleep(0.001)
		sleep(0.5)
		
		while duty2 <= 7.2:
			duty2 += 0.1
			q.ChangeDutyCycle(duty2)
			sleep(0.0051)
		sleep(0.5)
		
		while duty >= 7.0:
			duty -= 0.1
			p.ChangeDutyCycle(duty)
			sleep(0.05)
	
	
	p.stop()
	q.stop()


def camera_controller(camera=None, name=None):
	if camera is None:
		camera = PiCamera()
	if name is None:
		name = 'x.jpg'
	else:
		name = str(name)+'.jpg'
	print ("camera")	
	camera.start_preview()
	sleep(1)
	camera.capture(name)
	camera.stop_preview()
	print ("re")
	return name


def sensor_controller(GPIO):
	sensor = x
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(sensor,GPIO.IN)
	if GPIO.input(sensor):
		return True
	return False

if __name__ == '__main__':
	name = 0
	try:
		camera = PiCamera()
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		
		while True:
			name += 1
			#if sensor_controller(GPIO) is True:
			image_file = camera_controller(camera=camera, name=name)
			response = server_connectivity(image_file)
			# elbow motor
			motor_controller(GPIO, classifier=int(response))
			# wrist motor
			#motor_controller(GPIO, 1, angle=90, servoPIN=20)
			sleep(5)
			
	except KeyboardInterrupt:
		GPIO.cleanup()
		print("Serviced {} images".format(name))
