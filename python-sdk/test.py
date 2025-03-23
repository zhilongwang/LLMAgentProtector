from polymorphic_prompt_assembler import PolymorphicPromptAssembler

system_prompt = "Please summary the user input. \n{user_input}\n"
user_input = "Half Moon Bay is a picturesque coastal town in Northern California, located about 30 miles south of San Francisco. Known for its stunning ocean views, sandy beaches, and rugged cliffs, it offers a perfect retreat for nature lovers and outdoor enthusiasts. Visitors can explore scenic trails, surf at famous Mavericks, or relax along the coastline. The town’s historic Main Street features charming shops, art galleries, and cozy cafés. With its rich agricultural heritage, fresh seafood, and the popular Pumpkin Festival, Half Moon Bay blends small-town charm with breathtaking natural beauty, making it an ideal destination for a peaceful coastal escape."
protector = PolymorphicPromptAssembler(system_prompt = system_prompt)
secured_prompt = protector.PromptAssemble(user_input = user_input)

print(secured_prompt)
