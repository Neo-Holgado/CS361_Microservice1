import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
socket.send_string("Find the treasure")
message = socket.recv()
print(f"{message.decode()}")
socket.send_string("Q")
