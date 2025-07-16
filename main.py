import os
from dotenv import load_dotenv

from agents import (
   Agent ,  #a
   Runner ,  
   OpenAIChatCompletionsModel ,
   RunConfig
)

load_dotenv()

gemini_api_key = ("GEMINI_API_KEY")

First_agent = Agent(name = "Helloo-agent" , instruction = "you are a helpfull agent ")
