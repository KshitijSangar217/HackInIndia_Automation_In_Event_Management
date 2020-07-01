from django.shortcuts import render
import smtplib
from email.message import EmailMessage


def home(request):
    return render(request, 'home.html')

def returndata(request):
    if request.method == "POST":
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()  # Traffic encryption
        s.login("kshitijsangarofficial@gmail.com", "YOURPASSWORD")

        msg = EmailMessage()
        msg['Subject'] = "demo"
        msg['From'] = "kshitijsangarofficial@gmail.com"
        msg['To'] = "kshitijsangar@gmail.com"
        gmail_content = "Hello guys"
        msg.set_content(gmail_content)

        s.send_message(msg)
        s.quit()
        data = "sent to all"
        print('\n\n\n\n\n\n\n\n mails sent\n\n\n')
    return render(request, 'home.html', {'data':data})