from weakref import ref

from flask import Blueprint, request, render_template, redirect, url_for, flash
from database import SessionLocal
from models import Campaign, Driver, Vehicle
from sqlalchemy import func
from datetime import datetime, date

main = Blueprint("main", __name__)


# Dashboard Page
@main.route("/dashboard")
def dashboard():
    db = SessionLocal()

    # Date filters
    start_date = request.args.get("start")
    end_date = request.args.get("end")

    query = db.query(Driver)

    if start_date:
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        query = query.filter(Driver.created_at >= start_date_obj)

    if end_date:
        end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
        query = query.filter(Driver.created_at <= end_date_obj)

    drivers = query.all()

    campaigns = db.query(Campaign).all()

    today = date.today()

    dashboard_data = []

    for campaign in campaigns:
        campaign_drivers = [d for d in drivers if d.campaign_id == campaign.id]

        total_signups = len(campaign_drivers)

        completed = 0

        for d in campaign_drivers:
            valid_vehicle = any(
                v.insurance_expiry_date >= today for v in d.vehicles
            )
            if valid_vehicle:
                completed += 1

        conversion_rate = (completed / total_signups) if total_signups > 0 else 0

        dashboard_data.append({
            "campaign": campaign,
            "total": total_signups,
            "completed": completed,
            "conversion_rate": round(conversion_rate * 100, 2)
        })

    # Sign-ups over time
    time_series_query = db.query(
        func.date(Driver.created_at),
        func.count(Driver.id)
    )

    if start_date:
        time_series_query = time_series_query.filter(
            Driver.created_at >= start_date_obj
        )

    if end_date:
        time_series_query = time_series_query.filter(
            Driver.created_at <= end_date_obj
        )

    time_series = (
        time_series_query
        .group_by(func.date(Driver.created_at))
        .all()
    )

    dates = [str(row[0]) for row in time_series]
    counts = [row[1] for row in time_series]

    campaign_names = [row["campaign"].name for row in dashboard_data]
    conversion_rates = [row["conversion_rate"] for row in dashboard_data]

    return render_template(
        "dashboard.html",
        data=dashboard_data,
        dates=dates,
        counts=counts,
        campaign_names=campaign_names,
        conversion_rates=conversion_rates,
        start_date=start_date,
        end_date=end_date
    )


# Driver Signup
@main.route("/signup", methods=["GET", "POST"])
def signup():
    db = SessionLocal()

    if request.method == "POST":
        try:
            ref = int(request.args.get("ref"))
        except (TypeError, ValueError):
            return "Invalid campaign", 400

        # Find or create campaign
        campaign = db.query(Campaign).filter_by(id=ref).first()
        if not campaign:
            return "Invalid campaign", 400

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

        return redirect(url_for("main.vehicle", driver_id=driver.id, ref=ref))

    ref = request.args.get("ref")
    campaign = None
    if ref:
        campaign = db.query(Campaign).filter_by(id=ref).first()
        
    return render_template("signup.html", campaign=campaign)


# Vehicle Registration
@main.route("/vehicle", methods=["GET", "POST"])
def vehicle():
    db = SessionLocal()
    driver_id = int(request.args.get("driver_id"))
    ref = request.args.get("ref")

    if request.method == "POST":
        try:
            expiry = datetime.strptime(
                request.form["insurance_expiry_date"], "%Y-%m-%d"
            ).date()

            vehicle = Vehicle(
                driver_id=driver_id,
                make=request.form["make"],
                model=request.form["model"],
                year=int(request.form["year"]),
                insurance_policy_number=request.form["insurance_policy_number"],
                insurance_expiry_date=expiry
            )

            db.add(vehicle)
            db.commit()

            if expiry >= date.today():
                flash("Vehicle registered successfully!", "success")
            else:
                flash("Vehicle added, but insurance is expired.", "error")

            return redirect(url_for("main.dashboard"))

        except Exception:
            flash("Error submitting vehicle information.", "error")
            return redirect(url_for("main.dashboard"))

    return render_template("vehicle.html", driver_id=driver_id, ref=ref)


# CREATE CAMPAIGN FORM
@main.route("/campaigns/new", methods=["GET", "POST"])
def create_campaign():
    db = SessionLocal()

    if request.method == "POST":
        name = request.form["name"]
        source = request.form["source"]

        # prevent duplicates
        existing = db.query(Campaign).filter_by(name=name).first()
        if existing:
            return "Campaign already exists", 400

        campaign = Campaign(name=name, source=source)
        db.add(campaign)
        db.commit()

        return redirect(url_for("main.dashboard"))

    return render_template("create_campaign.html")