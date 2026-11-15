# ⚡ CI/CD Demo Quickstart & Hands-On Guide

This note provides a quick, practical example of how to use, test, and deploy this automated CI/CD demo.

---

## 🎯 What is this CI/CD Demo?

A modern DevOps pipeline combining:
1. **Local Test & Simulation Engine** (`tests/test_website.py` & `simulate_pipeline.py`)
2. **Interactive Web Dashboard** (`index.html`, `assets/`)
3. **Cloud CI/CD Automation** (`.github/workflows/deploy.yml` on GitHub Actions)
4. **Zero-Downtime Production CDN** (GitHub Pages)

---

## 🚀 Practical Example: 4 Ways to Use It

### Scenario 1: Run the Interactive Web Portal Locally

Preview the clean dashboard and click the interactive buttons:

```bash
cd /home/Aishwar/demo
./simulate_pipeline.py --serve
```

1. Open your browser and go to: **`http://localhost:8080/`**
2. Click **"Simulate CI/CD Pipeline" ⚡** to watch stages 1 through 5 light up in sequence.
3. Click **"Run Test Suite"** to run client-side verification checks.
4. Press `Ctrl + C` in your terminal when you want to stop the server.

---

### Scenario 2: Run the 5-Stage Pipeline in Your Terminal

Simulate the exact steps executed by the GitHub Actions cloud runner:

```bash
cd /home/Aishwar/demo
./simulate_pipeline.py
```

**What it does:**
- **Stage 1 (Trigger):** Detects git commit hash on branch `main`.
- **Stage 2 (Lint):** Validates HTML, CSS, JS, and workflow syntax.
- **Stage 3 (Unit Tests):** Runs all 6 Python unit tests.
- **Stage 4 (Build):** Simulates dynamic `sed` metadata injection.
- **Stage 5 (Deploy):** Simulates zero-downtime deployment to GitHub Pages.

---

### Scenario 3: See How CI Catches Errors (Safety Circuit Breaker)

Simulate what happens if someone pushes broken code:

```bash
cd /home/Aishwar/demo
./simulate_pipeline.py --fail-test
```

**Result:**
- CI runs unit tests, detects the regression, and immediately halts with exit code 1.
- **Deployment is blocked**, keeping production 100% safe from bad releases.

---

### Scenario 4: Push Changes to Live Production (Real CI/CD)

Whenever you edit files and push to GitHub, the real cloud pipeline triggers automatically:

```bash
cd /home/Aishwar/demo

# 1. Stage and commit your changes
git add .
git commit -m "feat: updated website headline"

# 2. Push to GitHub
git push origin main
```

**Where to check live:**
- **GitHub Actions Runner:** [https://github.com/aishwar2/demo/actions](https://github.com/aishwar2/demo/actions)
- **Live Production Website:** [https://aishwar2.github.io/demo/](https://aishwar2.github.io/demo/)

---

## 🧪 Run Unit Tests Directly

Run the official test suite executed by the CI server:

```bash
cd /home/Aishwar/demo
python3 -m unittest discover -s tests -p "test_*.py" -v
```

---

## 📋 Quick Command Cheat Sheet

| Task | Command |
| :--- | :--- |
| **Launch Browser Dashboard** | `./simulate_pipeline.py --serve` |
| **Simulate Full Pipeline (CLI)** | `./simulate_pipeline.py` |
| **Simulate CI Failure Gate** | `./simulate_pipeline.py --fail-test` |
| **Run Python Unit Tests** | `python3 -m unittest discover -s tests -v` |
| **Deploy Live to GitHub** | `git push origin main` |
