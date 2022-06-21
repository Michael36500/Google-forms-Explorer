import test2 as ts
import threading
import time

#List of driver threads
driverThreads = []
import requests
import random
from tqdm import tqdm
import time
import threading
#need to check 1 133 827 315 385 150 725 554 176 combinations

class bot:

    def forms():
        iteration = random.randint(0,100)
        list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
        print(a)
        for a in range(iteration, 1133827315385150725554176, 100):
            if a % 1000 == 0:
                print(a)
            web = str(list[a/62]) + str(list[a/3844]) + str(list[a/238328]) + str(list[a/14776336]) + str(list[a/916132832]) + str(list[a/56800235584]) + str(list[a/3521614606208]) + str(list[a/218340105584896]) + str(list[a/13537086546263552]) + str(list[a/839299365868340224]) + str(list[a/520365606838370938888]) + str(list[a/3226266762397899821056]) + str(list[a/200028539268669788905472]) + str(list[a/12401769434657526912139264]) + str(list[a/768909704948766668552634368]) + str(list[a/47672401706823533450263330816]) + str(list[a/1525516854618353070408426586112])

            response = requests.get('https://forms.gle/{}'.format(web))
            if response.status_code == 200:
                print(web)
    def __init__(self):
        t = threading.Thread(target=self.forms)
        t.start
        t.join

# inputText = input("What do you want to generate with AI : ")
# inputText = "Space"
# inputText = ["city", "sunset", "sea", "forest", "airship", "port", "robot", "factory", "human", "fly", "waterfall", "tank", "giant robot", "steamtrain", "train"]

# for a in inputText:

# inputText = "".join([x.capitalize() for x in inputText.split(" ")])
# iterations = int(input("Number of iterations : "))
iterations = 10

for a in range(iterations):
    bot()

# #Create directory
# # if not os.path.exists(inputText):
# #     os.mkdir(inputText)

# for j in range(iterations):
#     #Add thread to the list
#     # driverThreads.append(threading.Thread(target=ts.forms, kwargs={"start":j}))
#     driverThreads.append(threading.Thread(target=ts.forms, kwargs={'iteration':j}))
#     # print(driverThreyads)
# # print("asodigf")


# #Start all threads
# for i in driverThreads:
#     try:
#         # imgType = i._kwargs.get("imgType")
#         iteration = i._kwargs.get("iteration")-1
#         print(f"Starting Thread, Iteration {iteration}")
#         i.start()
#         print(i, "               start")    
#     except:
#         print(i)
#         pass
# # for i in driverThreads:
# #     print(i,"      joined")
# #     i.join()
# # time.sleep(5)
# # print(driverThreads)
# # #Wait for the end of all threads
# # for i in driverThreads:

