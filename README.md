# Full Stack Internship Assignment

This repository contains my solution for the Full Stack Internship Technical Assignment.

## Part 1 – Token Optimization

Implemented two strategies to reduce token usage in an AI agent pipeline:

- Prompt compression by removing redundant context.
- Context filtering / retrieval so only relevant information is sent to the model.

Result:

| Metric       | Before  | After  |
| ------------ | ------- | ------ |
| Input Tokens | 100,000 | 38,000 |
| Reduction    | -       | 62%    |

Quality remained almost unchanged while reducing cost and improving response speed.

---

## Part 2 – Debugging

Debugged an unreliable multi-agent workflow by:

- Checking logs for each pipeline step.
- Reproducing intermittent failures.
- Validating API responses.
- Identifying timeout, malformed output and incorrect data issues.
- Adding logging, retries and output validation.

---

## Part 3 – CI/CD

Implemented a GitHub Actions pipeline that:

- Runs flake8 linting.
- Runs pytest automatically.
- Deploys to staging after successful tests on the main branch.

Secrets should be stored using GitHub Secrets instead of hardcoding API keys.

If production deployment fails, rollback to the previous stable release immediately while investigating logs.

---

## Tech Stack

- Python
- Git
- GitHub Actions
- Pytest
- Flake8

---

## Repository Structure

```
.github/workflows/
part1/
part2/
part3/
README.md
```
