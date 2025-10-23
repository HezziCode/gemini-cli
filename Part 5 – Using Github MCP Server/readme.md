## Model Context Protocol (MCP)

**🔹 What You’ll Learn**

Gemini CLI already has built-in tools, but MCP Servers let it connect to external systems (like GitHub, Firebase, or Google AI APIs).

This allows Gemini CLI to read, write, and act on data beyond your computer while still being controlled from the terminal.

**⚙️ 1. Configuring MCP Servers**

All configuration lives in the .gemini/settings.json file.

**Example base structure:**

```
{
  "selectedAuthType": "vertex-ai",
  "theme": "Default",
  "mcpServers": {
    "github": {
      "httpUrl": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "<YOUR_GITHUB_PAT>"
      },
      "timeout": 5000
    }
  }
}
```

**🧩 Key fields:**

`command`, `url`, or `httpUrl` how Gemini CLI connects

`args`, `headers`, `env`, `cwd` connection details

`trust` allow actions without confirmation (⚠️ use carefully)

`includeTools` / `excludeTools` choose which tools from the server are available

**Check your MCP setup anytime:**

```
/mcp
```

**🧠 2. Example: GitHub MCP Server**

- Requires a GitHub Personal Access Token (PAT)

- Lets Gemini CLI do things like:

    - Read and edit files in your repo

    - Commit and push changes
 
    - Fix issues automatically

**Demo flow:**

1. Gemini detects an error in a README file

2. Fixes it locally

3. Commits and pushes via GitHub MCP Server
 
*If Gemini CLI finds Git locally, it’ll use that unless you explicitly make it use the MCP Server.*

**💡 3. What You Can Do**

*With MCP Servers configured, Gemini CLI can:*
 
- Auto-fix repo issues

- Generate or update docs
 
- Implement and push new features

- Interact with GitHub Issues or PRs

- Later: connect to Firebase, Google Workspace, or Generative AI services

**🧾 4. Summary**

**Gemini CLI** + **MCP Servers** = Local AI + Remote Power
You teach Gemini how to talk to outside tools safely.
In this part, we focused on **GitHub MCP Server** configuring it, authenticating, and using it to detect and fix code issues automatically.


### Next up: Part 6 More MCP Servers (Firebase, Google Workspace, and Gen AI)