# text to speech programm

'''import win32com.client
 
speaker = win32com.client.Dispatch("SAPI.SpVoice")
s = input("enter a text:")
speaker.Speak(s)'''

import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
s = input("enter a text:")
speaker.Speak(s)

