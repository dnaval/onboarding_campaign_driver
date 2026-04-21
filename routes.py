from flask import Blueprint, request, render_template, redirect, url_for
from database import SessionLocal
from models import Campaign, Driver, Vehicle
from datetime import datetime

main = Blueprint("main", __name__)


# ✅ Driver Signup
@main.route("/signup", methods=["GET", "POST"])
def signup():
    db = SessionLocal()

    if request.method == "POST":
        ref = request.args.get("ref", "unknown")

        # Find or create campaign
        campaign = db.query(Campaign).filter_by(name=ref).first()
        if not campaign:
            campaign = Campaign(name=ref, source="unknown")
            db.add(campaign)
            db.commit()

        driver = Driver(
            full_name=request.form["full_name"],
            email=request.form["email"],
            phone=request.form["phone"],
            license_number=request.form["license_number"],
            license_state=request.form["license_state"],
            campaign_id=campaign.id
        )

        db.add(driver)
        db.commit()

        return redirect(url_for("main.vehicle", driver_id=driver.id))

    return render_template("signup.html")


# ✅ Vehicle Registration
@main.route("/vehicle", methods=["GET", "POST"])
def vehicle():
    db = SessionLocal()
    driver_id = request.args.get("driver_id")

    if request.method == "POST":
        vehicle = Vehicle(
            driver_id=driver_id,
            make=request.form["make"],
            model=request.form["model"],
            year=int(request.form["year"]),
            insurance_policy_number=request.form["insurance_policy_number"],
            insurance_expiry_date=datetime.strptime(
                request.form["insurance_expiry_date"], "%Y-%m-%d"
            ).date()
        )

        db.add(vehicle)
        db.commit()

        return "Vehicle registered successfully!"

    return render_template("vehicle.html", driver_id=driver_id)