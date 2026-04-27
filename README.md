# TBKNS HUB – Django Version

Converted from Flask to Django 4.2+

## Project Structure
```
tbkns_hub_django/
├── manage.py
├── requirements.txt
├── tbkns_hub/                  # Django project package
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── core/                       # Main app
    ├── views.py                # All route handlers (was app.py)
    ├── urls.py                 # URL patterns (was @app.route decorators)
    ├── data.py                 # In-memory data store
    ├── decorators.py           # admin_required decorator
    └── templates/
        ├── core/
        │   └── index.html      # Public website
        └── admin_panel/
            ├── admin_base.html
            ├── admin_login.html
            ├── admin_dashboard.html
            ├── admin_projects.html
            ├── admin_clients.html
            ├── admin_team.html
            ├── admin_tasks.html
            ├── admin_finance.html
            └── admin_messages.html
```

## Setup & Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run migrations (for session support)
```bash
python manage.py migrate
```

### 3. Run the server
```bash
python manage.py runserver
```

### 4. Open in browser
- **Website**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin

### Admin Credentials
- Username: `admin`
- Password: `tbkns2024`
> ⚠️ Change these in `core/data.py` before deploying!

## Key Flask → Django Changes

| Flask | Django |
|-------|--------|
| `@app.route(...)` | `path(...)` in `urls.py` |
| `render_template(...)` | `render(request, ...)` |
| `session["admin"]` | `request.session["admin"]` |
| `redirect(url_for(...))` | `redirect('url_name')` |
| `request.form.get(...)` | `request.POST.get(...)` |
| `request.get_json()` | `json.loads(request.body)` |
| `jsonify(...)` | `JsonResponse(...)` |
| `{{ "{:,}".format(n) }}` | `{{ n\|floatformat:0 }}` |
| `{{ stats.revenue_monthly \| tojson }}` | `{{ stats.revenue_monthly\|safe }}` |
| `{% if '/projects' in request.path %}` | `{% block nav_projects %}{% endblock %}` per-page |
| `<form method="POST">` | `<form method="POST">{% csrf_token %}` |

## Production Upgrade Checklist
- [ ] Replace `core/data.py` with proper Django models + database
- [ ] Use Django's built-in auth (`django.contrib.auth`) instead of session-based admin
- [ ] Set `DEBUG = False` and configure `ALLOWED_HOSTS`
- [ ] Move `SECRET_KEY` to environment variable
- [ ] Configure email backend for contact form
- [ ] Deploy with Gunicorn + Nginx
- [ ] Add HTTPS (Let's Encrypt)

## GitHub Pages Hosting

The public landing page can be hosted for free with GitHub Pages using the static copy in `docs/`.

1. Create a GitHub repository.
2. Push this project to GitHub.
3. In GitHub repository settings, enable Pages and set the source to `main` branch and `docs/` folder.
4. After a few minutes, your site will be available at `https://<username>.github.io/<repo>/`.

### Notes
- The static site in `docs/index.html` uses EmailJS for the contact form.
- GitHub Pages can only host the static landing page, not the Django backend or admin panel.

## Deploy on Render

Render can host the Django backend and admin panel for free.

### Required files
- `requirements.txt` now includes `gunicorn`, `psycopg2-binary`, and `dj-database-url`
- `Procfile` starts Gunicorn
- `render.yaml` defines the Render service
- `runtime.txt` pins Python 3.11

### Render setup steps

1. Create a GitHub repository and push this project.
2. Log in to Render and connect your GitHub account.
3. Create a new **Web Service**.
4. Choose the repository and `main` branch.
5. Set the build command to:
   ```bash
   pip install -r requirements.txt
   ```
6. Set the start command to:
   ```bash
   gunicorn tbkns_hub.wsgi --log-file -
   ```
7. Add environment variables in Render:
   - `DEBUG=False`
   - `SECRET_KEY=<your-production-secret>`
   - `DJANGO_SETTINGS_MODULE=tbkns_hub.settings`
   - `ALLOWED_HOSTS=<your-render-service>.onrender.com`
   - `DATABASE_URL=postgres://...` (optional if using Render Postgres)
   - `DJANGO_EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend`
   - `EMAIL_HOST=smtp.yourprovider.com`
   - `EMAIL_PORT=587`
   - `EMAIL_HOST_USER=...`
   - `EMAIL_HOST_PASSWORD=...`
   - `EMAIL_USE_TLS=True`
   - `DEFAULT_FROM_EMAIL='TBKNS HUB <noreply@tbknshub.com>'`

### Optional: add a managed database

For production, use Render Postgres instead of SQLite:
1. Create a Postgres database in Render.
2. Copy its `DATABASE_URL` into your Web Service environment.
3. Run `python manage.py migrate` from Render's shell.

### Database note
If `DATABASE_URL` is unset, the app falls back to SQLite at `db.sqlite3`.
