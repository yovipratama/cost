# Publication source checklist

- [x] Baseline LR/RF/LSTM/Attention LSTM/TCN + Initial COST included.
- [x] Improved COST core architecture, training and ablations included.
- [x] Initial clinical gradient attribution, per-feature pruning, and threshold sweep included from source.
- [x] Gating, trained sparse random control, validation, calibration, statistical tests covered.
- [x] Snapshot prediction reconstruction helper included.
- [x] No notebook outputs or execution counts.
- [x] No clinical dataset, prediction vectors, or model checkpoint in the repository archive.
- [ ] Run against original authorized clinical data and checkpoints if claiming full numerical reproducibility.
- [ ] Verify implementation–manuscript MICE/missingness and cohort issues in `docs/PAPER_CODE_AUDIT.md` before presenting code as *exactly* the method described by the manuscript.
- [ ] Replace local Colab Drive paths and ensure authorized users can configure private data storage.
- [x] Colab account metadata (display name, userId, timestamps) removed from notebook cells; personal Drive folder name replaced by `COST_PROJECT`.
- [x] MIT LICENSE added (code and documentation only, not the clinical datasets).
- [x] Repository published at https://github.com/yovipratama/cost.
- [ ] Replace the manuscript Code Availability placeholder with the verified URL.
