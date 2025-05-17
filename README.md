# 🤖 FRIDAY – Personal Assistant Chatbot

FRIDAY is a smart, local assistant chatbot built using **Python, Django, and basic frontend tools**. It simulates a human-like assistant that can interact, perform calculations, open apps, respond to natural prompts, and much more.

---

## 🚀 Features

- 🧠 Smart response handling (greetings, vulgarity filters, shutdown, etc.)
- 🧮 Geometry calculator (area, volume, surface area for 2D/3D shapes)
- 🕰️ Displays live time, date, and day
- 🌐 Opens selected websites (YouTube, Google, LinkedIn, etc.)
- 💬 Stores and displays last 10 chat messages
- 🎨 Clean, color based UI with OnePlus Sans font
- 💻 Built from scratch in C originally, now ported to Django
- 💾 SQLite database integration
- 🎬 Typing animation for smoother UX
- ❌ Handles grammatical mistakes and loose command prompts
- 🔒 Gracefully shuts down with farewell messages

---

## 🛠️ Tech Stack

| Frontend | Backend | Database | Hosting |
|----------|---------|----------|---------|
| HTML, CSS | Python (Django) | SQLite | GitHub (code) / Render (optional) |

---

## 💻 How to Run Locally

```bash
git clone https://github.com/akajayesh/FRIDAY.git
cd FRIDAY
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


⚠️ Note: This project is hosted on Render’s free plan.  
The service **sleeps after 15 minutes** of inactivity to save server cost.  
Please allow 10–20 seconds for the bot to wake up if it's been idle.

✅ Local version supports full functionality like app opening and system-level tasks.  
🌐 Cloud version handles website redirects, chat, date, time, and math commands.
