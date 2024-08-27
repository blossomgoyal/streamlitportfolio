FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Explicitly install Streamlit
RUN pip install streamlit

COPY . .

EXPOSE 8501

# Make sure the entrypoint script is executable
RUN chmod +x /app/entrypoint.sh

# Use an entrypoint script
ENTRYPOINT ["/app/entrypoint.sh"]