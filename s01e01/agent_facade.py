from requests import HTTPError
import s01e01.html_parser as html_parser
from common.models.agent_engine import AgentEngine
from s01e01.config import LOGIN_URL, USERNAME, PASSWORD, OPENAI_API_KEY
import requests

print(f"Uruchomiono moduł: {__name__}")
class LoginAgent:
    def __init__(self):
        self.session = requests.Session()
        self.engine = AgentEngine(OPENAI_API_KEY)

    def fetch_login_page(self):
        print("hacking . . . . .")
        res = self.session.get(LOGIN_URL)
        # res = requests.get(LOGIN_URL)

        print(f"Status: {res.status_code}")
        if res.status_code != 200:
            raise HTTPError("Robots detect your attempts, be careful, you are not anonymous anymore")
        return res.text

    def extract_question(self, html: str) -> str:
        return html_parser.extract_protection_phrase(html)

    def break_protection(self, question: str) -> str:
        return self.engine.break_robots_system_protection(question)

    def submit_login(self, answer: str) -> str:
        form_data = {
            "username": USERNAME,
            "password": PASSWORD,
            "answer": answer
        }
        res = self.session.post(LOGIN_URL, data = form_data, headers={"Content-Type":"application/x-www-form-urlencoded"})
        return res.content