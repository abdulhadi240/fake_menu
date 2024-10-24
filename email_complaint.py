from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def create_complaint_template(customer_id,customer_name, customer_email, phone_number, complaint_text):
    # HTML template for complaint email
    template = f"""
    <html>
        <body>
            <h1>Customer Complaint</h1>
            <p>Dear Support Team,</p>
            <p>A new complaint has been registered by the following customer:</p>
            <p><strong>Customer ID:</strong> {customer_id}</p>
            <p><strong>Customer Name:</strong> {customer_name}</p>
            <p><strong>Email Address:</strong> {customer_email}</p>
            <p><strong>Phone Number:</strong> {phone_number}</p>
            <p><strong>Complaint Details:</strong> {complaint_text}</p>
            <p>Please reach out to the customer for further clarification.</p>
            <p>Thank you!</p>
        </body>
    </html>
    """
    return template



def send_complaint_email(customer_id,customer_name, customer_email, phone_number, complaint_text):
  # Email configuration
  sender_email = 'ah912425@gmail.com'  # Replace with your Gmail address
  sender_password = 'jbwt vicb iatm ulje'  # Replace with your Gmail App Password
  subject = 'New complain registered'
  email = 'biggbuy1@gmail.com'
  # Create the MIMEMultipart object
  msg = MIMEMultipart('alternative')
  msg['Subject'] = subject
  msg['From'] = sender_email
  msg['To'] = email

  # Generate the HTML content from the template
  html_content = create_complaint_template(customer_id,customer_name, customer_email, phone_number, complaint_text)

  # Attach the HTML content to the email
  msg.attach(MIMEText(html_content, 'html'))

  # Connect to the SMTP server (in this case, Gmail)
  with smtplib.SMTP('smtp.gmail.com', 587) as server:
    # Start TLS for security
    server.starttls()

    # Login to your Gmail account
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, [email], msg.as_string())


