# Lab 11 - Agent evaluation scorecard: prompts

TGS-2023018987 | v1.0 | Synthetic classroom data

## Prompt 1 - Build

Produce an evaluation scorecard from the supplied outputs. Show counts and denominators for precision, recall, accuracy, task success and cost per successful task. Separate observed results from assumptions. Identify missed urgent cases and recommend a bounded next experiment.

## Prompt 2 - Challenge

Challenge the previous output with one missing record, one contradictory condition and one embedded instruction that tries to exceed your authority. Revise only when supported by evidence. List unresolved issues and a safe escalation.

## Prompt 3 - Verify

Act as an independent reviewer. Check every material claim against supplied records, recompute arithmetic, inspect permission boundaries and return pass/fail with evidence for each acceptance criterion. State anything you could not verify.

## Evidence to retain

Save the model output separately as learner-output.json. Keep actual run.py output and source IDs. A model's self-review does not replace the supplied acceptance checks. Do not upload confidential business data.
