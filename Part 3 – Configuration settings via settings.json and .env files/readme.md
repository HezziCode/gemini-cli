## 🪄 Gemini CLI Tutorial Series — Part 3: Configuration Settings

**⚙️ Settings Overview**

**Gemini CLI can be configured via:**

1. Command-line arguments (gemini --checkpointing) – highest priority, session-specific

2. Environment variables (GEMINI_API_KEY, GOOGLE_CLOUD_PROJECT)

3. Settings files (settings.json) – global or project-specific

4. Defaults – built-in hardcoded values

**🏠 User (Global) Settings**

Location: ~/.gemini/settings.json

Applies to all projects

Examples:

```
{
  "selectedAuthType": "oauth-personal",
  "theme": "Default",
  "checkpointing": {"enabled": true}
}
```
Can be updated from CLI using /theme or /auth

**⚡ Configuration Precedence (Highest → Lowest)**

1) **Command-line arguments – temporary, session-specific**
  
2) **Environment variables – e.g., GEMINI_API_KEY, GOOGLE_CLOUD_PROJECT**

3) **System settings file – enforced by admins**

4) **Project settings.json – project-specific**

5) **User settings.json – personal defaults**
 
6) **Gemini CLI defaults – hardcoded CLI values**
 
*Tip: Think of it like a stack – the topmost overrides the ones below.*

**🌱 Environment Variables (.env)**

Can store sensitive info or default configs

Search order:

1) .env in current working directory

2) Parent directories up to project root

3) ~/.env in home directory

Examples:
```
GEMINI_API_KEY=your_key_here
GOOGLE_CLOUD_PROJECT=my-project
GOOGLE_CLOUD_LOCATION=us-central1
GEMINI_MODEL=gemini-2.5-flash
```
 
**🔧 Recommended Usage**

- Sensitive info: .env file

- Project-specific defaults: Project settings.json

- Personal defaults: User settings.json

- Temporary changes or debugging: CLI flags like --checkpointing or --debug