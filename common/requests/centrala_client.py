import json as jsonik
from urllib.parse import urljoin

import requests
from typing import Any, Optional, Dict

__all__ = ["CentralaClient"]

class CentralaClient:
    def __init__(self, custom_url: Optional[str] = None):
        self.session= requests.session()
        self.CENTRALA_URL = custom_url if custom_url is not None else "https://c3ntrala.ag3nts.org"

    def get(
            self,
            path: list,
            *,
            params: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, str]] = None,
            timeout: Optional[int] = 10,
            **kwargs
    ) -> Any:
        url = urljoin(self.CENTRALA_URL, prepare_path(*path))
        response = self.session.get(
            url,
            params=params,
            headers=headers,
            timeout=timeout,
            **kwargs
        )
        response.raise_for_status()
        return response

    def post_answer(
            self,
            path: list,
            *,
            task_id: str,
            apikey: str,
            payload: Optional[str] = None,
            params: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, str]] = None,
            timeout: Optional[int] = 10,
            **kwargs
    ) -> Any:
        url = urljoin(self.CENTRALA_URL, prepare_path(*path))
        data = prepare_answer(task_id, apikey, payload)


        print(f"centrala body: \n {data}")
        response = self.session.post(url,
                        data=data,
                        headers=headers,
                        timeout=timeout,
                        **kwargs
        )
        response.raise_for_status()
        return response



def prepare_path(*args) -> str:
        return "/".join(a.strip("/") for a in args)

def prepare_answer(task_id: str, apikey: str, task_content: str) -> str:
    r = {
        "task": task_id,
        "apikey": apikey,
        "answer": task_content
    }
    return jsonik.dumps(r)