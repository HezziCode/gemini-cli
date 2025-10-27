# 🚀 Gemini CLI Tutorial Series — Part 8: Building Your Own MCP Server

**🔹 What You’re Learning**
 
#### In this part, you’ll stop being just a user of Gemini CLI and start being a creator.
#### You’ll build your own MCP (Model Context Protocol) server — which is basically a small web service that gives Gemini CLI new powers or connects it to your private data.


### 🧩 What Is a Custom MCP Server?

##### A custom MCP (Model Context Protocol) server is your own mini-backend that Gemini can talk to. 
##### Think of it like this:

##### Gemini = your smart assistant
##### MCP Server = your custom toolbox

##### By creating your own MCP server, you can teach Gemini new skills — like greeting users, checking grammar, summarizing code, or connecting to a private API.

### ⚙️ What Our “Greet” MCP Does

##### In our example, we built a tiny MCP called “MyFirstMCPServer.”
##### It has one tool called greet, which takes a name and returns a friendly message.

#### Example:

```
greet Huzaifa
```
#### Gemini calls your MCP → the MCP runs your tool → returns:

```
Hello Huzaifa! It's a pleasure to connect from your first MCP Server.
```
 
#### So instead of Gemini just generating text, it’s now calling real functions you wrote.

### 🔮 What’s Next?

#### Now that your greet MCP works, you can:
 
#### Add more tools inside the same server (e.g., reverse_text, get_time, etc.)
 
#### Create new MCP servers for different tasks (like “Technical Editor” or “Code Reviewer”)

#### Expose these servers to Gemini through your settings.json — and run them just like built-in commands.

## Our first custom MCP server 👇

**🔹 Step 1: Setup Project Folder**
###### Create and enter a directory for your project:

```
mkdir my-mcp-server
cd my-mcp-server
```

**2. Create project & venv**
```
uv venv 
# activate venv:
# windows: .venv\Scripts\activate
uv add fastmcp
```

**4. Hello MCP — server.py (minimal)**
###### Create server.py with exactly this code:

```
from fastmcp import FastMCP

mcp = FastMCP(name="MyFirstMCPServer")

@mcp.tool
def greet(name: str) -> str:
    """Returns a friendly greeting"""
    return f"Hello {name}! It's a pleasure to connect from your first MCP Server."

if __name__ == "__main__":
    # transport "http" exposes /mcp/ endpoint
    mcp.run(transport="http", port=8080)
```

**5. Run the server (dev)**
###### use fastmcp runner (recommended for dev + inspector):

```
fastmcp run server.py --transport="http" --port=8080
```

###### You should see a line like:

```
MCP Server listening at http://127.0.0.1:8080/mcp/
```

**6. Inspect (optional but recommended)**
###### Start the MCP Inspector UI to explore tools:

```
fastmcp dev server.py --ui-port=9080 --server-port=5080
# open http://127.0.0.1:9080 in your browser
# choose Streamable HTTP, URL http://127.0.0.1:8080/mcp/ and Connect
```

#### Click Tools → List Tools to see greet.

**7. Tell Gemini about your MCP server**
#### 📂 Where the .gemini Folder Must Be

##### Gemini CLI automatically looks for its configuration (including settings.json) inside your user’s home directory, not your project folder.

###### That means:

##### On Windows, this path usually is:

```
C:\Users\<your-username>\.gemini\
```

##### Inside it, you should have:

```
settings.json
```
**⚠️ Why It Matters**

#### If you place .gemini inside another folder (for example, inside your project folder or desktop),
#### Gemini won’t find it, and your custom commands or MCP servers won’t load.

#### So even if your MCP server is running perfectly (e.g., http://127.0.0.1:8080/mcp/), Gemini will show errors like:


```
Error: Unknown command /mcp
or
Cannot connect to MCP server
```

##### because it never read the correct settings.json.

**✅ Fix / Correct Setup**

1. Go to your home folder:
`C:\Users\<YourName>\`

2. Create a `.gemini` folder (if not already there).

2. Inside it, make sure you have:

```
settings.json
```

#### Add your MCP server config in that settings.json:

```
{
  "mcpServers": {
    "my-mcp-server": {
      "httpUrl": "http://127.0.0.1:8080/mcp/"
    }
  }
}
```
 
#### Restart Gemini CLI — now it will detect your server successfully 🎯