# Frozen numeric metric export

This table exports numeric results from the author's existing thesis experiment files. No source functions, model weights, binaries, private paths or personal identifiers are included.

- `sample_id`: benchmark function and optimization condition; one unique key per case.
- `benchmark_family`, `opt`: dataset family and O0–O3 condition.
- `compile_pass`, `reexec_pass`: 0/1 results; a compiler rejection remains a measured failure (0).
- `edit_similarity`, `codebleu`, its four components, `embedding_similarity`: existing source-reference scores; CodeSage input truncation flags are retained.
- `sk2_r2i_valid`, `ida_r2i_valid`, `sk2_minus_ida_r2i_valid`: adapted R2I within the candidate/IDA context; the difference is candidate minus IDA.
- `sk2_r2i_vs_source`: candidate score in the separate source-reference context, if available.

Empty values mean unavailable, not zero. `valid` in an R2I score column name is part of the original field name, not a Boolean. Output aggregates state the valid n. No ground-truth semantic labels are inferred from compilation results.
