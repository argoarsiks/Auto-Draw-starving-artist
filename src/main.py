import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
from drawer import start_draw

print("""
██████╗░██╗░░░██╗      ░█████╗░██████╗░░██████╗░░█████╗░░█████╗░██████╗░░██████╗
██╔══██╗╚██╗░██╔╝      ██╔══██╗██╔══██╗██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔════╝
██████╦╝░╚████╔╝░      ███████║██████╔╝██║░░██╗░██║░░██║███████║██████╔╝╚█████╗░
██╔══██╗░░╚██╔╝░░      ██╔══██║██╔══██╗██║░░╚██╗██║░░██║██╔══██║██╔══██╗░╚═══██╗
██████╦╝░░░██║░░░      ██║░░██║██║░░██║╚██████╔╝╚█████╔╝██║░░██║██║░░██║██████╔╝
╚═════╝░░░░╚═╝░░░      ╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░
""")

def main():
    print(f"Choose a function:\n"
          f"1: Choose picture and start draw")
    user_choice = int(input("Your choice: "))
    if user_choice == 1:
        try:
            print("You have five seconds to open the Roblox window.")
            draw = start_draw()
            if draw == True:
                main()
        except Exception as e:
            print(f"Erorr {e}")
    

if __name__ == "__main__":
    main()