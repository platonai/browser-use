import asyncio
import os

from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from pydantic import SecretStr

from browser_use import Agent

# dotenv
load_dotenv()

api_key = os.getenv('DEEPSEEK_API_KEY', '')
if not api_key:
	raise ValueError('DEEPSEEK_API_KEY is not set')

task = """
    go to https://www.amazon.com/s?k=best+selling+books+last+30+days
    click on the dropdown menu on the top right corner that shows "Sort by: Featured"
    then select "Best Sellers" from the dropdown
    """

async def run_agent():
	agent = Agent(
		task=task,
		llm=ChatDeepSeek(
			base_url='https://api.deepseek.com/v1',
			model='deepseek-chat',
			api_key=SecretStr(api_key),
		),
		use_vision=False,
	)

	await agent.run()

if __name__ == '__main__':
	asyncio.run(run_agent())
