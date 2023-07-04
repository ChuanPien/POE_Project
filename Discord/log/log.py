import datetime, time

def log(msg):
    server = msg.guild.id
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    with open(f"log/{server}.txt", "a", encoding='utf8') as text_file:
        print(f"<{st}>\nName : {msg.author.name} | ID : {msg.author.id}\nChannel Name : {msg.channel.name} | Channel ID : {msg.channel.id}\nMsg : {msg.content}\n-------------------------", file=text_file)

def poe(msg):
    player = msg.author.id
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    with open(f"log/{player}.txt", "a", encoding='utf8') as text_file:
        print(f"<{st}>\nName : {msg.author.name}\nChannel Name : {msg.channel.name} | Channel ID : {msg.channel.id}\nMsg : {msg.content}\n-------------------------", file=text_file)
