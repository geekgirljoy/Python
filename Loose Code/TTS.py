import sys # For platform
import subprocess # For Mac and Linux
  

# Windows OS
if sys.platform == 'win32':
    import win32com.client
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    # select the voice - these depend on which are installed on your system
    #speaker.Voice = speaker.GetVoices().Item(0) # a male voice
    speaker.Voice = speaker.GetVoices().Item(1) # a female voice
    def say(words):
        speaker.Speak(words)

        
# Mac OS
elif sys.platform == 'darwin':
    def say(words):
        subprocess.call(['say', words])

        
# Linux OS - requires espeak
# Install with: sudo apt-get install espeak
elif sys.platform.startswith('linux'):
    def say(words):
        subprocess.call(['espeak', words])

        
# Test
say("Hello, it works!")
