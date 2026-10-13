# Metric Analysis

- Original metric records: 400.
- Compilation: 341/400 (85.25%).
- Re-execution: 258/400 (64.50%).
- Compiled but failed tests: 83.

| Metric | Valid n | Mean | Median |
|---|---:|---:|---:|
| compile_pass | 400 | 0.853 | 1.000 |
| reexec_pass | 400 | 0.645 | 1.000 |
| edit_similarity | 400 | 0.590 | 0.581 |
| codebleu | 400 | 0.440 | 0.433 |
| codebleu_ngram | 400 | 0.253 | 0.234 |
| codebleu_weighted_ngram | 400 | 0.276 | 0.266 |
| codebleu_syntax | 400 | 0.612 | 0.625 |
| codebleu_dataflow | 400 | 0.622 | 0.609 |
| embedding_similarity | 400 | 0.610 | 0.622 |
| sk2_r2i_valid | 362 | 0.881 | 0.901 |

The CSV correlations include a separate matrix of pairwise sample sizes. A score of zero is retained; a missing value is excluded only from the affected comparison.

The analysis uses the saved thesis metric records. Manual-label AUC results are reported separately in the project README.
