# Mass Email Distribution System using AWS Lambda, S3, and SES

This serverless project allows you to automatically send personalized mass emails using **AWS Lambda**, **Amazon S3**, and **Amazon SES**. Upload a CSV file to S3, and Lambda will read the file, extract recipient names and email addresses, and send emails via SES.

---

## 🧰 Tech Stack

- **AWS Lambda** – Serverless compute for processing CSV and sending emails.
- **Amazon S3** – Stores the uploaded CSV files.
- **Amazon SES (Simple Email Service)** – Sends the emails.
- **Python 3.12** – Runtime for Lambda function.

---

## 📁 Folder Structure
- lambda_fuction.py
- Email.
- README.md


---

## 📥 CSV Format 

Upload your file to S3 bucket path: `uploads/Email2.csv`

```csv
email,name
badarqashakoor25@gmail.com,Badarqa
hirahshakoor@hotmail.com,Hirah
Make sure it's saved as UTF-8 (no BOM). Use CSV UTF-8 (Comma delimited) in Excel.

## **How It Works**
Upload Email2.csv to S3 bucket (myemailbucketbybadarqa/uploads/Email2.csv)

AWS Lambda is triggered manually or via a scheduled event.

Lambda reads the CSV, parses each row, and sends a personalized email using SES.

