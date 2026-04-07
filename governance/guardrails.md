---
type: guardrails
version: "1.0.0"
---

# Guardrails: RaizAncestral

> Auto-generated from detected conventions

## Context

- **Files analyzed:** 15
- **Overall confidence:** high
- **Generated:** 2026-03-18

### Code Style

| ID | Level | Guardrail | Verification | Derived from |
|----|-------|-----------|--------------|--------------|
| must-style-001 | MUST | Use 4-space indentation | ruff check . | Convention |
| must-style-002 | MUST | Use double quotes for strings | ruff check . | Convention |
| must-style-003 | MUST | Maximum line length: 79 characters | ruff check . | Convention |

### Naming

| ID | Level | Guardrail | Verification | Derived from |
|----|-------|-----------|--------------|--------------|
| must-naming-001 | MUST | Function names: snake_case | Manual review | Convention |
| must-naming-002 | MUST | Class names: PascalCase | Manual review | Convention |
| must-naming-003 | MUST | Constant names: UPPER_SNAKE_CASE | Manual review | Convention |

### Structure

| ID | Level | Guardrail | Verification | Derived from |
|----|-------|-----------|--------------|--------------|
| should-structure-001 | SHOULD | Source code in src/ layout (src/kokoro) | Manual review | Convention |
| should-structure-002 | SHOULD | Tests in tests/ directory | Manual review | Convention |

### Security

| ID | Level | Guardrail | Verification | Derived from |
|----|-------|-----------|--------------|--------------|
| must-security-001 | MUST | Never commit client personal data (phones, emails, names) to git | `git log -p -S "phone"` returns empty | Incident 2026-04-07 |
| must-security-002 | MUST | `.kokoro/` directory always in .gitignore | `grep .kokoro .gitignore` | Incident 2026-04-07 |
| must-security-003 | MUST | No API keys, tokens, or secrets in tracked files | Pre-commit check | Convention |

### Voice & Vocabulary

| ID | Level | Guardrail | Verification | Derived from |
|----|-------|-----------|--------------|--------------|
| must-voice-001 | MUST | Skills use Eduardo's vocabulary (inversión, creación, invitado) | `tests/vocabulary_check.py` | RF-03 |
| must-voice-002 | MUST | Skills never use prohibited words (precio, producto, cliente, gratis) | `tests/vocabulary_check.py` | RF-03 |
| should-voice-001 | SHOULD | Skills reference Proyector strategy (esperar invitación) | Manual review | RF-03 |

### Process

| ID | Level | Guardrail | Verification | Derived from |
|----|-------|-----------|--------------|--------------|
| must-process-001 | MUST | Phases are sequential — skills cannot skip phases | Skill structure review | RF-02 |
| should-process-001 | SHOULD | Onboarding before any phase work | `/kokoro-onboard` exists | RF-08 |

---

*Conventions detected by `raise init --detect` (2026-03-18). Security guardrails added 2026-04-07 after audit.*
