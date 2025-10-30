# 🚀 Gemini CLI Tutorial Series — Part 10: Gemini CLI and VS Code Integration

### 🔹 1. Why This Part Matters

#### Normally, Gemini CLI runs in a terminal. But reviewing code differences or working with large projects is easier in VS Code.
So, this integration lets Gemini CLI:

- Understand your active file and selected code.

- Show diffs (code changes) directly inside VS Code’s editor.

- Let you accept or reject Gemini’s suggested code from within VS Code.

#### It makes Gemini feel like a native coding assistant inside your IDE rather than just a terminal bot.

### 🔹 2. Update Gemini CLI First

#### Before doing anything, make sure you’re on v0.4.0 or later:

```
npm install -g @google/gemini-cli@latest
gemini -v
```

### 🔹 3. Install the Gemini CLI VS Code Extension

#### 1 Open VS Code.

#### 2 Open its Integrated Terminal (Ctrl + ~ or Cmd + ~).

#### 3 Inside that terminal, start Gemini:

```
gemini
```

#### 4 Gemini may ask:
 
**“Do you want to connect VS Code Editor for Gemini CLI?”**
 
- ✅ Type yes.

- It installs the extension automatically from the VS Code Marketplace.

#### If you don’t get the popup, run manually:

```
/ide install
```

**🧠 Important:**

#### Run this inside the Integrated Terminal in VS Code not in an external one — or you’ll see a connection error.

### 🔹 4. Verify Installation

**After installation:**

#### 1. Go to Extensions Tab in VS Code.

#### 2. Search for “Gemini CLI” — it should appear as installed.

#### 3. Restart VS Code and open a project folder.

**Now you can launch Gemini via:**

#### Integrated Terminal, or

#### Command Palette → type “Gemini CLI”.

#### To confirm connection:

```
/ide status
```

**✅ Output should show “Connected to VS Code IDE”.**

### 🔹 5. Try Out the Integration
 
**Example 1 — Code Selection**

#### 1. Open a file (e.g. server.py)
and paste this sample code inside:
```
import time

def process_data(data):
    total = 0
    for value in data:
        total += value
    return total

def main():
    data = [1, 2, 3, 4, 5]
    result = process_data(data)
    print("Result:", result)

if __name__ == "__main__":
    main()
```
#### 2. Highlight a code snippet

#### 3. In Gemini Terminal:

**✅ Gemini understands your selection and explains it — no copy-paste needed.**

**Example 2 — Code Diff**

**Ask Gemini:**

```
optimize this code for readability
```

#### 2. Gemini applies the change.

#### 3. VS Code opens a Diff View — see differences, with buttons:

- ✅ Accept Diff

- ❌ Close Diff
 
#### You can approve/reject changes directly from there.

### 🔹 8. Why This Matters

#### This integration gives:

#### Context-aware prompts (Gemini knows what file/code you selected)

#### Native diff viewer (view/edit inside VS Code)

#### Smoother workflow for devs who live in VS Code

**🔧 Quick Commands**

```
/ide install      # Install extension
/ide status       # Check connection
gemini            # Launch Gemini CLI inside VS Code
```