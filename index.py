import pyautogui
import pygetwindow as gw
import time

# ambil semua window chrome yang terlihat
browsers = [w for w in gw.getWindowsWithTitle('') if 'chrome' in w.title.lower() and w.visible]

text = 'ibusayang'

if not browsers:
    print("Tidak ada window Chrome ditemukan.")
    exit()

print(f"Menemukan {len(browsers)} window Chrome:")
for i, win in enumerate(browsers):
    print(f"{i + 1}. {win.title}")

print("\nMemulai rotasi fokus (setiap 10 detik)...\n")

# proses setiap window hanya sekali
for i, win in enumerate(browsers):
    try:
        win.activate()
        print(f"Fokus ke Chrome #{i + 1} - {win.title}")
        time.sleep(3)

        input_box = pyautogui.locateOnScreen('box.png', confidence=0.7)

        if input_box: 
            center_x, center_y = pyautogui.center(input_box)

            pyautogui.click(center_x, center_y)
            time.sleep(1)

            pyautogui.write("aku sayang kamu", interval=0.05)
            print("BERHASIL NGETIk")

            pyautogui.keyDown("Enter")
        else:
            print("Gambar gak di temuin bang")

    except Exception as e:
        print(f"Gagal mengaktifkan window: {e}")
        continue

print("\nSemua window Chrome sudah difokuskan. Program selesai.")