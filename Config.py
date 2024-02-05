import pyodbc
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
import tempfile
import logging
current_date = datetime.now().strftime('%d/%m/%Y')
bucket_value = datetime.now().strftime('%Y%m%d')

excelName=f"TVS_LMS_MissingDealerUpdate{current_date}"

logging.basicConfig(
    filename='lmsapp.log',
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s]: %(message)s',
)

query1 = f"SELECT * FROM ThresholdMaster WHERE CONVERT(date, created_on) = CONVERT(date, '{current_date}', 103)"
query2 = f"SELECT * FROM TVSDealerThresholdFeeds feeds JOIN ThresholdMaster master ON feeds.DealerId = master.dealer_id AND feeds.branchId = master.branch_id WHERE bucket = '{bucket_value}' AND CONVERT(date, master.created_on) = CONVERT(date, '{current_date}', 103)"
query3 = f"SELECT * FROM TVSDealerThresholdFeeds feeds JOIN ThresholdMaster master ON feeds.DealerId = master.dealer_id AND feeds.branchId = master.branch_id WHERE bucket = '{bucket_value}' AND CONVERT(date, master.created_on) = CONVERT(date, '{current_date}', 103) AND feeds.thresholdGetdate IS NULL"
query4 = f"UPDATE A SET a.maxcount = RA.threshold from  TVSDealerThresholdFeeds A INNER JOIN ThresholdMaster RA ON A.DealerId = RA.dealer_id and a.branchId = RA.branch_id where bucket = '{bucket_value}' and CONVERT(date,RA.created_on)=CONVERT(date, '{current_date}', 103) and  a.thresholdGetdate IS NULL"