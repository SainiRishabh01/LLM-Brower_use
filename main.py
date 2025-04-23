import asyncio
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent

# Load .env file containing GOOGLE_API_KEY
load_dotenv()

async def main():
    task_description = """
    Your task is to test the website: https://www.farmley.com

    Follow these steps:
    1. Click on the 'Sign in' button
    2. Enter email as 'test@example.com'
    3. Enter password as 'test123'
    4. Click on the 'Sign in' button

    Then verify: User should see 'My account' page
    Return whether the test PASSED or FAILED with a brief explanation.
    """

    # ✅ Set up Gemini LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro-latest",  # Ensure this matches what you have access to!
        temperature=0.3,
    )

    # ✅ Create agent
    agent = Agent(
        task=task_description,
        llm=llm
    )

    # ✅ Run agent
    await agent.run()

# ✅ Entry point
if __name__ == "__main__":
    asyncio.run(main())
