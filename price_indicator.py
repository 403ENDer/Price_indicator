import discord
import requests
from bs4 import BeautifulSoup
import validators

TOKEN = 'MTA1MTAxMTkzNDU5NTU4ODE0OA.GCqD4L.n3JBELZEg3cJbiv3PWEOCHHiJcdhvvXgs1hR2E'

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)



@client.event
async def on_ready():
    print('{0.user}'.format(client)) 
        

@client.event
async def on_message(message):
    user = str(message.author).split('#')[0]
    channel = str(message.channel.name)
    content = str(message.content)
    print(f'{user} = {content}  ({channel})')
    
    if message.author == client.user:
        return

    if message.channel.name == 'price-predictor':
        if content.lower() == 'hi':
            await message.channel.send(f'Hi {user}')    
            return

        elif validators.url(content):
            if flip_url(content):
                price_o = check_price_o(content)
                price = check_price(content)
                await message.channel.send(f"Original price {price_o}\nToday's price is {price}")
                return
            
            else:
                await message.channel.send(f'Oops you entered a wrong url...😢\nEnter a url of flipkart...')
                

        elif content.lower() == 'bye':
            await message.channel.send(f'See you later {user}') 
            return

        elif content.lower() == '/stop':
            await client.close()

def flip_url(url):
    if 'flipkart' in url:
        return True
    else :
        return False


def check_price_o(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content,'html5lib')
    price = (soup.find('div', attrs = {"class" :"_2p6lqe"})).text
    return price



def check_price(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content,'html5lib')
    price = (soup.find('div', attrs = {"class" :"_16Jk6d"})).text
    return price

client.run(TOKEN) 
  