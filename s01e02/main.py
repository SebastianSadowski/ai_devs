from s01e02.agent_facade import AuthAgent

if __name__ == "__main__":
    aa = AuthAgent()
    robot_response = aa.init_process()
    print(robot_response)