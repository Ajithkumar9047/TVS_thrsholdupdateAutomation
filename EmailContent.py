# email.py
from Config import *
def email_generator(excel_file_name):
    from_email = 'ajithkumar@newgendigital.com'
    from_password = 'uroqpjoiixmnrxxb'
    to_email='ajithkumaraji9047@gmail.com'
    cc_email=''
    #to_email = 'ashish.thakur@tvsmotor.com'
    #cc_email = 'arun.reddy@newgendigital.com, priyadharshini@newgendigital.com, prasanth@newgendigital.com'
    subject = '<Re: Daily Threshold Update>'

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Cc'] = cc_email
    msg['Subject'] = subject

    # Email body
    body = f'''
        <html>
        <head>
            <style>
                body {{
                    font-family: Verdana, sans-serif;
                    font-size: 14px;
                    color: black;
                }}
                p {{
                    margin: 10px 0;
                }}
            </style>
        </head>
        <body>
            <p>Hi Ashish,</p>
            <p>Please refer to the attachment below for details regarding the threshold master and threshold feeds for {current_date}.</p>
            <b style="color: blue;">Thanks & Regards,<br></b>
            <p>Ajithkumar Sekar | Technical support executive<br>
            Newgen Digital Works Pvt. Ltd.<br>
            M: (+91) 8072467327<br>
            W: <a href="http://www.newgen.co">www.newgen.co</a><br>
            A: No.2/579, Singaravelan Street, Chinna Neelankarai Chennai - 600041.</p>
        </body>
        </html>
    '''
    msg.attach(MIMEText(body, 'html'))

    # Attach the Excel file
    excel_attachment = open(excel_file_name, 'rb')
    excel_part = MIMEApplication(excel_attachment.read(), Name=excelName)
    excel_attachment.close()
    excel_part['Content-Disposition'] = f'attachment; filename="{excel_file_name}"'
    msg.attach(excel_part)

    try:
        # Set up the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)

        # Send the email
        recipients = [to_email] + cc_email.split(', ')
        server.sendmail(from_email, recipients, msg.as_string())
        print("Email sent successfully!")
        logging.info("Email sent successfully!")

    except Exception as e:
        print("An error occurred:", str(e))
        logging.error("An error occurred:%s", str(e))

    finally:
        server.quit()
