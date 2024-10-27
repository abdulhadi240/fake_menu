from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def create_order_template(customer_id, customer_name, customer_email, phone_number, menuid, quantity, instructions):
    # Redesigned HTML template
    template = f"""
    <html>
        <body style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.8; background-color: #f4f4f4; padding: 30px;">
            <div style="max-width: 650px; margin: 0 auto; background-color: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);">
                <!-- Header Section -->
                <div style="background-color: #4CAF50; color: white; padding: 20px; text-align: center;">
                    <h1 style="margin: 0; font-size: 24px;">🎉 New Order Alert!</h1>
                    <p style="margin: 5px 0;">You've received a new order. Check the details below.</p>
                </div>

                <!-- Content Section -->
                <div style="padding: 20px;">
                    <h2 style="color: #333;">Customer Details</h2>
                    <table style="width: 100%; margin-top: 10px; border-collapse: collapse;">
                        <tr style="background-color: #f9f9f9;">
                            <td style="padding: 10px; font-weight: bold; border-bottom: 1px solid #ddd;">Customer ID:</td>
                            <td style="padding: 10px; border-bottom: 1px solid #ddd;">{customer_id}</td>
                        </tr>
                        <tr>
                            <td style="padding: 10px; font-weight: bold; border-bottom: 1px solid #ddd;">Name:</td>
                            <td style="padding: 10px; border-bottom: 1px solid #ddd;">{customer_name}</td>
                        </tr>
                        <tr style="background-color: #f9f9f9;">
                            <td style="padding: 10px; font-weight: bold; border-bottom: 1px solid #ddd;">Email:</td>
                            <td style="padding: 10px; border-bottom: 1px solid #ddd;">{customer_email}</td>
                        </tr>
                        <tr>
                            <td style="padding: 10px; font-weight: bold; border-bottom: 1px solid #ddd;">Phone:</td>
                            <td style="padding: 10px; border-bottom: 1px solid #ddd;">{phone_number}</td>
                        </tr>
                    </table>

                    <h2 style="color: #333; margin-top: 20px;">Order Details</h2>
                    <table style="width: 100%; margin-top: 10px; border-collapse: collapse;">
                        <tr style="background-color: #f9f9f9;">
                            <td style="padding: 10px; font-weight: bold; border-bottom: 1px solid #ddd;">Menu ID:</td>
                            <td style="padding: 10px; border-bottom: 1px solid #ddd;">{menuid}</td>
                        </tr>
                        <tr>
                            <td style="padding: 10px; font-weight: bold; border-bottom: 1px solid #ddd;">Quantity:</td>
                            <td style="padding: 10px; border-bottom: 1px solid #ddd;">{quantity}</td>
                        </tr>
                        <tr style="background-color: #f9f9f9;">
                            <td style="padding: 10px; font-weight: bold; border-bottom: 1px solid #ddd;">Instructions:</td>
                            <td style="padding: 10px; border-bottom: 1px solid #ddd;">{instructions}</td>
                        </tr>
                    </table>

                    <p style="margin-top: 20px; font-size: 16px;">
                        Please contact the customer for any clarifications or additional details. 
                    </p>

                    <p style="color: #555;">Thank you for your prompt action!</p>
                </div>

                <!-- Footer Section -->
                <div style="background-color: #f1f1f1; text-align: center; padding: 10px;">
                    <p style="margin: 0; font-size: 14px; color: #777;">
                        © 2024 Your Company Name. All Rights Reserved.
                    </p>
                </div>
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


