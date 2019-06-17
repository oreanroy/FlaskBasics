Basics of Websockets


Internet Porotocol Suite

{ Application Layer }     [ HTTP, Websockets, SSL, IMAP, POP ]
{ InternetLayer }         [ ipv4, ipv6 ]
{ Transport Layer }       [ TCP, UDP ]

The TCP takes care of amking sure all packages reach the destination unaffected and in proper oder
The UDP is used for streaming videos and other similar tasks

HTTP is a  stateless protocol that is the present state is not depend on 

{ HTTP is sateless 
	After the initial request is done, the server-client communication is lost. }

{ Clients specify actions .
	GET / POST / PUT / DELETE }

{ Data sent with headers 
	Headers sent with request  AND response }


{ AJAX
	asynchronously send data to server without refreshing
	request->
	____________________________________________________
					        <- Response
	
	request -> 
Client	___________________________________________________  Server
					        <- Response
      
	request ->
	____________________________________________________
						<- Response

	can countinue to send data and make request after conection }


## WebSockets

	{ Full-duplex bi-directional Communication! }

	// To switch to websockets you send a header that you wana shift over to websocket
	// it uses the same tcp conection that was originaly established
	// no headers in socket requests( only sent during initial handshake)
	// 
	{ webSockets is a HTTP upgrade!
		uses the same TCP connection over ws:// or wss:// }
	{ Easy to implement and standardised! }
	{ Only sends headers once! }

// caniuse.com check browser compatability 

// Alternative to Websockets

## Polling and long Polling 

	{ Alternative to WebSockets 
		Much better backwards compatibillity! }

	{ Polling 
		Send AJAX request every x amount of seconds for new data
		(not real time) }
	{ Long Pollig
		Send request to server and keep connection open untill new data }

## Server sent Events
	
	{ Another "real-time" alternative 
		Uses EventSource API to send messages from server 
		Not truly bi-directional }

	{ Generally requires an event loop }
	
	{ No binary message capability }

## Intended Use case
	
	{ WebSockets not==replacement for HTTp
		WS is an upgrade for HTTP.
		HTTP provides automatic caching
		WS often needs special configuration for load balancing
		cant communicate with REST }
	{ Use when You need full-duplex connection
		Useful web-based games, chatting application,anything 
		which needs low-latency realtime connection! } 

## WebSockets CLients
	
	{ USed to interface with WebSocket Servers 
	// The Js file that i fetched in script in chat app sort of cdn
		Bulit in many languages(including python) }
	{ Most common client is web based and uses javascript }
	{ Require the server to be able to interface WS }

## Websocket clientside code
	
	const socket = new WebSocket('ws://localhost:8000');

	// this fucntion is called when socket is connected
	socket.onopen = (event) => {
	//on connection, do something..
	socket.send("hi hi connectd me "); // sending the string to server
	});

	//This is called when the server sends back something
	
	socket.onmessage = (event) => {
	// message from server
	console.log(event.data);
	});


## SocketIO
 	Makes the native socket makes then nicer and easier to use
	it has certain fallback mechanish. Like if a server and client do 
	not agree on a handshake it can fallback to long polling
	
	{ Javascript library for manupulating WebSockets
		includes fallback mechanism and auto-reconnection }
	{ Hndles disconnection and connection events }
	{ Namespacing and Room broadcasting } // group of clients to talk to 

	
	## clinet side code of socket.io
	
	var socket = io("http://localhost:8000/<MY_NAMESPACE>');

	//this connects to the socket server
	socket.on('connect', () => {
	  socket.emit('event_on_my_server', data="new conection");
	});
	
	// custom made events can be sent
	socket.on('my_custom_event', (data) => {
	  // do something
	});
 
## Python Servers w/WebSockets

{ SocketIO
	with python-socketio:
		flask, Tornado, Pyramid, Bottle, Sanic, AioHTTP, Tornado }
{ Native webSockets
	out of the box
		sanic,AioHTTP,Tornado
		with library
			Flask,Django(Channels 2.0), Bottle }



## Native sockets in flask
	
	// import setup application above
	
	socket = Sockets(app)
	
	@socket.route('/my_sockets')
	def my_socket_event(WS):
	  while not ws.closed:
	    message = WS.receive()
	    ws.send(message)
## SocketIO Server
	// you can use custom events and can send to mutliple people that is to a groups
	//import setup application above
	socket = socketio.Server()

	@socket.on('my custom event', namespace='/pycon')
	def custom_event(session_id, data):
	  // do stuff with data from client, send to all connected tp 'Pycon'
	  socket.emit('my event on the server', data, broadcast = True)

	app = socketio.Middleware(socket, app)
	# start server below

## Performance comparision

	{ HTTP and websockets have same sized header } // socket only sends its once
	{ 2bytes/msgoverhead } // for other messages unlike 
	{ SocketIO increaes latency and initial conection
	   uder the hood starts:
             uses AJAX long Polling initialy and then upgrades }	
