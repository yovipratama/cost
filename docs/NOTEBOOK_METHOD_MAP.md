# Notebook map by research methodology

The numbered notebooks are **topic-based**, not a chronological log of peer review. Source code was retained, execution outputs cleared, and display titles updated; underlying experimentation is unchanged.

| Notebook | Research method / scope | Paper relationship |
|---|---|---|
| 01 | Cohort preparation, baselines, Initial COST, Improved COST, component ablations | Sections III–IV; Tables VI–XXIV; notebook contains several phases |
| 02 | Architecture-matched gating ON/OFF training | Controlled-gating isolation (Table XXV) |
| 03 | Gating isolation diagnostic and training support | Controlled-gating implementation |
| 04 | Frozen-model external validation on eICU | External-validation analysis |
| 05 | Independently trained random-mask sparse control and eICU domain-shift audit | Sparse control and external robustness |
| 06 | Diagnostic and validation audits | Supplementary analyses; inspect notebook cells for exact scope |
| 07 | Temporal sensitivity, calibration, frozen gating interventions, ON/OFF analysis | Calibration, observation-window and mechanism analyses |
| 08 | Paired DeLong and patient-level bootstrap from stored predictions | Learned gating versus trained random-mask significance |

**Important:** File numbering is an index, **not** a runnable dependency order. Some experiments require saved predictions or external notebooks/assets. This release does not claim that an end-to-end run was independently validated. Source notebooks may still contain internal historical revision terminology in comments and markdown; those notes are retained as provenance rather than rewritten into potentially misleading claims.
