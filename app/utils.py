from textwrap import dedent




def build_review_prompt(code: str) -> str:
    from .prompts import REVIEW_PROMPT_TEMPLATE


    code = dedent(code)
    return REVIEW_PROMPT_TEMPLATE.format(code=code)