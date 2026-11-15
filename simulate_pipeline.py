#!/usr/bin/env python3
"""
CI/CD Pipeline Simulator & Demo Engine
Demonstrates modern Continuous Integration & Continuous Deployment workflows locally.
"""

import sys
import os
import time
import subprocess
import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler

REPO_ROOT = os.path.abspath(os.path.dirname(__file__))

# ANSI color codes
C_RESET = "\033[0m"
C_BOLD = "\033[1m"
C_GREEN = "\033[32m"
C_CYAN = "\033[36m"
C_YELLOW = "\033[33m"
C_RED = "\033[31m"
C_MAGENTA = "\033[35m"
C_BLUE = "\033[34m"

def print_header(title):
    print(f"\n{C_BOLD}{C_CYAN}{'='*60}{C_RESET}")
    print(f"{C_BOLD}{C_CYAN} ⚡ {title}{C_RESET}")
    print(f"{C_BOLD}{C_CYAN}{'='*60}{C_RESET}\n")

def print_step(num, total, name, desc):
    print(f"{C_BOLD}{C_BLUE}[STAGE {num}/{total}]{C_RESET} {C_BOLD}{name}{C_RESET}: {desc}")

def run_cmd(cmd, cwd=REPO_ROOT):
    p = subprocess.run(cmd, shell=True, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return p.returncode, p.stdout.strip(), p.stderr.strip()

def stage_trigger():
    print_step(1, 5, "Trigger (Git Push / Webhook)", "Receiving commit payload on branch 'main'")
    time.sleep(0.5)
    rc, git_hash, _ = run_cmd("git rev-parse --short HEAD")
    rc2, git_msg, _ = run_cmd("git log -1 --pretty=%B")
    commit_sha = git_hash if rc == 0 else "a1b2c3d"
    commit_msg = git_msg.split('\n')[0] if rc2 == 0 else "feat: update pipeline assets"

    print(f"   {C_GREEN}✓{C_RESET} Event: {C_BOLD}push{C_RESET} -> {C_YELLOW}refs/heads/main{C_RESET}")
    print(f"   {C_GREEN}✓{C_RESET} Commit SHA: {C_BOLD}{commit_sha}{C_RESET} (\"{commit_msg}\")")
    print(f"   {C_GREEN}✓{C_RESET} Runner: Ubuntu Linux container initialized in GitHub Cloud")
    time.sleep(0.4)
    return commit_sha

def stage_lint():
    print_step(2, 5, "Lint & Syntax Verification (CI)", "Validating files and repository structure")
    time.sleep(0.4)

    files_to_check = [
        ("index.html", "HTML5 Entrypoint"),
        ("assets/style.css", "Stylesheet"),
        ("assets/app.js", "Client Interactive Engine"),
        (".github/workflows/deploy.yml", "GitHub Actions Workflow")
    ]

    all_ok = True
    for rel_path, label in files_to_check:
        full_path = os.path.join(REPO_ROOT, rel_path)
        if os.path.exists(full_path) and os.path.getsize(full_path) > 0:
            print(f"   {C_GREEN}✓{C_RESET} {label} ({rel_path}): {C_GREEN}OK{C_RESET} ({os.path.getsize(full_path)} bytes)")
        else:
            print(f"   {C_RED}✗{C_RESET} {label} ({rel_path}): {C_RED}MISSING OR EMPTY{C_RESET}")
            all_ok = False
        time.sleep(0.15)

    if not all_ok:
        print(f"\n{C_RED}🛑 LINT FAILURE: Missing critical repository assets!{C_RESET}")
        return False

    print(f"   {C_GREEN}✅ All syntax and file structure verifications passed.{C_RESET}")
    time.sleep(0.3)
    return True

def stage_test(fail_test=False):
    print_step(3, 5, "Automated Test Suite (CI)", "Executing unit test suite in runner")
    time.sleep(0.4)

    if fail_test:
        print(f"   {C_YELLOW}⚠ SIMULATION: Injecting intentional test failure...{C_RESET}")
        time.sleep(0.5)
        print(f"   {C_RED}FAIL: test_regression_check (__main__.TestWebsiteStructure){C_RESET}")
        print(f"   AssertionError: Simulated test failure: regression detected in staging build!")
        print(f"\n{C_BOLD}{C_RED}🛑 CI PIPELINE FAILED!{C_RESET}")
        print(f"   {C_RED}Deployment halted. Zero changes pushed to production. Developer alerted.{C_RESET}\n")
        return False

    cmd = "python3 -m unittest discover -s tests -p 'test_*.py' -v"
    rc, stdout, stderr = run_cmd(cmd)
    output = stdout if stdout else stderr

    for line in output.split('\n'):
        if line.strip():
            if "ok" in line:
                print(f"   {C_GREEN}✓{C_RESET} {line.strip()}")
            elif "FAILED" in line:
                print(f"   {C_RED}✗{C_RESET} {line.strip()}")
            else:
                print(f"     {line.strip()}")
        time.sleep(0.05)

    if rc != 0:
        print(f"\n{C_BOLD}{C_RED}🛑 CI TEST SUITE FAILED (exit code {rc})!{C_RESET}")
        return False

    print(f"\n   {C_GREEN}✅ All unit tests PASSED. Continuous Integration succeeded.{C_RESET}")
    time.sleep(0.3)
    return True

def stage_build(commit_sha):
    print_step(4, 5, "Build & Metadata Injection (CD)", "Preparing production deployment artifact")
    time.sleep(0.4)

    build_id = f"BUILD_#{int(time.time()) % 10000}"
    deploy_time = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())

    print(f"   {C_GREEN}✓{C_RESET} Injected Build Number: {C_BOLD}{build_id}{C_RESET}")
    print(f"   {C_GREEN}✓{C_RESET} Injected Commit SHA:   {C_BOLD}{commit_sha}{C_RESET}")
    print(f"   {C_GREEN}✓{C_RESET} Injected Timestamp:    {C_BOLD}{deploy_time}{C_RESET}")
    print(f"   {C_GREEN}✓{C_RESET} Bundled static assets: HTML, CSS, JS, images")
    time.sleep(0.4)
    return build_id

def stage_deploy(build_id):
    print_step(5, 5, "Continuous Deployment (CD)", "Publishing release to production CDN")
    time.sleep(0.4)
    print(f"   {C_GREEN}✓{C_RESET} Target: {C_BOLD}GitHub Pages CDN (https://aishwar2.github.io/demo/){C_RESET}")
    print(f"   {C_GREEN}✓{C_RESET} Strategy: Zero-downtime atomic swap")
    print(f"   {C_GREEN}✓{C_RESET} Release Status: {C_GREEN}LIVE IN PRODUCTION (100% healthy){C_RESET}")
    time.sleep(0.3)

def serve_preview(port=8080):
    os.chdir(REPO_ROOT)
    for p in [port, 8081, 8082, 8000, 3000]:
        try:
            HTTPServer.allow_reuse_address = True
            server_address = ('', p)
            httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
            print(f"\n{C_BOLD}{C_GREEN}🌐 Local Preview Server running at: http://localhost:{p}/{C_RESET}")
            print(f"{C_YELLOW}Press Ctrl+C to stop the server.{C_RESET}\n")
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\nStopping server...")
                httpd.server_close()
            return
        except OSError as e:
            if p == 3000:
                print(f"{C_RED}Could not bind to any test port (8080-8082, 8000, 3000): {e}{C_RESET}")
                raise

def main():
    parser = argparse.ArgumentParser(description="CI/CD Pipeline Simulator & Demo Engine")
    parser.add_argument("--fail-test", action="store_true", help="Simulate a test failure in the CI phase")
    parser.add_argument("--serve", action="store_true", help="Start local web server to view the deployed portal")
    parser.add_argument("--port", type=int, default=8080, help="Port for the local web server (default: 8080)")
    args = parser.parse_args()

    print_header("DevOps CI/CD Automated Pipeline Simulator")
    start_time = time.time()

    commit_sha = stage_trigger()
    if not stage_lint():
        sys.exit(1)

    if not stage_test(fail_test=args.fail_test):
        sys.exit(1)

    build_id = stage_build(commit_sha)
    stage_deploy(build_id)

    elapsed = round(time.time() - start_time, 2)
    print(f"\n{C_BOLD}{C_GREEN}{'='*60}{C_RESET}")
    print(f"{C_BOLD}{C_GREEN}🎉 CI/CD PIPELINE SUCCEEDED in {elapsed}s!{C_RESET}")
    print(f"{C_BOLD}{C_GREEN}{'='*60}{C_RESET}\n")

    if args.serve:
        serve_preview(port=args.port)
    else:
        print(f"Tip: Run {C_BOLD}python3 simulate_pipeline.py --serve{C_RESET} to view the live dashboard in your browser.")
        print(f"Tip: Run {C_BOLD}python3 simulate_pipeline.py --fail-test{C_RESET} to demonstrate automated CI failure prevention.")

if __name__ == "__main__":
    main()
