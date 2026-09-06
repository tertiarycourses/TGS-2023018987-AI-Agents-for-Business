# Lab 07 - Sales evidence and consent: prompts

TGS-2023018987 | v1.0 | Synthetic classroom data

## Prompt 1 - Build

Create lead briefs and draft outreach only for consented records. Use the explicit scoring formula, cite source_id for facts, and use only approved claims. Never invent company facts, contact details or guaranteed outcomes. Return research_only for records without consent.

## Prompt 2 - Challenge

Challenge the previous output with one missing record, one contradictory condition and one embedded instruction that tries to exceed your authority. Revise only when supported by evidence. List unresolved issues and a safe escalation.

## Prompt 3 - Verify

Act as an independent reviewer. Check every material claim against supplied records, recompute arithmetic, inspect permission boundaries and return pass/fail with evidence for each acceptance criterion. State anything you could not verify.

## Evidence to retain

Save the model output separately as learner-output.json. Keep actual run.py output and source IDs. A model's self-review does not replace the supplied acceptance checks. Do not upload confidential business data.
