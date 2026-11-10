# Provenance issues requiring an honest paper–code interpretation

This file records observations about original code, **not** instructions to redesign the accepted model.

1. In original Improved COST `preprocess_v2`, lab NaNs are converted to zeros before an `IterativeImputer` fit. The imputer therefore cannot impute NaNs already removed. The manuscript's generalized statement “MICE then zero-fill” does not describe this path exactly.
2. Missingness features computed after this fill may not encode original lab missingness. Do not assert that all 31 channels preserve original observation masks unless proven from the original data pipeline.
3. Original source selected first ICU stay per `hadm_id` in at least one cohort routine. This does not itself demonstrate one unique stay per `subject_id`. A downstream patient-level deduplication/overlap check would be needed to substantiate that manuscript claim.
4. The original notebooks mix self-contained and stateful code and may reference existing research cache/checkpoints; no runtime validation is asserted.

**Policy:** We intentionally retain original executable source cells rather than changing algorithms, preprocessing, or cohorts to manufacture agreement with manuscript prose. Dataset access restrictions mean we cannot independently recompute all reported outcomes from this release alone. If documentation or paper corrections are necessary, they should describe the original executed method.
