# COMP-429-Distance-Vector-Routing

##### **Group Members: Michael Balian and Arin Deravanesian**

---

### Prerequisites Before Running Application

###### -First you must install python on your machine. You can visit the python website for instructions on how to install: https://www.python.org/downloads/

###### -After installation, you can verify that python has installed successfully by running this command:

```
python --version
or
python3 --version

Note: Depending on the version you installed you will either have to use python or python3 as shown above
```

###### -If python is not found when running the version command then you have to set the system environment variables to point to the python directory on machine.

###### -You can find more information on setting environmental variables in this article: https://docs.python.org/3/using/windows.html

---

### How To Run Chat Application

###### -Open a terminal and CD into the projects root directory

###### -Run the main.py file to start application:

```
python main.py
or
python3 main.py

Note: Depending on the version you installed you will either have to use python or python3 as shown above
```

---

### How to use the Chat Application

###### -Once you have ran the main.py you will be prompted to enter the start up command "server -t topology_file -i seconds"

###### -You define the nodes initial topology file in a txt file and pass it as the param for -t

###### -Lastly for the -i you pass the interval in seconds for updates to be sent to neighboring nodes

###### -If your topology file is in the correct format and the startup command has the correct syntax the node should now be up and ready to send and receive packets.

###### -For the client side you have the available commands at your disposal:

```
update <server id 1> <server id 2> - Update a link cost between to nodes.
step - Send routing update to neighboring nodes immediately rather then waiting for periodic routing updates defined at startup
packets - Display the number of distance vector packets this server has recieved since start up.
display - Display the nodes routing table
disable <server id> - Disable link between defined server and inputed server
crash - Crash the node
```

### Group member contributions

#### **Michael Balian**

###### I worked on the client side, starup of application, and routing updates of this application, my work consisted of:

###### -Read initial topology file at startup and initialize periodic routing updates for defined interval

###### -Distance vector algo implementation when the server receives a routing update from neighboring nodes

#### **Arin Deravanesian**

###### I worked on the server side of the application, my work consisted of:

###### -Create a server socket to listen for incoming connections and information from the client

###### -Also create a connectionSocket for every message that comes in from a client, after that messages is handled we then close that connection socket but we do not close the server socket

###### -Lastly parse messages from a client to check if it is a Ready, RoutingTable, or Disable message.

---

### Chat Application Demo

##### You can find a brief application demo on youtube:

###### https://youtu.be/WfQprvfdklQ
