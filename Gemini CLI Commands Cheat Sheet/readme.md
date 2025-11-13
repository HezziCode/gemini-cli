# Gemini CLI Commands Cheat Sheet

| **Command** | **Sub-Commands/Options** | **Explanation** |
|-------------|---------------------------|--------------------------|
| `about` | None | Displays the current version information of Gemini CLI. |
| `auth` | None | Allows changing the authentication method for accessing Gemini models (e.g., API keys or OAuth). |
| `bug` | None | Opens a form or link to submit a bug report for Gemini CLI issues. |
| `chat` | `save <tag>`, `resume <tag>`, `list`, `delete <tag>` (inferred for removing saved chats) | Manages conversation history: save tags the current chat, resume loads a saved one, list shows all saved tags, delete removes a tagged chat. |
| `clear` | None | Clears the screen and resets the current conversation history in the CLI session. |
| `compress` | None | Summarizes and replaces the current context to reduce token usage and manage conversation length. |
| `copy` | None | Copies the last AI response or generated code snippet to the system clipboard. |
| `docs` | None | Opens the full Gemini CLI documentation in the default web browser. |
| `directory` | `add <path>`, `show`, `remove <path>` | Manages workspace directories: add includes a new directory, show lists current ones, remove excludes one. |
| `editor` | None | Sets or changes the preferred external text editor for editing prompts or code (e.g., vim, nano). |
| `extensions` | None (lists active ones) | Manages Gemini CLI extensions, including installing, updating, or removing them; use /extensions for list. |
| `help` | None | Provides help and usage information for Gemini CLI commands and features. |
| `ide` | `install`, `enable` | Manages integration with IDEs like VS Code: install sets up, enable activates the integration. |
| `init` | None | Analyzes the current project and generates a customized GEMINI.md file for AI-assisted development. |
| `mcp` | None (lists servers) | Manages Model Context Protocol (MCP) servers: lists configured ones and their tools. |
| `memory` | `show`, `refresh`, `read <key>`, `write <key> <value>`, `clear` | Interacts with memory: show displays combined context, refresh reloads GEMINI.md files, read retrieves saved data, write stores info, clear removes it. |
| `model` | None | Opens a dialog to select or configure the AI model (e.g., Gemini 1.5 Pro, Flash). |
| `privacy` | None | Displays the privacy notice regarding data handling and telemetry in Gemini CLI. |
| `quit` | None | Exits the Gemini CLI session gracefully. |
| `stats` | `[model]`, `[tools]` | Checks session statistics: model shows token usage per model, tools shows tool call counts. |
| `theme` | None | Changes the color theme or display style of the CLI interface. |
| `tools` | `[desc]` | Lists available Gemini CLI tools: desc adds detailed descriptions. |
| `settings` | None | Views and edits Gemini CLI settings via a friendly editor for settings.json. |
| `vim` | None | Toggles vim mode on/off for keyboard navigation and editing in the CLI. |
| `setup-github` | None | Sets up GitHub Actions integration for Gemini CLI in repositories. |
| `terminal-setup` | None | Configures terminal keybindings for multiline input in IDEs like VS Code, Cursor, or Windsurf. |
| `restore` | None | Lists or restores a project state checkpoint (may include sub-options for specific restores). |

#

- **Updates**: This list is combined from the official cheatsheet, blog series, and user-provided input. If there are changes in the latest version (e.g., post v0.8.1), check `/help` or docs for confirmation.


#

# It's end now. Hope you learned something. Goodbye, and have a nice day 🌼