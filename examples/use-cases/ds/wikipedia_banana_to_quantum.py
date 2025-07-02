import asyncio
import os
import sys

from browser_use.llm import ChatOpenAI
from examples.ui.streamlit_demo import provider

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from dotenv import load_dotenv

load_dotenv()

from browser_use import Agent

api_key = os.getenv('DEEPSEEK_API_KEY', '')
if not api_key:
    raise ValueError('DEEPSEEK_API_KEY is not set')

task = 'go to https://en.wikipedia.org/wiki/Banana and click on buttons on the wikipedia page to go as fast as possible from banna to Quantum mechanics'

async def run_search():
    agent = Agent(
        task=task,
        llm=ChatOpenAI(
            organization='deepseek',
            base_url='https://api.deepseek.com/',
            model='deepseek-chat',
            api_key=api_key,
        ),
        use_vision=False,
    )

    await agent.run()


if __name__ == '__main__':
    asyncio.run(run_search())
