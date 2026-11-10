# Paper-to-code audit (transparent release note)

This repository follows the **reported experiment scope** of `IEEE_ACCESS_FINAL_1043.docx`. Paper-defined parameters are listed under `config/paper_protocol.yaml`; see each notebook for the historical *actual* values applied when the experiments ran.

## Verified presence of implementations

- Initial COST and conventional baseline model classes, training and metrics: notebook 01.
- Initial COST feature attribution and pruning analysis and threshold sweep: notebook 01, newly sourced from the original `DS_RNN_MIMIC_IV_Mortality_Prediction` notebook.
- Improved COST model, optimizer/loss/configuration, snapshot ensemble, component ablation: notebook 02; corresponding original code appears in `DS_RNN_v2_Improvements (2)(1)`.
- Gating OFF/ON controls, trained random mask and statistical evaluation: notebooks 03, 04, 05, 07.
- Independent frozen-model eICU evaluation: notebook 06.
- Main improved checkpoint-based prediction reconstruction: notebook 08.

## Important provenance caveats (do not silently rewrite old code)

1. **Improved preprocessing**: an upstream `np.nan_to_num(..., nan=0)` call can precede the MICE imputer in a historical Improved function. Thus this implementation may not perform the same missing-lab estimation described by Table VIII. Missingness-mask definitions may be affected. A paper-faithful rewrite would be a **new** implementation and should not be represented as the original code underlying the published checkpoint.
2. **Cohort uniqueness**: one source contains `groupby('hadm_id').first()` and the manuscript describes one stay per `subject_id`. Without original subject-level audit output, unique-patient/zero-overlap claims cannot be independently verified from the uploaded source alone.
3. **Temporal split**: reconstructed admission years derived from MIMIC anchor metadata are not necessarily exact original calendar years; the implementation must be read on its own terms.
4. **Initial gradient attribution and threshold sweep**: these routines originate in the authentic Initial notebook; the originally supplied old sweep visualization labelled mask-sparsity as a FLOPs-reduction axis. That misleading visualization is not included here. The actual sweep routine is retained for Table XX and uses reported tau values.
5. **External validation**: code depends on authorized eICU raw data and stored model weights; those cannot be verified in this source-only package.
6. **New notebook 08** reads existing checkpoints and reconstructs predictions. Its outputs are absent from this source-only release.

**Release positioning**: this is a **source-code disclosure**, not a claim of exact end-to-end reproductions. No original training data, pretrained weights or numeric results are included.
