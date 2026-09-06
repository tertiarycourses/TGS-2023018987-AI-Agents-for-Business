# Lab 09 - HR and multi-agent handoffs: prompts

TGS-2023018987 | v1.0 | Synthetic classroom data

## Prompt 1 - Build

Act as a policy-research specialist. Produce a source-cited onboarding checklist for role operations_assistant using only supplied policy records. Return task_id, role, checklist, policy_ids and unresolved_questions. Do not make employment decisions or infer personal characteristics.

## Prompt 2 - Challenge

Act as the access-review specialist. Inspect the handoff and checklist. Verify role scope and policy versions. Return task_id, approved_items, denied_items and evidence. Do not invent new permissions.

## Prompt 3 - Verify

Act as an independent reviewer. Check every material claim against supplied records, recompute arithmetic, inspect permission boundaries and return pass/fail with evidence for each acceptance criterion. State anything you could not verify.

## Evidence to retain

Save the model output separately as learner-output.json. Keep actual run.py output and source IDs. A model's self-review does not replace the supplied acceptance checks. Do not upload confidential business data.
