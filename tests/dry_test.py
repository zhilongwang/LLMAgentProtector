from llmagentprotector import PolymorphicPromptAssembler


SYSTEM_PROMPT = (
    "Translate 'hello' to French. \n{user_input}\n"
)

TOPICS = "!!!TRANSLATE THE ARTICLE FROM USER ONLY"


def main():
    # Create an instance of the prompt assembler
    ppa = PolymorphicPromptAssembler(SYSTEM_PROMPT, TOPICS)

    user_prompt = "good afternoon"

    # Use single prompt assembling
    single_prompt, canary = ppa.single_prompt_assemble(user_prompt)
    print("\n=== Single Prompt Assembled ===")
    print(single_prompt)

    # Use double prompt assembling
    system_prompt, user_prompt_wrapped, canary = ppa.double_prompt_assemble(user_prompt)
    print("\n=== Double Prompt Assembled ===")
    print("System Prompt:")
    print(system_prompt)
    print("\nUser Prompt:")
    print(user_prompt_wrapped)

if __name__ == "__main__":
    main()