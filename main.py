from client.llm_client import LLMClient



asyc def main():
    client=LLMClient()
    messages=[{
        "role":"user",
        "content":"Hello, how are you?"
    }
    ]
    await client.chat_completion(messages,False)
    print("Done")