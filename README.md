# Random Quote Generator

A Python-based microservice capable of receiving requests for an inspirational quote through TCP connections set up via ZeroMQ after the user completes a challenge.

### How It Works

Microservice 1 runs as a server using ZeroMQ REP socket.

   * It listens for incoming value requests via a TCP server connection.
   * It sends back a random value depending on the request format of the sender.
   * Requests musts be made in valid string format.

### Request formats
As stated above, all requests must be in valid string format.

| Request  | Return/Action                      |
|----------|------------------------------------|
| One element == "Q"  | Break communication and shut down the server |
| One element != "Q" | A random string quote |

### Making a Request

1. Establish a ZeroMQ context object
2. Create a socket w/ the context & establish connection on the host and port with 'socket = context.socket(zmq.REQ)'
   * connection is currently set to target "tcp://localhost:55555"
3. Create a valid string object in a format listed in the table above.
4. Send the string quote via 'socket.send_json()'

#### Example Request
```python
import zmq

context = zmq.Context()

print("Connecting to server")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:55555")

socket.send_string("ChallengeName")
```
### Receiving a Response

After having received the request, assign a variable equal to 'socket.recv()'; it will generate a quote and send it back to the client.

#### Example of Receiving
```python
message = socket.recv()
print(f"{message.decode()}")
```

## UML

<img width="3086" height="2100" alt="image" src="https://github.com/user-attachments/assets/bd6d8fb6-f655-42e6-9785-672a5d428043" />


## Tech Stack

Python 3.13

ZeroMQ (pyzmq) — Microservice communication

### Author

Andrew Taylor & Nicole Nesbitt
