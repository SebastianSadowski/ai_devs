import requests
from requests import Response

from s01e02.config import VERIFY_URL, OPENAI_API_KEY
from common.models.agent_engine import AgentEngine

class AuthAgent:
    def __init__(self):
        self.session = requests.session()
        self.engine = AgentEngine(OPENAI_API_KEY)

    def init_process(self) -> str:
        init_message = {
            "msgID": "0",
            "text": "READY"
        }
        return self.session.post(VERIFY_URL,json=init_message).content

    def answer_question(self, question: str) -> Response:
        response = self.engine.answer_robots_authorization(question)
        print(response)
        return self.session.post(VERIFY_URL, data=response, headers={"Content-Type":"Application/json; charset=utf-8"}).content




