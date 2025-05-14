import requests
from s01e02.config import VERIFY_URL, OPENAI_API_KEY
from common.agent_engine import AgentEngine

class AuthAgent:
    def __init__(self):
        self.session = requests.session()
        self.engine = AgentEngine(OPENAI_API_KEY)

    def init_process(self) -> str:
        init_message = {
            "text": "READY",
            "msgID": "0"
        }
        return self.session.post(VERIFY_URL,json=init_message).content

    def answer_question(self, question: str) -> str:
        self.engine.answer_robots_authorization(question)


