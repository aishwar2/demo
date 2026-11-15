# 🚀 Automated CI/CD Test Website

An end-to-end demonstration of modern **Continuous Integration (CI)** and **Continuous Deployment (CD)** powered by **GitHub Actions** and **GitHub Pages**.

---

## 📖 What is CI/CD?

**CI/CD** bridges the gap between development and operations by automating the building, testing, and deployment of applications:

### 1. Continuous Integration (CI)
* **Goal:** Merge code changes frequently without breaking the main codebase.
* **Mechanism:** Every push or pull request automatically triggers automated linters, syntax validators, and test suites (`unittest`).
* **Benefit:** Detects bugs within seconds of writing code, preventing regression errors.

### 2. Continuous Delivery & Continuous Deployment (CD)
* **Continuous Delivery:** Automates packaging and prepares deployable artifacts ready for production with one click.
* **Continuous Deployment:** Takes every commit that passes the CI pipeline and releases it directly to the live production environment without human intervention.

---

## 🔄 The CI/CD Pipeline Flow

```mermaid
flowchart LR
    A[👨‍💻 Git Push to main] --> B[⚙️ GitHub Actions Runner]
    subgraph CI ["Continuous Integration"]
        B --> C[🔍 Checkout Code]
        C --> D[🧪 Run Python Unit Tests]
        D --> E{Tests Pass?}
    end
    E -- ❌ No --> F[🛑 Build Fails & Developer Alerted]
    E -- ✅ Yes --> G[📦 Inject Run Metadata]
    subgraph CD ["Continuous Deployment"]
        G --> H[🚀 Deploy to GitHub Pages CDN]
        H --> I[🌐 Live Production Website]
    end
```

---

## 🛠️ Project Structure

```
├── .github/
│   └── workflows/
│       └── deploy.yml      # CI/CD pipeline definition
├── assets/
│   ├── app.js              # Interactive client simulation & DOM tests
│   └── style.css           # Modern dark-theme glassmorphism UI
├── tests/
│   └── test_website.py     # Automated test suite executed by CI runner
├── simulate_pipeline.py    # Local interactive CLI pipeline runner & previewer
├── index.html              # Main responsive web portal
└── README.md               # Documentation & setup guide
```

---

## ⚡ Interactive CI/CD Simulator (CLI)

Run the full 5-stage automated CI/CD pipeline locally with live logging:

```bash
# 1. Run full automated pipeline simulation (Trigger -> Lint -> Test -> Build -> Deploy)
./simulate_pipeline.py

# 2. Simulate pipeline failure (demonstrating how CI aborts before deployment)
./simulate_pipeline.py --fail-test

# 3. Launch local live preview server (http://localhost:8080)
./simulate_pipeline.py --serve
```

---

## 🧪 Running Unit Tests Locally

You can run the same automated test suite executed by the CI server on your local machine:

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

---

## ⚙️ Enabling GitHub Pages (One-Time 10-Second Setup)

To allow GitHub Actions to publish the site to GitHub Pages:
1. Open repository settings: [demo/settings/pages](https://github.com/aishwar2/demo/settings/pages)
2. Under **Build and deployment** > **Source**, change from *Deploy from a branch* to **GitHub Actions**.
3. Go to [demo/actions](https://github.com/aishwar2/demo/actions), click **CI/CD Pipeline & GitHub Pages Deploy** > **Re-run all jobs**.
4. Your live website is immediately published at:
   👉 **https://aishwar2.github.io/demo/**
