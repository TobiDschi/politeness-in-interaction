# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 15:30:57 2016

@author: Tobias
"""

import socket 
import time
import random
import csv
import re
from numpy.random import choice
import numpy

UDP_IP = socket.gethostbyname(socket.gethostname())
UDP_PORT = 8004 

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
conn.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST, 1) 
conn.bind((UDP_IP, UDP_PORT))
print('Serveraddress: ' + UDP_IP)

global ali_ula_points
ali_ula_points = 0
users = []
receivers = []
names = []
decision = ['yes','no']
value = [50, 100, 250, 500, 1000]
items = ['zuda', 'gupe', 'muyi', 'gisi', 'meba']  
requests = ['paho muzu', 'paho dumi']
markers = ['bu', 'so', 'na', 'te']
secondmarker = [' bu', '', ' so', '', ' na', '', ' te', '']


c = 0
         
def append_data_addr():
    global data, addr
    users.append(addr[0])

def receivers_append():
    global data, addr
    receivers.append(addr)
    
def establish_connection():
    global data, addr
    data, addr = conn.recvfrom(4096)
    try:
        data = data.decode()
    except TypeError:
        print('unknown type')
        data = ' ' 
    print(data)
    
def logout():
    global namepos
    name = str(names[namepos]) 
    users.remove(addr) 
    receivers.remove(addr) 
    names.remove(name) 
    sendback = name + ' withdrew from the experiment'
    sendback.encode()
    send(sendback)

def send(event):
    for i in receivers:
        addr = i
        try:
            conn.sendto(event, addr)
        except TypeError:
            event = event.encode()
            conn.sendto(event, addr)
        
def append_user():
    append_data_addr()
    receivers_append()
    names.append(data)
    sendback = str(data) + ' has joined the experiment.'
    sendback = sendback.encode() 
    send(sendback)
        
def start_experiment():     
    sendback = '\n Do you want to beginn with the experiment? (y/n) \n'
    sendback = sendback.encode()
    send(sendback)
    while True:
        establish_connection()
        response = data.lower()
        if response == 'y':
            names.append('ali')
            names.append('ula')
            offer_item()
            
def offer_item():
    global c
    c = c + 1
    if c > 20:
        end_experiment()
    else:
        global item
        item = random.choice(items)
        sendback = 'Paho wopudi ' + str(item) + ' gapi gipuko. Gipuko popudi 120 pidi. Hago paho gapi ruhu gipuko.' + '\n'
        sendback = sendback.encode()
        send(sendback)
        global probs
        probs = []
        global sentencecache
        sentencecache = []
        third_party_behaviour(item)
        time.sleep(1.3)
        fourth_party_behaviour(item)
        react_to_offer()
    
def react_to_offer():    
    timeout = time.time() + 120
    b = 0
    while True:
        establish_connection()
        if data:
            namepos_send()
            sentencecache.insert(namepos, data)
            b += 1
            if b == 2:
                time.sleep(1)
                give_object_accordingly(item) #upon changing this into give_object_accordingly() the experimental condition is changed into functional rather then decorative.
                break
            elif time.time() > timeout:
                sendback = '\n' + '120 pidi deyomu' + '\n'
                sendback.encode()
                send(sendback)
                time.sleep(1)
                offer_item()
            
def assess_statements():  
    index = 0
    for item in sentencecache:
        print(index)
        print(sentencecache)
        print(sentencecache[index])
        probs.append(100)
        posnumber1 = len(re.findall('\W[te]\w+', item))
        posnumber2 = len(re.findall('\W[na]\w+', item))
        negnumber1 = len(re.findall('\W[so]\w+', item))
        negnumber2 = len(re.findall('\W[bu]\w+', item))
        pos = (posnumber1 * 200) + (posnumber2 * 200)
        neg = (0.33 ** negnumber1) * (0.33 ** negnumber2)
        probs[index] = (1 + pos) * neg
        index = index + 1        
        te_vector()
        print(te_vector_list)
        na_vector()
        print(na_vector_list)
        so_vector()
        print(so_vector_list)
        bu_vector()
        print(bu_vector_list)         
    probs.append(aliprob)
    probs.append(ulaprob)
    
def give_object_accordingly(artifact):
    assess_statements()
    global getterlist
    getterlist = []    
    try:
        probindex = 0
        for i in names:
            prob = [probs[probindex], 100]
            print(probs)
            print(probs[probindex])
            probindex = probindex + 1
            yes_or_no = choice(decision, 1, p = convert_probs_to_1(prob))
            if yes_or_no == 'yes':
                getterlist.append(i)
                print('decision was yes')
            if yes_or_no == 'no':
                print('decision was no')
                time.sleep(0.01)
        sendback = 'Paho dumi gapi ' + artifact + ' ruhu ' + str(getterlist)
        sendback = sendback.encode()
        send(sendback)
        sendpoints(item)
        show_ali_ula_points(value[pointpos])
        write_to_csv(artifact)
        offer_item()
    except ValueError:
        print('Value Error, random distribution')
        give_object(artifact)
    
def convert_probs_to_1(probabilities):
    try:
        newprobabilities = [x / sum(probabilities) for x in probabilities]
        return newprobabilities
    except ZeroDivisionError:
        print('Zero Division Error, random distribution')
        give_object(item)
            
def ali_positive_strong():
    global aliprob
    aliprob = 200

def ali_positive_subtle():
    global aliprob
    aliprob = 200

def ali_negative_subtle():
    global aliprob
    aliprob = 33

def ali_negative_strong():
    global aliprob
    aliprob = 33        
        
def third_party_behaviour(artifact):
    time.sleep(3.7)
    rand_request = random.choice(requests)
    rand_marker = random.choice(markers)
    rand_secondmarker = random.choice(secondmarker)
    global aliphrase
    aliphrase = 'Ali mibo: ' + rand_request + ' ' + artifact + ' ' + rand_marker + rand_secondmarker
    if rand_marker == 'te':
        ali_positive_strong()
    elif rand_marker == 'na':
        ali_positive_subtle()
    elif rand_marker == 'so':
        ali_negative_subtle()
    elif rand_marker == 'bu':
        ali_negative_strong()
    sendback = aliphrase.encode()
    send(sendback)
    
def ula_positive_strong():
    global ulaprob
    ulaprob = 200

def ula_positive_subtle():
    global ulaprob
    ulaprob = 200

def ula_negative_subtle():
    global ulaprob
    ulaprob = 33

def ula_negative_strong():
    global ulaprob
    ulaprob = 33        
        
def fourth_party_behaviour(artifact):
    time.sleep(3.7)
    rand_request = random.choice(requests)
    rand_marker = random.choice(markers)
    rand_secondmarker = random.choice(secondmarker)
    global ulaphrase
    ulaphrase = 'Ula mibo: ' + rand_request + ' ' + artifact + ' ' + rand_marker + rand_secondmarker
    if rand_marker == 'te':
        ula_positive_strong()
    elif rand_marker == 'na':
        ula_positive_subtle()
    elif rand_marker == 'so':
        ula_negative_subtle()
    elif rand_marker == 'bu':
        ula_negative_strong()
    sendback = ulaphrase.encode()
    send(sendback)
        
def end_experiment():
    sendback = 'the experiment is now over'
    sendback.encode()
    send(sendback)
        
def give_object(artifact):
    global getterlist
    getterlist = []
    for i in names: 
        yes_or_no = random.choice(decision)
        if yes_or_no == 'yes':
            getterlist.append(i)
        if yes_or_no == 'no':
            time.sleep(0.01)
    sendback = '\n' + 'Paho dumi gapi ' + artifact + ' ruhu ' + str(getterlist)
    sendback = sendback.encode()
    send(sendback)
    sendpoints(item)
    write_to_csv(artifact)
    show_ali_ula_points(value[pointpos])
    time.sleep(3)
    offer_item()
    
def te_vector():
    global te_vector_list
    te_vector_list = []
    for item in sentencecache:
        te_vector_list.append(len(re.findall('\W[te]\w+', item)))

def na_vector():
    global na_vector_list 
    na_vector_list = []
    for item in sentencecache:
        na_vector_list.append(len(re.findall('\W[na]\w+', item)))
        
def so_vector():
    global so_vector_list 
    so_vector_list = []
    for item in sentencecache:
        so_vector_list.append(len(re.findall('\W[so]\w+', item)))
    
def bu_vector():
    global bu_vector_list 
    bu_vector_list = []
    for item in sentencecache:
        bu_vector_list.append(len(re.findall('\W[bu]\w+', item)))
    
def write_to_csv(artifact):
    with open('gamelog.csv', 'a') as csvfile:
        fieldnames = ['condition1', 'condition2', 'trial', 'player1', 'player2', 'player1winner', 'player2winner', 'player1_te_count', 'player1_na_count', 'player1_so_count', 'player1_bu_count', 'player2_te_count', 'player2_na_count', 'player2_so_count', 'player2_bu_count', 'artifact', 'player 1 phrase', 'player 2 phrase', 'aliphrase', 'ulaphrase']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writerow({'condition1' : 'non-competitive', 'condition2' : 'functional', 'trial' : str(c), 'player1': names[0], 'player2' : names[1],'player1winner' : player_winner(), 'player2winner' : player_winner(), 'player1_te_count' : str(te_vector_list[0]), 'player1_na_count' : str(na_vector_list[0]), 'player1_so_count' : str(so_vector_list[0]), 'player1_bu_count' : str(bu_vector_list[0]),'player2_te_count' : str(te_vector_list[1]), 'player2_na_count' : str(na_vector_list[1]), 'player2_so_count' : str(so_vector_list[1]), 'player2_bu_count' : str(bu_vector_list[1]), 'artifact' : artifact, 'player 1 phrase' : sentencecache[0], 'player 2 phrase' : sentencecache[1], 'aliphrase' : aliphrase, 'ulaphrase' : ulaphrase})
    
def player_winner():
    if users[0] and users[1] in getterlist:
        return 'yes'
    elif users[0] in getterlist:
        return 'yes'
    elif users[1] in getterlist:
        return 'yes'
    else:
        return 'no'
        
def show_ali_ula_points(pointvalue):
    if 'ali' in getterlist:
        global ali_ula_points
        ali_ula_points = ali_ula_points + pointvalue
        sendback = 'Ali Ula wopudi ' + str(ali_ula_points) + ' darone' + '\n'
    elif 'ula' in getterlist:
        global ali_ula_points
        ali_ula_points = ali_ula_points + pointvalue
        sendback = 'Ali Ula wopudi ' + str(ali_ula_points) + ' darone' + '\n'
    elif 'ali' and 'ula' in getterlist:
        global ali_ula_points
        ali_ula_points = ali_ula_points + pointvalue
        sendback = 'Ali Ula wopudi ' + str(ali_ula_points) + ' darone' + '\n'
    else:
        sendback = 'Ali Ula wopudi ' + str(ali_ula_points) + ' darone' + '\n'
    sendback = sendback.encode()
    send(sendback)
        
def sendpoints(artifact):
    global pointpos
    pointpos = items.index(item) 
    sendback = str(value[pointpos]) + ' darone pudoho ruhu ' + str(getterlist)
    sendback = sendback.encode()
    send(sendback)
    player1 = names[0]
    player2 = names[1]
    print(names)
    print(getterlist)
    if player1 in getterlist:    
        transfer_points(player1, value[pointpos])
        transfer_points(player2, value[pointpos])
    elif player2 in getterlist:
        transfer_points(player1, value[pointpos])
        transfer_points(player2, value[pointpos])
    elif player1 and player2 in getterlist:
        transfer_points(player1, value[pointpos])
        transfer_points(player2, value[pointpos])
    else:
        sendback = "Wosu darone pudoho ruhu gipuko" + '\n'
        sendback = sendback.encode()
        send(sendback)
    time.sleep(2)
        
def transfer_points(player, points):        
    try:
        playeraddr = names.index(player)
        points = str(points)
        points = points.encode()
        conn.sendto(points, receivers[playeraddr])
    except IndexError:
        sendback = "Wosu darone pudoho ruhu gipuko" + '\n'
        sendback = sendback.encode()
        send(sendback)
    
def namepos_send():
    global namepos
    namepos = users.index(addr[0]) 
    sendback = str(names[namepos]) + ' mibo: ' + data 
    sendback = sendback.encode() 
    send(sendback)
                                           
while True:
    establish_connection()
    a = users.count(addr[0]) 
    if a == 0:
        append_user()
    else:
        namepos_send()
        if a == 1:
            start_experiment()
