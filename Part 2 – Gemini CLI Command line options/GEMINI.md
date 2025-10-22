## This is the file where we give context to gemini cli
 
 While not strictly configuration for the CLI's behavior, context files (defaulting to GEMINI.md but configurable via the contextFileName setting) are crucial for configuring the instructional context (also referred to as "memory") provided to the Gemini model. This powerful feature allows you to give project-specific instructions, coding style guides, or any relevant background information to the AI, making its responses more tailored and accurate to your needs. The CLI includes UI elements, such as an indicator in the footer showing the number of loaded context files, to keep you informed about the active context.

Purpose: These Markdown files contain instructions, guidelines, or context that you want the Gemini model to be aware of during your interactions. The system is designed to manage this instructional context hierarchically.


## Example Context File Content (e.g., GEMINI.md)

Here's a conceptual example of what a context file at the root of a TypeScript project might contain:

```
Project: My Awesome TypeScript Library

General Instructions:
When generating new TypeScript code, please follow the existing coding style.
Ensure all new functions and classes have JSDoc comments.
Prefer functional programming paradigms where appropriate.
All code should be compatible with TypeScript 5.0 and Node.js 18+.

Coding Style:
Use 2 spaces for indentation.
Interface names should be prefixed with I (e.g., IUserService).
Private class members should be prefixed with an underscore (_).
Always use strict equality (=== and !==).

Specific Component: src/api/client.ts
This file handles all outbound API requests.
When adding new API call functions, ensure they include robust error handling and logging.
Use the existing fetchWithRetry utility for all GET requests.

Regarding Dependencies:
Avoid introducing new external dependencies unless absolutely necessary.
If a new dependency is required, please state the reason.

```


**If you have been working with LLMs for a while, you will know by now that these instructions are provided in good faith to the model and the exact results might not be what you want. It may require significant tuning of GEMINI.md, some additional parameters and more. Hence we should ideally be looking out for articles where Gemini CLI users will share what’s worked best for them and learn together.**
```
```

**Having said that, you can use Gemini CLI without a GEMINI.md file too. But you will quickly notice that eventually it would be good to have these files, which may provide overall global instructions for anything you do with Gemini CLI and then have project or task specific GEMINI.md files too. That’s just a pattern that I believe will emerge. But don’t fret too much on that at the moment. I just mentioned multiple GEMINI.mdfiles and that brings us to the next question.**