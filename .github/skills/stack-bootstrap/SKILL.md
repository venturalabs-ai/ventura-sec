---
name: stack-bootstrap
description: Bootstrap the smallest VenturaSec Python structure for the approved defensive analytics MVP using declared stack needs. Use when the repository is ready to move from incubation docs to executable code. Do not use when a functional defensive pipeline already exists or the task is only product scoping.
---

# Stack bootstrap

- Confirm the approved defensive use case and dataset before adding dependencies.
- Add only packages required by the first detection or triage path.
- Separate ingestion features models evaluation tests and synthetic fixtures.
- Keep sensitive operational logs and credentials out of Git.
- Add deterministic baseline tests and evaluation metrics.
- Document threat model dataset provenance and known blind spots.
- Reuse the shared repository CI standard.
