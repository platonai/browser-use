import asyncio
import os

from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

from browser_use import Agent

# dotenv
load_dotenv()

# api_key = os.getenv('DEEPSEEK_API_KEY', '')

# llm=ChatDeepSeek(
# 			base_url='https://api.deepseek.com/v1',
# 			model='deepseek-chat',
# 			api_key=SecretStr(api_key),
# 		),

api_key = os.getenv('VOLC_ENGINE_API_KEY', '')
if not api_key:
	raise ValueError('VOLC_ENGINE_API_KEY is not set')

llm = ChatOpenAI(
			base_url='https://ark.cn-beijing.volces.com/api/v3',
			model='doubao-1.5-pro-32k-250115',
			api_key=SecretStr(api_key),
		)


task = """
go to amazon and find the best selling t-shirts, give me the name, price, and a brief description.
    """

async def run_agent():
	agent = Agent(
		task=task,
		llm=llm,
		use_vision=False,
	)

	await agent.run()

if __name__ == '__main__':
	asyncio.run(run_agent())
