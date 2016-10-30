from mosquitto import
from serial import 
from random import



Board = serial ("/dev/cu.usbmodemfd111",9600, timeout=2)


client = mosquitto("Courtney090")

client.connect("10.212.62.136")

client.subscribe("/Lights")

def messageRecieved (broker, obj, msg):
    payload = msg.payload.decode()
    print("MESSAGE "+ msg.topic + " CONTAINING:" + payload)
    
    
    if (payload == "ON"):
        message= "1"
    if (payload == "OFF"):
        message= "0"
    board.write(message.encode())
    

    
client.on_message= messageRecieved


while (client !=None): client.loop()