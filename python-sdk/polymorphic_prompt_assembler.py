import random
import config

class PolymorphicPromptAssembler:
    """
    Polymorphic Prompt Assembling (PPA) introduces randomization into the prompt structure
    to protect LLM agents from prompt injection attacks.

    By randomly selecting unique separator pairs and embedding the user input between them,
    PPA creates unpredictable boundaries that adversarial instructions struggle to bypass.

    The assembled prompt is split into:
    1. A system prompt that clearly defines the boundary using the selected separators and
       instructs the model to ignore any embedded instructions.
    2. A user prompt where the actual user input is encapsulated between those separators.

    This technique mitigates prompt injection by making system-to-user transitions opaque to attackers.

    Example:
        >>> from polymorphic_prompt_assembler import PolymorphicPromptAssembler
        >>> protector = PolymorphicPromptAssembler()
        >>> user_input = "Half Moon Bay is a scenic coastal town in Northern California."
        >>> system_prompt, user_prompt = protector.PromptAssemble(user_input=user_input)
        >>> print(system_prompt)
        >>> print(user_prompt)
    """

    def __init__(self):
        self.SEPARATORS = config.SEPARATORS
        self.SYSTEM_PROMPT_TEMPLATE = config.SYSTEM_PROMPT
        self.USER_INPUT = config.ATTACK_PAYLOAD

    def PromptAssemble(self, user_input: str = None):
        """
        Assemble a protected prompt by inserting the user input between randomly chosen separators.

        Args:
            user_input (str): The user's raw input text.

        Returns:
            tuple: (system_prompt, user_prompt)
                - system_prompt (str): Describes the input boundaries and instructs the LLM.
                - user_prompt (str): User input wrapped inside the random separators.
        """
        input_text = user_input if user_input is not None else self.USER_INPUT
        left_sep, right_sep = random.choice(self.SEPARATORS)
        system_prompt = self.SYSTEM_PROMPT_TEMPLATE.format(sep=[left_sep, right_sep])
        user_prompt = f"{left_sep}{input_text}{right_sep}"

        return system_prompt, user_prompt
