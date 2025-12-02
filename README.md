# 🤖 LangChain Research Assistant (Gemini Tool-Calling Agent)

This project implements a robust research assistant using LangChain's Tool Calling Agent, powered by the **Gemini 2.5 Flash** model. The agent is designed to use external tools for factual searches, synthesize the information, and output the final research in a clean, predictable structured format using Pydantic.

## ✨ Features

* **Tool-Calling Agent:** Built using `create_tool_calling_agent` for efficient and reliable function/tool dispatch.
* **Multi-Tool Integration:** Leverages **Wikipedia** and **DuckDuckGo Search** for comprehensive research capabilities.
* **Structured Output:** Enforces a clean JSON output schema using the `ResearchResponse` Pydantic model.
* **Custom Tool:** Includes a custom `save_text_to_file` tool to persist structured research data locally.

---

## 🛠️ Project Structure and Components

### `main.py`

This is the core script where the agent, LLM, prompt, and execution logic are defined.

* **LLM:** `ChatGoogleGenerativeAI(model="gemini-2.5-flash")`
* **Agent:** `create_tool_calling_agent`
* **Execution:** `AgentExecutor`
* **Pydantic Model:** `ResearchResponse` (topic, summary, Sources, tools_used)

### `tools.py` (Implied Structure)

The external and custom tools are defined here and imported into `main.py`.

| Tool Name | Class/Function | Purpose |
| :--- | :--- | :--- |
| `search` | `DuckDuckGoSearchRun` | General web searches for current or specific information. |
| `wikipedia` | `WikipediaQueryRun` | Facts, historical information, and general knowledge. |
| `save_text_to_file` | `save_to_txt` (Custom) | Saves the final research output to a timestamped file. |

---

## ⚙️ Setup and Installation

### 1. Prerequisites

You must have **Python 3.10 or higher** installed.

### 2. Create and Activate Virtual Environment

### Create a virtual environment
```bash
python -m venv venv
```

### Activate the virtual environment
### On Windows PowerShell:
```bash
.\venv\Scripts\Activate
```
### On Linux/macOS:
```bash
source venv/bin/activate
```

### 3. Install Dependencies
Install all necessary Python libraries.
```bash
pip install -r .\requirements.txt
```
or

```Bash
pip install langchain-google-genai langchain-community langchain pydantic python-dotenv duckduckgo-search wikipedia
```
### 4. Configure API Key
The project requires a Gemini API Key.

1. Get your key from the Google AI documentation.
2. Create a file named .env in the root directory of the project.
3. Add your API key to the file:

```python
# .env file content
GOOGLE_API_KEY="YOUR_API_KEY_HERE"
```

## 🚀 How to Run Locally

1. Ensure your virtual environment is active and the .env file is configured.

2. Run the main script from your terminal:

```Bash
python main.py
```
3. The script will prompt you for a query:
```
What can i help you reseach? {input}
```
4. The agent will then execute the tool chain, and upon completion, it will attempt to parse and print the final structured output.


