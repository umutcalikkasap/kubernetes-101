# Kubernetes 101: Orchestrating AI Models at Scale 🚀

![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

This repository demonstrates how to deploy a **Machine Learning Inference Service** (simulated with FastAPI) using **Kubernetes**. It was created as a practical demo for the **MLOps (YZV448E)** course to showcase the transition from Docker containers to a fully orchestrated cluster.

## 🎯 Core Concepts Demonstrated
This project proves the "Superpowers" of Kubernetes discussed in the presentation:

1.  **Orchestration:** Managing multiple replicas of an AI model automatically.
2.  **Self-Healing:** If a model replica crashes, Kubernetes automatically restarts it.
3.  **Load Balancing:** Traffic is distributed evenly across available pods.
4.  **Infrastructure as Code:** The entire state is defined declaratively in YAML.

---

## 📂 Project Structure

```bash
kubernetes-mlops-101/
├── app/
│   ├── main.py            # The AI Model Inference API (FastAPI)
│   └── requirements.txt   # Python dependencies
├── k8s/
│   └── deployment.yaml    # K8s Manifest (Deployment + Service)
├── Dockerfile             # Instructions to build the "Brick" (Container)
└── README.md              # You are here!
```

---

## 🛠️ Prerequisites

To run this demo locally, you need:
* **Docker Desktop** (Running)
* **Minikube** (Local Kubernetes Cluster)
* **kubectl** (The CLI tool to talk to the cluster)

---

## 🚀 Quick Start (Live Demo Guide)

Follow these steps to deploy the AI model to your local cluster.

### 1. Start the Cluster
Start your local Kubernetes cluster using Minikube:
```bash
minikube start
```

### 2. Build the Docker Image
**Crucial Step:** Normally, if you use Docker build, the image is installed on your computer. But Kubernetes (Minikube) can't see it. We need to install it in Docker inside Minikube.
```bash
eval $(minikube docker-env)
```
```
docker build -t ml-model:v1 .
```
Expected Status: The steps in the Dockerfile flow (Python is downloaded, libraries are installed). At the end, it says Successfully tagged ml-model:v1.

### 3. Deploy to Kubernetes
Send the instructions (Manifest) to the "Captain" (Control Plane).
```bash
kubectl apply -f k8s/deployment.yaml
```

Verify that the pods (replicas) are being created:
```bash
kubectl get pods
# You should see 3 pods with status "ContainerCreating" -> "Running"
```

### 4. Access the Service
Since we are using Minikube, we need a tunnel to expose the LoadBalancer service to our localhost.
*(Run this in a separate terminal window)*
```bash
minikube tunnel
```

Now, get the External IP:
```bash
kubectl get services
```

### 5. Test the Model 🧠
Open your browser or use `curl` to ask for a prediction:

```bash
# Replace localhost with the External-IP if needed
curl "http://localhost/predict?input_data=0.8"
```

**Response:**
```json
{
  "prediction": "Cat",
  "confidence": 0.92,
  "served_by_pod": "ml-model-deployment-xyz-123"
}
```
*Note the `served_by_pod` field. If you refresh, you will see different pod names handling the request. This proves **Load Balancing**!*

---

## 🧪 Testing "Self-Healing" (Chaos Engineering)

To demonstrate Kubernetes' resilience during the presentation:

1.  List the running pods:
    ```bash
    kubectl get pods
    ```
2.  **Kill one pod** manually (Simulating a crash):
    ```bash
    kubectl delete pod <POD_NAME>
    ```
3.  Watch the magic happen immediately:
    ```bash
    kubectl get pods
    ```
    *Result:* You will see the old pod "Terminating" and a NEW pod already "Running" or "ContainerCreating". Kubernetes maintains the desired state (3 replicas) no matter what.

---

## Cleaning Time

To release memory:
```bash
    minikube stop
    ```


## 👨‍💻 Author
**Umut Çalıkkasap**
* Artificial Intelligence and Data Engineering
* Istanbul Technical University (ITU)
* 📧 calikkasap21@itu.edu.tr
