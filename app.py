from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>AWS DevOps Project 🚀</h1>
    <p>Successfully deployed on Amazon EKS using Terraform & Kubernetes</p>
    """

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
