# first of all import the socket library
import socket			

# next create a socket object
s = socket.socket()		
print ("Socket successfully created")


port = 12345		

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))		
print ("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(5)	
print ("socket is listening")		

# a forever loop until we interrupt it or
# an error occurs
while True:

# Establish connection with client.
 c, addr = s.accept()	
 print ('Got connection from', addr )

# send a hello to the client. encoding to send byte type.
 msg=input('enter the message:\n')
 c.send(msg.encode())

# Close the connection with the client
 c.close()

# Breaking once connection closed
 break