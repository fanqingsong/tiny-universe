


from tinyAgent.Agent_Ollama import Agent_Ollama


# agent = Agent('/root/share/model_repos/internlm2-chat-20b')

agent = Agent_Ollama('/home/song/Desktop/github/me/internlm2-chat-7b')


print(agent.system_prompt)


# print("------------------------ before 1 -----------------------------")

# response = agent.text_completion(text='你好', history=[])

# print("------------------------ after 1 -----------------------------")


# print("------------------------ before 2 -----------------------------")

# response = agent.text_completion(text='特朗普哪一年出生的？', history=[])

# print("------------------------ after 2 -----------------------------")


response = agent.text_completion(text='周杰伦是谁？', history=[])
# print(response)



# response = agent.text_completion(text='书生浦语是什么？', history=_)
# print(response)



