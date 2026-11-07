# Preprocessing provenance — important

Paper Table VIII describes training-set MICE laboratory imputation followed by final zero fill. The notebook sources contain **different actual implementations** that must not be silently harmonized after publication:

- Notebook 01, `preprocess_pipeline` (Initial COST): fit `IterativeImputer` on laboratory values containing NaNs (with all-NaN handling). This is consistent with actual multivariate imputation.
- Notebook 01, `preprocess_v2` (Improved COST), and corresponding copies in notebook 02 and notebook 05: run `np.nan_to_num(lab_train, nan=0.0)` **before** `IterativeImputer.fit`. The imputer cannot identify those zero-filled values as missing using its default missing-values setting. This is a substantive difference from literal MICE imputation of missing values.

Both source paths are preserved exactly. **Do not claim that Improved COST performed conventional MICE on original missing laboratory values solely from the notebook code.** The paper's Table VIII wording and the exact original run should be reconciled by the authors from checkpoint/preprocessing artifacts. Do not fix this by silently modifying code (which would create a different experiment).

The public repository cannot, on its own, establish which preprocessing checkpoint produced each published result. This limitation is explicit to prevent false reproducibility claims.
