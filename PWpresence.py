import time
import os
try:
    from pypresence import Presence
    from InquirerPy import inquirer
    from colorama import init, Fore
except ImportError:
    os.system('pip install pypresence InquirerPy colorama')
    from pypresence import Presence
    from InquirerPy import inquirer
    from colorama import init, Fore
    
init(autoreset=True)

clsr = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clsr()

client_id = '1021010790104436836'
RPC = Presence(client_id)
RPC.connect()

# -----------------------------------------------
# ------ Self customisation instructions --------
# A) If you want to include more subjects:
# 1. Add suitable 'key:value' pair in the picture_data dictionary
# 2. Add the same 'key' to the choices list of sub_ques
# 3. keys are sensitive so don't mess up capitalization
#
# B) If you want to change a particular image:
# 1. Just put the link of image(inside quotes '') in the 'value' part of the subject key:value pair


# ------- Pictures (change if you wanna) -------

picture_data = {
    'chemistry' : 'https://news.mit.edu/sites/default/files/styles/news_article__image_gallery/public/images/201706/MIT-Predicting-Reactions-1_0.jpg',
    'mathematics' : 'https://miro.medium.com/max/1400/1*L76A5gL6176UbMgn7q4Ybg.jpeg',
    'physics' : 'https://static3.bigstockphoto.com/3/1/1/large2/113833082.jpg',
    'biology' : 'https://media-exp1.licdn.com/dms/image/C4D1BAQHg6yM2QSvcyg/company-background_10000/0/1601919495731?e=2147483647&v=beta&t=mcu1a1ESCQIzDLn5YtMQvkrCYFQKv8QXFBP_-mJtxbM',
    'other' : 'https://media.istockphoto.com/vectors/-vector-id1254125223?k=20&m=1254125223&s=612x612&w=0&h=TPPIBeteH0FVR8bT3J7xi9fHgsR7QoF6iwg2pAhB030=',
}

# ------- Questions that would be asked -------

batch_ques = inquirer.text(
    message='Batch Name: ',
    completer={
        'Lakshya JEE' : None,
        'Arjuna JEE' : None,
        'Prayas' : None,
        'Manzil' : None,
        'Lakshya NEET' : None,
        'Arjuna NEET' : None,
        'Ummed' : None,
        'Yakeen' : None,
    }
)

sub_ques = inquirer.select(
    message='Subject: ',
    choices=['chemistry', 'mathematics', 'physics', 'biology', 'other'],
)

topic_ques = inquirer.text(
    message='Name of topic (What you\'re studying) :'
)



# ---------- begin ----------

def initial():
    clsr()
    print(f'    {Fore.BLUE}+---     ---  +--   +--    ---')
    print(f'    {Fore.CYAN}|   \   /     |  \  |  \  /')
    print(f'    {Fore.GREEN}|    |  |     |  /  |  /  |')
    print(f'    {Fore.YELLOW}|   /   \     | \   |--   \\')
    print(f'    {Fore.RED}+---     ---  |  \  |      ---')
    print(f"""
        
    {Fore.YELLOW}Developed by: {Fore.CYAN}SingletLinkage (@QC#2293)
    {Fore.YELLOW}Client ID: {Fore.RED}{client_id}
    {Fore.YELLOW}Version: {Fore.RED}1.3
{Fore.CYAN}The answer these questions to set up your rich discord presence! :)
    """)

def get_details():
    cur_time = time.time()
    heading = batch_ques.execute()
    sub = sub_ques.execute()
    content = topic_ques.execute()

    return {'time':cur_time, 'batch':heading, 'sub':sub, 'topic':content}

def update_rpc(stuff):
    try:
        pic = picture_data[stuff['sub']]
    except KeyError as e:
        pic = picture_data['other']

    try:
        RPC.clear()
    except Exception as e:
        RPC.connect()

    RPC.update(
        state=stuff['topic'],
        details=stuff['batch'],
        start=stuff['time'],
        large_image=pic,
        large_text=stuff['sub']
    )

    print('Enjoy your rich presence on discord :)')

initial()
try:
    update_rpc(get_details())
except Exception as e:
    error = f'{e} and {type(e)}'

while True:
    lol = input('To exit application: press Enter')
    if not lol:
        break
    
    

