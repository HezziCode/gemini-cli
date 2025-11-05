# 🚀 Gemini CLI Tutorial Series — Part 11: Gemini CLI Extensions

### 🔹 1. What Are Gemini CLI Extensions?

#### Extensions are like plugins that expand what Gemini CLI can do.
#### They let you add your own tools, commands, or automations — just like how VS Code extensions add features to the editor.

#### 👉 Think of them as “mini-apps” that Gemini CLI can load and talk to.

**Examples:**
 
- A /jira command to create tickets.
 
- A /translate command for docs.

- A /deploy command to trigger CI/CD.

 
### 🔹 2. Why Extensions Matter

#### Without extensions, Gemini CLI only has its built-in tools. With them, you can:

- Add domain-specific logic (DevOps, docs, AI tools, etc.)

- Integrate APIs (e.g., GitHub, Slack, Firebase)
 
- Make your CLI modular and scalable

#### 💡 You’re basically giving Gemini new “skills.”

**🧩 Extension**

An extension can include everything — MCP server, commands, API logic, etc.
It’s like a mini-app inside Gemini that adds new powers.

You can have `/translate`, `/github`, `/weather` — all inside one extension.

🧠 So think:
Extension = container for all logic, tools, and servers.


**⚙️ MCP Server**

“MCP = connect 3rd-party apps” 

An MCP server is like the engine inside or outside the extension.

It can connect Gemini to external services like `GitHub`, `Firebase`, or `Notion`.

For example: GitHub MCP lets Gemini push code, create PRs, or read repos directly.

#### 🧩 Key difference:

MCP server = does the heavy work (like calling APIs).

Extension = tells Gemini when and how to use that server.

👉 You can use MCP inside an extension OR run it separately — but using it inside extensions keeps everything organized and reusable.

**💬 Custom Commands**
 
“Commands = project-specific short actions” — spot on 👏

Commands are shortcuts for actions or prompts.
For example, `/prompt` or `/setup` or `/deploy`.

They don’t always need a full extension or MCP just small logic that runs quickly.

#### 🪄 Think:
Custom command = quick helper
Extension = full plugin
MCP server = powerful backend brain

**🧠 Quick Summary**

| Concept        | Role                                     | Example                  |
| -------------- | ---------------------------------------- | ------------------------ |
| **Extension**  | Full plugin (can include MCP + commands) | `/translate`, `/weather` |
| **MCP Server** | Connects Gemini to real apps/APIs        | GitHub MCP, Firebase MCP |
| **Command**    | Small local shortcut                     | `/prompt`, `/setup`      |



### 🔹 3. Folder Structure
 
#### By default, Gemini looks for extensions inside:

```
~/.gemini/extensions/
```

#### Each extension lives in its own folder:

```
.gemini/
 └── extensions/
      └── my-extension/
           ├── gemini-extension.json  
           ├── package.json
           ├── tsconfig.json
           ├── src/
           │   └── server.ts
           └── commands/
               └── example.toml

```

#### You can also include:

#### package.json (if using Node.js)

#### Extra config files or assets

### 🔹 4. Creating Your First Extension

**🧩 Step 1: Make Folder**

```
mkdir -p ~/.gemini/extensions/hello-world
cd ~/.gemini/extensions/hello-world
```

**🧩 Step 2: Add gemini-extension.json**

#### Create a file named `gemini-extension.json`:

```
{
  "name": "my-extension",
  "version": "1.0.0",
  "description": "A custom Gemini CLI extension built with TypeScript and MCP.",
  "entry": "dist/server.js",
  "language": "nodejs",
  "extension": {
    "type": "mcp",
    "supports": ["generate", "edit", "restore"]
  },
  "commands": {
    "path": "./commands"
  }
}
```

**🧩 Step 3: Add server.ts**

#### Create a new file `server.ts`:

```
import { MCPServer } from "@modelcontextprotocol/sdk";

const server = new MCPServer({
  name: "my-extension",
  version: "1.0.0"
});

server.tool("hello", async (input) => {
  const name = input?.text || "developer";
  return { text: `👋 Hello, ${name}! This is your custom Gemini CLI extension.` };
});

server.start();
```
 
### 🔹 5. Test It Out
#### Restart Gemini CLI and type:

```
/hello-world Huzaifa
```

**✅ Output:**

```
👋 Hello, Huzaifa! This is your custom Gemini CLI extension.
```

### 🔹 6. Publishing or Sharing
 
#### You can share your extension by:
 
1. Zipping the folder

2. Or pushing it to GitHub

#### Then others can install it by:
```
gemini extension install <repo-url>
```

