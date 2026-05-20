#!/usr/bin/env python3
import os
import sys
import time
import socket
import subprocess
import shutil
import platform
import urllib.request
import json
import random

# phonenumbers पैकेज चेक और इंस्टॉल
try:
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone
except ImportError:
    os.system('pip3 install phonenumbers --break-system-packages')
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone

def print_banner():
    os.system('clear')
    print("\033[1;31m") 
    print("  ██████╗ ██████╗ ██╗██╗   ██╗ █████╗ ███╗   ██╗███████╗██╗  ██╗██╗   ██╗")
    print("  ██╔══██╗██╔══██╗██║╚██╗ ██╔╝██╔══██╗████╗  ██║██╔════╝██║  ██║██║   ██║")
    print("  ██████╔╝██████╔╝██║ ╚████╔╝ ███████║██╔██╗ ██║███████╗███████║██║   ██║")
    print("  ██╔═══╝ ██╔══██╗██║  ╚██╔╝  ██╔══██║██║╚██╗██║╚════██║██╔══██║██║   ██║")
    print("  ██║     ██║  ██║██║   ██║   ██║  ██║██║ ╚████║███████║██║  ██║╚██████╔╝")
    print("  ╚═╝     ╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ")
    print("                        --- PRIYANSHU EXPLOIT FRAMEWORK ---")
    print("\033[0m")

def show_live_status():
    # टाइम और बैटरी हटा दी गई है, अब सिर्फ रियल स्टोरेज स्टेटस दिखेगा
    try:
        total, used, free = shutil.disk_usage("/")
        disk_used = used // (2**30)
        disk_total = total // (2**30)
        storage_str = f"{disk_used}GB Used / {disk_total}GB Total"
    except:
        storage_str = "Error Reading Storage"

    print("\033[1;37m+-----------------------------------------------------------------+")
    print(f"|                     💾 STORAGE: {storage_str:<32}        |")
    print("+-----------------------------------------------------------------+\033[0m")

def advanced_hacker_animation():
    os.system('clear')
    print("\033[1;33m[!] ACCESSING CORE SYSTEM TERMINAL...\033[0m")
    time.sleep(0.4)
    
    for _ in range(8):
        binary_line = "".join(random.choice(["0", "1", " ", "■", "▫"]) for _ in range(40))
        print(f"\033[1;32m\t{binary_line}\033[0m")
        time.sleep(0.06)
        
    print("\n\033[1;36m[+] BYPASSING LOCAL FIREWALL...")
    time.sleep(0.2)
    
    for percent in range(0, 101, 25):
        sys.stdout.write(f"\r[+] CRACKING ENCRYPTION BLOCKS... [{percent}%]")
        sys.stdout.flush()
        time.sleep(0.12)
        
    print("\n[+] SYSTEM BREACH SUCCESSFUL.")
    time.sleep(0.2)
    
    print("\n\033[1;35m=======================================")
    print("       SCANNING USER IDENTITY...       ")
    print("=======================================\033[0m")
    
    scans = ["[ █ ] TARGET: PRIYANSHU EXPLOIT", "[ █ ] ACCESS ROUTE: LOCALHOST", "[ █ ] STATUS: PENDING PASSWORD VERIFICATION"]
    for scan in scans:
        print(f"\t\033[1;37m{scan}\033[0m")
        time.sleep(0.3)
    print("\n\033[1;33m[!] IDENTITY CONFIRMED. ENTER AUTHENTICATION KEY TO INTEGRATE INTERFACE.\033[0m\n")

# --- आपके सभी ओरिजिनल टूल्स ---

def real_port_scanner():
    print_banner()
    show_live_status()
    print("\033[1;33m[+] REAL PORT SCANNER (POWERED BY NMAP ENGINE)\033[0m")
    target = input("\033[1;37mEnter Target Website or IP: \033[0m").strip()
    if not target: return
    try:
        target_ip = socket.gethostbyname(target)
        print(f"\033[1;32m[+] Target IP Resolved: {target_ip}\033[0m")
    except socket.gaierror:
        print("\033[1;31m[-] Error: Host could not be resolved.\033[0m")
        input("\n\033[1;33mPress Enter to go back...\033[0m")
        return
    print("\033[1;33m[*] Scanning common ports... Please wait...\033[0m")
    cmd = ["nmap", "-p", "21,22,80,443", "-sV", target_ip]
    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, _ = process.communicate()
        lines = stdout.split('\n')
        for line in lines:
            if "PORT" in line: print(f"\033[1;35m{line}\033[0m")
            elif "open" in line: print(f"\033[1;32m{line}\033[0m")
    except Exception as e: print(f"\033[1;31m[-] Error: {e}\033[0m")
    input("\n\033[1;33mPress Enter to go back to Menu...\033[0m")

def advance_info_scanner():
    print_banner()
    show_live_status()
    print("\033[1;33m[+] ADVANCED SYSTEM INFO SCANNER\033[0m")
    total, used, free = shutil.disk_usage("/")
    disk_total, disk_used = total // (2**30), used // (2**30)
    print("\n\033[1;32m[+] HARDWARE SPECS:\033[0m")
    print(f" \033[1;35m•\033[1;37m OS Distribution     : \033[1;32m{platform.system()}\033[0m")
    print(f" \033[1;35m•\033[1;37m Base Storage Usage  : \033[1;32m{disk_used} GB / {disk_total} GB Used\033[0m")
    input("\n\033[1;33mPress Enter to go back to Menu...\033[0m")

def advanced_number_osint():
    print_banner()
    show_live_status()
    print("\033[1;33m[+] ADVANCED PHONE NUMBER OSINT SCANNER\033[0m")
    raw_number = input("\033[1;37mEnter Phone Number: \033[0m").strip()
    if not raw_number: return
    if not raw_number.startswith('+'): raw_number = "+91" + raw_number
    try:
        parsed_number = phonenumbers.parse(raw_number, None)
        location = geocoder.description_for_number(parsed_number, "en")
        service_provider = carrier.name_for_number(parsed_number, "en")
        print("\033[1;32m[+] CORE TELECOM DATA DETECTED:\033[0m")
        print(f" \033[1;35m•\033[1;37m Registered Region : \033[1;32m{location}\033[0m")
        print(f" \033[1;35m•\033[1;37m Carrier Operator  : \033[1;32m{service_provider}\033[0m")
    except Exception as e: print(f"\033[1;31m[-] Scan Error: {e}\033[0m")
    input("\n\033[1;33mPress Enter to go back to Menu...\033[0m")

def real_ip_tracker():
    print_banner()
    show_live_status()
    print("\033[1;33m[+] REAL-TIME IP GEO-LOCATION TRACKER\033[0m")
    ip_target = input("\033[1;37mEnter Target IP Address: \033[0m").strip()
    if not ip_target: return
    try:
        url = f"http://ip-api.com/json/{ip_target}"
        req = urllib.request.urlopen(url, timeout=5)
        data = json.loads(req.read().decode())
        if data.get("status") == "success":
            print("\n\033[1;32m[+] LIVE TARGET LOCATION DETECTED:\033[0m")
            print(f" \033[1;35m•\033[1;37m Country Name     : \033[1;32m{data.get('country')}\033[0m")
            print(f" \033[1;35m•\033[1;37m City/Region      : \033[1;32m{data.get('city')} ({data.get('regionName')})\033[0m")
    except Exception as e: print(f"\033[1;31m[-] API Error: {e}\033[0m")
    input("\n\033[1;33mPress Enter to go back to Menu...\033[0m")

def anime_combat_simulator():
    print_banner()
    show_live_status()
    print("\033[1;33m[+] ANIME COMBAT SIMULATOR (ASCII BATTLE)\033[0m")
    char1 = input("\033[1;37mEnter Fighter 1 Name (e.g., Obito): \033[0m").strip()
    char2 = input("\033[1;37mEnter Fighter 2 Name (e.g., Madara): \033[0m").strip()
    if not char1 or not char2: return

    for i in range(1, 4):
        print_banner()
        show_live_status()
        print(f"\n\t\033[1;31m⚡ BATTLE INITIATED: {char1} VS {char2} ⚡\033[0m\n")
        spaces = " " * (25 - i*4)
        mid_dash = "-" * (i*2)
        print(f"\tO{mid_dash}     {spaces}     O")
        print(f"\t/|\\    {spaces}    /|\\")
        print(f"\t/ \\    {spaces}    / \\")
        time.sleep(0.3)

    p1_power = random.randint(80, 100)
    p2_power = random.randint(80, 100)
    print("\n\033[1;32m[+] FINAL BATTLE REPORT:\033[0m")
    if p1_power > p2_power:
        print(f" 🏆 \033[1;32mWINNER: {char1} wins with an Epic Finisher! 🎉\033[0m")
    else:
        print(f" 🏆 \033[1;32mWINNER: {char2} counters and wins! 🎉\033[0m")
    input("\n\033[1;33mPress Enter to go back to Menu...\033[0m")

def cyber_snake_game():
    width, height = 20, 10
    snake = [[5, 5], [5, 4], [5, 3]]
    food = [3, 3]
    score = 0
    while True:
        os.system('clear')
        print("\033[1;32m=========================================")
        print(f"   🐍 CYBER SNAKE GAME | SCORE: {score}   ")
        print("=========================================\033[0m")
        print(" Controls: W (Up) | S (Down) | A (Left) | D (Right) | Q (Quit)")
        print("-" * (width + 2))
        for y in range(height):
            print("|", end="")
            for x in range(width):
                if [y, x] in snake: print("\033[1;32m*\033[0m", end="")
                elif [y, x] == food: print("\033[1;31m$\033[0m", end="")
                else: print(" ", end="")
            print("|")
        print("-" * (width + 2))
        move = input("\033[1;33m[?] Next Move > \033[0m").strip().lower()
        if move == 'q': break
        head = list(snake[0])
        if move == 'w': head[0] -= 1
        elif move == 's': head[0] += 1
        elif move == 'a': head[1] -= 1
        elif move == 'd': head[1] += 1
        else: continue
        if head[0] < 0 or head[0] >= height or head[1] < 0 or head[1] >= width or head in snake:
            print("\n\033[1;31m💥 GAME OVER! 💥\033[0m")
            time.sleep(1.5)
            break
        snake.insert(0, head)
        if head == food:
            score += 10
            food = [random.randint(0, height-1), random.randint(0, width-1)]
        else: snake.pop()

def secure_cyber_diary():
    diary_file = "cyber_notes.txt"
    while True:
        print_banner()
        show_live_status()
        print("\033[1;35m[+] SECURE CYBER DIARY & CREDS VAULT\033[0m")
        print(" [1] View Stored Secret Notes")
        print(" [2] Add New Secret Note")
        print(" [3] Clear All Stored Notes")
        print(" [4] Go Back to Main Menu")
        sub_choice = input("\033[1;33m[?] Select Option > \033[0m").strip()
        
        if sub_choice == '1':
            print_banner()
            show_live_status()
            print("\033[1;32m[+] DECRYPTING YOUR SECURE NOTES:\033[0m")
            if os.path.exists(diary_file):
                with open(diary_file, "r") as f: notes = f.read()
                print(notes if notes.strip() else "\033[1;33m[!] Vault is empty!\033[0m")
            else: print("\033[1;33m[!] No notes found.\033[0m")
            input("\n\033[1;33mPress Enter to go back...\033[0m")
        elif sub_choice == '2':
            print_banner()
            show_live_status()
            new_note = input("\n\033[1;37mWrite Note >>> \033[0m").strip()
            if new_note:
                current_time = time.strftime("%Y-%m-%d %H:%M:%S")
                with open(diary_file, "a") as f: f.write(f"[{current_time}] {new_note}\n")
                print("\033[1;32m\n[✔] Note securely logged!\033[0m")
                time.sleep(1)
        elif sub_choice == '3':
            if os.path.exists(diary_file): os.remove(diary_file)
            print("\033[1;32m[+] Vault purged successfully.\033[0m")
            time.sleep(1)
        elif sub_choice == '4': break

def cyber_stylizer_clock():
    while True:
        print_banner()
        show_live_status()
        print("\033[1;36m[+] CYBER TEXT STYLIZER\033[0m")
        text_input = input("\033[1;37mEnter Name to Stylize (or 'q' to go back): \033[0m").strip()
        if text_input.lower() == 'q' or not text_input: break
        print(f"\n\033[1;32m //===  {text_input.upper()}  ===//\033[0m")
        input("\n\033[1;33mPress Enter to go back...\033[0m")

def ai_anime_quote_generator():
    print_banner()
    show_live_status()
    print("\033[1;33m[+] AI ANIME QUOTE GENERATOR (POWERED BY GEMINI)\033[0m")
    character = input("\033[1;37mEnter Anime Character Name (e.g., Obito, Madara): \033[0m").strip()
    if not character: return
    print(f"\n\033[1;32m[*] Summoning Gemini AI Engine to extract {character}'s mind...\033[0m")
    
    quotes_db = {
        "madara": "Wake up to reality! Nothing ever goes as planned in this accursed world...",
        "obito": "The moment people come to know love, they run the risk of carrying hate.",
        "itachi": "People live their lives bound by what they accept as correct and true."
    }
    
    api_key = "YOUR_API_KEY" 
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    headers = {'Content-Type': 'application/json'}
    prompt_text = f"Give a badass dialogue spoken by {character} from the anime."
    data = {"contents": [{"parts": [{"text": prompt_text}]}]}
    
    try:
        req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='POST')
        with urllib.request.urlopen(req, timeout=5) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            quote = res_data['candidates'][0]['content']['parts'][0]['text']
            print(f"\n\033[1;32m 🔥 {character.upper()}: \"{quote}\"\033[0m")
    except:
        selected = quotes_db.get(character.lower(), "In the ninja world, those who break the rules are scum, but those who abandon their friends are worse than scum!")
        print(f"\n\033[1;31m 🔥 {character.upper()}: \"{selected}\"\033[0m")
        
    input("\n\033[1;33mPress Enter to go back to Menu...\033[0m")

def priyanshu_menu():
    while True:
        print_banner()
        show_live_status()
        print("\033[1;32m[+] Access Granted! Welcome Priyanshu.\033[0m")
        print("\033[1;37m=================================================================\033[0m")
        print(" \033[1;36m[1]\033[1;37m Real Port & Service Scanner (Nmap Recon)")
        print(" \033[1;36m[2]\033[1;37m Advanced System & Network Info Scanner")
        print(" \033[1;36m[3]\033[1;37m Phone Number Advanced OSINT Lookup")
        print(" \033[1;36m[4]\033[1;37m IP Geo-Location Tracker & OSINT")
        print(" \033[1;36m[5]\033[1;37m AI Anime Quote Generator (Gemini Engine) 🔥")
        print(" \033[1;36m[6]\033[1;37m Anime Combat Simulator (ASCII Battle)")
        print(" \033[1;36m[7]\033[1;37m Cyber Snake Game (Timepass Mini-Game) 🎮")
        print(" \033[1;36m[8]\033[1;37m Secure Cyber Diary & Creds Vault 🔒")
        print(" \033[1;36m[9]\033[1;37m Cyber Text Stylizer Banner ⏰")
        print(" \033[1;36m[10]\033[1;37m Exit Tool")
        print("\033[1;37m=================================================================\033[0m")
        choice = input("\033[1;33m[?] Priyanshu-Exploit > \033[0m").strip()
        if choice == '1': real_port_scanner()
        elif choice == '2': advance_info_scanner()
        elif choice == '3': advanced_number_osint()
        elif choice == '4': real_ip_tracker()
        elif choice == '5': ai_anime_quote_generator()
        elif choice == '6': anime_combat_simulator()
        elif choice == '7': cyber_snake_game()
        elif choice == '8': secure_cyber_diary()
        elif choice == '9': cyber_stylizer_clock()
        elif choice == '10': sys.exit()

def check_password():
    advanced_hacker_animation()
    password = input("\033[1;31m[?] ENTER SECURE PASSWORD: \033[0m")
    if password == "priyanshu0014":
        print("\033[1;32m\n[+] Access Approved! Initializing Menu...\033[0m")
        time.sleep(0.6)
        priyanshu_menu()
    else:
        print("\033[1;31m\n[-] Intruder Detected! Access Denied.\033[0m")
        sys.exit()

if __name__ == '__main__':
    check_password()
