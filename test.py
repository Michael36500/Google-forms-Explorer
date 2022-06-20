import requests
import random
import tqdm
import time
#need to check 1 133 827 315 385 150 725 554 176 combinations

list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]

for a in range(1133827315385150725554176):
    web = str(list[a%62]) + str(list[a%3844]) + str(list[a%238328]) + str(list[a%14776336]) + str(list[a%916132832]) + str(list[a%56800235584]) + str(list[a%3521614606208]) + str(list[a%218340105584896]) + str(list[a%13537086546263552]) + str(list[a%839299365868340224]) + str(list[a%520365606838370938888]) + str(list[a%3226266762397899821056]) + str(list[a%200028539268669788905472]) + str(list[a%12401769434657526912139264]) + str(list[a%768909704948766668552634368]) + str(list[a%47672401706823533450263330816]) + str(list[a%1525516854618353070408426586112])

    print(web, "     ", a)

    time.sleep(0.05)