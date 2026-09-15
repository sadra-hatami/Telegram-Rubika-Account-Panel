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

</div>

---

# 📑 Table of Contents

- [About](#-about)
- [Why This Project?](#-why-this-project)
- [How It Works](#-how-it-works)
- [What Each Side Does](#-what-each-side-does)
- [Project Structure](#-project-structure)
- [Main File](#-main-file)
- [The rubpy Folder](#-the-rubpy-folder)
- [Technologies](#️-technologies)
- [Usage](#️-usage)
- [Configuration](#️-configuration)
- [Target Audience](#-target-audience)
- [Limitations](#-limitations)
- [Security Notes](#-security-notes)
- [Related Repositories](#-related-repositories)
- [FAQ](#-frequently-asked-questions)
- [Contributing](#-contributing)
- [Contact](#-contact)
- [License](#-license)
- [Copyright](#-copyright)
- [Support](#-support)

---

# 📖 About

**Telegram Rubika Account Panel** is a two-part Python project.

The first part is a Telegram bot written with **Pyrogram**. That bot is the control panel: you open it in Telegram, press buttons, and send replies.

The second part is a Rubika **user-account** client written with **rubpy**. That client logs into a Rubika account the same way a normal app user would, not the way a group bot logs in with a bot token.

When you tap a button in Telegram, `sender.py` translates that action into a `rubpy.Client` call. The result comes back to the same Telegram chat.

This repository is not a Rubika group-management bot. The group bots in this profile use the `rubka` library. This panel uses `rubpy` and a user session.

> **Tagline:** *A Telegram bot panel, built with Pyrogram and rubpy, that controls a Rubika user account instead of a group bot.*

---

# 🚀 Why This Project?

Rubika bots and Rubika user clients are easy to mix up.

- A **group bot** joins a group with a token and manages that group.
- A **user client** signs into a personal account and can see that account's profile, chats, and contacts.

This project exists to keep a Telegram-based control layer on top of a user client. The Telegram bot is only the remote control. The actual Rubika work happens inside `rubpy`.

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
2. Only the configured owner can use the panel.
3. A callback button or a reply message chooses an action.
4. The script opens `async with rubpy.Client(session_name)`.
5. rubpy sends the request to Rubika and returns the result.
6. The Telegram bot shows a short status message.

The bundled `rubpy` package talks to Rubika infrastructure such as `web.rubika.ir`. It is a third-party user client, not the official Rubika bot API.

---

# 🔀 What Each Side Does

| Side | Library | Account type | Role |
|------|---------|--------------|------|
| Telegram panel | Pyrogram | Telegram bot token | Buttons, questions, status messages |
| Rubika account | rubpy | User session | Profile and account actions |
| Group bots in this profile | rubka | Rubika bot token | Group locks and moderation |

If you need group locks, use [Rubika Group Bot](https://github.com/sadra-hatami/Rubika-Group-Bot) or [Rubika Advanced Group Bot](https://github.com/sadra-hatami/Rubika-Advanced-Group-Bot). Those projects are separate.

---

# 📁 Project Structure

```text
Telegram-Rubika-Account-Panel/
├── sender.py
└── rubpy/
    ├── __init__.py          # exports Client, Message, handlers
    ├── client.py            # main async Rubika client
    ├── emoji.py
    ├── crypto/              # request encryption
    ├── gadgets/             # helpers, methods, errors
    ├── network/             # connection and proxy helpers
    ├── sessions/            # saved login sessions
    ├── structs/             # message and result models
    └── sync/                # non-async copy of the same client
```

`sender.py` is the panel.  
`rubpy/` is the engine.

---

# 📄 Main File

`sender.py` is the only application file.

It does three jobs:

1. **Creates the Telegram bot** with Pyrogram (`Client`, callback buttons, owner filter).
2. **Asks the operator for input** with `Bot.ask(...)` when a field is needed, such as a new first name or bio.
3. **Calls rubpy** inside `async with rubpy.Client(name)` to apply the change on the Rubika account.

Typical panel actions in the current script:

- Show basic account information
- Edit first name, last name, and bio
- Work with a saved Rubika session name
- Receive a document in Telegram and store it locally

The Telegram token in the public file is a placeholder (`توکن بزار`). Replace it through environment variables. Do not commit a real token.

---

# 📦 The rubpy Folder

`rubpy` is a vendored third-party library (version `6.4.7` in `__init__.py`).

It is included next to `sender.py` so the panel can run with:

```python
import rubpy
async with rubpy.Client(name) as app:
    ...
```

Important pieces:

- `Client` — login and API calls
- `sessions/` — how a login is stored after the first sign-in
- `network/` — connection details
- `crypto/` — request protection
- `sync/` — the same client without asyncio

This folder is not a Rubika group-bot SDK. It is a user-account SDK.

---

# 🛠️ Technologies

- Python 3.8+
- Pyrogram
- rubpy 6.4.7 (bundled)
- asyncio

No web server and no database are required for the panel itself. rubpy may create local session files after login.

---

# ▶️ Usage

```bash
git clone https://github.com/sadra-hatami/Telegram-Rubika-Account-Panel.git
cd Telegram-Rubika-Account-Panel
pip install pyrogram tgcrypto
```

Set secrets first, then start the panel:

```bash
python sender.py
```

Open the Telegram bot as the owner account and use the on-screen buttons.

Use this only with a Rubika account you own.

---

# ⚙️ Configuration

Keep secrets outside the repository:

```python
import os

api_id = int(os.environ["TELEGRAM_API_ID"])
api_hash = os.environ["TELEGRAM_API_HASH"]
token = os.environ["TELEGRAM_BOT_TOKEN"]
```

Also ignore local files that must never be committed:

```text
.env
*.session
*.session-journal
downloads/
__pycache__/
```

---

# 🎓 Target Audience

- Developers who want to see a Telegram bot driving another Python client
- Learners comparing `rubka` group bots with `rubpy` user clients
- Maintainers cleaning and documenting this panel

---

# ⚠️ Limitations

- The panel is a single script, not a packaged app.
- Rubika login depends on a valid user session.
- Some strings in `sender.py` are leftovers from older edits and should be removed.
- Features that touch other people's accounts, bulk sending, or third-party lookup APIs should not be used.

---

# 🔐 Security Notes

- Never commit a real Telegram bot token.
- Never commit Rubika session files.
- Move `api_id` and `api_hash` to environment variables.
- Remove leftover third-party usernames and external API URLs.
- Do not share this panel with people who should not control the target account.

---

# 🔗 Related Repositories

- [Rubika Group Bot](https://github.com/sadra-hatami/Rubika-Group-Bot) — small group lock bot
- [Rubika Advanced Group Bot](https://github.com/sadra-hatami/Rubika-Advanced-Group-Bot) — full group platform

---

# ❓ Frequently Asked Questions

### Is this a Rubika group bot?

No. A group bot uses a Rubika bot token and the `rubka` library. This project controls a user account from Telegram.

### Why is the `rubpy` folder inside the repo?

So `sender.py` can import the client without installing the package separately.

### Can I use it without Telegram?

Not in the current design. Telegram is the remote control. rubpy is the account client.

### Does it need a server?

Only a machine that can run Python and stay online while you use the panel.

---

# 🤝 Contributing

Cleanup pull requests are welcome, especially for secret handling, unused functions, and leftover third-party strings.

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
