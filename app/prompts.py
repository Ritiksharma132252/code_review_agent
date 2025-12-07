REVIEW_PROMPT_TEMPLATE = """
You are an expert senior software engineer and technical writer.


Task: Given a code snippet delimited by triple backticks, do the following:


1. Provide a concise **summary** of what the code does (2-4 sentences).
2. Provide a **code review** with categorized bullets: Bugs, Security, Performance, Style, Readability, and Testing.
- For each issue include: severity (Low/Medium/High), line numbers (if determinable), and suggested fixes.
3. Produce **documentation** suitable for the code: a module summary and docstrings for each function/class (use reST or Google style).
4. Provide an **improved version** of the code with the suggested fixes applied. Make sure improved code preserves original behavior unless explicitly recommending a change.
5. Provide a short **diff** summary (what changed) and a short **test list** the user should run to validate the changes.


Respond in Markdown with clearly separated sections labeled:
- Summary
- Code Review
- Documentation
- Improved Code
- Diff Summary
- Tests to Run


Here is the code:


```{code}```
"""