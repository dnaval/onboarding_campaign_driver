from database import SessionLocal, engine, Base
from models import Campaign, Driver, Vehicle
from datetime import datetime, timedelta, date
import random

# Reset DB (simple MVP approach)
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# --- Campaigns ---
campaign_sources = {
    "summer_launch": "facebook",
    "black_friday": "google",
    "referral_bonus": "referral",
}

campaigns = {}

for name, source in campaign_sources.items():
    campaign = Campaign(name=name, source=source)
    db.add(campaign)
    db.commit()
    campaigns[name] = campaign

# --- Fake Data ---
first_names = ["John", "Jane", "Mike", "Anna", "Chris", "Sara"]
last_names = ["Smith", "Doe", "Brown", "Wilson", "Taylor"]

vehicle_makes = ["Toyota", "Honda", "Ford", "BMW"]
vehicle_models = ["Corolla", "Civic", "F-150", "X5"]

def random_date_within_days(days=14):
    return datetime.utcnow() - timedelta(days=random.randint(0, days))


# --- Generate Drivers ---
for _ in range(40):
    campaign_name = random.choice(list(campaigns.keys()))
    campaign = campaigns[campaign_name]

    full_name = f"{random.choice(first_names)} {random.choice(last_names)}"

    driver = Driver(
        full_name=full_name,
        email=f"{full_name.replace(' ', '').lower()}@example.com",
        phone=f"+1-555-{random.randint(1000,9999)}",
        license_number=f"LIC{random.randint(10000,99999)}",
        license_state="AB",
        campaign_id=campaign.id,
        created_at=random_date_within_days(10)
    )

    db.add(driver)
    db.commit()

    # --- Add vehicles to ~70% of drivers ---
    if random.random() < 0.7:
        has_valid_insurance = random.random() < 0.7  # 70% valid

        expiry = (
            date.today() + timedelta(days=random.randint(1, 30))
            if has_valid_insurance
            else date.today() - timedelta(days=random.randint(1, 30))
        )

        vehicle = Vehicle(
            driver_id=driver.id,
            make=random.choice(vehicle_makes),
            model=random.choice(vehicle_models),
            year=random.randint(2010, 2023),
            insurance_policy_number=f"POL{random.randint(1000,9999)}",
            insurance_expiry_date=expiry
        )

        db.add(vehicle)
        db.commit()

print("Database seeded successfully!")