import json
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from .data import DATA, ADMIN_CREDS
from .decorators import admin_required


# ─── Public Views ────────────────────────────────────────────────────────────

def index(request):
    return render(request, 'core/index.html')


@csrf_exempt
@require_POST
def contact(request):
    try:
        data = json.loads(request.body)
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        service = data.get('service', '').strip() or 'General Inquiry'
        message = data.get('message', '').strip()

        if not name or not email or not message:
            return JsonResponse({
                "status": "error",
                "message": "Name, email, and message are required."
            }, status=400)

        subject = f'{service} enquiry from {name}'
        body = (
            f'Name: {name}\n'
            f'Email: {email}\n'
            f'Service: {service}\n\n'
            f'Message:\n{message}'
        )
        recipient = ['tbknshub@gmail.com']

        try:
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                recipient,
                fail_silently=False,
                reply_to=[email],
            )
        except BadHeaderError:
            return JsonResponse({"status": "error", "message": "Invalid email header."}, status=400)
        except Exception as exc:
            return JsonResponse({
                "status": "error",
                "message": "Unable to send email. Check your email settings."
            }, status=500)

        item_id = max((m['id'] for m in DATA['messages']), default=0) + 1
        DATA['messages'].insert(0, {
            'id': item_id,
            'from': name,
            'subject': subject,
            'time': 'Just now',
            'read': False,
        })

        return JsonResponse({"status": "success", "message": "Message sent successfully."})
    except ValueError:
        return JsonResponse({"status": "error", "message": "Invalid JSON payload."}, status=400)
    except Exception:
        return JsonResponse({"status": "error", "message": "Unable to submit message."}, status=500)


# ─── Admin Auth ───────────────────────────────────────────────────────────────

def admin_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == ADMIN_CREDS['username'] and password == ADMIN_CREDS['password']:
            request.session['admin'] = True
            return redirect('admin_dashboard')
        error = 'Invalid credentials'
    return render(request, 'admin_panel/admin_login.html', {'error': error})


def admin_logout(request):
    request.session.pop('admin', None)
    return redirect('admin_login')


# ─── Admin Pages ──────────────────────────────────────────────────────────────

@admin_required
def admin_dashboard(request):
    projects = DATA['projects']
    messages = DATA['messages']
    stats = {
        'total_projects': len(projects),
        'active_projects': len([p for p in projects if p['status'] == 'In Progress']),
        'total_clients': len(DATA['clients']),
        'total_revenue': sum(p['value'] for p in projects),
        'pending_tasks': len([t for t in DATA['tasks'] if t['status'] == 'Pending']),
        'unread_messages': len([m for m in messages if not m['read']]),
        'revenue_monthly': DATA['revenue_monthly'],
        'recent_projects': projects[:5],
        'recent_messages': messages[:3],
    }
    return render(request, 'admin_panel/admin_dashboard.html', {'stats': stats})


@admin_required
def admin_projects(request):
    projects = DATA['projects']
    return render(request, 'admin_panel/admin_projects.html', {
        'projects': projects,
        'count_in_progress': len([p for p in projects if p['status'] == 'In Progress']),
        'count_completed': len([p for p in projects if p['status'] == 'Completed']),
        'count_review': len([p for p in projects if p['status'] == 'Review']),
    })


@admin_required
def admin_clients(request):
    return render(request, 'admin_panel/admin_clients.html', {'clients': DATA['clients']})


@admin_required
def admin_team(request):
    return render(request, 'admin_panel/admin_team.html', {'team': DATA['team']})


@admin_required
def admin_tasks(request):
    return render(request, 'admin_panel/admin_tasks.html', {'tasks': DATA['tasks']})


@admin_required
def admin_finance(request):
    projects = DATA['projects']
    total = sum(p['value'] for p in projects)
    completed = sum(p['value'] for p in projects if p['status'] == 'Completed')
    return render(request, 'admin_panel/admin_finance.html', {
        'projects': projects,
        'total': total,
        'completed': completed,
        'outstanding': total - completed,
    })


@admin_required
def admin_messages(request):
    return render(request, 'admin_panel/admin_messages.html', {'messages': DATA['messages']})


# ─── API Endpoints ────────────────────────────────────────────────────────────

@admin_required
def api_stats(request):
    return JsonResponse({
        'projects': len(DATA['projects']),
        'clients': len(DATA['clients']),
        'revenue': sum(p['value'] for p in DATA['projects']),
        'tasks_pending': len([t for t in DATA['tasks'] if t['status'] == 'Pending']),
    })
