# COST — Controlled Sparsity for Clinical Time-Series Modeling

Code and analysis notebooks associated with the accepted IEEE Access article **“COST: Controlled Sparsity for Reliable Clinical Time-Series Modeling: A Trade-off Analysis in ICU Mortality Prediction.”**

## Scope
This is a **source-code and protocol release**, organized by scientific experiment rather than editorial revision history. Eight notebooks are provided without executed outputs. No MIMIC-IV/eICU-CRD patient records, per-patient predictions, trained weights, or credentials are distributed.

**Data access:** Both clinical datasets require independent authorization through [PhysioNet](https://physionet.org/). Follow `docs/DATA_ACCESS.md`. Access restrictions do not require distributing patient data.

## Study workflow and notebooks

| Notebook | Research objective | Prerequisites |
|---|---|---|
| `01_cohort_baselines_initial_cost_and_improved_model.ipynb` | Dataset processing, conventional baselines, Initial COST, Improved COST, ablations and statistics | Authorized preprocessed MIMIC cache / raw data as expected by the notebook |
| `02_architecture_matched_gating_training.ipynb` | Architecture-matched gating experiments and independent runs | MIMIC cache and defined model components |
| `03_controlled_gating_isolation.ipynb` | Controlled gating ON/OFF | Uses definitions/runtime state from the relevant Improved COST setup; see notebook preflight |
| `04_external_validation_eicu.ipynb` | Frozen-model external validation | Authorized eICU-CRD files, previously trained frozen checkpoint and MIMIC training preprocessing statistics |
| `05_independently_trained_sparse_control_and_domain_shift.ipynb` | Trained random-mask comparator, domain shift | Authorized clinical files and saved model artifacts |
| `06_experimental_diagnostics_and_validation_audits.ipynb` | Model/metric, FLOPs, artifact provenance checks | Original model artifacts; some optional discovery cells scan a local research folder |
| `07_calibration_temporal_and_gating_analyses.ipynb` | Calibration, 48-hour sensitivity, mask intervention and paired analyses | Saved, aligned predictions/identifiers and optional checkpoints |
| `08_paired_statistical_significance.ipynb` | Patient-paired DeLong/bootstrap, learned vs trained random | Aligned prediction arrays for seeds 42–44; **no training** |

**Execution:** these are complementary experiment notebooks, **not** eight serial one-click stages. See `docs/EXECUTION_GUIDE.md` and `docs/EXPERIMENT_PROTOCOL.md`. To use Colab, copy the notebooks and authorized files into your own Drive, then change the `COST_PROJECT` base path in setup cells. Never commit your Drive's clinical files.

## Core reference parameters

- 48-hour observation window; 31 original temporal and 11 static variables; Improved model reports 93 temporal channels after adding missingness and delta-time features.
- MIMIC-IV chronological splits: 2008–2015 train, 2016–2017 validation, 2018–2019 test. No subject overlap.
- Initial COST: five seeds 42–46. Improved COST: three seeds 42–44.
- Improved COST: AdamW, learning rate 3e-4, weight decay 1e-4, batch 64, up to 120 epochs, patience 15, two-layer bidirectional LSTM hidden size 256, four attention heads, dropout 0.3, fixed gate τ=0.5, snapshot ensemble of five checkpoints.
- Masked dimensions are **attenuated to 10%**, not hard-removed; reported binary latent sparsity is not hardware speedup.

A complete **paper-to-code target checklist** is in `docs/MANUSCRIPT_CODE_MATRIX.md`. `config/manuscript_reference.yaml` is **documentation only**; do not mistake it for a configuration automatically loaded by original research notebooks.

## Honest reproducibility statement

Source notebooks and disclosed configs can be inspected without protected data. Re-execution requires approved access and, for follow-on analyses, the saved checkpoints/prediction artifacts from earlier experiments. Original notebooks include exploratory cells; a historical audit cell that only opened an unavailable old notebook was removed in four instances (see `docs/CHANGE_LOG.md`). **No training, model architecture, loss, or metric computation cell was modified by this packaging step.** Some originally executed preprocessing paths differ between Initial and Improved COST; they are preserved unchanged for scientific provenance (`docs/PREPROCESSING_PROVENANCE.md`). Consequently, this release is **not certified to regenerate every published number from a fresh machine** until authors verify access and run their original assets.

## Integrity and privacy

Run `python tools/audit_repository.py` to check notebook validity, output stripping, and source-reference issues. See `docs/PRIVACY_CHECK.md` before publication. The repository does not grant a license automatically; authors should add an appropriate license after rights review. For citation, use the GitHub repository's real public URL and ideally a fixed release/tag; do not fill a fictional URL in the manuscript.
