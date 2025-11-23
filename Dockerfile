# Python 3.9'un hafif (slim) versiyonunu kullan
FROM python:3.9-slim

# Konteyner içindeki çalışma klasörümüz
WORKDIR /app

# Önce gereksinimleri kopyala ve yükle (Cache avantajı için)
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Şimdi kodların geri kalanını kopyala
COPY app/ .

# Konteyner çalıştığında bu komutu çalıştır
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]