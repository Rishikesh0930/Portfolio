import os
from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib import messages
import requests
import json

def home_page(request):
    json_file_home = os.path.join(settings.BASE_DIR, 'static/json/home.json')
    with open(json_file_home, 'r', encoding='utf-8') as f:
        home = json.load(f)
    return render(request, 'home.html', {"home": home})

def about_page(request):
    json_file_about = os.path.join(settings.BASE_DIR, 'static/json/about.json')
    with open(json_file_about, 'r', encoding='utf-8') as f:
        about = json.load(f)
    return render(request, 'about.html', {"about": about})

def project_page(request):
    return render(request, 'project.html')

def skills_page(request):
    return render(request, 'Skills.html')

def resume_page(request):
    json_file_resume = os.path.join(settings.BASE_DIR, 'static/json/resume.json')
    with open(json_file_resume, 'r', encoding='utf-8') as f:
        resume = json.load(f)
    return render(request, 'resume.html', {"resume": resume})

def send_telegram_message(text):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        return False
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }
    try:
        response = requests.post(url, data=payload, timeout=10)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def contact_page(request):
    json_file_contact = os.path.join(settings.BASE_DIR, 'static/json/contact.json')
    with open(json_file_contact, 'r', encoding='utf-8') as f:
        contact = json.load(f)
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        subject = request.POST.get("subject", "")
        message = request.POST.get("message", "")
        if not all([name, email, subject, message]):
            messages.error(request, "All fields are required.")
            return redirect("contact-page")
        if len(name)<3 or len(name)>30:
            messages.error(request, "Name should be between 3 and 30 characters.")
            return redirect("contact-page")
        if len(email)<8 or "@" not in email or "." not in email:
            messages.error(request, "please Enter the valid email address.")
            return redirect("contact-page")
        if len(subject)>100:
            messages.error(request, "Subject should be less than 100 character.")
            return redirect("contact-page")
        if len(message)<30:
            messages.error(request, "Message should be greater than 30 characters.")
            return redirect("contact-page")      
        text =(
        f"<b>Subject - </b>{subject}\n"
        f"<b>Email - </b> {email}\n"
        f"<b>Name - </b> {name}\n\n"
        f"{message}"
        )
        success = send_telegram_message(text)
        if success:
            messages.error(request, "Message sent successfully!\nIf you don’t receive a reply within 1 hour,\nplease contact me via email.")
        else:
            messages.error(request, "Message failed. Try again later.")
        return redirect("contact-page")
    return render(request, 'contact.html', {"contact": contact})