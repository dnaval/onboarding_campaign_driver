# 🚚 Driver Onboarding & Campaign Tracking System

A lightweight Flask application that simulates a driver acquisition funnel with campaign tracking, vehicle registration, and analytics dashboard.

The system demonstrates how different acquisition channels (Facebook, Google, Referral) convert into completed driver sign-ups.

---

## Features

### Driver Onboarding Flow
- Driver sign-up form (name, email, phone, license info)
- Campaign tracking via URL parameter: /signup?ref=<campaign_id>

- Multi-step flow with vehicle registration

---

### Vehicle Registration
- Vehicle details per driver
- Insurance validation (expiry-based)
- Supports multiple vehicles per driver

---

### Campaign Dashboard
- Total sign-ups per campaign
- Completed sign-ups (valid insured vehicles)
- Conversion rate per campaign
- Sign-ups over time (Chart.js visualization)
- Date range filtering

---

### Campaign Management
- Dynamic campaign creation via UI
- Campaigns stored in database:
- `id` (used in URLs)
- `name` (display label)
- `source` (facebook, google, referral)
- Sidebar auto-updates based on database content

---

## Tech Stack

- Python 3
- Flask
- SQLAlchemy
- SQLite
- Jinja2 Templates
- Chart.js (frontend charts)

---

## 🗂 Project Structure
app/
app.py
models.py
routes.py
database.py
templates/
base.html
signup.html
vehicle.html
dashboard.html
create_campaign.html
seed.py
requirements.txt

## Author
Wrapped Media
Engineer: Daniel Naval