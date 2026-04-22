# Setup Instructions

## Requirements

* Python 3.9+
* pip

---

## Run the App (Single Command)

```bash id="run01"
pip install -r requirements.txt && python seed.py && python app.py
```

---

## What This Does

1. Installs dependencies
2. Resets and seeds SQLite database (`app.db`)
3. Starts Flask development server

---

## Access the App

* Dashboard:
  http://127.0.0.1:5000/dashboard

* Signup (campaign-based):
  http://127.0.0.1:5000/signup?ref=1

* Create Campaign:
  http://127.0.0.1:5000/campaigns/new

---

## Campaign Flow

1. Admin creates campaign (e.g. "summer_launch")
2. Campaign is assigned an auto-generated **ID**
3. Sidebar dynamically lists campaigns
4. Signup uses:

   ```
   /signup?ref=<campaign_id>
   ```

---

## Notes

* SQLite is auto-generated via `seed.py`
* Database is reset on every run (MVP-friendly)
* No external services required
