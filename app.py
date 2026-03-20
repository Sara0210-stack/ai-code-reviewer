import streamlit as st
import requests
import ast

st.set_page_config(page_title="AI Code Reviewer", layout='centered')

st.header("🤖 AI Code Reviewer (AST + LLM)")

code = st.text_area("Enter your Python code here:")

if st.button("Review Code"):

    if not code.strip():
        st.warning("Please enter some code to review.")

    else:
        st.subheader("Your Code")
        st.code(code, language='python')

        # ---------------------------
        # Syntax Check
        # ---------------------------
        st.subheader("🔍 Syntax Check")

        try:
            ast.parse(code)
            error_message = "No syntax errors."
            st.success("✅ No syntax errors found.")
        except SyntaxError as e:
            error_message = str(e)
            st.error(f"❌ Syntax Error: {e}")

        # ---------------------------
        # AI Review
        # ---------------------------
        st.subheader("🤖 AI Review")

        prompt = f"""
You are a Python code reviewer.

Fix the Python code below.

Code:
{code}

Detected Syntax Error:
{error_message}

Explain clearly:
1. What is wrong
2. How to fix it
3. Provide corrected code

Keep answer short and concise.
"""

        with st.spinner("Reviewing code..."):

            try:
                response = requests.post(
                    "http://127.0.0.1:1234/v1/chat/completions",
                    json={
                        "model": "phi-3.1-mini-4k-instruct",
                        "messages": [
                            {"role": "user", "content": prompt}
                        ]
                    }
                )

                result = response.json()
                output = result['choices'][0]['message']['content']

                # Clean weird responses
                if "I do not" in output or "I cannot" in output:
                    output = "⚠️ Model response unclear. Please try simpler input."

                st.subheader("📖 Explanation")
                st.write(output)

            except Exception as e:
                st.error(f"⚠️ Error connecting to model: {e}")