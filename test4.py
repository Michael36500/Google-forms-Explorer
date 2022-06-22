import requests
import time
# import threading
from threading import Thread
from multiprocessing import Process
# from multiprocessing import Process


def forms(iteration):
    
    list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
    # print(a)
    for a in range(iteration, 1133827315385150725554176, 10):
        found = open("found.txt", "w")
        # print(a)
        # if a % 1000 in range(0, 100):
        if a % 1000 in range (0, 100):
            print("thread {} on {}k".format(iteration, a//1000))
            # print(a, end=" ")
        web = str(list[a%62]) + str(list[a//62%62]) + str(list[a//3844%62]) + str(list[a//238328%62]) + str(list[a//14776336%62]) + str(list[a//916132832%62]) + str(list[a//56800235584%62]) + str(list[a//3521614606208%62]) + str(list[a//218340105584896%62]) + str(list[a//13537086546263552%62]) + str(list[a//839299365868340224%62]) + str(list[a//520365606838370938888%62]) + str(list[a//3226266762397899821056%62]) + str(list[a//200028539268669788905472%62]) + str(list[a//12401769434657526912139264%62]) + str(list[a//768909704948766668552634368%62]) + str(list[a//47672401706823533450263330816%62])

        response = requests.get('https://forms.gle/{}'.format(web))
        time.sleep(10)
        print(iteration, web)
        if response.status_code == 200:
            print(web, "     found")
            found.write("{}\n".format(web))

        
        # print(web)


def threads(iter):
    threads = []
    for i in range(1):
        print(iter, " ", i)
        print("    thread {}".format(i))
        threads.append(Thread(target=forms, args = (i+(iter*10)),))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()   

processes = []

if __name__ == '__main__':    
    for i in range(1):
        print("process {}".format(i))
        processes.append(Process(target=threads, args = (float(i),)))

    for process in processes:
        process.start()

    # for process in processes:
    #     process.join()