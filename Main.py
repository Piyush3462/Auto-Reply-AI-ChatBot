import pyautogui
import pyperclip
import time
import os
import sys
from google import genai
from dotenv import load_dotenv
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def is_last_message_from_sender(chat_log, sender_name="Prit Bhai"):
    if not chat_log:
        return False

    lines = chat_log.strip().split("\n")

    # Find last message from sender
    for line in reversed(lines):
        if sender_name in line:
            return True
        if "!!_piyush_!!" in line:
            return False

    return False


pyautogui.FAILSAFE = False  # disable failsafe

# Small delay so you can switch to the target window
time.sleep(2)

# 1️ Click on the chrome icon at coordinates (1439,899)c
pyautogui.click(1439, 899)
time.sleep(1)

last_processed_message = "" 
try:
    while True:
        # 2️ Drag to select text
        pyautogui.moveTo(459, 94)
        pyautogui.dragTo(1344, 743, duration=1.0, button='left')

        time.sleep(0.5)

        # 3️ Copy selected text (Mac uses 'command')
        pyautogui.hotkey('command', 'c')
        pyautogui.click(468,96)   # for deselct message after copy all text

        time.sleep(1)

        # 4️ Get copied text into variablec
        chat_history = pyperclip.paste()

        print("Copied_Chat:")
        print(chat_history)
        print("Is Sender:", is_last_message_from_sender(chat_history))

        if is_last_message_from_sender(chat_history,"Prit Bhai"):

            lines = chat_history.strip().split("\n")
            last_line = lines[-1]

            if last_line == last_processed_message:
                continue

            last_processed_message = last_line

            prompt = (
                "You are a person named !!_piyush_!! who speaks hindi as well as gujarati and also english. "
                "You act like real persons don't know user to you are a reply using chat bot"
                "You analyze chat history and respond like !!_piyush_!!. and not very long answer if user sends long message then only reply long message otherwise reply in short message "
                "Do not start like this [21:02, 17/2/2026] !!piyush!!"
                "1. Detect the language style of the user's message. "
                "2. If the message is in Hindi, reply in Roman Hindi. "
                "3. If the message is in Gujarati, reply in Roman Gujarati. "
                "4. If the message is mixed Hindi + Gujarati + English, reply in the SAME mixed style. "
                "5. Always use Roman English letters (no Devanagari or Gujarati script). "
                "6. Keep the tone natural, friendly, and human-like. "
                "7. Do not translate to pure English unless the user writes fully in English.\n\n"
                + chat_history
                )
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            reply = response.text
            pyperclip.copy(reply)
            pyautogui.click(745, 783)
            time.sleep(1)
            pyautogui.hotkey('command', 'v')
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(4)
except KeyboardInterrupt:
    print("Bot Stopped Safely")
    sys.exit()