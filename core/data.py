# In-memory data store (replace with DB models in production)

DATA = {
    "projects": [
        {"id": 1, "name": "Shoprite E-Commerce Portal", "client": "Shoprite NG", "status": "In Progress", "value": 450000, "date": "2024-12-01"},
        {"id": 2, "name": "HR Management System", "client": "TechCorp Ltd", "status": "Completed", "value": 280000, "date": "2024-11-15"},
        {"id": 3, "name": "Power BI Dashboard", "client": "AgroBase", "status": "Review", "value": 150000, "date": "2024-12-10"},
        {"id": 4, "name": "Brand Identity Package", "client": "StartupX", "status": "Completed", "value": 95000, "date": "2024-11-28"},
        {"id": 5, "name": "Mobile App (iOS/Android)", "client": "LogiTrack", "status": "In Progress", "value": 620000, "date": "2024-12-05"},
    ],
    "clients": [
        {"id": 1, "name": "Shoprite NG", "email": "tech@shoprite.ng", "projects": 2, "total_spent": 730000},
        {"id": 2, "name": "TechCorp Ltd", "email": "cto@techcorp.ng", "projects": 1, "total_spent": 280000},
        {"id": 3, "name": "AgroBase", "email": "admin@agrobase.ng", "projects": 1, "total_spent": 150000},
        {"id": 4, "name": "StartupX", "email": "founder@startupx.io", "projects": 1, "total_spent": 95000},
        {"id": 5, "name": "LogiTrack", "email": "ops@logitrack.ng", "projects": 1, "total_spent": 620000},
    ],
    "team": [
        {"id": 1, "name": "Adewale Okonkwo", "role": "Lead Developer", "tasks": 8, "status": "Active"},
        {"id": 2, "name": "Chisom Nweke", "role": "UI/UX Designer", "tasks": 5, "status": "Active"},
        {"id": 3, "name": "Emeka Eze", "role": "Data Analyst", "tasks": 3, "status": "Active"},
        {"id": 4, "name": "Fatima Bello", "role": "Digital Marketer", "tasks": 4, "status": "Active"},
    ],
    "tasks": [
        {"id": 1, "title": "Finalize homepage UI", "project": "Shoprite E-Commerce Portal", "assignee": "Chisom Nweke", "priority": "High", "due": "2024-12-20", "status": "Pending"},
        {"id": 2, "title": "Integrate payment gateway", "project": "Shoprite E-Commerce Portal", "assignee": "Adewale Okonkwo", "priority": "High", "due": "2024-12-22", "status": "In Progress"},
        {"id": 3, "title": "Build KPI metrics page", "project": "Power BI Dashboard", "assignee": "Emeka Eze", "priority": "Medium", "due": "2024-12-18", "status": "Pending"},
        {"id": 4, "title": "iOS push notifications", "project": "Mobile App (iOS/Android)", "assignee": "Adewale Okonkwo", "priority": "High", "due": "2024-12-25", "status": "In Progress"},
        {"id": 5, "title": "Social campaign assets", "project": "Brand Identity Package", "assignee": "Fatima Bello", "priority": "Low", "due": "2024-12-15", "status": "Completed"},
    ],
    "messages": [
        {"id": 1, "from": "Shoprite NG", "subject": "Payment Gateway Update", "time": "2h ago", "read": False},
        {"id": 2, "from": "LogiTrack", "subject": "App Testing Feedback", "time": "5h ago", "read": False},
        {"id": 3, "from": "AgroBase", "subject": "Dashboard Revision Request", "time": "1d ago", "read": True},
    ],
    "revenue_monthly": [320000, 410000, 290000, 580000, 470000, 620000, 510000, 740000, 680000, 820000, 760000, 950000],
}

ADMIN_CREDS = {"username": "tobyknows", "password": "Exkoma50"}
