#!/usr/bin/env python3.11

import openai                                 	# pip3 install openai - Works over Python +3.11.x
import emoji                                    # pip3 install emoji
import configparser
from xdg.BaseDirectory import xdg_config_home   # pip3 install pyxdg
from colorama import Fore, Style				# pip3 install colorama
from time import sleep

user_config = xdg_config_home
config = configparser.ConfigParser()

try:
    config.read(f"{user_config}/openai_client.conf")
    api_token = config.get('openai', 'token')
except:
    print(Fore.RED + "Error!: File does not exist " + Fore.YELLOW +"~/.config/openai_client.conf" + Style.RESET_ALL)
    print(Fore.YELLOW + "Creating a new configuration file...\n")
    sleep(3)
    print(Fore.GREEN + "Finished!, you can enter your token by editing"+ Fore.YELLOW + " ~/.config/openai_client.conf")
    config["openai"] = {
            "token": ""
        }
    with open(f"{user_config}/openai_client.conf", "w") as file_config:
        config.write(file_config)
    
    exit(1)
    
openai.api_key = api_token

# print("""
# 	Welcome to PyGPT CLI!
# 	Creator: Spectrasonic
# 	Version: 1.0
#       """)

print("")
print(Fore.GREEN +	"	Welcome to PyGPT CLI!")
print(Fore.RED + 	"	Creator: Spectrasonic")
print(Fore.YELLOW + "	Version: 1.0")
print(Fore.GREEN + "	Source Code: https://github.com/spectrasonic117/pygpt")
print("")
print(Fore.GREEN + "Type \"Q\" to Exit")



while True:
	model_engine = "text-davinci-003"
	prompt = input(Fore.CYAN + "🧑 You: " + Style.RESET_ALL)
	if "exit" in prompt or "quit" in prompt or "Q" in prompt or "q" in prompt:
		break
	completion = openai.Completion.create(
		engine = model_engine,
		prompt = prompt,
		max_tokens=1024,
		n = 1, stop = None,
		temperature = 0.7
		)

	response = completion.choices[0].text
	print(Fore.GREEN + "🤖 ChatGPT:" +  Style.RESET_ALL + response)