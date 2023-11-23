# // ---------------------------------------------------------------------
# // ------- [Welcome Bot] Pretty Print
# // ---------------------------------------------------------------------

# // ---- Imports
import os
import datetime
import colorama as tcolor

tcolor.init()
os.system("color") # for windows. enables ansi or whatever

# // ---- Main
# // Print
def __setup(title: str, msg: str, emoji: str, style: str, color: str):
    return f"{style}{color}[{title}] [{datetime.datetime.now()}]{tcolor.Fore.RESET} {emoji} | {msg}{tcolor.Style.RESET_ALL}"

def warn(msg: str):
    print(__setup("WARNING", msg, "⚠", tcolor.Style.DIM, tcolor.Fore.LIGHTYELLOW_EX))

def info(msg: str):
    print(__setup("INFO", msg, "📚", tcolor.Style.DIM, tcolor.Fore.LIGHTBLACK_EX))
    
def error(msg: str):
    print(__setup("ERROR", msg, "❌", tcolor.Style.DIM, tcolor.Fore.LIGHTRED_EX))

def success(msg: str):
    print(__setup("SUCCESS", msg, "✅", tcolor.Style.DIM, tcolor.Fore.LIGHTGREEN_EX))
    
# // Input
def query(msg: str):
    return input(__setup("INPUT", msg, "💻", tcolor.Style.DIM, tcolor.Fore.LIGHTBLUE_EX))