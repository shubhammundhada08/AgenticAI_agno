from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.team import Team

load_dotenv()

eng_agent = Agent(name="English Agent", role="You answer questions in English" )
chn_agent = Agent(name="Chinese Agent", role="You answer questions in Chinese" )
hin_agent = Agent(name="Hindi Agent", role="You answer questions in Hindi" )

team_leader = Team(
        model=Groq(id="openai/gpt-oss-120b"),
        members=[eng_agent,chn_agent,hin_agent],
        markdown=True,
        show_members_responses=True,
        instructions="""All member agents must respond in their specific language. 
                        Do not route just one agent.
                         Output the response of all Agents.
                     """
)
        
team_leader.print_response("Capital of India?")

# agent.print_response("If I have done MBA from IIM in India and want to switch to analytics domain, recommend the jobs I can apply for in India.")

# agent.print_response("What is your knowledge cutt-off.")

#TO add tools like duck duck go and time setup
#agent.print_response("What date and festival is it in India tomorrow.")

