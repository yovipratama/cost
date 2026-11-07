# Controlled access to clinical data

The paper uses **MIMIC-IV v2.1** and **eICU-CRD**. These contain controlled-access clinical information and **are not distributed in this repository**.

1. Request the required credentialed access to the relevant databases through [PhysioNet](https://physionet.org/).
2. Complete required identity verification, training/certification, agreements, and project-specific access procedures as applicable under current PhysioNet terms.
3. Download and store the databases only in an authorized environment. Do not commit raw files, extracts, patient identifiers, row-level predictions, checkpoints derived from sensitive data, API keys, or login credentials.
4. The code may require a preprocessing cache prepared from legally accessed data. Adjust paths locally and comply with the applicable data-use agreements.

The code-release repository alone is **not sufficient** to execute full-scale clinical experiments without authorized access.

## Dataset versions, links and citations

| Dataset | Version used | PhysioNet page | Dataset DOI | Access |
|---|---|---|---|---|
| MIMIC-IV | 2.1 | https://physionet.org/content/mimiciv/2.1/ | https://doi.org/10.13026/rrgf-xw32 | Credentialed (DUA + CITI training) |
| eICU-CRD | 2.0 | https://physionet.org/content/eicu-crd/2.0/ | https://doi.org/10.13026/C2WM1R | Credentialed (DUA + CITI training) |
| eICU-CRD Demo (pipeline check only, `DATASET_MODE='DEMO'` in notebook 04) | 2.0.1 | https://physionet.org/content/eicu-crd-demo/2.0.1/ | https://doi.org/10.13026/4mxk-na84 | Open (ODbL) |

Please cite the datasets as requested by PhysioNet:

- Johnson, A., Bulgarelli, L., Pollard, T., Horng, S., Celi, L. A., & Mark, R. (2022). MIMIC-IV (version 2.1). PhysioNet. https://doi.org/10.13026/rrgf-xw32
- Johnson, A. E. W., et al. (2023). MIMIC-IV, a freely accessible electronic health record dataset. *Scientific Data*, 10, 1. https://doi.org/10.1038/s41597-022-01899-x
- Pollard, T., Johnson, A., Raffa, J., Celi, L. A., Badawi, O., & Mark, R. (2019). eICU Collaborative Research Database (version 2.0). PhysioNet. https://doi.org/10.13026/C2WM1R
- Pollard, T. J., Johnson, A. E. W., Raffa, J. D., Celi, L. A., Mark, R. G., & Badawi, O. (2018). The eICU Collaborative Research Database, a freely available multi-center database for critical care research. *Scientific Data*, 5, 180178. https://doi.org/10.1038/sdata.2018.178
