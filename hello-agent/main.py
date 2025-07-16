import os

from dotenv import load_dotenv
from agents import (
    Agent,
    Runner,
    OpenAIChatCompletionsModel,
    RunConfig
)
from openai import AsyncOpenAI


load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
client = AsyncOpenAI(api_key = openai_api_key)


My_Agent = Agent(name = "Assitant" , instructions = "you are a helpful agent , Answere user after deep understanding of its prompt and give Answere in acurrate, short and important point.")

my_model = OpenAIChatCompletionsModel(
    model = "gpt-3.5-turbo",
    openai_client= client
)

My_Agent.model = my_model

user_input = input("user :")
response = Runner.run_sync(My_Agent, user_input )

print(response.final_output)