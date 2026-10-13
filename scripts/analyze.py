"""Re-analyse exported original metric records; no inference/scoring is rerun."""
from pathlib import Path
import json
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
out = ROOT / 'results'
out.mkdir(exist_ok=True)
df = pd.read_csv(ROOT / 'data/humaneval_mbpp_metrics.csv')
assert len(df) == 400 and df.sample_id.is_unique
assert set(df.opt) == {'O0','O1','O2','O3'}
assert df[['compile_pass','reexec_pass']].isin([0,1]).all().all()
assert (df.reexec_pass <= df.compile_pass).all()
metrics = ['compile_pass','reexec_pass','edit_similarity','codebleu',
 'codebleu_ngram','codebleu_weighted_ngram','codebleu_syntax','codebleu_dataflow',
 'embedding_similarity','sk2_r2i_valid']
summary = df[metrics].agg(['count','mean','median','std']).T
summary.to_csv(out/'metric_summary.csv',index_label='metric')
df.groupby('opt')[['compile_pass','reexec_pass']].agg(['count','mean']).to_csv(out/'by_optimization.csv')
# Pairwise complete observations; rank within each pair, so missingness is correct.
corr = pd.DataFrame(index=metrics,columns=metrics,dtype=float)
counts = corr.copy()
for a in metrics:
    for b in metrics:
        pair = df[[a,b]].dropna() if a != b else df[[a]].dropna()
        counts.loc[a,b] = len(pair)
        corr.loc[a,b] = pair.iloc[:,0].rank().corr(pair.iloc[:,-1].rank())
corr.to_csv(out/'spearman.csv',index_label='metric')
counts.astype(int).to_csv(out/'spearman_pair_counts.csv',index_label='metric')
compiled = int(df.compile_pass.sum()); passed = int(df.reexec_pass.sum())
lines = ['# Recomputed results','',
 f'- Original metric records: {len(df)}.',
 f'- Compilation: {compiled}/{len(df)} ({compiled/len(df):.2%}).',
 f'- Re-execution: {passed}/{len(df)} ({passed/len(df):.2%}).',
 f'- Compiled but failed tests: {compiled-passed}.','',
 '| Metric | Valid n | Mean | Median |','|---|---:|---:|---:|']
for name,row in summary.iterrows():
    lines.append(f'| {name} | {int(row["count"])} | {row["mean"]:.3f} | {row["median"]:.3f} |')
lines += ['', 'The CSV correlations include a separate matrix of pairwise sample sizes. A score of zero is retained; a missing value is excluded only from the affected comparison.',
 '', 'These are re-aggregations of frozen thesis metrics, not a fresh model run. AUC figures in the project README are reported from the thesis and are not recomputed here because finalized case-level labels are not bundled.']
(out/'REPORT.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
(out/'environment.json').write_text(json.dumps({'pandas':pd.__version__},indent=2)+'\n')
print('\n'.join(lines[2:6]))
