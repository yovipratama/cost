# Execution guide (data access required)

1. Obtain approved MIMIC-IV v2.1 and eICU-CRD access from PhysioNet. Data are intentionally excluded.
2. Set up Colab / Python with GPU-enabled PyTorch, and dependencies in `requirements.txt`; individual notebooks may install further modules.
3. Copy notebook source and authorized data to your own drive; adjust `COST_PROJECT` root in setup cells.
4. Use notebook 01 for baselines and main models, notebook 02/03 for matched gating, 05 for independently trained sparse control, 04 for frozen eICU validation. Notebook 07 is downstream calibration and sensitivity; 08 uses saved aligned patient predictions and **does not train**. Notebook 06 audits stored artifacts.
5. *Not sequential by numbering*: some notebooks require preceding runtime variables or saved `.npz`/`.pt` artifacts. The preflight in notebook 03 identifies the exact shared state required. A new Colab runtime cannot bypass those dependencies by changing filenames.
6. Verify sample/subject alignment, 48-h endpoint, cohort size, parameter values, and experiment-specific metrics against the manuscript before declaring result reproduction.

The repository deliberately has no one-click fabricated pipeline that would silently substitute an untested method for the implementation actually run.
