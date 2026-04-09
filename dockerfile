FROM python:3.14-slim
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt
COPY app/ /app/
COPY ansible/ /ansible/
COPY state/ /state/
RUN chmod +x /ansible/vault-pass.sh
WORKDIR /
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["sleep", "infinity"]