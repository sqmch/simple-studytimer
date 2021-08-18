# Studytimer

A very simple python script for setting a timer that ends with a Windows notification.

I personally use it to set [Pomodoro intervals](https://en.wikipedia.org/wiki/Pomodoro_Technique) for my study sessions.

## Setup

Create a virtual environment:
```
py -m venv venv
```
Install dependencies:
```
pip install -r requirements.txt
```

## How to use:
Run script with desired interval in ms (ex. 1500 for 25min):
```
python st.py 1500
```

---

I recommend setting an alias for convenience. How to set one varies a bit based on the type of terminal used. The alias will let you start the timer from anywhere on your CLI by just typing the chosen alias, for example "st".

PowerShell example (replace path):
```
function StudyTimer {python C:\dev\py\simple-studytimer\st.py 1500}
Set-Alias st StudyTimer
```

The above will make the command "st" start a 25min timer that ends with a Windows notification.

Note that you may need to put those lines in your profile.ps file so that they run each time. You can easily find the file by running the ```echo $profile``` command.
