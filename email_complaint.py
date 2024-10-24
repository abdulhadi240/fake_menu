from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def create_complaint_template(customer_id,customer_name, customer_email, phone_number, complaint_text):
    # HTML template for complaint email with optional image
    template = f"""
    <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; background-color: #f9f9f9; padding: 20px;">
            <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; border-radius: 10px; padding: 20px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
              <div style="margin-top: 20px;"><img src="https://www.intotheminds.com/blog/app/uploads/complaint-banner.jpg" alt="Complaint Image" style="max-width: 100%; height: auto; border-radius: 5px;"></div>
                <h1 style="color: #333333;">Customer Complaint</h1>
                <p>Dear Support Team,</p>
                <p>A new complaint has been registered by the following customer:</p>
                
                <table style="width: 100%; margin-top: 10px; border-collapse: collapse;">
                    <tr>
                        <td style="padding: 8px; font-weight: bold; border-bottom: 1px solid #ddd;">Customer Name:</td>
                        <td style="padding: 8px; border-bottom: 1px solid #ddd;">{customer_id}</td>
                    </tr>
                    <tr>
                        <td style="padding: 8px; font-weight: bold; border-bottom: 1px solid #ddd;">Customer Name:</td>
                        <td style="padding: 8px; border-bottom: 1px solid #ddd;">{customer_name}</td>
                    </tr>
                    <tr>
                        <td style="padding: 8px; font-weight: bold; border-bottom: 1px solid #ddd;">Email Address:</td>
                        <td style="padding: 8px; border-bottom: 1px solid #ddd;">{customer_email}</td>
                    </tr>
                    <tr>
                        <td style="padding: 8px; font-weight: bold; border-bottom: 1px solid #ddd;">Phone Number:</td>
                        <td style="padding: 8px; border-bottom: 1px solid #ddd;">{phone_number}</td>
                    </tr>
                    <tr>
                        <td style="padding: 8px; font-weight: bold; border-bottom: 1px solid #ddd;">Complaint Details:</td>
                        <td style="padding: 8px; border-bottom: 1px solid #ddd;">{complaint_text}</td>
                    </tr>
                </table>

            

                <p style="margin-top: 20px;">Please reach out to the customer for further clarification.</p>
                <p>Thank you!</p>
            </div>
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


