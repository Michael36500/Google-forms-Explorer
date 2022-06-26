import requests
import tblib.pickling_support
tblib.pickling_support.install()
import time
# import threading
from threading import Thread
from multiprocessing import Process
# from multiprocessing import Process

thrd = 20

def forms(iteration):
    print(iteration)
    global thrd
    
    list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
    # print(a)
    for a in range(iteration, 1133827315385150725554176, thrd):
        found = open("found.txt", "w")
        # print(a)
        # if a % 1000 in range(0, 100):
        if a % 1000 in range (0, 50):
            print("thread {} on {}k".format(iteration, a//1000))
            # print(a, end=" ")
        web = str(list[a%62]) + str(list[a//62%62]) + str(list[a//3844%62]) + str(list[a//238328%62]) + str(list[a//14776336%62]) + str(list[a//916132832%62]) + str(list[a//56800235584%62]) + str(list[a//3521614606208%62]) + str(list[a//218340105584896%62]) + str(list[a//13537086546263552%62]) + str(list[a//839299365868340224%62]) + str(list[a//520365606838370938888%62]) + str(list[a//3226266762397899821056%62]) + str(list[a//200028539268669788905472%62]) + str(list[a//12401769434657526912139264%62]) + str(list[a//768909704948766668552634368%62]) + str(list[a//47672401706823533450263330816%62])

        response = requests.get('https://forms.gle/{}'.format(web), timeout=0.01)
        # time.sleep(10)
        # print(iteration, web)
        if response.status_code == 200:
            print(web, "     found")
            found.write("{}\n".format(web))
        # break

        
        # print(web)


# def threads(iter):
    # iter = str(iter)
    
    # l = len(iter)

    # iter = iter[:l-1]
    # iter = iter[1:]
    # print(iter)
    # iter = int(iter)

    # print(type(iter))


threads = []
# print(iter)
for i in range(thrd):
    # print(iter, " ", i)
    # print("    thread {}".format(i))
    # arg = i + iter
    # arg = range(arg)
    threads.append(Thread(target=forms, args = (i,)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()   
# threads(0)

# processes = []

# if __name__ == '__main__':    
#     for i in range(1,3):
#         print("process {}".format(i))
#         processes.append(Process(target=threads, args = ([int(i)],)))

#     for process in processes:
#         process.start()

#     # for process in processes:
#     #     process.join()