import smtplib

from email_config import *
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from email_templates.email_templates_eng import *
from email_templates.email_templates_chn import *


def send_email(receivers, email_type, msg_content, language='english'):
    if language == 'english':
        exp_complete_1 = exp_complete_1_eng
        exp_complete_2 = exp_complete_2_eng
        exp_progress_1 = exp_progress_1_eng
        exp_progress_2 = exp_progress_2_eng
        emergency_1 = emergency_1_eng
        emergency_2 = emergency_2_eng
    elif language == 'chinese':
        exp_complete_1 = exp_complete_1_chn
        exp_complete_2 = exp_complete_2_chn
        exp_progress_1 = exp_progress_1_chn
        exp_progress_2 = exp_progress_2_chn
        emergency_1 = emergency_1_chn
        emergency_2 = emergency_2_chn
    else:
        raise NotImplementedError('Unsupported language. ')
    if email_type == 'exp_complete':
        template_1 = exp_complete_1
        template_2 = exp_complete_2
        sub_email = 'Heimdall Watchtower: Experiment Complete'
    elif email_type == 'exp_progress':
        template_1 = exp_progress_1
        template_2 = exp_progress_2
        sub_email = 'Heimdall Watchtower: Experiment Progress'
    elif email_type == 'error':
        template_1 = emergency_1
        template_2 = emergency_2
        sub_email = 'Heimdall Watchtower: Emergency'
    else:
        raise NotImplementedError('Not supported email type. ')

    for a_person in receivers:
        def send_email(msg):
            try:
                server = smtplib.SMTP('smtp.gmail.com', port=587)
                server.ehlo()
                server.starttls()
                server.login(EMAIL_S_ADDRESS, PASSWORD)
                message = msg
                server.sendmail(EMAIL_S_ADDRESS, a_person, message)
                server.quit()
                print('Success: Email sent!')
            except Exception:
                traceback.print_exc()

        message = MIMEMultipart("alternative")
        if sub_email is not None:
            message["Subject"] = sub_email
        else:
            message["Subject"] = "Incoming Transmission"
        message["From"] = EMAIL_S_ADDRESS
        message["To"] = a_person

        html = template_1 + msg_content + template_2

        part2 = MIMEText(html, 'html', 'utf-8')

        # message.attach(part1)
        message.attach(part2)

        send_email(message.as_string())

        print('Email sent! ')


if __name__ == '__main__':
    test_msg = 'Experiment start time: 2021-Jul-10-19:10:24 <br>' \
               'Experiment purpose: evaluating the performance of positional embedding <br>' \
               'Best top-1 accuracy: 86.9 <br>' \
               'Best top-5 accuracy: 95.5 <br>' \
               'Best epoch number: 50 <br>'
    send_email(receivers=['zhenyue.qin@anu.edu.au',
                          ''],  # Type in your email address to have a try
               email_type='exp_complete',  # email_type; email_type
               msg_content=test_msg,
               language='english')
