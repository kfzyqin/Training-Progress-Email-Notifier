from email_sender import send_email


if __name__ == '__main__':
    test_msg = 'This is a test message. '
    send_email(receivers=['zhenyue.qin@anu.edu.au'],  # Type in your email address to have a try
               email_type='exp_complete',  # email_type; email_type
               msg_content=test_msg,
               language='english')
