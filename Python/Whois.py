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

if len(sys.argv) != 2:
    os.system('cls' if os.name=='nt' else 'clear')
    print(colors.RED + "\n[!] "+ colors.WHITE+"Use: python " + sys.argv[0], colors.BLUE + "<ip>\n")
    sys.exit(1)

# Global
url = 'http://ip-api.com/json/'+sys.argv[1]

# Functions
def handler(signum, frame):
    os.system('cls' if os.name=='nt' else 'clear')
    print(colors.RED + '\n[!] Exiting succes (CTRL + C)..\n', signum)
    time.sleep(2)
    os.system('cls' if os.name=='nt' else 'clear')
    sys.exit(1)

signal.signal(signal.SIGINT, handler)

def print_slow(str):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.05)

def get_info():
    try:
        res = requests.get(url)
        data = res.content.decode()
        data = json.loads(data)
    except:
        os.system('cls' if os.name=='nt' else 'clear')
        time.sleep(0.3)
        print_slow(colors.RED + '\n An error occurred\n')
        sys.exit(1)
    try:
        ip = data['query']
        isp = data['isp']
        lat = data['lat']
        lot = data['lon']
        city = data['city']
        country=data['country']
    except:
        os.system('cls' if os.name=='nt' else 'clear')
        print_slow(colors.RED + '\n[!]'+ colors.WHITE +' Provide a valid ip please\n')
        time.sleep(0.3)
        sys.exit(1)

    os.system('cls' if os.name=='nt' else 'clear')
    print(f''' {colors.RED}
▄█    ▄   ▄████  ████▄     ▄█ █ ▄▄  
██     █  █▀   ▀ █   █     ██ █   █ 
██ ██   █ █▀▀    █   █     ██ █▀▀▀  
▐█ █ █  █ █      ▀████     ▐█ █     
 ▐ █  █ █  █                ▐  █    
   █   ██   ▀                   ▀
    ''')
    print_slow(colors.BLUE +'\nIp                 =                 '+ip)
    print_slow('\nIsp                =                 '+isp)
    print_slow('\nZip                =                 '+ip)
    print_slow('\nGeo                =                 '+str(lat)+' '+str(lot))
    print_slow('\nCity               =                 '+city)
    print_slow('\nCountry            =                 '+country+'\n')
    
if __name__ == '__main__':
    get_info()
