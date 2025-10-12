<div align="center">

<a href="https://files.catbox.moe/j2yhce.jpg">
  <img src="https://files.catbox.moe/j2yhce.jpg" width="300" height="300" />
</a>

----------------------------------------------------
A **Group Manager Bot** built with **Pyrogram** + **MongoDB** for managing Telegram groups

</div>

---

## ⭐ Features
- **Owner Command**: `/broadcast`, `/stats`
- **Group Moderation**: kick, ban/unban, mute/unmute, warn, warns, resetwarns, promote/demote  
- **Auto Welcome System** with placeholders (`{username}`, `{mention}`, etc.)  
- **Dynamic Start Message** with text, image, and inline buttons  
- **MongoDB Storage** for data persistence  
- **Beautiful Inline UI** and modular codebase  

---
<details>
<summary><b>🔸 Deploy on VPS / Localhost</b></summary>

### 1. Fork & Star ⭐
- Click **Fork** (top-right of GitHub repo)  
- Then click **Star** ⭐ to support this project!  

---

### 2. Get Your Fork URL
```
https://github.com/<your-username>/group_manager_bot.git
```

---

### 3. Setup Your VPS
Install system packages:
```
sudo apt update && sudo apt upgrade -y
sudo apt install -y git python3 python3-pip python3-venv tmux nano
```

---

### 4. Clone Your Fork
```
git clone https://github.com/<your-username>/group_manager_bot.git
cd group_manager_bot
python3 -m venv venv
source venv/bin/activate
```

---

### 5. Install Dependencies
```
pip install --upgrade pip && pip install -r requirements.txt
```

---

### 6. Configure the Bot
```
nano config.py
```

⚙️ required fields

```
API_ID = your_api_id
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"
MONGO_URL = "your_mongodb_url"
OWNER_ID = your_tg_id
```

✅ Save with: `Ctrl + O`, then Enter  
❌ Exit with: `Ctrl + X`

### 7. Run the Bot
```
tmux new -s groupbot
source venv/bin/activate
python3 main.py
```

➡️ Detach (keep it running): `Ctrl + B`, then `D`

</details>

---

<p align="center">
  <a href="https://sevalla.com"><img src="https://img.shields.io/badge/Deploy%20on-Sevalla-orange?style=for-the-badge&logo=vercel"></a>
</p>

> ✅ You can easily deploy this Group help bot on **[Sevalla](https://sevalla.com)** – A powerful and beginner-friendly hosting platform.
---

<div align="center">

### ☕ Support Me!
If you enjoy my work, consider buying me a coffee ❤️  

<a href="https://files.catbox.moe/4elv8g.jpg" target="_blank">
  <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="45" width="190" alt="Buy Me a Coffee" />
</a>

</div>

---

## 📱 Connect with Me

<p align="center">
<a href="https://www.instagram.com/learning_bots"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"></a>
<a href="https://t.me/learning_bots"><img src="https://img.shields.io/badge/Telegram%20Group-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"></a>
<a href="https://t.me/learningbots79"><img src="https://img.shields.io/badge/Telegram%20Channel-0088cc?style=for-the-badge&logo=telegram&logoColor=white"></a>
<a href="https://youtube.com/@learning_bots?si=aNUuRSfZD7na78GM"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white"></a>
</p>

---

## ⚠️ License / Usage Terms

This project is open-source under a **custom license** by [Yash](https://github.com/learningbots79).

✅ You Can:
- Use this code for personal or educational purposes  
- Host your own version **with proper credits**  
- Modify or improve the code (while keeping credit intact)

🚫 You Cannot:
- Remove author credits or change project name  
- Sell, rent, or resell this code or any modified version  
- Claim ownership or re-upload it without permission  

If you want to use this project commercially,  
please contact the author at [@learningbots79](https://t.me/learningbots79).

---

**Author:** [learningbots79](https://github.com/learningbots79)  
**Support Group:** [@learning_bots](https://t.me/learning_bots)  
**Update Channel:** [@learningbots79](https://t.me/learningbots79)  
**YouTube:** [Learning Bots](https://youtube.com/@learning_bots)
