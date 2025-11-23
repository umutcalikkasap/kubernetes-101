# Kubernetes 101: Orchestrating AI Models at Scale 🚀

A practical demonstration of deploying, scaling, and orchestrating AI inference services using Kubernetes and Docker. Prepared for MLOps Course (Fall 2025).




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
