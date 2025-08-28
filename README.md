
# Discord Role Deleter Bot By NAINOO

A Discord bot that allows server administrators to delete **all roles** safely with confirmation.  

⚠️ **Warning:** This bot will permanently delete roles (except `@everyone` and roles higher than the bot). Use only on servers you control.



## Features

- Delete all roles in a server with a confirmation prompt.
- Only executable by administrators.
- Skips `@everyone` and roles above the bot’s top role.
- Shows a confirmation message before deleting.



## Requirements

- Python 3.11+
- [discord.py](https://pypi.org/project/discord.py/)

Install dependencies:

```bash
pip install -r requirements.txt
````

---

## Setup

1. Clone or download this repository.
2. Create a `bot.py` file and copy the code from the bot script.
3. Replace `"YOUR_BOT_TOKEN"` with your Discord bot token.
4. Run the bot:

```bash
python bot.py
```

---

## Usage

1. Type `!delroles` in your server.
2. Bot will ask for confirmation:

   ```
   ⚠️ Are you sure you want to delete ALL roles in this server?
   Type !confirmdel within 30 seconds to continue.
   ```
3. Type `!confirmdel` to delete all roles.
4. The bot will respond with how many roles were deleted.

---

## Notes

* Make sure the bot’s role is **higher than the roles you want to delete** and has **Manage Roles** permission.
* Roles that the bot cannot delete (higher than its top role) will be skipped.
* Use this bot **responsibly** to avoid accidental permission loss.

---

## License

This project is open-source. Use it at your own risk.

```

---

If you want, I can also make a **full zip-ready project structure** with `bot.py`, `requirements.txt`, and `README.md` ready to run immediately.  

Do you want me to do that?
```
