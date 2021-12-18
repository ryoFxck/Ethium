import os, sys, requests, time
from dhooks import Webhook

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

banner = """
  (`\ .-') /`   ('-. .-. .-')   ('-. .-.                          .-. .-')   
   `.( OO ),' _(  OO)\  ( OO ) ( OO )  /                          \  ( OO )  
,--./  .--.  (,------.;-----.\ ,--. ,--. .-'),-----.  .-'),-----. ,--. ,--.  
|      |  |   |  .---'| .-.  | |  | |  |( OO'  .-.  '( OO'  .-.  '|  .'   /  
|  |   |  |,  |  |    | '-' /_)|   .|  |/   |  | |  |/   |  | |  ||      /,  
|  |.'.|  |_)(|  '--. | .-. `. |       |\_) |  |\|  |\_) |  |\|  ||     ' _) 
|         |   |  .--' | |  \  ||  .-.  |  \ |  | |  |  \ |  | |  ||  .   \   
|   ,'.   |   |  `---.| '--'  /|  | |  |   `'  '-'  '   `'  '-'  '|  |\   \  
'--'   '--'   `------'`------' `--' `--'     `-----'      `-----' `--' '--' 
"""

def cls():
        os.system('cls' if os.name == 'nt' else 'clear')

def Init():
    cls()
    while True:
        try:
            print(colors.RED+ banner)
            WebhookURL = input(colors.BLUE+ 'Webhook URL> ')
            url = WebhookURL
            requests.post(WebhookURL, {'content': 'Deleting..'})
            WebhookURL = (Webhook(WebhookURL))
            WebhookURL.get_info()
            cls()
            print(banner)
            print('Default Name                 =                 '+WebhookURL.default_name)
            print('DefaultAvatar                =                 '+WebhookURL.default_avatar_url)
            print('Server ID                    =                 '+WebhookURL.guild_id)
            print('Channel ID                   =                 '+WebhookURL.channel_id)
            time.sleep(3)
            cls()
            requests.delete(url)
            print(colors.RED+'[!]'+colors.WHITE+' Webhook delete succes')
            break
        except:
            cls()
            print(colors.RED+'[!] Webhook Invalid')
            time.sleep(2)
            cls()
            Init()
if __name__ == '__main__':
    Init()

    © 2021 GitHub, Inc.

    Terms
    Privac
