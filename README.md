# 🛡️ Automated Python Password Generator
### CI/CD & Containerization Project

## 📌 Project Overview
This project demonstrates a full **DevOps Lifecycle**. I developed a Python-based security tool, containerized it using **Docker**, and implemented an automated **CI/CD pipeline** via **GitHub Actions** for testing and deployment to **Docker Hub**.

---

## 🚀 Workflow Steps (End-to-End)

### 1. Development & Containerization
* **Code**: Developed `pass_gen.py` to generate secure passwords based on user input.
* **Dockerize**: Created a `Dockerfile` to package the Python environment.
* **Local Build**: 
  ```bash
  docker build -t pass-gen-tool .
