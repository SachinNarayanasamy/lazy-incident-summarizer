# 🦥 Lazy Incident Summarizer

A tiny local AI tool for turning long IT incident/ticket descriptions into a concise summary, priority suggestion, key issue, and suggested next action.

## Why it exists

Reading repetitive ticket descriptions takes time. This tool lets an IT support/developer quickly turn a long incident into an actionable summary.

## Open-source AI

The app uses **Gemma 3 1B**, an open-weight model, through **Ollama**. Inference runs locally on the user's machine.

No hosted AI API is required.

## Run locally

### 1. Install Ollama

Install Ollama from https://ollama.com/

### 2. Download the model

```bash
ollama pull gemma3:1b
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the app

```bash
streamlit run app.py
```

Then open the local Streamlit URL shown in your terminal.

## Example

Input:

> Users in the Chennai office are unable to access the internal VPN since 9:30 AM. Multiple employees report authentication failures. The issue started after the morning network maintenance window.

Example output:

- Summary: Chennai office users are experiencing VPN authentication failures since 9:30 AM.
- Priority: High
- Key Issue: Multiple users cannot authenticate to the VPN.
- Suggested Next Action: Check the VPN authentication service and changes made during the maintenance window.

## Hacktoberfest Week 3

Built for the **Hacktoberfest Open-Source AI Challenge: Week 3 — Slow and Steady**.

The goal is simple: automate the boring part of reading incident descriptions so people can spend less time reading and more time resolving.

## License

MIT
