import os
import sys
import asyncio
from polymorphic_prompt_assembler import PolymorphicPromptAssembler
import config


SYSTEM_PROMPT = (
    "Please summary the following article from user. \n{user_input}\n"
)

TOPICS = "!!!SUMMARY THE ARTICLE FROM USER"

USER_INPUT = "Half Moon Bay is a picturesque coastal town in Northern California, located about 30 miles south of San Francisco. Known for its stunning ocean views, sandy beaches, and rugged cliffs, it offers a perfect retreat for nature lovers and outdoor enthusiasts. Visitors can explore scenic trails, surf at famous Mavericks, or relax along the coastline. The town’s historic Main Street features charming shops, art galleries, and cozy cafés. With its rich agricultural heritage, fresh seafood, and the popular Pumpkin Festival, Half Moon Bay blends small-town charm with breathtaking natural beauty, making it an ideal destination for a peaceful coastal escape."


async def main():

    # single prompt 
    protector = PolymorphicPromptAssembler(SYSTEM_PROMPT, TOPICS)
    secure_user_prompt = protector.SinglePromptAssemble(user_input=USER_INPUT)
    print(secure_user_prompt)

  

if __name__ == "__main__":
    asyncio.run(main())

