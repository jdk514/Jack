
import subprocess, importlib
import jarvis_metro as jm
import settings
#importlib.import_module("jarvis_metro")

import pdb

def_loc = os.environ['default_location']

def jarvis_tts(text_list):
    for text in text_list:
        try:
            command = "pico2wave -w lookdave.wav \"%s\" && aplay lookdave.wav" % text
            subprocess.check_output(command, shell=True)
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))


if __name__ == "__main__":
    text_list = jm.get_train_text(def_loc["station"], def_loc["destination"], def_loc["color"])
    jarvis_tts(text_list)
