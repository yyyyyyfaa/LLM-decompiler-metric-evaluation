# Optional presentation figures; run after python scripts/analyze.py.
if (!requireNamespace("ggplot2", quietly=TRUE)) stop("Install ggplot2 first")
library(ggplot2)
dir.create("figures", showWarnings=FALSE)
x <- read.csv("data/humaneval_mbpp_metrics.csv")
rates <- data.frame(check=c("Compilation", "Re-execution"),
                    rate=c(mean(x$compile_pass),mean(x$reexec_pass)))
p <- ggplot(rates,aes(check,rate))+geom_col(fill="#24546D",width=.55)+
  geom_text(aes(label=sprintf("%.2f%%",100*rate)),vjust=-.6,size=5)+
  scale_y_continuous(limits=c(0,1),labels=function(v)paste0(100*v,"%"))+
  theme_minimal(base_size=12)+labs(title="Compilation does not guarantee passing tests",
    subtitle="HumanEval + MBPP | 400 frozen thesis outputs",x=NULL,y="Success rate",
    caption="341 compiled; 258 passed all supplied tests. No new model inference.")
ggsave("figures/compilation_vs_execution.png",p,width=8,height=5,dpi=160)
