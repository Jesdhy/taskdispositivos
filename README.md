# Transformers de Hugging Face y Pinecone 🤖

## 📘 About The Project

This project allows you to convert textual content from a PDF file into semantic vectors using Hugging Face's `sentence-transformers` models, and store them in a Pinecone vector index for intelligent meaning-based searches.

## 📑 Table of Contents

- [📘 About The Project](#about-the-project)
- [🚀 Getting Started](#getting-started)
  - [🔧 Prerequisites](#prerequisites)
  - [📥 Installation](#installation)
  - [⚙️ Running](#running)
- [🤝 Contributing](#contributing)

## 🚀 Getting Started
## 🔧 Prerequisites
**Python**: This project requires **Python 3.10.11**. Make sure you have this version installed on your system.
You can check your Python version by running:
```bash
python --version
 ```
## 📥 Installation

1.- Clone the repository

   ```sh
   git clone https://github.com/Jesdhy/taskdispositivos.git
  ```
2.- Create a virtual environment
 ```sh
    python python -m venv venv
   ```
 ```sh
    source venv\Scripts\activate 
   ```
3.- Install
```sh
    pip install pymupdf langchain langchain-community pinecone-client python-dotenv sentence-transformers
```
## ⚙️ Running

dowload pdf: https://drive.google.com/file/d/17dCygOfsJi_yRS9J5sFkiE3CLda1Xg2c/view?usp=sharing

  ```sh
    python main.py
   ```

## 🤝 Contributing
Thank you for your interest in contributing to this project! Here are some guidelines for doing so:

Link Hugging Face: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

1. **Fork the repository** and clone the project to your local machine.
2. **Create a new branch** for your changes.
3. **Commit your changes** with a clear, descriptive message.
4. **Submit a Pull Request** with a description of your changes.

Thank you for helping improve this project!