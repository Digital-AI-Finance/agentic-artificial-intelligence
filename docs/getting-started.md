---
layout: default
title: Getting Started
nav_order: 4
---

# Getting Started

Welcome to Agentic AI! This guide will help you set up your environment and run your first agent.

## Quick Start Options

### Option 1: Google Colab (Recommended for beginners)

The fastest way to get started - no local setup required!

1. Click any notebook link on the course homepage
2. The notebook opens in Google Colab
3. Add your API key in Colab secrets
4. Run the cells!

### Option 2: Local Development

For a full development environment on your machine.

## Local Setup Guide

### Step 1: Prerequisites

Ensure you have the following installed:

```bash
# Check Python version (need 3.11+)
python --version

# Check pip
pip --version

# Check git
git --version
```

### Step 2: Clone the Repository

```bash
git clone https://github.com/Digital-AI-Finance/agentic-artificial-intelligence.git
cd agentic-artificial-intelligence
```

### Step 3: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate on macOS/Linux
source venv/bin/activate

# Activate on Windows
.\venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Configure API Keys

Create a `.env` file in the project root:

```bash
# .env file
OPENAI_API_KEY=sk-your-key-here
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

{: .warning }
Never commit your `.env` file to version control!

### Step 6: Verify Installation

```python
# test_setup.py
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Say 'Hello, Agent!'"}],
    max_tokens=10
)

print(response.choices[0].message.content)
```

Run the test:
```bash
python test_setup.py
```

You should see: `Hello, Agent!`

## Getting API Keys

### OpenAI

1. Go to [platform.openai.com](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new secret key
5. Copy and save securely

### Anthropic

1. Go to [console.anthropic.com](https://console.anthropic.com/)
2. Sign up or log in
3. Navigate to API Keys
4. Create a new key
5. Copy and save securely

{: .note }
Both providers offer free credits for new accounts. Check their current offers.

## Running Notebooks

### Jupyter Lab (Local)

```bash
# Install Jupyter
pip install jupyterlab

# Start Jupyter
jupyter lab
```

Navigate to any week's notebook folder and open the `.ipynb` file.

### VS Code

1. Install the Python and Jupyter extensions
2. Open the repository folder
3. Open any `.ipynb` file
4. Select your Python interpreter
5. Run cells with Shift+Enter

## Troubleshooting

### API Key Not Found

```
Error: OPENAI_API_KEY not found
```

**Solution:** Ensure `.env` file exists and contains your key, and you're running from the project root.

### Module Not Found

```
ModuleNotFoundError: No module named 'langchain'
```

**Solution:** Activate your virtual environment and run `pip install -r requirements.txt`.

### Rate Limit Errors

```
Error: Rate limit exceeded
```

**Solution:** Wait a few seconds between API calls. Consider using `time.sleep(1)` between requests.

### Connection Errors

```
Error: Connection timeout
```

**Solution:** Check your internet connection. If using a VPN, try disabling it.

## Next Steps

1. Complete [Week 1: Introduction to Agentic AI]({{ '/weeks/week-1' | relative_url }})
2. Read the [ReAct paper](https://arxiv.org/abs/2210.03629)
3. Join the course [GitHub Discussions](https://github.com/Digital-AI-Finance/agentic-artificial-intelligence/discussions)

## Getting Help

- **Technical Issues:** Open a [GitHub Issue](https://github.com/Digital-AI-Finance/agentic-artificial-intelligence/issues)
- **Course Questions:** Use [GitHub Discussions](https://github.com/Digital-AI-Finance/agentic-artificial-intelligence/discussions)
- **Private Matters:** Email the instructor

---

Ready to build your first agent? Let's go!
