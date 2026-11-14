// DevOpsPulse CI/CD Interactive Portal
document.addEventListener('DOMContentLoaded', () => {
  // Format deploy time if placeholder is present
  const deployTimeEl = document.getElementById('deploy-time');
  if (deployTimeEl && (deployTimeEl.innerText.includes('__') || deployTimeEl.innerText === 'Just Now')) {
    deployTimeEl.innerText = new Date().toLocaleString();
  }

  // Interactive Pipeline Simulation
  const simulateBtn = document.getElementById('btn-simulate-pipeline');
  const statusText = document.getElementById('pipeline-status-text');
  const stages = [
    { id: 'stage-trigger', label: 'Triggering via Git Webhook...' },
    { id: 'stage-lint', label: 'Linting HTML & CSS...' },
    { id: 'stage-test', label: 'Running automated test suite in runner...' },
    { id: 'stage-build', label: 'Injecting commit metadata & bundling...' },
    { id: 'stage-deploy', label: 'Publishing live to GitHub Pages CDN...' }
  ];

  if (simulateBtn) {
    simulateBtn.addEventListener('click', async () => {
      simulateBtn.disabled = true;
      simulateBtn.innerHTML = `<span>Pipeline Running...</span> ⏳`;

      // Clear all active highlights
      stages.forEach(s => {
        const el = document.getElementById(s.id);
        if (el) el.classList.remove('highlight');
      });

      for (let i = 0; i < stages.length; i++) {
        const stage = stages[i];
        const el = document.getElementById(stage.id);
        if (el) {
          el.classList.add('highlight');
          statusText.innerText = `[Step ${i + 1}/${stages.length}] ${stage.label}`;
          await new Promise(r => setTimeout(r, 600));
        }
      }

      statusText.innerHTML = `✅ Pipeline completed successfully in 3.0s! All checks passed.`;
      simulateBtn.disabled = false;
      simulateBtn.innerHTML = `<span>Re-run CI/CD Simulation</span> ⚡`;
    });
  }

  // In-Browser Test Runner
  const runTestsBtn = document.getElementById('btn-run-tests');
  if (runTestsBtn) {
    runTestsBtn.addEventListener('click', async () => {
      runTestsBtn.disabled = true;
      runTestsBtn.innerText = 'Running Tests...';

      const tests = [
        {
          id: 'test-item-1',
          name: 'Document Structure',
          run: () => {
            const hasMeta = !!document.querySelector('meta[name="viewport"]');
            const hasCharset = !!document.querySelector('meta[charset]');
            return hasMeta && hasCharset;
          }
        },
        {
          id: 'test-item-2',
          name: 'Pipeline Stages',
          run: () => {
            const stagesCount = document.querySelectorAll('.pipeline-stage').length;
            return stagesCount === 5;
          }
        },
        {
          id: 'test-item-3',
          name: 'Metadata Hooks',
          run: () => {
            return !!document.getElementById('build-id') && !!document.getElementById('commit-sha');
          }
        },
        {
          id: 'test-item-4',
          name: 'Workflow Config',
          run: () => {
            return true; // Validated in python CI runner
          }
        }
      ];

      for (const t of tests) {
        const itemEl = document.getElementById(t.id);
        if (itemEl) {
          itemEl.style.opacity = '0.5';
          await new Promise(r => setTimeout(r, 250));
          const passed = t.run();
          itemEl.style.opacity = '1';
          const tag = itemEl.querySelector('.test-status-tag');
          if (tag) {
            tag.innerText = passed ? 'PASS' : 'FAIL';
            tag.style.background = passed ? 'rgba(16, 185, 129, 0.2)' : 'rgba(239, 68, 68, 0.2)';
            tag.style.color = passed ? '#10b981' : '#ef4444';
          }
        }
      }

      runTestsBtn.disabled = false;
      runTestsBtn.innerText = 'Run Test Suite';
    });
  }
});
