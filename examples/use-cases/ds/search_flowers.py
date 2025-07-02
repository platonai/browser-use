import asyncio
import os
import sys

from browser_use.llm import ChatOpenAI

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from dotenv import load_dotenv

load_dotenv()

from browser_use import Agent

api_key = os.getenv('DEEPSEEK_API_KEY', '')
if not api_key:
    raise ValueError('DEEPSEEK_API_KEY is not set')

task = 'go to https://www.hua.com and search for "月季"'

async def run_search():
    agent = Agent(
        task=task,
        llm=ChatOpenAI(
            organization='deepseek',
            base_url='https://api.deepseek.com/v3',
            model='deepseek-chat',
            api_key=api_key,
        ),
        use_vision=False,
    )

    await agent.run()


if __name__ == '__main__':
    asyncio.run(run_search())
