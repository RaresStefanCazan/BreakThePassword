import serial
import time
import random

port = "COM3" 
baud_rate = 115200

ser = serial.Serial(port, baud_rate, timeout=1)
time.sleep(2) 


alphabet = "9876543210qazwsxedcrfvtgbyhnmikolpQAZWSXEDCRFVTGBYHNUJOLP"


def generate_random(seed, a=4291010243, c=179203):
    seed = (a - seed * c) % 65536
    return seed / 65536.0, seed  


def generate_password(seed):
    password = ""
    for _ in range(64):
        rnd, seed = generate_random(seed)  
        password += alphabet[int(rnd * len(alphabet))]
    return password


found = False
attempts = 0

while not found:
    attempts += 1
    random_seed = random.randint(1, 65535)  
    #random_seed = random.randint(327670, 327690)
    #random_seed = 327680
    guessed_password = generate_password(random_seed)
    if(attempts % 100 == 0):
        print(f"Incercarea {attempts} cu seed {random_seed}: {guessed_password}")
        ser.write((guessed_password + "\n").encode())  

    time.sleep(0.1)  
    while ser.in_waiting > 0:
        response = ser.readline().decode().strip()
        if response == "TRUE":  
            print(f"Parola a fost gasita după {attempts} incercari: {guessed_password}")
            found = True
        elif response == "FALSE":
            pass 


ser.close()
