import pygetwindow as gw
import time

# ambil semua window chrome yang terlihat
browsers = [w for w in gw.getWindowsWithTitle('') if 'chrome' in w.title.lower() and w.visible]

if not browsers:
    print("Tidak ada window Chrome ditemukan.")
    exit()

current_index = 0

while True:
    # ambil window chrome sesuai index
    win = browsers[current_index]
    win.activate()
    print(f"Fokus ke Chrome #{current_index + 1} - {win.title}")

    # tunggu 10 detik
    time.sleep(10)

    # pindah ke chrome berikutnya
    current_index += 1
    if current_index >= len(browsers):
        current_index = 0   # ulang dari awal
