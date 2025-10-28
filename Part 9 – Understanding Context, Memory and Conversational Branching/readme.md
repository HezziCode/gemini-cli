# 🚀 Gemini CLI Tutorial Series — Part 9: Understanding Context, Memory, and Conversational Branching

### 🔹 1. Why This Part Matters
 
#### So far, we’ve built tools and commands for Gemini CLI.Now we’ll learn how Gemini “remembers” — both short-term (context) and long-term (memory). Understanding this helps you control how Gemini behaves, avoids confusion, and lets you resume old chats easily. 

### 🔹 2. Context — Gemini’s Short-Term Memory

Think of context as what Gemini currently “sees” — like RAM in a computer.
It’s temporary. If you restart Gemini or use `/clear`, it’s gone.

#### What’s inside the context:

1. System Instruction — base rules Gemini follows.

2. GEMINI.md files — instruction files loaded from your project and global folder.

3. Current Directory Awareness — Gemini reads your folder to adapt (e.g., if it sees package.json, it knows it’s a Node.js project).

4. Conversation History — all messages you and Gemini exchange in that session.

5. Extra Data You Load
    - `@file.txt` → loads that file into memory.

    - `!ls` → runs shell commands, and output gets added to context too.

#### Context Limit:

##### Gemini 2.5 Pro has a 1 million token window — enough to fit an entire codebase or document.
##### But more context ≠ always better. Too much noise causes context bloat → Gemini gets confused.

🔹 3. Controlling Context
 
###### Gemini gives two powerful commands:

| Command     | What It Does                          | When to Use                                       |
| ----------- | ------------------------------------- | ------------------------------------------------- |
| `/clear`    | Wipes everything — start fresh        | When switching to a new task                      |
| `/compress` | Summarizes current chat to save space | For long sessions, keeps essence but frees tokens |


#### Example:

```
/clear
/compress
```
 
### 🔹 4. Conversational Branching — Switching Between Topics
 
###### Developers multitask — you might be planning a feature, debugging code, and learning something all at once.
 
###### Instead of losing your place, Gemini lets you save and resume conversations with `/chat.`

#### 💬 Core Commands

| Command              | Description                  | Example                      |
| -------------------- | ---------------------------- | ---------------------------- |
| `/chat save <tag>`   | Save current conversation    | `/chat save frontend-plan`   |
| `/chat list`         | List all saved chats         | `/chat list`                 |
| `/chat resume <tag>` | Restore a saved conversation | `/chat resume frontend-plan` |
| `/chat delete <tag>` | Delete a saved one           | `/chat delete frontend-plan` |
| `/clear`             | Reset before switching       | `/clear`                     |


### 🔹 5. Memory — Gemini’s Long-Term Brain

##### Now, memory is different — it’s persistent.
##### Even if you close Gemini, these settings and facts stay.

**There are two types:**

#### 1️⃣ Instructional Memory → GEMINI.md files

###### Used to define rules or persona Gemini should follow every time.

#### File hierarchy (important):

| Level         | Location              | Use                                   |
| ------------- | --------------------- | ------------------------------------- |
| Global        | `~/.gemini/GEMINI.md` | Always loaded (your default behavior) |
| Project       | `<project>/GEMINI.md` | Overrides global for that project     |
| Sub-directory | `src/docs/GEMINI.md`  | Local tweaks for specific folders     |


#### Gemini merges all these automatically.

#### You can check and reload them with:

```
/memory show      # view combined instructions
/memory refresh   # reload GEMINI.md after editing
```

#### ✅ You can also modularize:

```
@/path/to/other.md
```
**This imports another markdown file — great for large setups.**

#### 2️⃣ Factual Memory → Remembering Facts

##### Gemini can remember specific details you tell it to save.

#### Two ways:

| Method                    | Description                                   | Example                                                |
| ------------------------- | --------------------------------------------- | ------------------------------------------------------ |
| **SaveMemory Tool**       | Gemini auto-remembers facts (e.g., your name) | “Remember that my name is Huzaifa.”                    |
| **`/memory add` command** | Manual addition to memory                     | `/memory add "My favorite CSS framework is Tailwind."` |

**Stored in:**

`~/.gemini/GEMINI.md`
 
#### Then you can test it by prompting:

**“Create a webpage using my preferred CSS framework.”**
 
##### If you added Tailwind earlier, Gemini should pick it up automatically.


 
## Congrats — you’ve now mastered context, memory, and conversational branching 🚀
