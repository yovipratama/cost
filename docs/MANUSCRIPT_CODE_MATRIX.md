# Manuscript (IEEE_ACCESS_FINAL_1043) ↔ code verification matrix

| Manuscript expectation | Target notebook/function | State |
|---|---|---|
| Heart-failure ICD I50*/428*, adult ≥18, LOS >24h, 48h first ICU stay | Main data preparation in notebook 01 and externally generated cohort cache | Partial: cache construction source is not wholly self-contained |
| Cohort counts 14,707 (2,024 deaths), chronological split 2008–2019, zero subject overlap | notebook 01, notebook 07 audit | Defined, requires controlled data to confirm |
| Initial 48×31 temporal, 11 static | notebook 01 | Source present |
| Improved 48×93 with mask/delta | `preprocess_v2` in notebook 01, 02, 05/07 | Source present; preprocessing discrepancy documented |
| Initial COST 5 seeds, Adam/Weighted BCE/CosineAnnealingLR | notebook 01 | Source present |
| Improved COST 3 seeds; hyperparams Table XI | notebook 01 + notebook 02 | Source present, compare exact run flags |
| Gating residual attenuation at τ=.5; mask sparsity definition | notebooks 01/02/03/07 | Source present; interpretation separate from FLOPs |
| Gating ON vs OFF 3 seed comparisons | notebook 03/07 | Source present, depends on stored run artifacts |
| Independently trained random-mask control | notebook 05 | Source present |
| Per-seed paired DeLong + patient bootstrap p=.224 | notebook 08 | Source present; depends on saved, aligned patient predictions |
| Platt calibration, ECE/Brier, 48h early-death sensitivity | notebook 07 | Source present, depends on original artifacts |
| eICU external frozen evaluation | notebook 04/05 | Source present, requires model and authorized eICU data |
| Source-only release is executable end-to-end | Across repo | **Not certified**, requires original data, artifacts, and independent verification |
