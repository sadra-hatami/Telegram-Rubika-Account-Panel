<div align="center">

# Telegram Rubika Account Panel
# 📱🤖

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

</div>

---

# 📑 Table of Contents

- [About](#-about)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Technologies](#️-technologies)
- [Usage](#️-usage)
- [Configuration](#️-configuration)
- [Target Audience](#-target-audience)
- [Security Notes](#-security-notes)
- [Related Repositories](#-related-repositories)
- [Contributing](#-contributing)
- [Contact](#-contact)
- [License](#-license)
- [Copyright](#-copyright)
- [Support](#-support)

---

# 📖 About

**Telegram Rubika Account Panel** is a Python project that connects two sides:

- A Telegram bot built with **Pyrogram** as the control interface
- A Rubika user client built with **rubpy** as the account side

The operator talks to the Telegram bot. The script then uses a local `rubpy` package to act on a Rubika user account, such as reading account information or updating profile fields.

This is not a Rubika group-management bot. Group bots in this profile use `rubka` and a bot token. This panel uses a user-account client.

> **Tagline:** *A Telegram control panel for managing a Rubika user account with the rubpy library.*

---

# ⚙️ How It Works

1. `sender.py` starts a Telegram bot with Pyrogram.
2. The operator sends commands or button actions in that Telegram chat.
3. The script opens a `rubpy.Client` session.
4. The requested action is applied to the linked Rubika account.

```text
Telegram (Pyrogram)  →  sender.py  →  rubpy.Client  →  Rubika user account
```

---

# 📁 Project Structure

```text
Telegram-Rubika-Account-Panel/
├── sender.py          # Telegram panel and Rubika client calls
└── rubpy/             # Bundled rubpy user-client library
    ├── client.py
    ├── crypto/
    ├── gadgets/
    ├── network/
    ├── sessions/
    ├── structs/
    └── sync/
```

`rubpy` is vendored next to `sender.py` so the panel can import it without a separate install step.

---

# 🛠️ Technologies

- Python 3.8+
- Pyrogram (Telegram bot interface)
- rubpy 6.4.7 (bundled Rubika user client)
- asyncio

---

# ▶️ Usage

```bash
git clone https://github.com/sadra-hatami/Telegram-Rubika-Account-Panel.git
cd Telegram-Rubika-Account-Panel
pip install pyrogram tgcrypto
```

Then set your own Telegram bot token and owner ID in `sender.py` through environment variables, not hardcoded values. Start the panel with:

```bash
python sender.py
```

Use the bot only with an account you own. Do not publish tokens, sessions, or API secrets.

---

# ⚙️ Configuration

Move secrets out of the source file:

```python
import os

api_id = int(os.environ["TELEGRAM_API_ID"])
api_hash = os.environ["TELEGRAM_API_HASH"]
token = os.environ["TELEGRAM_BOT_TOKEN"]
```

Add a `.gitignore` for session files, downloads, and `.env`.

---

# 🎓 Target Audience

- Developers studying how a Telegram bot can drive another client library
- People comparing `rubka` group bots with `rubpy` user clients

This repository is a technical panel, not a replacement for [Rubika Group Bot](https://github.com/sadra-hatami/Rubika-Group-Bot) or [Rubika Advanced Group Bot](https://github.com/sadra-hatami/Rubika-Advanced-Group-Bot).

---

# 🔐 Security Notes

- Never commit a real Telegram bot token.
- Never commit Rubika session files.
- Keep `api_id` and `api_hash` in environment variables.
- Remove leftover third-party usernames and external API URLs before a public release.
- Use the panel only on accounts you control.

---

# 🔗 Related Repositories

- [Rubika Group Bot](https://github.com/sadra-hatami/Rubika-Group-Bot) — small group lock bot (`rubka`)
- [Rubika Advanced Group Bot](https://github.com/sadra-hatami/Rubika-Advanced-Group-Bot) — full group platform (`rubka`)

---

# 🤝 Contributing

Suggestions and cleanup pull requests are welcome, especially for secret handling and removing leftover third-party strings.

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

If this repository helped you understand the difference between a Rubika group bot and a user-account client, please consider giving it a ⭐ on GitHub.

---

<div align="center">

## Designed & developed with ❤️ for the developer community of Iran and the world by **Sadra Hatami**

</div>
