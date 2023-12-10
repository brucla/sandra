from instagrapi import Client
from time import sleep
import random
import modules/printheader

# credenziali account
USR = "username"
PWD = "1234"

# numero di chat da recuperare in ordine dalla più recente
n_chats = 100

cl = Client()

not_logged = True
while not_logged:
    print("Inserisci codice di verifica a 2 fattori e premi invio")
    A2F = input("Premi semplicemente invio se l'autenticazione a 2 fattori non è abilitata \n")
    try:
        cl.login(USR, PWD,verification_code = A2F)
        not_logged = False
    except Exception as e:
        print(e)
print("Log-in riuscito!")

print(f"Recupero delle ultime {n_chats} chat.")
threads = cl.direct_threads(n_chats)

# Set di testi da prelevare casualmente
#testi = [f"Ciao {chat.users[0].full_name}!","Ciao! Grazie per l'aiuto", "🔆","Bonjour 🐻‍❄️"]
with open("tsti.txt", encoding = 'utf-8') as f:
    testi = [line.rstrip('\n') for line in f]

input(f"Premi invio per avviare broadcast verso {n_chats} chat o ctrl+C per annullare:")
for i,chat in enumerate(threads):    
    cl.direct_send(random.sample(testi,1), thread_ids = [chat.pk])
    print(f"{i+1}/{n_chats}")

    # una volta ogni bunch_size messaggi l'attesa è più lunga
    bunch_size = 15
    if (i+1)%bunch_size:
        sleep(3)
    else:
        sleep(10)

input("Broadcast completato!")
