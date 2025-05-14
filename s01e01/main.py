from requests import HTTPError

from agent_facade import LoginAgent

if __name__ == "__main__":
    ag = LoginAgent()
    print("agent ready to mission")
    try:
        entry = ag.fetch_login_page()
        print("Latest security seems to be not breakable...")

        protection_phrase = ag.extract_question(entry)

        print(f"GOT YA. Protection phrase {protection_phrase}")
        res = ag.break_protection(protection_phrase)
        print(f"Work in progress. . . . . . our agent did it! answer is {res} ")

        res = ag.submit_login(res)

        with open("robot_secrets.html", "wb") as f:
            f.write(res)

    except HTTPError as e:
        print(e)