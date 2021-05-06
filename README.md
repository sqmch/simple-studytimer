# Studytimer

A very simple python script for setting a timer that ends with a Windows notification.

I personally use it to set my [Pomodoro intervals](https://en.wikipedia.org/wiki/Pomodoro_Technique) for my study sessions.

## How to use

Create a virtual environment:
```
py -m venv venv
```
Install dependencies:
```
pip install -r requirements.txt
```
Run script with desired interval in ms (ex. 1500 for 25min):
```
py st.py 1500
```

---

I recommend setting an alias for convenience. How to set one varies a bit based on the type of terminal used. The alias will let you start the timer from anywhere on your CLI by just typing the chosen alias, for example "st".

I use [cmder](https://cmder.net/) and the way to set an alias on cmder is:
```
alias <name_of_alias>=cd c:/your_path/to_script_folder &t py st.py <your_desired_interval>
```
Example:
```
alias st=cd c:/pythonprojects/studytimer &t py st.py 1500
```
The above will make the command "st" start a 25min timer.
