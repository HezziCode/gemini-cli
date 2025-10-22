## 🪄 Gemini CLI Tutorial Series — Part 2: Command-Line Options

**🔄 Keep Gemini CLI Updated**

**Gemini CLI evolves quickly. Upgrade anytime with:**

`npm upgrade -g @google/gemini-cli`

**Check version:**

`gemini -v`

**⚙️ Common CLI Options**

| Option                   | Purpose                                                       |
| ------------------------ | ------------------------------------------------------------- |
| `-h` / `--help`          | List all available commands and options                       |
| `-v` / `--version`       | Show Gemini CLI version                                       |
| `-y` / `--yolo`          | YOLO mode: auto-accept all actions (use carefully!)           |
| `-m` / `--model`         | Choose model (`gemini-2.5-pro` or `gemini-flash-2.5`)         |
| `-p` / `--prompt`        | Non-interactive mode: run a single prompt and get the result  |
| Positional prompt        | Simply type: `gemini "Your prompt here"`                      |
| `-d` / `--debug`         | Debug mode: shows context loading, memory, and CLI internals  |
| `-c` / `--checkpointing` | Enable checkpointing: saves project state before file changes |

**🧠 GEMINI.md (Context / Memory)**

*Provides project-specific instructions (coding style, rules, dependencies)*

*CLI searches hierarchy:*

*Global: ~/.gemini/GEMINI.md*
 
*Project root*
 
*Local subfolders*

*CLI concatenates multiple files for “memory”*
 
*Use /memory refresh to reload updates*

*You can use Gemini CLI without GEMINI.md, but context files improve AI accuracy and consistency.*

**⚡ Quick Tips**
 
- Start Gemini CLI from the folder where you want your project

- Debug mode helps understand context, memory, and tool execution

- Use positional prompts or -p for automation pipelines