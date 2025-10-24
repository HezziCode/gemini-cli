# 🚀 Gemini CLI Tutorial Series — Part 7: Custom Slash Commands

## 🔹 1. What Are Custom Slash Commands?

In Gemini CLI, slash commands (like /mcp or /help) are shortcuts for actions.

Custom slash commands let you create your own command like /plan, /summarize, /commit, etc.

## 🔹 2. Why They Matter

Reuse powerful prompts instead of typing them again and again.

Maintain consistency — e.g., every plan or commit follows your structure.

Build your AI-powered workflow library (custom tools for writing, coding, docs, etc.).

💡 Big takeaway: “Custom commands turn prompting into automation.”

## 🔹 3. Preparing the Environment

**Update Gemini CLI:**

```
npm install -g @google/gemini-cli@latest
gemini -v   # atleast v0.4.0+
```

## 🔹 4. Building Your First Command: /plan

### Before we jump in, let’s do one small setup step so Gemini knows where to find your custom tool.

**🧩 Prerequisite:**

To create a custom tool, you must add a `.toml` file inside a special folder called `.gemini/commands`.
This folder is where Gemini CLI looks for your personal commands.

Use `~/.gemini/commands/` → to make your command available from any project (global).

Or use `./.gemini/commands/` inside a project → to keep it only for that project.

Example structure (for a project command):

```
my-project/
└── .gemini/
    └── commands/
        └── plan.toml
``` 
#### Once the file is there, Gemini can detect it as soon as you restart the CLI.

**Step 1: Create File**
``` 
~/gemini/commands/plan.toml
```

**Step 2: Define Behavior**

Open `plan.toml` and add:
 
```
description="Creates a detailed strategic plan."
prompt = """
Your role is a strategist.
Think deeply and make a step-by-step plan for: {{args}}
Do NOT write or execute code.
Structure your answer as:
1. Understanding the Goal
2. Analysis
3. Strategy
4. Verification
5. Challenges
"""
```

**Step 3 – Run Your Command**

Restart Gemini CLI → then type:

```
/plan build a weather app
```

#### ✅ You’ll see a clear, markdown-structured plan — no code.

### 🔹 5. Pro-Level Use Cases

| Type          | Example Command            | Purpose          |
| ------------- | -------------------------- | ---------------- |
| `/plan`       | planning workflows         | project strategy |
| `/summarize`  | summarize code/docs        | productivity     |
| `/git:commit` | AI-written commit messages | dev tools        |
| `/tech-edit`  | enforce style guide        | doc quality      |
