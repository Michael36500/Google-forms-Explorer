import requests
import random
from tqdm import tqdm
import time
import threading
#need to check 1 133 827 315 385 150 725 554 176 combinations


def forms(iteration):
    list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
    print
    for a in range(iteration, 1133827315385150725554176, 10):
        
        print(a)
        web = str(list[random.randint(0,61)]) + str(list[random.randint(0,61)]) + str(list[random.randint(0,61)]) + str(list[random.randint(0,61)]) + str(list[random.randint(0,61)]) + str(list[random.randint(0,61)]) + str(list[random.randint(0,61)]) + str(list[random.randint(0,61)]) + str(list[random.randint(0,61)]) + str(list[random.randint(0,61)]) + str(list[random.randint(0,61)]) + str(list[random.randint(0,61)]) + str(list[random.randint(0,61)]) + str(list[random.randint(0,61)]) + str(list[random.randint(0,61)]) + str(list[random.randint(0,61)]) + str(list[random.randint(0,61)])

        response = requests.get('https://forms.gle/{}'.format(web))
        if response.status_code == 200:
            print(web)



driverThreads = []

for j in range(10):
    #Add thread to the list
    driverThreads.append(threading.Thread(target=forms, args=(j)))

#Start all threads
for i in driverThreads:
    try:
        imgType = i._kwargs.get("imgType")
        iteration = i._kwargs.get("iteration")+1
        print(f"Starting Thread, Type {imgType}, Iteration {iteration}")
        i.start()
    except:
        print("ASD")
        pass
    # time.sleep(5)

#Wait for the end of all threads
for i in driverThreads:
    i.join()
