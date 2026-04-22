# AI Usage & Prompts

This project used AI tools to accelerate implementation and refine architecture decisions.

---

## 1. Campaign System Design

**Prompt:**

> Refactor campaign system so signup uses campaign ID instead of name and ensure dynamic sidebar rendering.

**Outcome:**

* Introduced ID-based routing
* Improved data integrity design
* Updated sidebar to dynamically render campaigns

---

## 2. Database Modeling

**Prompt:**

> Generate relational schema for campaigns, drivers, and vehicles with proper foreign keys in SQLAlchemy.

**Outcome:**

* Initial models generated
* Adjusted to include created_at and relationships

---

## 3. Signup Flow Fix

**Prompt:**

> Ensure campaign reference from query parameter is stored and used in driver creation.

**Outcome:**

* Fixed issue where campaign name was incorrectly used instead of ID
* Improved lookup logic

---

## 4. Dynamic UI Sidebar

**Prompt:**

> Create a Flask + Jinja sidebar that dynamically lists campaigns from database.

**Outcome:**

* Implemented Flask context processor
* Eliminated hardcoded navigation

---

## 5. Dashboard Analytics

**Prompt:**

> Calculate conversion rate per campaign including completed vs total drivers.

**Outcome:**

* Implemented Python-based aggregation for simplicity
* Later optimized structure for clarity

---

## 6. Seed Data Generation

**Prompt:**

> Generate realistic seed data for campaigns, drivers, and vehicles with valid/invalid insurance distribution.

**Outcome:**

* Created structured seed script with realistic funnel behavior
* Ensures meaningful dashboard visualization

---

## 7. UI Enhancements

**Prompt:**

> Add active navigation highlighting and improve sidebar UX for campaign-based navigation.

**Outcome:**

* Implemented active state logic using request context
* Improved usability of navigation flow

---

## Key Observations

* AI significantly accelerated boilerplate generation
* Manual refinement was required for:

  * ID vs name consistency
  * relational integrity
  * UX flow correctness

---

## Final Note

AI was used as a development accelerator, while architecture decisions were manually validated and adjusted for correctness and maintainability.
