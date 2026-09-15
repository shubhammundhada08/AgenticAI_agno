from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools

load_dotenv()

def build_agent():
        return Agent(model=Groq(id="openai/gpt-oss-120b"), tools=[DuckDuckGoTools()],  markdown=True, instructions="Act as if you are a career coucellor", add_datetime_to_context=True)

agent = build_agent()

# agent.print_response("If I have done MBA from IIM in India and want to switch to analytics domain, recommend the jobs I can apply for in India.")

# agent.print_response("What is your knowledge cutt-off.")

#TO add tools like duck duck go and time setup
#agent.print_response("What date and festival is it in India tomorrow.")

