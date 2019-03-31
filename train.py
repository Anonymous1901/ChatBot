from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from requests import get
from bs4 import BeautifulSoup
import os

bot= ChatBot('Jarvis')

trainer = ListTrainer(bot)

for file in os.listdir('C:/Users/Anonymous/Desktop/ChatBot/data/'):

    chats = open('C:/Users/Anonymous/Desktop/ChatBot/data/' + file, 'r').readlines()

    trainer.train(chats)

name=input( "Jarvis : Hii, my name is Jarvis. How can I call you? \n-> ")

print('Hi',name,'nice to meet you')

while True:

    request = input (name + ":- ")

    response = bot.get_response(request)

    if response.confidence > 0.1:
        
        print('Jarvis : ', response, '\n')
 
    elif request == ("bye"):

        print('Hope to see you soon '+ name)

        break

    else:
        
        try:
            url  = "https://en.wikipedia.org/wiki/"+ request
            page = get(url).text
            soup = BeautifulSoup(page,"lxml")
            p    = soup.find_all("p")
            print(p[1].text)

        except Exception as error:
            
            print('Jarvis: Sorry i have no idea about that.')