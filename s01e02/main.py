from s01e02.agent_facade import AuthAgent

if __name__ == "__main__":
    aa = AuthAgent()
    robot_response = aa.init_process()
    print(robot_response)
    structured_answer = aa.answer_question(robot_response)
    print(structured_answer)
    with open("control.html", "wb") as f:
        f.write(structured_answer)