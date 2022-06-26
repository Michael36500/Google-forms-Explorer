import requests
import tblib.pickling_support
tblib.pickling_support.install()
import time
# import threading
from threading import Thread

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def forms(iteration):
    # setup chromedriver
    CHROME_DRIVER_PATH = "c:/Users/ambro/webdrivers/chromedriver.exe"   # add your chromedriver path
    browserOptions = Options()
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH,options=browserOptions)
    driver.get("https://www.alza.cz/Order1.htm")    



    print(iteration)
    
    list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]

    for a in range(iteration, 1133827315385150725554176, 20):
        found = open("found.txt", "w")
        if a % 1000 in range (0, 50):
            print("thread {} on {}k".format(iteration, a//1000))

        web = str(list[a%62]) + str(list[a//62%62]) + str(list[a//3844%62]) + str(list[a//238328%62]) + str(list[a//14776336%62]) + str(list[a//916132832%62]) + str(list[a//56800235584%62]) + str(list[a//3521614606208%62]) + str(list[a//218340105584896%62]) + str(list[a//13537086546263552%62]) + str(list[a//839299365868340224%62]) + str(list[a//520365606838370938888%62]) + str(list[a//3226266762397899821056%62]) + str(list[a//200028539268669788905472%62]) + str(list[a//12401769434657526912139264%62]) + str(list[a//768909704948766668552634368%62]) + str(list[a//47672401706823533450263330816%62])

        response = requests.get('https://forms.gle/{}'.format(web))
            
        if response.status_code == 200:
            print(web, "     found")
            found.write("{}\n".format(web))

        break



threads = []

for i in range(50):
    threads.append(Thread(target=forms, args = (i,)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()   
