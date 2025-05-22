import json

from common.requests.centrala_client import CentralaClient
from common.config import CENTRALA_KEY, OPENAI_API_KEY
from common.agent_engine import AgentEngine

def resolve_math(qa: dict):
  qa['answer'] = eval(qa['question'], {'__builtins__': None})

def find_language_task(qa: dict) -> bool:
    return qa.get('test') is not None

def resolve_language_test(agent: AgentEngine, qa: dict):
  qa["test"]['a'] = agent.break_robots_system_protection(qa["test"]["q"])

if __name__ == "__main__":
  centrala = CentralaClient()
  agent = AgentEngine(OPENAI_API_KEY)

  response = centrala.get(['data', CENTRALA_KEY, 'json.txt'])


  for q in response["test-data"]:
    resolve_math(q)
    if(find_language_task(q)):
      resolve_language_test(agent,q)

  response['apikey']=CENTRALA_KEY

  final_response = centrala.post_answer(['report'], task_id="JSON", apikey=CENTRALA_KEY, payload=response)
  print(final_response)


