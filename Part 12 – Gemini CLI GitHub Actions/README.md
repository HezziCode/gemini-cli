# 🚀 Gemini CLI Tutorial Series — Part 12: GitHub Actions Integration

### 🔹 1. What’s Happening Here?

Until now, Gemini CLI worked locally — in your terminal like your personal assistant.
Now, in this part, we take Gemini CLI to the cloud and make it a part of your GitHub workflow.


**Think of it like this:**
 
#### “Gemini CLI stops being just a tool you use — it becomes a teammate that works with your repository.”

**So instead of typing commands locally, Gemini CLI can:**

- Review pull requests automatically 🧠
- Add labels to GitHub issues 🏷️
- Reply when you mention it in comments 💬
 
#### This is powered by GitHub Actions — GitHub’s built-in automation feature.

### 🔹 2. Before You Start
**Make sure your Gemini CLI is up to date.**
```
npm install -g @google/gemini-cli@latest
gemini -v
```

Version must be at least `0.4.0+`.

### 🔹 3. What You’ll Build
 
#### We’ll create a small demo project and teach Gemini CLI to manage it automatically.

**Project: ASCII Art Generator 🎨**
 
#### A simple Flask web app that converts text into ASCII art.
 
*Here’s our plan:*

1. Make the project locally.

2. Push it to GitHub.

3. Connect Gemini CLI GitHub Actions.

4. Test automation (issues, PR reviews, comments).

### 🔹 4. Coding the Project (Locally)

**Create a folder and open Gemini CLI.**

```
mkdir ascii-art-generator && cd ascii-art-generator
gemini
```

**Now use Gemini prompts step by step:**

***Prompt 1:***
```
Create a simple Python Flask web app named app.py with one route / that uses a template index.html.
```

***Prompt 2:***

```
Create templates/index.html with a text input, font dropdown, and submit button.
```

***Prompt 3:***
```
Update app.py to handle form submission and generate ASCII art using pyfiglet.
```

***Prompt 4:***

```
Create requirements.txt with Flask and pyfiglet.
```

**✅ Folder structure after setup:**

```
ascii-art-generator/
├── app.py
├── requirements.txt
└── templates/
    └── index.html
```

### 🔹 5. Pushing to GitHub

#### Use Gemini CLI’s GitHub MCP integration or normal Git commands.
 
**Using Gemini CLI:**

**Ask:**

#### “Create a .gitignore file for this project.”

#### “Push this project to a new GitHub repo named my-ascii-art-generator.”

**Gemini will:**

- Create `.gitignore`
 
- Initialize git

- Create repo on GitHub

- Push files

**Manual Commands (if needed):**

```
git init
git add .
git commit -m "Initial commit: Create Flask ASCII art generator"
git branch -M main
git remote add origin <YOUR_REPO_URL>
git push -u origin main
```

### 🔹 6. Automate Tasks with Gemini CLI


**🤖 Pull Request Reviews**

- **Create a new branch:**

```
git checkout -b add-new-font
```
 
- **Add a new font in `index.html`**

- **Push and create a PR.**

## “Now Gemini CLI isn’t just your coding buddy it’s your full-time GitHub assistant.”!