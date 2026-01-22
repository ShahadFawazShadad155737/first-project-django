import datetime

name = input("Enter your name: ")

hour = datetime.datetime.now().hour

if hour < 12:
    greeting = "Good morning"
    motivational_phrase = "Remember that every day is a new opportunity to change your life."
elif hour < 18:
    greeting = "Good afternoon"
    motivational_phrase = "Enjoy the little things, for they are what make a big day."
else:
    greeting = "Good evening"
    motivational_phrase = "Relax, recharge, and prepare for a successful tomorrow."

print(greeting, name)
print(motivational_phrase)