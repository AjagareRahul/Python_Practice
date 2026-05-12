'''import tkinter as tk

lyrics = """खुदा भी जब तुम्हें
मेरे पास देखता होगा
इतनी अनमोल चीज़
दे दी कैसे, सोचता होगा!

तू बेमिसाल है,
तेरी क्या मिसाल दूँ
आसमान से आई है,
यही कह के टाल दूँ
"""

root = tk.Tk()
root.title("🎧 Lyrics Player")
root.geometry("500x400")

label = tk.Label(root, text=lyrics, font=("Arial", 14), justify="center")
label.pack(pady=50)

root.mainloop()'''


import time
import sys

lyrics = """खुदा भी जब तुम्हें
मेरे पास देखता होगा
इतनी अनमोल चीज़
दे दी कैसे, सोचता होगा!
"""

for char in lyrics:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)   # typing speed