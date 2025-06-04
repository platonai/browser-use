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

task="打开baidu.com，搜索框输入 PulsarRPA, 点击回车，搜索结果打开后，访问前三个网页，最后总结结果"

async def run_search():
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
	asyncio.run(run_search())
