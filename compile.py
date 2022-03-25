import os

files = [
    "srcs\\commands\\end.py",
    "srcs\\commands\\start.py",
    "srcs\\commands\\turn.py",
    "srcs\\commands\\begin.py",
    "srcs\\commands\\info.py",
    "srcs\\commands\\end.py",
    "srcs\\commands\\about.py",
    "srcs\\utils.py",
    "srcs\\gameManager.py",
    "srcs\\ai.py",
    "srcs\\moves.py",
]

files_list = ""
for file in files:
    files_list += " " + file

os.system("pip install pyinstaller")
os.system("pyinstaller main.py" + files_list + " --name pbrain-gomoku-ai.exe --onefile")
os.system("copy .\\dist\\pbrain-gomoku-ai.exe .")
