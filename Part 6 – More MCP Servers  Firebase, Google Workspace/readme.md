# 🚀 Gemini CLI Tutorial Series — Part 6: More MCP Servers

#### Firebase • Google Workspace • Gen AI Media Services • MCP Toolbox for Databases

**We implemented this Firebase MCP server in our project, and you can choose what you want to do** 
### 🔹 1. Firebase MCP Server

**🧠 Concept**

Bridges Gemini CLI with your Firebase projects.

Lets Gemini read, query, and modify Firestore data or configurations.

Requires Firebase CLI for authentication.

**⚙️ Setup Steps**
 
1 Login to Firebase

```
npx -y firebase-tools@latest login --reauth
```
→ Opens browser → authenticate your Google account.

2 Add MCP Server entry in `settings.json `

```
{
  "mcpServers": {
    "firebase-mcp": {
      "command": "npx",
      "args": ["@gannonh/firebase-mcp@latest"]
    }
  }
}
```

3 Launch Gemini CLI, then run:

```
/mcp
```

→ Lists all Firebase tools (project listing, Firestore access, etc.).

4 Try it

Ask: “List all Firebase projects.”

Ask: “Initialize Firebase in this directory.”

Ask: “Show sessions with duration > 45 min.”
 
###### 💡 Practical tip: Ensure the correct Firebase project is linked to your Google Cloud Project using firebase_update_environment.

### 🔹 2. Google Gen AI Media Services (MCP Servers)

**🧠 Concept**

##### Integrates Imagen, Veo, Chirp, Lyria, AV Tool — Google’s Generative AI media models — with Gemini CLI using Vertex AI Creative Studio MCP.

**⚙️ Setup Steps**

Clone repo:

**git clone** https://github.com/GoogleCloudPlatform/vertex-ai-creative-studio.git


#### Navigate to /experiments/mcp-genmedia and build all servers (mcp-veo-go, mcp-imagen-go, etc.).

**In settings.json, add:**
 
```
{
  "mcpServers": {
    "imagen": {
      "command": "mcp-imagen-go",
      "env": {
        "GENMEDIA_BUCKET": "YOUR_BUCKET",
        "PROJECT_ID": "YOUR_PROJECT_ID"
      }
    }
  }
}
```

##### (Repeat for Veo, Chirp, Lyria, AV Tool)

**Run Gemini CLI → /mcp → new creative tools appear.**

## 💡 Try it

**“Generate an image of Mumbai skyline during sunset.”
→ Uses mcp-imagen-go and stores output in your Google Cloud bucket**


### 🔹 3. MCP Toolbox for Databases
**🧠 Concept**

#### A single MCP Server that connects Gemini CLI to multiple databases (BigQuery, Postgres, MySQL, Snowflake, etc.).

**⚙️ Setup Steps**

##### Download binary:
 
**mkdir mcp-toolbox && cd mcp-toolbox
export VERSION=0.14.0** 

`curl -O https://storage.googleapis.com/genai-toolbox/v$VERSION/darwin/arm64/toolbox
chmod +x toolbox`


**Add entry to settings.json:**

```
"BigQueryServer": {
  "command": "/path/to/toolbox",
  "args": ["--prebuilt", "bigquery", "--stdio"],
  "env": {"BIGQUERY_PROJECT": "YOUR_PROJECT_ID"}
}
```

(Optional) Create a tools.yaml for custom SQL queries:

```
sources:
  my-bq-source:
    kind: bigquery
    project: YOUR_PROJECT_ID
tools:
  search_release_notes_bq:
    kind: bigquery-sql
    statement: |
      SELECT product_name, description
      FROM `bigquery-public-data.google_cloud_release_notes.release_notes`
      ORDER BY published_at DESC
```

**Restart Gemini CLI → /mcp → see database tools.**

💡 Try: “Show release notes for the past 7 days from BigQuery.”


| MCP Server           | Use Case                               | Requires                  | Example Prompt                        |
| -------------------- | -------------------------------------- | ------------------------- | ------------------------------------- |
| **Firebase**         | Manage Firestore, auth, env setup      | Firebase CLI              | “List all Firebase projects.”         |
|                           |
| **Gen AI Media**     | Imagen, Veo, Chirp, Lyria              | Vertex AI Creative Studio | “Generate an image.”                  |
| **Database Toolbox** | Query BigQuery/Postgres etc.           | Toolbox binary            | “Show latest BigQuery release notes.” |
