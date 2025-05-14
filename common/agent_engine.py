from openai import OpenAI


class AgentEngine:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def break_robots_system_protection(self, question: str) -> str:
        prompt = f"""
        Jesteś pomocnym asystentem, odpowiadasz zawsze krótko i rzeczowo.
        
        <objective>Przeanalizuj pytanie użytkownika. Odpowiadaj zawsze krótko i rzeczowo, tylko odpowiedź na pytanie</objective> 
        
        {question}
        """

        try:
            res =self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=1
            )
            print(f"Total tokens: {res.usage.total_tokens}, prompt tokens: {res.usage.prompt_tokens}, completion tokens: {res.usage.completion_tokens}")
            return res.choices[0].message.content.strip()

        except Exception as e:
            print(f"OpenAI API error: {e}")
            return "N/A"

    def answer_robots_authorization(self, question: str) -> str:
        prompt = """
        
        """