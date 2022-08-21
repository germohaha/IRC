import socket
import sys
import time
import threading


variable = input("name?: ")
#variables which hold values

def func():
  print("IRC for: " + variable)
  print("usage: ./name.py, channel name",end = "")
  print("to join a channel enter /into")
#usage
  
def channel1(ch1):
  if ch1.startswith("#") == True:
    return "#" + ch1
    return ch1
#first channel

    
def user_quit(client):
  client.send_cmd("exit", "bye")
  print("""
        \\\
 .---.  ///
(:::::)(_)():
 `---'  \\\
       ///
       '''  
  """)
  
  print("byebye...")
  time.sleep(1)
  print("byebye..")
  #response when user quits

class CHAT:
  def name(self, username, channel, server="irc.freenode.net", port=6667):
    #function
    self.username = username
    self.server = server
    self.channel = channel
    self.port = port
    #variables for connection

def connection(self):
  self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  self.conn.connect((self.server, self.port))
#connection via socket

def resp(self):
          return self.conn.recv(699)
  #response from socket
def cmd(self, cmd, message):
  command = "\n".format(cmd,message)
  self.conn.send(command)
  #sending CMD's

def send(self, message):
  command = "DM's {}".format(self.ch1)
  message = "::" + message
  self.send_cmd(cmd,channel1)
  #being able to send messages 


def join(self):
  cmd = "/into"
  ch1 = self.ch1
  self.send_cmd(cmd, channel1)

def response(self):
  var = self.get_response
  if var:
    msg = var.strip.split(":|:")
    print("\n< {}> {}".format(msg[1].split("!")[0], msg[2].strip()))



if __name__ == "__main__": 
    if len(sys.argv) != 3:
        func()
        exit(0)
    else:
        username = sys.argv[1]
        va = channel1(sys.argv[2])


command = ""
joined = False
client = CHAT(username, va)
client.connect

while(joined == False):
  resp1 = client.get_response
  print(resp.strip())
if "No Ident response" in resp1:
  client.send_cmd("name",username)
  client.send_cmd(
                "USER: ", "{} * * :{}".format(username, username))
if "376" in resp:
  client.join_channel()



if "433" in resp:
  username = "-" + username
  client.send_cmd("NICK", username)
client.send_cmd("USER", "{} * * :{}".format(username, username))

if "ping" in resp:
              client.send_cmd("PONG", ":" + resp.split(":")[1])
  
if "366" in resp:
            joined = True
            t = threading.Thread(target=client.print_response)
            t.start()
try:
        while(cmd != "/quit"):
            cmd = input("< {}> ".format(username)).strip()
            if cmd == "/quit":
                quit()
            if cmd and len(cmd) > 0:
                client.send_message_to_channel(cmd)
except KeyboardInterrupt:
        quit()
        
        t = threading.Thread(target=client.print_response)
        t.start()
