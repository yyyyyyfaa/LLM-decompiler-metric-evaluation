# Metric Records

`humaneval_mbpp_metrics.csv` contains 400 records from the thesis experiments. Each row identifies one function and optimisation condition. Blank fields indicate unavailable measurements; measured failures retain a score of zero.

| Field | Meaning |
|---|---|
| `sample_id` | Unique function and optimisation identifier |
| `benchmark_family`, `opt` | Benchmark and O0–O3 optimisation level |
| `compile_pass`, `reexec_pass` | Compilation and test results, encoded as 0 or 1 |
| `edit_similarity` | Source-reference edit similarity |
| `codebleu` | Combined CodeBLEU score |
| `codebleu_ngram`, `codebleu_weighted_ngram`, `codebleu_syntax`, `codebleu_dataflow` | CodeBLEU components |
| `embedding_similarity` | CodeSage similarity |
| `codesage_reference_truncated`, `codesage_candidate_truncated` | CodeSage input truncation flags |
| `sk2_r2i_valid`, `ida_r2i_valid` | Adapted R2I scores in the output/IDA comparison |
| `sk2_minus_ida_r2i_valid` | Output score minus IDA score |
| `sk2_r2i_vs_source`, `source_r2i`, `sk2_minus_source_r2i` | Scores and difference in the separate source comparison |

Each summary reports its valid sample count. Correlations use records valid for both metrics, with sample counts exported to a separate matrix. The R2I columns named `valid` contain scores, not Boolean flags.

The export contains numerical results and benchmark identifiers. The original experiment-file hashes are in `provenance.json`.
