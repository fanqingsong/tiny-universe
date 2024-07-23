import os, json
import requests

"""
工具函数

- 首先要在 tools 中添加工具的描述信息
- 然后在 tools 中添加工具的具体实现

- https://serper.dev/dashboard
"""

class Tools:
    def __init__(self) -> None:
        self.toolConfig = self._tools()
    
    def _tools(self):
        tools = [
            # {
            #     'name_for_human': 'Bing搜索',
            #     'name_for_model': 'bing_search',
            #     'description_for_model': 'Bing搜索是一个通用搜索引擎，可用于访问互联网、查询百科知识、了解时事新闻等。',
            #     'parameters': [
            #         {
            #             'name': 'search_query',
            #             'description': '搜索关键词或短语',
            #             'required': True,
            #             'schema': {'type': 'string'},
            #         }
            #     ],
            # },
            {
                'name_for_human': 'shell command',
                'name_for_model': 'execute_shell',
                'description_for_model': 'This tool can help you execute shell command.',
                'parameters': [
                    {
                        'name': 'search_query',
                        'description': 'shell command',
                        'required': True,
                        'schema': {'type': 'string'},
                    }
                ],
            }

        ]
        return tools

    def bing_search(self, search_query: str):
        print("------------ mock bing search -------------------")

        return "Sorry, I don't know."

        url = "https://google.serper.dev/search"

        payload = json.dumps({"q": search_query})
        headers = {
            'X-API-KEY': '修改为你自己的key',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload).json()

        return response['organic'][0]['snippet']
