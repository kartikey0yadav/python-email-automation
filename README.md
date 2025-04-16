# 📧 Email Automation with Python

A simple and powerful Python script to send personalized emails in bulk using data from an Excel sheet. Ideal for small teams, educators, HR professionals, or anyone who wants to automate regular email communication.

---

## 📌 Features

- Read recipient names and emails from an Excel file
- Personalized greeting for each contact
- Sends plain-text emails via Gmail's SMTP
- Debug mode enabled for easier troubleshooting
- Easily customizable message template

---

## 🛠️ Requirements

- Python 3.x
- Required Python packages:
  - `pandas`
  - `openpyxl`
  - `smtplib` (built-in)
  - `email` (built-in)

Install dependencies with:

```bash
pip install pandas openpyxl
```
## 📁 Email-Automation

- ├── email_automation.py
- ├── data.xlsx              # Excel file with contacts
- ├── Documentation.pdf
- ├── Novelty.pdf
- ├── Future_Scope.pdf
- └── README.md

---

## 📋 How to Use
Prepare Your Excel File

1. Make sure data.xlsx has the following columns:


- `Full name`	`Email Address`
- `John Doe`	`john@example.com`
- `Jane Smith`	`jane@example.com`

## Update Email Credentials

- In `email_automation.py`, set your Gmail address and app password:
  - `FROM` = `'your-email@gmail.com'`
  - `PASS` = `'your-app-password'`
### ⚠️ Important: Use App Passwords instead of your regular Gmail password.

## Run the Script

`python email_automation.py` 
- Each contact will receive a personalized email message.

---

## 🔒 Security Best Practices

- Do not commit your credentials to version control.

- Use `.env` files or environment variables to store sensitive data.

- For production, consider using OAuth2 with Gmail API instead of SMTP login.

## 🚀 Future Scope
- HTML email templates for richer designs

- Support for attachments (PDFs, images, etc.)

- Scheduled email sending (via cron or apscheduler)

- Integration with Google Sheets API

GUI using Tkinter, Flask, or Streamlit

Email analytics (open/click tracking)
