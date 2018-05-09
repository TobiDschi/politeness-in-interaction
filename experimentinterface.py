# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 15:31:13 2016

@author: Tobias
"""


import socket #import networking functions
import time #importing time, so we can give our client some time to process information
from tkinter import * #imports the functions we need for our graphical interface
import _thread #imports threading, so various clients can connect to the server at the same time via an own thread each

UDP_PORT = 8004 #we define the port as being the same as on the server

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #and also define the connection through the socket just as in the case of the server

plyrscore = 0
scoredisplay = str(plyrscore)

def startthread(): #defines the function start thread 
    _thread.start_new_thread(receive, ()) #this enables every user to send and receive at the same time because there are different threads

def send(event): #here we define what has to happen when a client wants to send something
    global UDP_IP #first we set the IP global, so that the server has actually access
    print(UDP_IP)
    message = str(entry.get()) #then we define a message as a string that comes to the programm via the get method on "entry". this is defined later in the code as being everything that is written in the text window. so we have to get it from the text window.
    message = message.encode() #we encode the mesasge
    conn.sendto(message, (UDP_IP, UDP_PORT)) #and then send it to e correct ip and port
    entry.delete(0,END) #then the entry from the window has to be deleted as we need room for new messages

def receive(): #we define how the programm receives a message
    history = '' #we define the historial as to be empty
    time.sleep(0.1) #and then give the programm 0.2 seconds to just wait, this is actually important because otherwise the connection will not yet be opened, when we want to receive something and an OS error rises.
    while True: #loops
        data, addr = conn.recvfrom(4096) #data and address are defined to be received from the connection (the buffer rate is set to 4096)
        data = data.decode() #and we decodeeverything that comes through the connection (very different from python two where strings are sent through connections. python 3 however sends byte like objects which have to be decoded)
        history = history + '\n' + data #when ever something is received the history is going to be appended by new data
        textentry.config(state = NORMAL) #we than need to set the text entry window  open to print messages (down in the code is has been closed by default so only the server can print in it but never the user as such.)
        textentry.insert(END, (str(data) + '\n')) #we send the new historial to the window.
        textentry.config(state = DISABLED) #we than disable the entering of text in the window again since users should still not write in there.
        textentry.pack(fill = BOTH, expand = YES) #some cosmetics on the position of the text entry window.
        time.sleep(0.1)        #we then give it a pause again
        
def getserver(event): #how to get to the server
    global UDP_IP #the IP is set global to grant access
    UDP_IP = str(IPentry.get()) #and the programm gets the IP from the window that is designed to entry the ip
    time.sleep(0.1)
    name = str(nameentry.get()) #so is the name obtained from the corresponding window (how these are generated is described below)
    login.destroy() #after this has been done we want to destroy the window in which this was done
    startthread() #calls function 
    name = name.encode() #encodes message
    conn.sendto(name, (UDP_IP, UDP_PORT)) #sends name to the correct IP and port

def logout(): #if somebody puts "i quit" 
    message = '!I quit!'
    message = message.encode() #this message is encoded
    conn.sendto(message, (UDP_IP, UDP_PORT)) #then sent
    exptgui.destroy() #and the graphical user interface will be destroyed
    
login = Tk() #this creates the login window
login.geometry('300x150+400+400') #this sets the geometry of the loin windo
login.title('Experiment Login') #this gives the window a title
login.resizable(0,0) #this makes the window unrezisable, so it cannot be dragged to be bigger or smallers

IPtag = Label(login, text = 'Please type in the servers IP (ask team):', font = 'Arial') #this defines a message in the GUI namely, "type in the ip address"
IPtag.pack(side = TOP, fill = BOTH) #this sets the correct position for the text
IPentry = Entry(login) #this makes a little window in which you can put the ip
IPentry.pack(side = TOP, fill = BOTH) #and sets it to the right place
nametag = Label(login, text = 'please enter a nickname', font = 'Arial') #the same goes for the name
nametag.pack(side = TOP, fill = BOTH)
nameentry = Entry(login) #and for the window where to put the nae
nameentry.pack(side = TOP, fill = BOTH)
serverbutton = Button(login, font = 'Arial', text = 'Join Experiment!', command = getserver) #we than create a button that says "join experiment" and upon clicking calls the function "getserver" 
serverbutton.pack(side = TOP, fill = BOTH) #some cosmetics on the button
serverbutton.bind('<ButtonRelease-1>', getserver) #redundancy
nameentry.bind('<Return>', getserver) #this binds the function "getserver" to the return key, IF you are currently writing in the nickname entry window
login.mainloop() #this closes the mainloop for the login window and makes it constantly shown (until destroyed by calling the getserver method)

exptgui = Tk() #this is the actual interface for our chatroom
exptgui.geometry('650x600+400+400') #specify some geometry (namely how wide and long the window will be and where on the screen it will spawn)
exptgui.title('Experiment: Chat') #give it a name

textentry = Text(exptgui, width = 160, font = 'Arial') #this defines the reading window of the chatroom and what we can do in there
textentry.config(state = DISABLED) #and it says that you can NOT write in it: only the server will be able to write in it.
textentry.pack(fill = BOTH, expand = YES) #some cosmetics
entry = Entry(exptgui, width = 80) #and this is the window where you can actually enter some message
entry.pack(side = LEFT) #which is packed to the left

score = Label(exptgui, text = 'Score: ' + scoredisplay, font = 'Arial')
score.pack(side = LEFT, fill = BOTH)

sendbutton = Button(exptgui, width = 6, font = 'Arial', text = 'Send', command = send) #right from that you will find a button that says send and is linked to the function "send" which we defined higher
sendbutton.pack(fill = BOTH, side = RIGHT, expand = NO) #cosmetics
sendbutton.bind('<ButtonRelease-1>', send) #redundancy
entry.bind('<Return>', send) #and whilst you are writing in the entry window you will be able to just press the return button and send the mesage without actually clicking the button

exptgui.protocol('WM_DELETE_WINDOW', logout) #if the window of thechat is deleted, we will logout the person, so he doesn't go on in the chat although his window crashed
exptgui.mainloop() #and this closes the loop for the chatting environment and makes it appear.
