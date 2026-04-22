# Technical Decisions

---

## 1. Stack Choice

* Flask + Jinja (server-rendered)
* SQLAlchemy ORM
* SQLite database

### Reason

Fast to build, minimal setup, ideal for MVP demonstration.

### Trade-off

Not production-scalable; no async or API separation.

---

## 2. Campaign System Design (Key Update)

Campaigns are now fully dynamic:

* Created by users via `/campaigns/new`
* Stored with:

  * `id` (primary key, immutable)
  * `name` (display label)
  * `source` (facebook, google, referral)

### Signup Flow Uses:

```
/signup?ref=<campaign_id>
```

### Reason

Using **ID instead of name** ensures:

* Stable URLs
* Safe renaming of campaigns
* Avoids collisions

---

## 3. Separation of Concerns

| Field  | Purpose                 |
| ------ | ----------------------- |
| id     | System reference (URLs) |
| name   | Display label           |
| source | Acquisition channel     |

---

## 4. Dynamic Sidebar

Campaigns are injected globally using a Flask context processor.

### Reason

Ensures:

* Always up-to-date UI
* No duplication across templates

---

## 5. Data Model

* Campaign → Driver → Vehicle (1-to-many relationships)

### Reason

Represents funnel:

```
Campaign → Acquisition → Registration → Completion
```

---

## 6. Signup Conversion Logic

A driver is considered “completed” if:

* They have at least one vehicle
* AND insurance is not expired

---

## 7. Seed Strategy

* DB reset on each run
* Generates:

  * Multiple campaigns
  * Mixed valid/invalid insurance data
  * Time-distributed drivers

### Reason

Ensures meaningful dashboard analytics without manual setup.

---

## 8. UI Strategy

* Sidebar navigation with active state
* Campaign-based signup entry points
* Flash messages for feedback

### Trade-off

Minimal styling, no design system.

---

## 9. Why No Authentication

Out of scope for MVP; focus is on funnel tracking, not user access control.

---

## Summary

This version prioritizes:

* Data-driven campaign management
* Stable tracking via IDs
* Simple but realistic analytics flow
