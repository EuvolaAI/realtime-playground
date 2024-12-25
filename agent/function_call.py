import logging
from typing import Annotated

import aiohttp
from dotenv import load_dotenv
from livekit.agents import (
    llm,
)
import json

logger = logging.getLogger("my-worker")

class AgentFunc(llm.FunctionContext):
    '''
    The class defines a set of LLM functions that the assistant can execute.
    '''
    @llm.ai_callable(
            name="name",
            description="Called when the user asks about his/her name. This function will return the his/her name"
            )
    async def get_my_name(self):
        url = f"https://test.smartapetech.com/livekit/whoami"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    weather_data = await response.text()
                    # response from the function call is returned to the LLM
                    data = json.loads(weather_data)
                    # response from the function call is returned to the LLM
                    logging.info(f"weather si {data.get('data').get('Name')}")
                    return f"{data.get('data').get('Name')}."
                else:
                    raise Exception(
                        f"Failed to get weather data, status code: {response.status}"
                    )
    @llm.ai_callable(
            name="myhobby",
            description="Called when the user asks about his/her hobby. This function will return the  result"
            )
    async def get_my_hobby(self):
        return f"吃饭,睡觉,打豆豆"