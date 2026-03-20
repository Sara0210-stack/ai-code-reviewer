# 🤖 AI Code Reviewer

An intelligent AI-powered code review application built using Python, Streamlit, and LLMs. This tool analyzes Python code, detects syntax errors, explains issues, and suggests improvements with corrected code.

---

## 🚀 Features

* 🔍 Syntax error detection using Python `ast`
* 🤖 AI-powered code review using LLM (via API / local model)
* 🧠 Explanation of issues in simple language
* 🛠️ Suggested fixes and improvements
* 💻 Clean and interactive UI using Streamlit

---

## 🧰 Tech Stack

* Python
* Streamlit
* AST (Abstract Syntax Tree)
* LLM API (Groq / Local Model via LM Studio)
* Requests library

---

## 📌 How It Works

1. User inputs Python code in the UI
2. Code is checked for syntax errors using `ast`
3. The code is sent to an AI model
4. AI analyzes the code and returns:

   * Issues
   * Fixes
   * Explanation
5. Output is displayed in a clean format

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-code-reviewer.git
cd ai-code-reviewer
```

---

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the app

```bash
streamlit run app.py
```

---

## 🔐 API Setup

If using API:

* Add your API key in the code OR use `.env` file

Example:

```env
API_KEY=your_api_key_here
```

---

## 📷 Output Example

The app detects syntax errors and provides:

* Explanation of error
* Suggested fix
* Corrected code

---

## 🎯 Use Cases

* Beginners learning Python
* Debugging code quickly
* Understanding errors clearly
* Improving coding skills

---

## 🚀 Future Improvements

* Support for multiple programming languages
* Better UI enhancements
* Integration with VS Code
* Code quality scoring

---

## 👩‍💻 Author

Sara Shaikh

---

## ⭐ Acknowledgment

Built as part of AI/ML learning and project portfolio development.
