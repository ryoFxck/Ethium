import sys, time, os, signal, json, requests

# Colors
class colors:
    BLACK  = '\33[30m'
    RED    = '\33[31m'
    GREEN  = '\33[32m'
    YELLOW = '\33[33m'
    BLUE   = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE  = '\33[36m'
    WHITE  = '\33[37m'

# Ctrl C
def handler(signum, frame):
    os.system('cls' if os.name=='nt' else 'clear')
    print(colors.RED + '\n[!] Exiting succes (CTRL + C)..\n', signum)
    time.sleep(2)
    os.system('cls' if os.name=='nt' else 'clear')
    sys.exit(1)

signal.signal(signal.SIGINT, handler)

def spamWebhook():
    banner = '''
 __    __     _     _                 _    
/ / /\ \ \___| |__ | |__   ___   ___ | | __
\ \/  \/ / _ \ '_ \| '_ \ / _ \ / _ \| |/ /
 \  /\  /  __/ |_) | | | | (_) | (_) |   < 
  \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\
'''
    print(colors.BLUE + banner)
    webhookURL = input(colors.RED +'\n\n [!] ' + colors.WHITE +'Webhook URL: ')
    time.sleep(0.3)
    os.system('cls' if os.name == 'nt' else 'clear')

    print(colors.BLUE + banner)
    webhookName = input(colors.RED + '\n\n [!] ' + colors.WHITE + 'Webhook Name: ')
    time.sleep(0.3)
    os.system('cls' if os.name == 'nt' else 'clear')

    print(colors.BLUE + banner)
    webhookMessage = input(colors.RED + '\n\n [!] ' + colors.WHITE + 'Webhook Message: ')
    time.sleep(0.3)
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        try:
            print(colors.BLUE + banner)
            WebhookAmount = int(input(colors.RED +'\n\n [!] ' + colors.WHITE + 'Amount: '))
            time.sleep(0.3)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        except:
            time.sleep(0.3)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(colors.RED + '[!] '+ colors.WHITE +' It is not a valid amount.')
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

    if len(webhookMessage) > 1999:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colors.RED+'[!]'+colors.WHITE+' The message is too long, try again')
        time.sleep(3)
        spamWebhook()
    else:            
        data = {
            "avatar_url": 'https://images-ext-2.discordapp.net/external/OXYJicMhwKGhCp-03MyGas_0vyO9GzAQVP2unVPxrrs/%3Fsize%3D2048/https/cdn.discordapp.com/avatars/894594416952623105/a710a2f0e5ade6472011e8a71683a1de.png?width=670&height=670',
            "username": webhookName,
            "content": webhookMessage
        }
        print(colors.RED + '[!]'+colors.WHITE+' I successfully spammed this webhook')
        for i in range(WebhookAmount):
            time.sleep(0.1)
            try:
                requests.post(webhookURL, json = data)
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(colors.RED +'[!]'+colors.WHITE+' An error occurred sending the message, try again')
                os.system('cls' if os.name == 'nt' else 'clear')
                time.sleep(2)
                spamWebhook()

if __name__ == '__main__':
    spamWebhook()
