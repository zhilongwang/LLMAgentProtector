import random
import config

class PolymorphicPromptAssembler:
    def __init__(self, system_prompt:str=None):
        """ Initialize the protection.
        Args:
            system_prompt(str):required

        Example 1 (with system prompt):
                >>> system_prompt = "Please summary the user input. \n{user_input}\n"
                >>> protector = PolymorphicPromptAssembler(system_prompt = system_prompt)
                >>> user_input = "Half Moon Bay is a picturesque coastal town in Northern California, located about 30 miles south of San Francisco. Known for its stunning ocean views, sandy beaches, and rugged cliffs, it offers a perfect retreat for nature lovers and outdoor enthusiasts. Visitors can explore scenic trails, surf at famous Mavericks, or relax along the coastline. The town’s historic Main Street features charming shops, art galleries, and cozy cafés. With its rich agricultural heritage, fresh seafood, and the popular Pumpkin Festival, Half Moon Bay blends small-town charm with breathtaking natural beauty, making it an ideal destination for a peaceful coastal escape."
                >>> secured_prompt = protector.PromptAssemble(user_input = user_input)

        """
        self.SEPARATORS     =  config.SEPARATORS
        self.FORMAT_CONSTRAIN = config.FORMAT_CONSTRAIN            
        self.system_prompt =  system_prompt 

    def PromptAssemble(self, user_input:str=None):
        """ Enhance the prompt that send to LLM
            Args:

                user_input(str):required

            Returns:
                secured_prompt(str): This is a secure prompt.

            
        """
        left_sep, right_sep = random.choice(self.SEPARATORS)
        
        format_constrain = self.FORMAT_CONSTRAIN.format(left_sep=left_sep, right_sep=right_sep)
        format_constrain = "\n" + format_constrain + "\n" + left_sep + "\n" + user_input + "\n" + right_sep + "\n" 
        return self.system_prompt.replace("{user_input}", format_constrain)
        
