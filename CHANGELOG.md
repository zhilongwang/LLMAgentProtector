All notable changes to **LLMAgentProtector** will be documented in this file.  
This project follows [Semantic Versioning](https://semver.org/).

---

## [v1.2.0] - 2025-07-09

### ✨ New Features
- **🔐 Prompt Leakage Detection**: Added `leak_detect()` method to identify if polymorphic separators leak into the LLM's output.
- **🪺 Canary Tracking**: Prompt assembly methods now return `(left_sep, right_sep)` canary tokens for downstream leakage detection.

### 🧠 Improvements
- Refined prompt formatting and separator rendering for enhanced stealth and consistency.

---

## [v1.0.0] - 2025-06-01

### 🚀 Initial Release
- Core implementation of the `PolymorphicPromptAssembler` class.
- Support for randomized separator injection via `single_prompt_assemble()`.
- Configurable system prompt constraints for anti-prompt injection protection.

---
