# Part 3 – CI/CD and Deployment

## 1. CI/CD Pipeline

The GitHub Actions workflow performs the following steps:

- Trigger on every push.
- Trigger on pull requests to the main branch.
- Install Python dependencies.
- Run flake8 for linting.
- Run pytest for testing.
- If tests pass and code is merged into the main branch, deploy the application to the staging environment.

---

## 2. Managing Secrets

API keys and secrets should never be stored directly in the repository.

Instead, GitHub Actions Secrets should be used.

Example:

Settings

↓

Secrets and Variables

↓

Actions

↓

OPENAI_API_KEY

The workflow accesses secrets using:

```yaml
${{ secrets.OPENAI_API_KEY }}
```

Benefits:

- Secure
- Encrypted
- Not visible in repository history

---

## 3. Rollback Plan

If a production deployment fails, my first five minutes would be:

1. Stop the deployment.
2. Check monitoring dashboards and logs.
3. Roll back to the previous stable version.
4. Verify application health.
5. Investigate the root cause after service is restored.

This approach minimizes downtime while ensuring users regain access as quickly as possible.
