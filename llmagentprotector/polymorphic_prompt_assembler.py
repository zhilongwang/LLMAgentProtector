import random
from . import config

class PolymorphicPromptAssembler:
    """
    Polymorphic Prompt Assembling (PPA) introduces randomization into the prompt structure
    to protect LLM agents from prompt injection attacks.

    By randomly selecting unique separator pairs and embedding the user input between them,
    PPA creates unpredictable boundaries that adversarial instructions struggle to bypass.

    In double_prompt_assemble, the assembled prompt is split into:
    1. A system prompt that clearly defines the constraints and
       instructs the model to ignore any embedded instructions.
    2. A user prompt where the actual user input is encapsulated between those separators.

    In single_prompt_assemble, the single assembled prompt contains both the constraints and user input.

    The leak_detect detect the prompt leakage by check if the separator appears in the model response.

    This technique mitigates prompt injection by inserting polymorphic boundary between instruction and user input. 

    Example:
        >>> from polymorphic_prompt_assembler import PolymorphicPromptAssembler
        >>> protector = PolymorphicPromptAssembler()
        >>> user_input = "Half Moon Bay is a scenic coastal town in Northern California."
        >>> system_prompt, user_prompt = protector.PromptAssemble(user_input=user_input)
        >>> print(system_prompt)
        >>> print(user_prompt)
        >>> response = await call_gpt(system_prompt, user_prompt)
        >>> prompt_leaked = protector.leak_detect(response, canary)
    """

    def __init__(self, system_prompt:str=None, task_topic:str=None):
        self.SEPARATORS     =  config.SEPARATORS
        self.TOPIC_CONSTRAIN = config.TOPIC_CONSTRAIN
        self.ANTI_PROMPT_LEAKAGE_CONSTRAIN = config.ANTI_PROMPT_LEAKAGE_CONSTRAIN
        self.FORMAT_CONSTRAIN = config.FORMAT_CONSTRAIN
        self.secure_system_prompt = system_prompt + self.ANTI_PROMPT_LEAKAGE_CONSTRAIN + "\n\n" + self.TOPIC_CONSTRAIN.replace("{task_topic}", task_topic)      

    def single_prompt_assemble(self, user_input: str = None):
        """
        This method assemble one protected prompt (secure_prompt) by inserting the user input between randomly chosen separators. This single prompts serve for the case developer only pass one prompt to LLM when developping agent.  

        Args:
            user_input (str): The user's raw input text.

        Returns:
            tuple: (user_prompt)
                - secure_prompt (str): User input wrapped inside the random separators.
                - canary ((left_sep, right_sep)): Canary are left_sep and right_sep that are embedded into model input and used to detect the prompt leakage.
        """

        left_sep, right_sep = random.choice(self.SEPARATORS)
        format_constrain = self.FORMAT_CONSTRAIN.format(left_sep=left_sep, right_sep=right_sep)
        format_constrain = "\n" + format_constrain + "\n\n" + left_sep + "\n" + user_input + "\n" + right_sep + "\n" 
        return self.secure_system_prompt.replace("{user_input}", format_constrain), (left_sep, right_sep)


    def double_prompt_assemble(self, user_input: str = None):
        """
        
        This method assemble two protected prompts (secure_system_prompt, secure_user_prompt) by inserting the user input between randomly chosen separators. This two prompts serve for the case developer want to pass both system prompt and user prompts to LLM when developping agent.   
        
        Args:
            user_input (str): The user's raw input text.

        Returns:
            tuple: (secure_system_prompt, secure_user_prompt)
                - secure_system_prompt (str): Describes the input boundaries and instructs the LLM.
                - secure_user_prompt (str): User input wrapped inside the random separators.
                - canary ((left_sep, right_sep)): Canary are left_sep and right_sep that are embedded into model input and used to detect the prompt leakage.
        """

        left_sep, right_sep = random.choice(self.SEPARATORS)
        self.secure_system_prompt 
        self.secure_user_prompt = self.FORMAT_CONSTRAIN.format(left_sep=left_sep, right_sep=right_sep) +  "\n\n" + left_sep + "\n" + user_input + "\n" + right_sep + "\n"
        return self.secure_system_prompt, self.secure_user_prompt, (left_sep, right_sep)
    

    """
        
        This method detect the prompt leakage by check if the separator appears in the model response.

        Args:
            response (str): the LLM output.
            tuple: (left_sep, right_sep): Canary is used to detect the prompt leakage.
        Returns:
            detected (bool): whether prompt leakage is detected.
        """
    def leak_detect(self, response, canary):
        left_sep, right_sep = canary
        if left_sep in response or right_sep in response:
            return True
        return False

