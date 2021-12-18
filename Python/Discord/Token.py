import signal, os, sys, json, requests, time

# Colors
class colors:
    BLACK = '\33[30m'
    RED = '\33[31m'
    GREEN = '\33[32m'
    YELLOW = '\33[33m'
    BLUE = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE = '\33[36m'
    WHITE = '\33[37m'


def ctrl_c(signum, frame):
    print(colors.RED + '\n[!]Exiting.. (CTRL + C)\n', signum)
    sys.exit(1)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


signal.signal(signal.SIGINT, ctrl_c)


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)


# Main
def Init():
    cls()
    print(colors.BLUE + '''
        ,----,                                        
      ,/   .`|                                        
    ,`   .'  :              ,-.                       
  ;    ;     /          ,--/ /|                       
.'___,/    ,'  ,---.  ,--. :/ |                ,---,  
|    :     |  '   ,'\ :  : ' /             ,-+-. /  | 
;    |.';  ; /   /   ||  '  /      ,---.  ,--.'|'   | 
`----'  |  |.   ; ,. :'  |  :     /     \|   |  ,"' | 
    '   :  ;'   | |: :|  |   \   /    /  |   | /  | | 
    |   |  ''   | .; :'  : |. \ .    ' / |   | |  | | 
    '   :  ||   :    ||  | ' \ \'   ;   /|   | |  |/  
    ;   |.'  \   \  / '  : |--' '   |  / |   | |--'   
    '---'     `----'  ;  |,'    |   :    |   |/       
                      '--'       \   \  /'---'        
                                  `----'              
                                                      
    ''')
    token = input(colors.RED + '[!]' + colors.WHITE + ' Enter the token: ')
    data = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discordapp.com/api/v6/users/@me', headers=data)

    if r.status_code != 200:
        cls()
        print(colors.RED + '[!]' + colors.WHITE +
              ' The token you entered is invalid (401)')
        time.sleep(2)
        Init()
    else:
        cls()
        x = r.json()
        # Data..

        username = x['username']
        id = x['id']
        discriminator = x['discriminator']
        nsfw = x['nsfw_allowed']
        email = x['email']
        phone = x['phone']
        mfa = x['mfa_enabled']
        verified = x['verified']
        nitro = False

        r = requests.get(
            'https://discordapp.com/api/v6/users/@me/billing/subscriptions',
            headers=data).json()

        nitro = bool(len(r) > 0)
        if phone == None:
            phone = 'Does not have a number'
        if nsfw == True:
            nsfw = 'Has nsfw enabled'
        else:
            nsfw = 'Has nsfw disabled'

        if verified == True:
            verified = 'The email is verified'
        else:
            verified = 'The email is not verified'

        if nitro == False:
            nitro = 'This user has no nitro'
        else:
            nitro = 'This user has nitro'

        if mfa == True:
            mfa = 'If you have two factor authentication'
        else:
            mfa = 'Does not have two-factor authentication'

        print(colors.RED + '''
 /$$$$$$            /$$$$$$         
|_  $$_/           /$$__  $$        
  | $$   /$$$$$$$ | $$  \__//$$$$$$ 
  | $$  | $$__  $$| $$$$   /$$__  $$
  | $$  | $$  \ $$| $$_/  | $$  \ $$
  | $$  | $$  | $$| $$    | $$  | $$
 /$$$$$$| $$  | $$| $$    |  $$$$$$/
|______/|__/  |__/|__/     \______/ 
''')
    print_slow(colors.BLUE + '\nUsername                 =                 ' +
               username + '#' + discriminator)
    print_slow('\nId                       =                 ' + id)
    print_slow('\nNsfw?                    =                 ' + nsfw)
    print_slow('\nEmail                    =                 ' + email)
    print_slow('\nPhone                    =                 ' + phone)
    print_slow('\nVerified                 =                 ' + (verified))
    print_slow('\nNitro                    =                 ' + (nitro))
    print_slow('\nmfa                      =                 ' + (mfa) +'\n')


if __name__ == '__main__':
    Init()
