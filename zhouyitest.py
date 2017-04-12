import json
import discord
import pydle
import asyncio
from reptest import get
from tornado.platform.asyncio import AsyncIOMainLoop
AsyncIOMainLoop().install()

with open("zclient_data.json", "r") as f:
    clientdata = json.load(f)


#######ELIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIiiiii



def iching(message):
    if "+help" in message.lower():
        return ['I am an Iching bot short and stout.']
    elif "dick" in message.lower():
        return get('dick')
    else:
        return get('iching')
        


discordclient = discord.Client()

@discordclient.event
@asyncio.coroutine
def on_message(message):
    if "zhouyi" in message.content.lower() or discordclient.user.mention in message.content or isinstance(message.channel, discord.PrivateChannel) and not message.author.bot:
        try:
             for card in iching(message.content):
                for g in range (len(card)):
                   output = card[g] 
                   yield from discordclient.send_message(message.channel, message.author.mention+": "+" " + output)
        except discord.errors.Forbidden:
            pass

#--------------------------
### this returns the first letter from every array entry and compresses it into a single string
      #  try:
             #  yield from discordclient.send_message(message.channel, message.author.mention+": "+" ".join([card[0]+"/n" for card in iching(message.content)]))
       # except discord.errors.Forbidden:
        #    pass
#---------------------------

###this returns everything but parses every letter alone in its own message to the server
     #   try:
         #   for output in iching(message.content):
           #   for g in range (len(output)): 
            #   yield from discordclient.send_message(message.channel, message.author.mention+": "+" ".join([output[g]]))
     #   except discord.errors.Forbidden:
          #  pass



discordclient.run(clientdata["token"])


