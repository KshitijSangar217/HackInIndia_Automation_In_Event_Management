from django.shortcuts import render
import smtplib
from email.message import EmailMessage
from django.core.files.storage import FileSystemStorage


def home(request):
    return render(request, 'home.html')



def returndata(request):
    if request.method == "POST":
        print(request.GET)
        uploaded_file = request.FILES["document"]
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)

        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()  # Traffic encryption
        s.login("kshitijsangarofficial@gmail.com", "myfirstloverituu@mom.com")

        excelFile = "DemoExcelFile.xlsx"  # Mail
        emailID = "kshitijsangarofficial@gmail.com"
        pwd = "pwd"
        subject = "New Video's UP"
        htmlfile_loc = "FinalTemplate.html"
        #with open(htmlfile_loc, 'r', encoding='utf8') as file:
         #   html_Content = str(file.read().replace('{username}', "NAME").replace('{org_image}', "org_image"))




        msg = EmailMessage()
        msg['Subject'] = "demo"
        msg['From'] = "kshitijsangarofficial@gmail.com"
        msg['To'] = "kshitijsangar@gmail.com"
        gmail_content = "Hello guys"
        msg.set_content(gmail_content)

        # Attaching the Poster
        f = open('excelmedia/' + uploaded_file.name, 'rb')
        fdata = f.read()
        # fname = 'images/' + CertificateFileName
        fname = 'DemoImage.pdf'

        msg.add_attachment(fdata, maintype='application', subtype='octet-stream', filename=fname)

        s.send_message(msg)
        s.quit()
        data = "sent to all"
        print('\n\n\n\n\n\n\n\n mails sent\n\n\n')
    return render(request, 'home.html', {'data':data})