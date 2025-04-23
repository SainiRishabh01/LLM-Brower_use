🔍 LLM-Powered Website Test Automation using Browser-Use + Gemini
This project is a prototype for automating test cases on a live website using a Large Language Model (LLM) and the Browser-Use automation tool.
The LLM interprets plain English test steps, executes them on the browser, and compares the final output with the expected result.

📌 Objective
Build a prototype that:

Accepts a test case (steps + expected output)

Parses and executes steps via the Browser-Use agent

Validates the output

Returns a structured result (PASS/FAIL + explanation)

🧠 Prompt Design Approach
The task prompt provided to the LLM follows a natural, concise structure with:

A clear objective: what website to test and how

Step-by-step instructions in sequential order

A clear expected outcome

Explicit instruction to return "PASS or FAIL" with explanation

Example used:
Your task is to test the website: https://www.farmley.com

Follow these steps:
1. Click on the 'Sign in' button
2. Enter email as 'test@example.com'
3. Enter password as 'test123'
4. Click on the 'Sign in' button

Then verify: User should see 'My account' page
Return whether the test PASSED or FAILED with a brief explanation.
This prompt ensures the LLM can translate natural language into browser actions.

⚙️ Execution & Validation Logic
Tech Stack:
🧠 LLM: Gemini-1.5-Pro via langchain_google_genai

🧪 Browser Agent: browser-use package

🐍 Language: Python 3.10+

Execution Flow:
User runs main.py

LLM receives a prompt with:

Website URL

Step-by-step test case

Expected outcome

browser_use.Agent:

Parses test steps

Executes them in a Chromium browser

Collects visual or DOM feedback

LLM analyzes the results and compares them with the expected outcome

Outputs a structured test result

Validation Logic:
Text Presence: LLM checks if the text 'My account' is present on the page

Fail Explanation: If not found, LLM provides possible reasons like login failure or incorrect flow

🚧 Challenges & Resolutions

Challenge	Resolution
❌ gemini-pro model not found	Updated to gemini-1.5-pro-latest, the correct supported model
❌ run() coroutine not awaited	Used asyncio.run() to correctly run async function
⚠️ Unstructured test results	Enforced a structured return format (PASS/FAIL + explanation) in prompt
⛔ Callback errors with LLM object	Used proper ChatGoogleGenerativeAI class with supported args
✅ Evaluation Criteria Breakdown

Category	Notes
Prompt Design	Clear, structured prompt for LLM to act as a QA tester
Browser-Use Integration	Fully integrated and auto-launches Chromium with step execution
Result Validation	Validates output using DOM/text presence; future support for screenshots possible
Clarity & Documentation	Code is modular, async-compliant, and easy to read. Full setup explained
Bonus – Self-Healing Logic	Retry logic supported by LLM fallback; alternate selectors and retries possible using advanced prompts or browser_use settings
🚀 How to Run
Clone the repo and install dependencies:
Create a .env file:
GOOGLE_API_KEY=your_api_key
Run the script:
python main.py
