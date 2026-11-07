# Reproducibility and execution boundaries

## Source provenance

The eight cleaned notebooks are copied from the previously assembled research-source ZIP; no algorithm rewrite or automatic conversion to invented `src/` modules was performed. Cell outputs are cleared. A prior packaging step substituted the original Google Drive folder label with `COST_PROJECT` to avoid publishing the author's local directory name. **The code is not guaranteed path-portable as shipped.**

## Prerequisites

- A legally obtained MIMIC-IV v2.1 cohort prepared following the paper, and externally a credentialed eICU-CRD cohort.
- Saved `.npz` features/labels, trained checkpoints and aligned patient-level prediction artifacts for some notebooks.
- CUDA GPU only when rerunning training; notebook 08 does not retrain.
- A suitable Colab/PyTorch environment. Dependencies listed in requirements are not the original exact pip lock.

## Expected workflow

1. Run the cohort preparation stages in the original notebook workflow using controlled-access data, preserving the study's patient-level chronological partitioning.
2. Train/evaluate initial and improved COST under original settings.
3. Use saved checkpoint/prediction artifacts for gating controls, significance, calibration and external evaluation.
4. Keep all patient-level arrays and trained checkpoints outside Git history.

## Known portability limitations

- Notebook 02 references `DS_RNN_MIMIC_IV_Mortality_Prediction.ipynb`; that source filename is **not included** in the uploaded material. If this block is required, supply the owned original notebook or change the reference to a verified equivalent with **identical** functionality.
- Notebook 04 contains lookups for old source notebook filenames (for example `COST_Master_AllExperiments_CLEAN.ipynb`); renamed notebook files are not automatically resolved at those paths.
- Some notebooks load original precomputed files, cached patient sets and checkpoints and therefore do not run from an empty project directory.
- The presence of `np.nan_to_num` and `IterativeImputer` in some notebooks warrants a **source-provenance check of their execution order** before asserting the paper's MICE→remaining zero-fill preprocessing exactly matches the saved data used for publication.

## What the static audit does *not* establish

A passing `tools/audit_repository.py` result proves notebook JSON integrity, cleared outputs and a few privacy/packaging conditions. It **does not** prove experimental metric reproduction, exact checkpoint provenance, patient-split equality, or an exact Python environment.
