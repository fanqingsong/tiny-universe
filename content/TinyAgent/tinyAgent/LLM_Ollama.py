from typing import Dict, List, Optional, Tuple, Union

from openai import OpenAI


'''
curl http://localhost:11434/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "qwen:0.5b",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Hello!"
            }
        ]
    }'
 
'''



class BaseModel:
    def __init__(self, path: str = '') -> None:
        # self.path = path
        pass

    def chat(self, prompt: str, history: List[dict]):
        pass

    def load_model(self):
        pass

class InternLM2Chat(BaseModel):
    def __init__(self, path: str = '') -> None:
        super().__init__(path)
        # self.load_model()

        client = OpenAI(
            base_url='http://10.80.11.197:8000/v1',
            # required but ignored
            api_key='ollama',
        )

        self.client = client


    # def load_model(self):
    #     print('================ Loading model ================')
    #     self.tokenizer = AutoTokenizer.from_pretrained(self.path, trust_remote_code=True)
    #     self.model = AutoModelForCausalLM.from_pretrained(self.path, torch_dtype=torch.float16, trust_remote_code=True).cuda().eval()
    #     print('================ Model loaded ================')

    def chat(self, prompt: str, history: List[dict], meta_instruction:str ='') -> str:
        # response, history = self.model.chat(self.tokenizer, prompt, history, temperature=0.1, meta_instruction=meta_instruction)
        # return response, history

        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": meta_instruction
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model='/mnt/AI/models/internlm2_chat_7b/',
        )

        print(chat_completion)

        ret = chat_completion.choices[0].message.content

        return ret



# if __name__ == '__main__':
#     model = InternLM2Chat('/root/share/model_repos/internlm2-chat-7b')
#     print(model.chat('Hello', []))