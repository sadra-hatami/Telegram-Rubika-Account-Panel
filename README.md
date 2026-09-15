<div align="center">

# Telegram Rubika Account Panel
# 📱🤖📱

### A Telegram Control Panel for a Rubika User Account

A Python panel that receives commands in Telegram and applies them to a Rubika user account through the bundled `rubpy` client library.

<br>

# 👨‍💻 **Sadra Hatami**

### *Developer • Software Engineer • Creator*

<br>

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pyrogram](https://img.shields.io/badge/Telegram-Pyrogram-2AABEE?style=for-the-badge&logo=telegram&logoColor=white)](https://github.com/pyrogram/pyrogram)
[![Rubpy](https://img.shields.io/badge/Library-Rubpy-8E44AD?style=for-the-badge)](https://pypi.org/)
[![AsyncIO](https://img.shields.io/badge/AsyncIO-Asynchronous-2C3E50?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/library/asyncio.html)
[![Persian](https://img.shields.io/badge/Language-Persian-success?style=for-the-badge)](https://en.wikipedia.org/wiki/Persian_language)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
![GitHub](https://img.shields.io/badge/Open_Source-Project-black?style=for-the-badge&logo=github)

<br>

[🌐 GitHub Profile](https://github.com/sadra-hatami)
•
[📧 Email](mailto:sadra.hatami.1732@gmail.com)

</div>

---

# 📑 Table of Contents

- [About](#-about)
- [What This Project Is For](#-what-this-project-is-for)
- [Related Repositories](#-related-repositories)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Main File](#-main-file)
- [The rubpy Folder](#-the-rubpy-folder)
- [Technologies](#️-technologies)
- [Installation](#-installation)
- [Configuration](#️-configuration)
- [Usage](#️-usage)
- [Target Audience](#-target-audience)
- [Limitations](#-limitations)
- [FAQ](#-faq)
- [Security Notes](#-security-notes)
- [Contributing](#-contributing)
- [Contact](#-contact)
- [License](#-license)
- [Copyright](#-copyright)
- [Support](#-support)

---

# 📖 About

**Telegram Rubika Account Panel** is a Telegram-based control panel for a Rubika **user account**.

You talk to a Telegram bot built with **Pyrogram**. That bot then uses the bundled **rubpy** library to act on a Rubika account, such as reading account information or updating profile fields.

This repository is **not** a Rubika group bot. It does not join a group with a Rubika bot token and it does not lock group messages.

> **Tagline:** *A Telegram control panel for managing a Rubika user account with the rubpy library.*

---

# 🎯 What This Project Is For

Use this project when you want a **remote control in Telegram** for an account you own on Rubika.

It is for:

- Sending panel commands from Telegram
- Connecting that panel to a Rubika user session through `rubpy`
- Studying the difference between a user client and a group bot

It is **not** for:

- Managing a Rubika group
- Locking links, photos, or voice in a group
- Running AI, games, XP, or group reports

Those group features live in the other two repositories below.

---

# 🔗 Related Repositories

These three projects are related, but they are not the same thing.

| Repository | What it is | Library | Where it works |
|------------|------------|---------|----------------|
| **[Telegram Rubika Account Panel](https://github.com/sadra-hatami/Telegram-Rubika-Account-Panel)** | Telegram panel for a Rubika user account (this repo) | Pyrogram + `rubpy` | Telegram → user account |
| **[Rubika Group Bot](https://github.com/sadra-hatami/Rubika-Group-Bot)** | Simple group lock bot | `rubka` | Rubika groups |
| **[Rubika Advanced Group Bot](https://github.com/sadra-hatami/Rubika-Advanced-Group-Bot)** | Much more advanced group platform: locks, AI, games, XP, automation, SQLite | `rubka` | Rubika groups |

If you need a small group lock bot, use [Rubika Group Bot](https://github.com/sadra-hatami/Rubika-Group-Bot).  
If you need the much more advanced group bot, use [Rubika Advanced Group Bot](https://github.com/sadra-hatami/Rubika-Advanced-Group-Bot).  
If you need Telegram control over a Rubika user account, stay on this repository.

---

# ⚙️ How It Works

```text
You
 └─ Telegram chat
     └─ Pyrogram bot in sender.py
         └─ rubpy.Client
             └─ Rubika user account
```

1. `sender.py` starts a Telegram bot.
2. The owner presses a button or sends a reply.
3. The script opens `rubpy.Client`.
4. rubpy applies the action to the Rubika user account.
5. The Telegram bot shows the result.

The Telegram bot is only the remote control. The Rubika work happens inside `rubpy`.

---

# 📁 Project Structure

```text
Telegram-Rubika-Account-Panel/
├── sender.py
└── rubpy/
    ├── __init__.py
    ├── client.py
    ├── crypto/
    ├── gadgets/
    ├── network/
    ├── sessions/
    ├── structs/
    └── sync/
```

- `sender.py` — Telegram panel
- `rubpy/` — bundled Rubika user-client library

---

# 📄 Main File

`sender.py` creates the Telegram bot, asks the owner for input when needed, and calls `rubpy.Client`.

Typical panel actions:

- Show basic account information
- Edit first name, last name, and bio
- Work with a saved Rubika session name

The public token field should stay a placeholder. Put the real Telegram bot token in environment variables.

---

# 📦 The rubpy Folder

`rubpy` is a third-party user-account library (version `6.4.7` in this repo). It is included next to `sender.py` so the panel can import it without a separate install.

This is not the `rubka` library used by the group bots.

---

# 🛠️ Technologies

- Python 3.8+
- Pyrogram
- rubpy 6.4.7 (bundled)
- asyncio

---

# 🚀 Installation

```bash
git clone https://github.com/sadra-hatami/Telegram-Rubika-Account-Panel.git
cd Telegram-Rubika-Account-Panel
pip install pyrogram tgcrypto
```

```bash
python sender.py
```

---

# ⚙️ Configuration

```python
import os

api_id = int(os.environ["TELEGRAM_API_ID"])
api_hash = os.environ["TELEGRAM_API_HASH"]
token = os.environ["TELEGRAM_BOT_TOKEN"]
```

Ignore local secrets:

```text
.env
*.session
*.session-journal
downloads/
__pycache__/
```

---

# ▶️ Usage

1. Set Telegram API values and the bot token.
2. Run `sender.py`.
3. Open the Telegram bot as the owner.
4. Use the panel only with a Rubika account you own.

---

# 🎓 Target Audience

- Developers comparing a user-account client with a group bot
- People who want a Telegram remote control for their own Rubika account
- Maintainers documenting this panel next to the two group bots

---

# ⚠️ Limitations

- This is a single-script panel, not a group-management platform.
- Rubika login depends on a valid user session.
- Leftover third-party strings in `sender.py` should be removed before a public release.
- Use it only on accounts you control.

---

# ❓ FAQ

### Is this a group bot?

No. Group bots use `rubka` and a Rubika bot token. This panel uses Telegram + `rubpy` and a user session.

### Where is the simple group bot?

[Rubika Group Bot](https://github.com/sadra-hatami/Rubika-Group-Bot)

### Where is the advanced group bot?

[Rubika Advanced Group Bot](https://github.com/sadra-hatami/Rubika-Advanced-Group-Bot)

### Can I use this instead of adding a bot to a group?

No. This project does not replace group locks, games, AI, or group reports.

### Why is `rubpy` inside the repo?

So `sender.py` can import the user client without installing that package separately.

---

# 🔐 Security Notes

- Never commit a real Telegram bot token.
- Never commit Rubika session files.
- Move `api_id` and `api_hash` to environment variables.
- Remove leftover usernames and external API URLs from `sender.py`.

---

# 🤝 Contributing

Cleanup pull requests are welcome, especially for secret handling and unused leftover code.

---

# 📬 Contact

**Developer:**

### Sadra Hatami

📧 [Email](mailto:sadra.hatami.1732@gmail.com)

🌐 [GitHub](https://github.com/sadra-hatami)

---

# 📄 License

This project is licensed under the **MIT License**.

The bundled `rubpy` package is third-party code and keeps its original authorship.

---

# © Copyright

© 2026 **Sadra Hatami** — panel presentation and repository layout

`rubpy` remains the work of its original author.

---

# ⭐ Support

If this repository helped you understand the difference between a group bot and a user-account panel, please consider giving it a ⭐ on GitHub.

---

<div align="center">

## Designed & Developed with ❤️ for the developer community of Iran and the world by **Sadra Hatami**

</div>
