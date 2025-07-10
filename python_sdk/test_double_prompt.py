import os
import sys
import asyncio
from polymorphic_prompt_assembler import PolymorphicPromptAssembler
import config

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from utils.llm_utils import call_gpt


SYSTEM_PROMPT = (
    "Please summary the article from user. "
)

TOPICS = "!!!SUMMARY THE ARTICLE FROM USER"

USER_INPUT = "Half Moon Bay is a picturesque coastal town in Northern California, located about 30 miles south of San Francisco. Known for its stunning ocean views, sandy beaches, and rugged cliffs, it offers a perfect retreat for nature lovers and outdoor enthusiasts. Visitors can explore scenic trails, surf at famous Mavericks, or relax along the coastline. The town’s historic Main Street features charming shops, art galleries, and cozy cafés. With its rich agricultural heritage, fresh seafood, and the popular Pumpkin Festival, Half Moon Bay blends small-town charm with breathtaking natural beauty, making it an ideal destination for a peaceful coastal escape."


async def main():

    # double prompt 
    protector = PolymorphicPromptAssembler(SYSTEM_PROMPT, TOPICS)
    secure_system_prompt, secure_user_prompt = protector.DoublePromptAssemble(user_input=USER_INPUT)
    print("\033[92mSYSTEM PROMPT:\033[0m\n", secure_system_prompt)
    print("\033[92mUSER PROMPT:\033[0m\n", secure_user_prompt)
    response = await call_gpt(secure_system_prompt, secure_user_prompt)
    print("\033[92mRESPONSE:\033[0m\n", response)
    

if __name__ == "__main__":
    asyncio.run(main())

