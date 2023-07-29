import socket,cv2, pickle,struct
import img
import videoconversion
#import os
# create socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip = socket.gethostbyname(socket.gethostname()) 
port = 7099
client_socket.connect((host_ip,port)) 
data = b""
payload_size = struct.calcsize("Q")

while True:
	while len(data) < payload_size:
		packet = client_socket.recv(4*1024) # 4K
		if not packet: break
		data+=packet
	packed_msg_size = data[:payload_size]
	data = data[payload_size:]
	msg_size = struct.unpack("Q",packed_msg_size)[0]
	
	while len(data) < msg_size:
		data += client_socket.recv(4*1024)
	frame_data = data[:msg_size]
	data  = data[msg_size:]
	frame = pickle.loads(frame_data)
	img.start(frame)
	#frame = sample.start(frame)
	cv2.imshow("RECEIVING VIDEO",frame)
	key = cv2.waitKey(1) & 0xFF
	if key  == ord('q'):
		videoconversion.start()
		break
'''path = '.'
for f in os.listdir('.'):
	if f.endswith('jpg'):
		os.remove(f)'''
client_socket.close()