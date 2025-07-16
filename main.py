import os
from dotenv import load_dotenv

from agents import (
   Agent ,  #a
   Runner ,  
   OpenAIChatCompletionsModel ,
   RunConfig
)

load_dotenv()

First_agent = Agent(name = "Helloo-agent" , instruction = "you are a helpfull agent ")
