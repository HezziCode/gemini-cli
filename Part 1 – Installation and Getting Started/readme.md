## 🌟 Gemini CLI – Part 1: Installation and Getting Started (Simplified Summary)

**🔹 What is Gemini CLI?**

Gemini CLI is Google’s AI assistant that runs directly in your terminal.
It can understand your commands, interact with files, write code, run tools, and even connect to MCP servers and APIs all from the command line.


**🔹 Setup Options**
 
*Local Installation 
Make sure Node.js v20+ is installed and then Install Gemini CLI globally with this command: 👇*

`npm install -g @google/gemini-cli`

**Verify installation:**

`gemini -v`

**Launch:**

`gemini`

**🔹 First-Time Setup**

When you first run it:

Choose a theme.

Select an authentication method:

Google Login → free tier (60 requests/min, 1000/day)

API Key / Vertex AI → for higher limits
 
**🔹 Inside the Gemini CLI**

The status bar shows:

Current folder

Model (e.g., gemini-2.5-pro)

Context size left

Type /help to see all available commands (e.g., /tools, /docs, /stats, /quit).

It’s not sandboxes, meaning it can interact with your local files when you allow it.


**🔹 Basic Commands**

| Command  | Purpose                                      |
| -------- | -------------------------------------------- |
| `/help`  | Show all commands                            |
| `/tools` | List built-in tools                          |
| `/docs`  | Open documentation                           |
| `/stats` | Show session stats                           |
| `/quit`  | Exit Gemini CLI                              |
| `!`      | Switch to shell mode (run terminal commands) |

**🔹 Best Practice: Start from a Project Folder**

Launch Gemini CLI inside the folder where you want to work.
Example:

`/Users/E:/gemini-cli-projects/cli-series`


**🔹 Example Task: Build a Flask App**

**Prompt Gemini:**

**I would like to create a Python Flask Application that shows me a list of live scores of cricket matches. There is a RSS Feed for this that is available over here:**
  https://static.cricinfo.com/rss/livescores.xml. **Let's use that.**