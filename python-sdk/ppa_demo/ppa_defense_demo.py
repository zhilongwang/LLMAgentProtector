import asyncio
import json
import os
import sys
import random

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from llm_utils import call_gpt, classify_response_llama
from polymorphic_prompt_assembler import PolymorphicPromptAssembler
import config

NUM_ATTACKS = 100
RESULTS_FILE = "results/1ppa_demo_summary.json"

async def run_demo_attacks():
    protector = PolymorphicPromptAssembler()
    success_count = 0
    failure_count = 0
    results = []

    for i in range(NUM_ATTACKS):
        system_prompt, user_prompt = protector.PromptAssemble(config.ATTACK_PAYLOAD)
        response = await call_gpt(system_prompt, user_prompt)
        classification = classify_response_llama(response)

        if classification == "Defended":
            success_count += 1
        else:
            failure_count += 1

        results.append({
            "attempt": i + 1,
            "separator": user_prompt.split("\n")[0],  # show just the opening separator
            "classification": classification
        })

    summary = {
        "total_attempts": NUM_ATTACKS,
        "defended": success_count,
        "attacked": failure_count,
        "success_rate": f"{(success_count / NUM_ATTACKS) * 100:.2f}%",
        "details": results
    }

    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print(f"\nDemo completed. Summary saved to `{RESULTS_FILE}`.")

if __name__ == "__main__":
    asyncio.run(run_demo_attacks())
