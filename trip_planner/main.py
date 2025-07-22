import os

from dotenv import load_dotenv
from agents import (
    Agent,
    Runner,
    RunConfig,
)

load_dotenv()
gemeni_api_key = os.getenv("GEMINI_API_KEY")

model = 


Destination_agent = Agent(name = """Trip_Planner" , instruction = "youe are a trip planner agent ,
                                    who helps user to find best destination basically you provide good destination to user for better experience , your are only
                                    for provide detination to user """ )

Booking_agent = Agent(name = "booking_agent" , instruction = """you are a booking agent that help user to provide all booking details like suggest hotel
                                                                , provide cost of rent for every hotel , Provide Schedule Your work is only as booking agent""")

Explore_Agent = Agent(name = "explore_agent" , instruction = """your are a Exploring Agent an your work is to provide or suggest Arraction or foods or
                                                                culture of place based on its destination and its hotel or place or famous things about that places """)

main_agent = Agent(
    name = "main-agent",
    instructions = "you are a main agent that analyze user input and give handoff to its expert agent not give answere bs your own",
    handoffs = [Destination_agent, Booking_agent, Explore_Agent]
)

response = input("how can i help you in planning your trip?")
result = Runner.run_sync(main_agent , response , run_config = config)
print(result.final_output)

