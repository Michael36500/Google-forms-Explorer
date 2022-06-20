import requests
import random
import tqdm
#need to check 1 133 827 315 385 150 725 554 176 combinations

list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]

for a in tqdm(range(1133827315385150725554176)):
    web = str(list[a%26]) + str(list[a%26*26]) + str(list[a%26]) + str(list[a%26]) + str(list[a%26]) + str(list[a%26]) + str(list[a%26]) + str(list[a%26]) + str(list[a%26]) + str(list[a%26]) + str(list[a%26]) + str(list[a%26]) + str(list[a%26]) + str(list[a%26]) + str(list[a%26]) + str(list[a%26]) + str(list[a%26])
    response = requests.get('https://forms.gle/{}'.format(web))
    if response.status_code == 200:
        print(web)