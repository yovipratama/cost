# Release audit

This release is a best-effort packaging of research source notebooks, **not a claim of certified end-to-end replication**.

**Resolved:** Notebook filenames and README follow methodology. Historical diagnostic cells relying on absent legacy notebooks were removed from two notebooks (4 cells total). Code and evaluation algorithms were not edited.

**Known limitations:** upstream cohort-building data/cache and saved checkpoints are restricted/external; some notebooks rely on named saved predictions. The preprocessing in `preprocess_v2` zero-fills lab NaNs prior to `IterativeImputer.fit`; see PREPROCESSING_PROVENANCE.

**Disclosure:** Do not conceal a mismatch between manuscript wording and source implementation. Do not assert full execution from scratch without appropriate clinical data and original artifacts.
