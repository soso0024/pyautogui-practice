import pyautogui
from time import sleep

# These command are used to open Youtube on your browser
pyautogui.click(400, 50)  # Click to put drawing program in focus
pyautogui.typewrite("youtube.com")  # Type in the URL
pyautogui.typewrite(["enter"])  # Press the Enter key

sleep(5)

pyautogui.click(150, 390)  # Click on playlists botton

sleep(2)

pyautogui.click(
    450, 590
)  # Click on the study bgm playlist, you should manage the coordinates according to your screen
