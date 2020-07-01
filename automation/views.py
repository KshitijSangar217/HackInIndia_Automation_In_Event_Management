from django.shortcuts import render
import smtplib
from email.message import EmailMessage
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import pandas as pd
import xlrd
import os
from hackathon_automate import settings
from hackathon_automate.settings import BASE_DIR

in_development = True


def home(request):
    return render(request, 'home.html')



def returndata(request):
    if request.method == "POST":
        uploaded_file = request.FILES["document"]
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)

        # Variable Declarations
        emailID = "kshitijsangarofficial@gmail.com"
        pwd = "myfirstloverituu@mom.com"
        subject = "New Video's UP"
        organization_name = "TechWiz"
        logo_url = "https://legiit-service.s3.amazonaws.com/6e212075e04d1616b06a5e1398e10053/3ea07b3abe6146b58e53d68653e3a61f.jpg"
        description = "This is team techwiz and we are here to send automatic emails to all you participants."

        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()  # Traffic encryption
        s.login(emailID, pwd)

        file = pd.ExcelFile(uploaded_file)
        for sheet in file.sheet_names:
            print("\n\n<-- New Sheet -->\n")
            df1 = file.parse(sheet)
            for i in range(len(df1['EMAIL'])):
                # EDITING the NAME here

                #directory_path = os.path.join(BASE_DIR,"automation/templates/EmailTemplate1.html")
                with open(os.path.join(BASE_DIR,"automation/templates/ExampleTemplate2.html"), 'r', encoding='utf8') as file:
                    html_Content = str(file.read().replace('{username}', df1['NAME'][i]).replace('{logo_url}', logo_url).replace('{organization_name}', organization_name)).replace('{description}',description)
                msg = EmailMessage()
                msg['Subject'] = subject
                msg['From'] = emailID  # ===========================
                msg['To'] = df1['EMAIL'][i]
                msg.add_alternative(html_Content, subtype="html")
                s.send_message(msg)
                print("--> ", df1['SRNO'][i], ": ", df1['EMAIL'][i], " : Sent")
        s.quit()
        data = "sent to all"
        os.path.join(BASE_DIR, "automation/templates/ExampleTemplate1.html")
        print('\n\n\n\n\n\n\n\n mails sent\n\n\n')
        os.remove(os.path.join(BASE_DIR,"excelmedia/",uploaded_file.name))
    return render(request, 'home.html', {'data': data})