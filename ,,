# ============================================================
#Group Manager Bot
# Author: LearningBotsOfficial (https://github.com/LearningBotsOfficial) 
# Support: https://t.me/LearningBotsCommunity
# Channel: https://t.me/learning_bots
# YouTube: https://youtube.com/@learning_bots
# License: Open-source (keep credits, no resale)
# ============================================================

# Start from a lightweight Python image
FROM python:3.10-slim
WORKDIR /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt
    
# Environment variable to force unbuffered output (helps in logging)
ENV PYTHONUNBUFFERED=1

# Run the bot..
CMD ["python", "main.py"]
