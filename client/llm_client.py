from openai import AsyncOpenAI
from typing import List, Any
class LLMClient:
    def __init__(self)-> None:
        self._client : AsyncOpenAI() | None=None
     
    def get_client(self)-> AsyncOpenAI:
        if self._client is None:
            self._client = AsyncOpenAI(
                api_key="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",
                base_url="https://openrouter.ai/api/v1",
            )
        return self._client

    
    async def close(self)-> None:
        if self._client :
            await self._client.close()
            self._client = None
    

    async def chat_completion(self,
    messages:List[dict[str,Any]],
    stream:bool=True):
        client = self.get_client()
        kwargs = {
            "model":"mistralai/devstral-2512:free",
            "messages":messages,
            "stream":stream,
        }
        if stream:
            self._stream_response()
        else:
            self._non_stream_response(client,kwargs)

    aysnc def _stream_response(self):
        pass

    async def _non_stream_response(self,client: AsyncOpenAI, kwargs: dict[str,Any],):
        response=await client.chat.completions.create(**kwargs)
        print(response)

    



