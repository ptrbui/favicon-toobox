# Favicon Adjustment Tools

## About
This project was created with the goal of simulating a simple networking system that uses both TCP and UDP for transport 
layer protocols in C++. For better visualization and understanding, I used a dorm room booking system as a model. Clients
can log in as a member or a guest, and can query different types of rooms. Each different kind of room, single rooms, doubles, 
or suites have their own designated backend server. Logic and routing is done at the main server.

User information such as their usernames and passwords are encrypted during transport for security. For information about
the encryption scheme, see the encrypt() and decrypt() methods in client.cpp and serverM.cpp, where encryption is handled.


## Adding a Transparent Border
### `add-transparent-border.py`

The main server, also known as ServerM, is the intermediate server between the client and backend server. The main server 
communicates to clients using TCP, and to backend servers with UDP. The purpose of the main server is to verify the 
identities of users who don't log in as a guest. The main server forwards queries to their appropriate backend servers, 
and also handles invalid or error requests. The main server also has the ability to decrypt username and password so that 
they can be displayed on the main terminal.


## Changing The Color of a PNG Favicon
### `change-non-transparent-pixels.py`

The backend servers act as a database for the availability of dorm rooms. They report back to the main server, specifying 
information about rooms such as whether they exist, if they're available, or unavailable. The backend servers only communicate 
with the main server, and do so through UDP connections.


## Basic Favicon Generation
### `generate-shapes.py`

The client server handles requests from users. They accept queries from users, and are sent directly to the main server. 
Queries contain usernames, passwords, the type of query (i.e. Availability or Reservation), and room number. This information 
is sent to the main terminal, where most of the logic is done. Once processed, the main server will be sent back to and 
received by the client, where the response is then displayed.

