# Privacy and release check

- No authorized MIMIC-IV or eICU-CRD dataset copies, patient rows, per-patient prediction files, subject identifiers, cached `.npz`, or model checkpoints are included.
- No private credentials or PhysioNet authorization tokens should be included.
- Notebook source text can contain local Drive paths. `COST_PROJECT` is a neutral placeholder; update it privately after downloading.
- Inspect new uploads for accidental notebook outputs or patient-level data before committing.
- A generic source scan cannot prove absence of every secret; authors must verify any externally fetched configuration and notebooks.
