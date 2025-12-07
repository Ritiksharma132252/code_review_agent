from flask import Blueprint, render_template, request, current_app, flash
from .openai_client import OpenAIClient
from .utils import build_review_prompt


bp = Blueprint("main", __name__)




@bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")




@bp.route("/review", methods=["POST"])
def review():
    code = request.form.get("code")
    language = request.form.get("language", "python")
    if not code:
        flash("Please paste your code snippet.")
        return render_template("index.html")


    # build prompt and call OpenAI
    prompt = build_review_prompt(code)


    try:
        client = OpenAIClient()
        resp = client.review_code(prompt)


        # Extract text from response depending on the client
        # This block may need small adjustments based on openai package version
        text = ""
        if hasattr(resp, "output"):
        # for older/some SDKs
            text = resp.output[0].content[0].text
        else:
            text = getattr(resp, "text", None) or str(resp)


    except Exception as e:
        text = f"Error contacting OpenAI API: {e}"


    return render_template("result.html", result=text, original_code=code)