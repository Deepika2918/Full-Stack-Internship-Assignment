# AI Internship Assignment

This repository contains my solution for the AI Internship Technical Assignment.

## Part 1 – Token Optimization

Implemented two optimization strategies:

- Context Compression
- Retrieval-Augmented Prompting (RAG)

These reduce token usage from approximately **100K tokens** to **28K tokens**, lowering API cost and improving response time while maintaining output quality.

---

## Part 2 – Debugging

Documented a structured debugging workflow for an intermittent multi-agent pipeline.

The process includes:

- Reproducing failures
- Log analysis
- Component isolation
- JSON validation
- Timeout investigation
- Root cause analysis

---

## Part 3 – CI/CD

Created a GitHub Actions workflow that:

- Runs linting using flake8
- Runs tests using pytest
- Deploys to a staging environment after successful validation

The repository also includes a deployment strategy, secure secret management approach, and production rollback plan.

---

## Repository Structure

```
AI-Intern-Assignment/
│
├── part1/
├── part2/
├── part3/
├── .github/workflows/
└── README.md
```
