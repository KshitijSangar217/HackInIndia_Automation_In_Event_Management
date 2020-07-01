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

        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()  # Traffic encryption
        s.login("kshitijsangarofficial@gmail.com", "myfirstloverituu@mom.com")

        # Variable Declarations
        emailID = "kshitijsangarofficial@gmail.com"
        pwd = "myfirstloverituu@mom.com"
        subject = "New Video's UP"
        htmlfile_loc = "FinalTemplate.html"
        # NAME : Make sure that the name column is named "NAME" and email as "EMAIL" in the excelfile
        thumbnaillink = "https://miro.medium.com/max/1400/1*Bhqdl1UvZsuXrXbiE-ujsw.png"
        videotitle = 'Remove ScrollBar in SwiftUI List'
        videodescription = "When we create custom Views in SwiftUI, Sometimes Scroll Bar doesn't look nice. So, in this video, I am going to show you how to remove the scroll bar in SwiftUI List."
        videolink = 'https://youtu.be/oPp4htuqDOs'

        file = pd.ExcelFile(uploaded_file)
        for sheet in file.sheet_names:
            print("\n\n<-- New Sheet -->\n")
            df1 = file.parse(sheet)
            for i in range(len(df1['EMAIL'])):
                # EDITING the NAME here

                #directory_path = os.path.join(BASE_DIR,"automation/templates/EmailTemplate1.html")
                with open(os.path.join(BASE_DIR,"automation/templates/ExampleTemplate1.html"), 'r', encoding='utf8') as file:
                    html_Content = str(file.read().replace('{videodescription}', videodescription).replace('{username}',df1['NAME'][i]).replace('{videolink}', videolink).replace('{videotitle}', videotitle).replace('{thumbnaillink}',thumbnaillink))
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
    return render(request, 'home.html', {'data':data})