---
name: repo-mind
description: Automatically analyze GitHub repositories and reverse engineer software architecture. Activate when a user provides a GitHub link (github.com/...), asks to analyze a repository, understand a codebase, reverse engineer a project, evaluate SaaS potential, or improve a GitHub project.

---

# Repo Mind Skill

This skill analyzes GitHub repositories and provides strategic insights.

Capabilities:

1. Reverse engineer repository architecture
2. Summarize project files efficiently
3. Evaluate SaaS startup potential
4. Optimize the product using Elon Musk's framework

---

## When to Use This Skill

Activate this skill when the user:

- pastes a GitHub repository link
- asks to analyze a repository
- asks if a project could become a SaaS
- asks to reverse engineer a GitHub repo
- asks how to improve a project architecture

Example triggers:

Analyze this repo: https://github.com/user/project

Explain this GitHub repository.

Could this repo become a SaaS product?

Break down this codebase

---

# Automatic GitHub Detection

If the user message contains:

github.com/
https://github.com/
http://github.com/

assume it is a repository link and automatically run the repository analysis workflow.

---

## Instructions

When the skill is activated, follow this workflow:

Default entry command: /analyze-repo

1. Identify the GitHub repository.
2. Analyze the repository structure.
3. Detect the main technology stack.
4. Summarize key files and modules.
5. Evaluate SaaS startup potential.
6. Apply Elon Musk's product framework to improve the project.

Return results in structured sections.

---

## Token Efficiency Rules

To minimize token usage:

- Do NOT read every file in the repository.

Repository analysis priority order:

1. README.md
2. package.json / requirements.txt
3. main application entry file
4. folder structure
5. core modules

Avoid deep file reading unless necessary.

Most repositories can be understood from these sources.

Prefer analyzing repository structure over full file contents.

File explanations must be limited to **one sentence each**.

Ignore folders such as:

- node_modules
- build
- dist
- .git
- lock files

---

## Commands

### /analyze-repo

Analyze repository architecture.

Steps:

1. Scan folder tree
2. Identify tech stack
3. Summarize important files
4. Detect core functionality

Output format:

REPO SUMMARY
- Purpose
- Tech stack
- Key modules

FILE ANALYSIS
- file → short description

---

### /saas-potential

Evaluate whether the repository could become a SaaS product.

Steps:

1. Identify the problem solved
2. Evaluate market demand
3. Detect monetization opportunities
4. Estimate viral potential

Output:

SAAS REPORT
- Problem solved
- Target audience
- Monetization model
- Competitors
- SaaS score (0–10)

---

### /optimize-product

Apply Elon Musk's product framework.

Steps:

1. Question requirements
2. Delete unnecessary parts
3. Simplify architecture
4. Accelerate development
5. Automate processes
6. Optimize user experience
7. Plan for scalability

Output:

PRODUCT OPTIMIZATION REPORT
- Current architecture flaws
- Suggested improvements
- Feature roadmap

---

## References

- references/musk-framework.md

---

## Examples

- examples/example-output.md