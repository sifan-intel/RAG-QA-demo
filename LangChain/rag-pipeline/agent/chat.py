from tclogger import logger, Runtimer
from langchain_openai import AzureChatOpenAI

from .constants import OPENAI_ENVS


class OpenAIChat:
    def __init__(self, openai_envs: dict = None):
        if not openai_envs:
            self.openai_envs = OPENAI_ENVS
        self.create_chat()

    def create_chat(self):
        if self.openai_envs.get("api_type") == "azure":
            self.chat = AzureChatOpenAI(
                deployment_name = self.openai_envs.get("model"),
                azure_endpoint=self.openai_envs.get("endpoint"),
                api_key=self.openai_envs.get("api_key"),
                api_version=self.openai_envs.get("api_version"),
            )
        else:
            self.chat = AzureChatOpenAI(
                base_url=self.openai_envs.get("endpoint"),
                api_key=self.openai_envs.get("api_key"),
            )

    def get_chat_model(self):
        return self.chat


if __name__ == "__main__":
    pass
