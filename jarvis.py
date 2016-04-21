import speech_recognition as sr
import jarvis_metro as jm
import jarvis_tts as jtts
import settings
import pdb

modules = {"metro": jm.process_command}

def sphinx_stt(audio):
    try:
        import pocketsphinx
    except:
        import pocketsphinx
    try:
        return (r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        return ("error could not process")
    except sr.RequestError as e:
        return ("Sphinx error; {0}".format(e))

def google_stt(audio):
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        return (r.recognize_google(audio))
    except sr.UnknownValueError:
        return("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        return("Could not request results from Google Speech Recognition service; {0}".format(e))

def process_command(command):
    for module in modules:
        if module in command:
            modules[module](command)
            return
    jtts.jarvis_tts(["Command Not Found"])


if __name__ == "__main__":
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    result_sphinx = sphinx_stt(audio)
    if "jack" in result_sphinx:
        result_google = google_stt(audio)
        process_command(result_google.lower())
    else:
        jtts.jarvis_tts(["Commands Must Start With Jack"])
