import os
import sys
import asyncio
from polymorphic_prompt_assembler import PolymorphicPromptAssembler
import config

async def main():

    user_input = config.BENIGN_PAYLOAD
    protector = PolymorphicPromptAssembler()
    system_prompt, user_prompt = protector.PromptAssemble(user_input=user_input)

    secured_prompt = f"{system_prompt}\n\n{user_prompt}"

    print(secured_prompt)

if __name__ == "__main__":
    asyncio.run(main())

