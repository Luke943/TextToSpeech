import os
import time

import gtts
from playsound import playsound

TEMP_FILE = "temp.mp3"

MENU_OPTIONS = [
    "Enter text",
    "Read text from file",
    "Select language",
    "View all languages",
    "Exit",
]


def main():
    print("=== CLI TEXT TO SPEECH ===")
    print("Language: en")

    lang = "en"

    while True:
        for i, item in enumerate(MENU_OPTIONS):
            print(f"{i + 1}. {item}")

        while True:
            selection = input()
            try:
                option = MENU_OPTIONS[int(selection) - 1]
                break
            except:
                print(f"Invalid selection. Select 1 to {len(MENU_OPTIONS)}.")

        match option:
            case "Enter text":
                speak_text(input("Enter text... "), lang)
            case "Read text from file":
                filename = input("Enter filename... ")
                with open(filename, "r") as f:
                    text = f.read()
                    speak_text(text, lang)
            case "Select language":
                lang = input("Enter a language... ")
            case "View all languages":
                print(gtts.lang.tts_langs())
            case "Exit":
                return


def speak_text(text: str, lang: str):
    tts = gtts.gTTS(text, lang=lang)
    tts.save(TEMP_FILE)
    playsound(TEMP_FILE)
    os.remove(TEMP_FILE)


if __name__ == "__main__":
    main()
