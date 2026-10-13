# Evaluating Metrics for LLM-based Decompilers

My bachelor's thesis at LMU Munich examined how well automatic metrics reflect errors in code recovered by an LLM-based decompiler. I evaluated SK²Decompile, compared its outputs with source code and IDA pseudocode, and analysed the relationship between automatic scores and manual findings.

## Main findings

Of 400 HumanEval and MBPP outputs, **341 compiled and 258 passed all supplied tests**. The remaining 83 compilable outputs failed at least one test.

![Compilation and test results](figures/compilation_vs_execution.png)

Re-execution separated the manually reviewed groups more clearly than compilation: AUC was 0.920 versus 0.634 on 48 labelled cases. Source-similarity metrics performed differently across datasets. Readability also depended on the reference: 208 of 362 cases changed the direction of their score difference when the reference changed from IDA to source code.

These findings led me to examine which code properties each metric measures, how closely the metrics agree, and which errors remain in highly scored outputs. The manual analysis also covered floating-point calculations and boundary conditions.

## Study

| Dataset | Evaluation cases | Available outputs | Evaluation |
|---|---:|---:|---|
| HumanEval and MBPP | 400 | 400 | Compilation, test execution and source comparison |
| GitHub2025 | 200 | 200 | Function-name recovery |
| DecBench | 250 | 231 | Real-project source and binary comparison |

The study covered 850 cases and 831 available outputs. HumanEval/MBPP and GitHub2025 included matched functions compiled at O0–O3. The manual samples contained 50 HumanEval/MBPP functions and 100 DecBench cases, classified using the C0–C14 decompilation taxonomy.

I used AUC to compare scores against manual semantic labels and Spearman correlation to compare metric rankings. Valid sample counts were retained for each analysis. Compilation failures, missing inputs and extraction failures were recorded separately.

## Run the analysis

The repository includes 400 HumanEval/MBPP metric records from the thesis experiments. The Python script produces score summaries, results by optimisation level and pairwise Spearman correlations.

```sh
python -m pip install -r requirements.txt
python scripts/analyze.py
```

The compilation and test counts above are reproduced from these records. AUC and reference-comparison findings are reported from the thesis.

- [Results](results/REPORT.md)
- [Metric records and field definitions](data/README.md)
- [Analysis code](scripts/analyze.py)

To redraw the figure, install R and ggplot2, then run `Rscript --vanilla scripts/plot.R`.

## References

- Yifan Yang. *Evaluating and Enhancing Metrics for LLM-based Decompilers*. Bachelor's thesis, LMU Munich, 2026. Supervisor: Johannes Kinder; co-supervisor: Yunru Wang.
- SK²Decompile, the evaluated two-stage decompiler.

The numerical export and its source-file hashes are recorded in `provenance.json`.
