FROM python:3.9

WORKDIR /app

# Installing dependencies
RUN pip install transformers requests

# Script to fetch data and generate report
COPY report_generator.py .

# Set cron schedule to run every day at midnight, we can modify it as per our requirement
RUN echo "0 0 * * * python report_generator.py >> /app/report.txt" > crontab.txt
RUN crontab crontab.txt
RUN cron && crontab -e

# Start cron service
CMD ["cron", "-f"]
