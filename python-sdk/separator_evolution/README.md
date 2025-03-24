## Separator Evolution

This module supports **iterative expansion and testing of separator pairs** used in the **Polymorphic Prompt Assembling (PPA)** framework to defend against prompt injection attacks.

### What It Does

- Loads **high-performing separators** (ASR < 20%) from previous rounds  
- Uses **GPT** to generate structurally or semantically similar variants  
- Evaluates new separators against a **fixed attack prompt**  
- Stores **detailed and summary results** for each round in `/results`  

### Files

- `genetic_separator_script.py` — Main script to expand and evaluate separator variants  
- `load_good_separators.py` — Extracts good-performing separators to seed the next round  
- `results/` — Contains round-wise outputs (`round_1/`, `round_2/`, etc.)

### Usage

```bash
python genetic_separator_script.py
