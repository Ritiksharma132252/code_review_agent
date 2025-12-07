import os
from typing import Dict, Any

try:
    
    from openai import OpenAI
except Exception:
    OpenAI = None


class OpenAIClient:
    def __init__(self, api_key: str = None):
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY environment variable must be set")

        if OpenAI is None:
               raise RuntimeError("openai library not found. Install it in requirements.txt")

        self.client = OpenAI(api_key=api_key)

    def review_code(self, prompt: str, max_tokens: int = 800) -> Dict[str, Any]:
        """Send prompt to OpenAI and return response object."""
        resp = self.client.responses.create(
            model="gpt-4o-mini", 
            input=prompt,
            #max_tokens=max_tokens,
            temperature=0.2
        )
        
        return resp