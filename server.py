import socket, cv2, pickle,struct,imutils
import facerec
import img
#import videoconversion
import os
# Socket Create
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name  = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:',host_ip)
port = 7099
socket_address = (host_ip,port)

# Socket Bind
server_socket.bind(socket_address)

# Socket Listen
server_socket.listen(5)
print("LISTENING AT:",socket_address)

# Socket Accept
while True:
	client_socket,addr = server_socket.accept()
	print('GOT CONNECTION FROM:',addr)
	if client_socket:
		vid = cv2.VideoCapture(0)
		#facerec.start()
		#face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades  + "haarcascade_frontalface_default.xml")
		while(True):
			'''_,frame = vid.read()
			frame = imutils.resize(frame,width=640)
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			faces= face_cascade.detectMultiScale(gray, 1.3, 5)
			for (x, y, width, height) in faces:
				cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 3)'''
			frame = facerec.start(vid)
			#img.start(frame)
			a = pickle.dumps(frame)
			message = struct.pack("Q",len(a))+a
			client_socket.sendall(message)
			
			cv2.imshow('TRANSMITTING VIDEO',frame)
			key = cv2.waitKey(1) & 0xFF
			if key ==ord('q'):
				#videoconversion.start()
				'''for f in os.listdir('.'):
					if f.endswith('jpg'):
						server_socket.sendto(f, addr)'''
				client_socket.close()
				break
	vid.release()
	cv2.destroyAllWindows()
	exit
