## 🛠️ Gemini CLI Tutorial Series — Part 4: Built-in Tools

**⚙️ What Are Built-in Tools?**

- Tools enable Gemini CLI to interact with your local system, access the internet, and perform tasks beyond text generation.

- Examples of tasks:

    - Read/write local files

    - Examine folder contents

    - Fetch data from URLs or Google Search

    - Convert text to Markdown, summarize, extract info from images

Note: Built-in tools ≠ MCP Tools (external servers). MCP tools come later in the series.

**🔑 Key Points About Built-in Tools**

1. Safety first: Gemini asks for approval before running tools affecting files or network. 

    --approval-mode: manual or auto-approve

2. Multi-modal support: Works with text, images, and other file types.

**📝 Example Usage**

1. List all available tools

`/tools`

2. Read folder contents

`Are there any files in the folder?`

3. Google Search & Save

`Search for latest finance news in India and save to finance-news-today.txt`

**We use this prompt in this project you can use this prompt too**

Tools used: `GoogleSearch` + `WriteFile`

4. Fetch & Summarize Web Content

`Fetch Google Cloud Release Notes RSS feed and summarize updates from Sep 9, 2025`

5. Process Images / Multi-modal

`Extract Invoice Number, Date, Sender, Due Date, Due Amount from inv1.png, inv2.png…`
 
- Gemini reads image files and creates a structured table.

**🌟 Why It’s Powerful**
 
1- Automates repetitive tasks (file management, data extraction, web info gathering)

2- Works with local files, web, and multi-format data

3- Ensures control and approval for sensitive operations