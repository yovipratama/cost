# Experimental protocol as reported in the paper

**Reference**: IEEE_ACCESS_FINAL_1043.docx, Methods Tables VI–XIII and Results. The values below are an indexing guide, **not** a claim that every notebook cell has been validated to implement them identically.

| Setting | Paper value | Corresponding notebook(s) |
|---|---|---|
| Cohort | MIMIC-IV v2.1, HF ICD-10 I50 / ICD-9 428; adult; ICU stay >24h; first eligible ICU stay | 01, 02 |
| Observation / label | 48 hourly bins; in-hospital mortality | 01, 02 |
| Features | 31 temporal measures + 11 static; improved input values/mask/elapsed-time = 93 temporal dimensions | 01, 02 |
| Availability | ≥6 vital and ≥2 laboratory observations in 48h before imputation | 01, 02 |
| Split | Train 2008–2015, val 2016–2017, test 2018–2019; patient-exclusive | 01, 02 |
| Preprocess | Vital forward-fill ≤6h; MICE lab imputation, remaining zero-fill; fit normalization on train | 01, 02 |
| Initial COST | Adam, CosineAnnealingLR, weighted BCE, weighted sampler, seeds 42–46 | 01 |
| Improved COST | AdamW 3e-4, decay 1e-4, batch 64, OneCycleLR 10% warmup, 120 max epochs, patience 15 | 02 |
| Improved architecture | 2-layer bidirectional LSTM, hidden 256; 4-head attention dim 128; salience hidden 128 | 02 |
| Improved regularization | Dropout .3; stochastic depth .1; λ=5e-4; focal γ=2, α=.75; smoothing .05; R-Drop α=4 | 02 |
| Gating | τ=.5 with STE; masked dimensions multiplied by .1, not deleted | 02, 03, 05 |
| Runs / snapshots | Seeds 42,43,44; five snapshots per ensemble | 02 |
| Evaluation | AUROC, AUPRC, Brier, Sens@90% spec, runtime, params, FLOPs, memory | 01–07 |
| Additional inference | Paired DeLong; patient-level stratified paired bootstrap on stored predictions | 08 |
| External | Frozen model + train-derived normalization; no training on eICU | 04 |

**Important:** Verify the exact order of zero-fill and MICE in the notebook that built the published tensors, particularly if `np.nan_to_num` appears upstream of `IterativeImputer`. Avoid changing the published computation or rerunning experiments merely to match prose.
