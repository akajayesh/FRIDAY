import os
import math
from django.shortcuts import redirect, render
import re 
from datetime import datetime
from .browser_help import open_website
from .models import ChatHistory

def friday_response(command):
    command = command.lower()

    # ==== Basic Greetings ====
    if command in ["Hi","hi", "hello", "hey", "HII", "Hey"]:
        return "Hi there! I'm FRIDAY. How can I help you?"
    
    elif "name" in command:
        return "I am F.R.I.D.A.Y — your assistant made by a cool developer 😎"

    elif "how are you" in command:
        return "I'm always operational 💻 What about you?"

    # ==== Application Openers ====
    elif "notepad" in command:
        os.system("start notepad")
        return "Opening Notepad ✏️"

    elif "paint" in command:
        os.system("start mspaint")
        return "Opening Paint 🎨"

    elif "calculator" in command:
        os.system("start calc")
        return "Opening Calculator 🧮"

    elif "command prompt" in command or "cmd" in command:
        os.system("start cmd")
        return "Opening CMD 🔲"

    elif "file explorer" in command:
        os.system("explorer")
        return "Opening File Explorer 📁"
    
    elif command in ["open clock", "start clock"]:
        os.system("start ms-clock:")
        return "Opening Clock ⏰"

    elif command in ["open microsoft store", "open store", "open ms store"]:
        os.system("start ms-windows-store:")
        return "Opening Microsoft Store 🏪"

    elif command in ["open settings", "open windows settings"]:
        os.system("start ms-settings:")
        return "Opening Windows Settings ⚙️"


    elif command in ["open media player", "start media player", "start music", "start music app", "open music"]:
        os.system("start mswindowsmusic:")
        return "Opening Media Player 🎶"

    elif command in ["open windows security", "open defender"]:
        os.system("start windowsdefender:")
        return "Opening Windows Security 🛡️"
    #return "Sorry, I couldn't understand that. Try something else?"

    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time} ⏰"

    elif "date" in command:
        current_date = datetime.now().strftime("%B %d, %Y")
        return f"Today's date is {current_date} 📅"

    elif "day" in command:
        day_name = datetime.now().strftime("%A")
        return f"Today is {day_name} 🗓️"

    # ==== Maths Commands ====
    elif "area of square" in command:
        try:
            side = float(command.split()[-1])
            return f"Area of square is {side ** 2:.2f} units²"
        except:
            return "Usage: area of square <side>"

    elif "perimeter of square" in command:
        try:
            side = float(command.split()[-1])
            return f"Perimeter of square is {4 * side:.2f} units"
        except:
            return "Usage: perimeter of square <side>"

    elif "area of rectangle" in command:
        try:
            parts = command.split()
            l = float(parts[-2])
            b = float(parts[-1])
            return f"Area of rectangle is {l * b:.2f} units²"
        except:
            return "Usage: area of rectangle <length> <breadth>"

    elif "perimeter of rectangle" in command:
        try:
            parts = command.split()
            l = float(parts[-2])
            b = float(parts[-1])
            return f"Perimeter of rectangle is {2 * (l + b):.2f} units"
        except:
            return "Usage: perimeter of rectangle <length> <breadth>"

    elif "area of circle" in command:
        try:
            r = float(command.split()[-1])
            return f"Area of circle is {math.pi * r * r:.2f} units²"
        except:
            return "Usage: area of circle <radius>"

    elif "circumference of circle" in command:
        try:
            r = float(command.split()[-1])
            return f"Circumference of circle is {2 * math.pi * r:.2f} units"
        except:
            return "Usage: circumference of circle <radius>"

    elif "area of triangle" in command:
        try:
            parts = command.split()
            b = float(parts[-2])
            h = float(parts[-1])
            return f"Area of triangle is {(0.5 * b * h):.2f} units²"
        except:
            return "Usage: area of triangle <base> <height>"

    elif "area of parallelogram" in command:
        try:
            parts = command.split()
            b = float(parts[-2])
            h = float(parts[-1])
            return f"Area of parallelogram is {b * h:.2f} units²"
        except:
            return "Usage: area of parallelogram <base> <height>"

    elif "area of trapezium" in command:
        try:
            parts = command.split()
            a = float(parts[-3])
            b = float(parts[-2])
            h = float(parts[-1])
            return f"Area of trapezium is {0.5 * (a + b) * h:.2f} units²"
        except:
            return "Usage: area of trapezium <a> <b> <height>"

    elif "area of ellipse" in command:
        try:
            a = float(command.split()[-2])
            b = float(command.split()[-1])
            return f"Area of ellipse is {math.pi * a * b:.2f} units²"
        except:
            return "Usage: area of ellipse <a> <b>"

    # === 3D SHAPES ===
    elif "volume of cube" in command:
        try:
            s = float(command.split()[-1])
            return f"Volume of cube is {s**3:.2f} units³"
        except:
            return "Usage: volume of cube <side>"

    elif "tsa of cube" in command or "surface area of cube" in command:
        try:
            s = float(command.split()[-1])
            return f"TSA of cube is {6 * s**2:.2f} units²"
        except:
            return "Usage: tsa of cube <side>"

    elif "volume of cuboid" in command:
        try:
            l, b, h = map(float, command.split()[-3:])
            return f"Volume of cuboid is {l*b*h:.2f} units³"
        except:
            return "Usage: volume of cuboid <l> <b> <h>"

    elif "tsa of cuboid" in command:
        try:
            l, b, h = map(float, command.split()[-3:])
            tsa = 2 * (l*b + b*h + h*l)
            return f"TSA of cuboid is {tsa:.2f} units²"
        except:
            return "Usage: tsa of cuboid <l> <b> <h>"

    elif "volume of sphere" in command:
        try:
            r = float(command.split()[-1])
            return f"Volume of sphere is {(4/3) * math.pi * r**3:.2f} units³"
        except:
            return "Usage: volume of sphere <radius>"

    elif "surface area of sphere" in command:
        try:
            r = float(command.split()[-1])
            return f"Surface area of sphere is {4 * math.pi * r**2:.2f} units²"
        except:
            return "Usage: surface area of sphere <radius>"

    elif "volume of cylinder" in command:
        try:
            r, h = map(float, command.split()[-2:])
            return f"Volume of cylinder is {math.pi * r**2 * h:.2f} units³"
        except:
            return "Usage: volume of cylinder <r> <h>"

    elif "tsa of cylinder" in command:
        try:
            r, h = map(float, command.split()[-2:])
            tsa = 2 * math.pi * r * (r + h)
            return f"TSA of cylinder is {tsa:.2f} units²"
        except:
            return "Usage: tsa of cylinder <r> <h>"

    elif "volume of cone" in command:
        try:
            r, h = map(float, command.split()[-2:])
            return f"Volume of cone is {(1/3) * math.pi * r**2 * h:.2f} units³"
        except:
            return "Usage: volume of cone <r> <h>"

    elif "tsa of cone" in command:
        try:
            r, l = map(float, command.split()[-2:])
            tsa = math.pi * r * (l + r)
            return f"TSA of cone is {tsa:.2f} units²"
        except:
            return "Usage: tsa of cone <r> <slant height>"

    elif "volume of hemisphere" in command:
        try:
            r = float(command.split()[-1])
            return f"Volume of hemisphere is {(2/3) * math.pi * r**3:.2f} units³"
        except:
            return "Usage: volume of hemisphere <radius>"

    elif "surface area of hemisphere" in command:
        try:
            r = float(command.split()[-1])
            return f"Surface area of hemisphere is {3 * math.pi * r**2:.2f} units²"
        except:
            return "Usage: surface area of hemisphere <radius>"

    elif command.lower() in [
        "fuck you", "fuck u", "fuck off", "bitch", "mc", "bc", 
        "randika", "raand", "rand", "puta", "coma mierda", "fk off",
        "f u", "fck u", "f**k you", "screw you", "idiot", "dumbass",
        "a**hole", "motherf***er", "moron", "loser", "chutiya","FUCK YOU", "Fuck you"
    ]:
        return "Use proper language only!"            
    # ==== System Controls (Careful) ====
    elif "shutdown" in command:
        return "Shutdown command is disabled for safety."

    elif "restart" in command:
        return "Restart command is disabled for now."

    elif command in ["open youtube", "open google", "open linkedin",
                     "open whatsapp", "open gfg", "open chatgpt", "open instagram",
                     "github", "open stackoverflow", "open goclasses"
    ]:
        keyword = command.replace("open ", "")
        return open_website(keyword)

    elif "open" in command:
        return "That app isn’t supported yet, boss. Wanna add it?"             

    else:
        return "Sorry, I didn’t understand that. Try another command?"

    # ==== Fallback ====

def home(request):
    response = None
    user_command = None
    close_browser = False

    if request.method == 'POST':
        user_command = request.POST.get('command')
        response = friday_response(user_command)

        if any(word in user_command.lower() for word in ["bye", "exit", "quit", "see you", "close", "goodbye"]):
           return redirect('/bye/')

        elif any(word in user_command.lower() for word in ["who made you", "who built you", "your creator", "your developer", "who is your dev"]):
            response = "I was created by — A Proud and Pragmatic Lad, named as Jayesh Eknath Sutar. ⚡"

        ChatHistory.objects.create(user_input=user_command, bot_response=response)

    history = ChatHistory.objects.order_by('-timestamp')[:10]
    return render(request, 'home.html', {
        'response': response,
        'user_command': user_command,
        'history': history,
        'close_browser' : close_browser
    })
