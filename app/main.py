from fastapi import FastAPI
import random
import os
import time

app = FastAPI()

# MLOps: Model Versiyonunu ortam değişkeninden alalım
MODEL_VERSION = os.getenv("MODEL_VERSION", "v1.0.0")

@app.get("/")
def root():
    """Basit bir giriş noktası."""
    return {
        "message": "MLOps Inference Server is Running",
        "version": MODEL_VERSION
    }

@app.get("/predict")
def predict(input_data: float):
    """
    Ağır bir AI model tahminini simüle eder.
    """
    # Yapay bir gecikme ekleyelim (Sanki model düşünüyormuş gibi)
    # time.sleep(0.05) 
    
    # Sahte tahmin mantığı
    confidence = random.uniform(0.70, 0.99)
    prediction = "Cat" if input_data > 0.5 else "Dog"
    
    # Hangi Pod'un cevap verdiğini (HOSTNAME) dönüyoruz. 
    # Bu sayede Load Balancing'i kanıtlayacağız.
    return {
        "prediction": prediction,
        "confidence": round(confidence, 4),
        "model_version": MODEL_VERSION,
        "served_by_pod": os.getenv("HOSTNAME", "unknown-pod") 
    }

@app.get("/health")
def health_check():
    """
    Kubernetes 'Liveness Probe' burayı kontrol eder.
    Eğer 200 dönerse, K8s "bu pod yaşıyor" der.
    """
    return {"status": "healthy"}
