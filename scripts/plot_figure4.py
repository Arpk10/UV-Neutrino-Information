from pathlib import Path
import sys, matplotlib.pyplot as plt
R=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(R/'data')); from figure_data import *
out=R/'figs/generated/figure4.png'; fig,ax=plt.subplots(figsize=(7,4.2)); labels=[r'$B_{ee}$',r'$B_{\mu\mu}$',r'$B_{\tau\tau}$',r'$B_{e\mu}$',r'$B_{e\tau}$',r'$B_{\mu\tau}$']
for y,l in zip(norms,labels): ax.loglog(eps,y,label=l)
ax.axvline(1,ls='--',lw=1); ax.set(xlabel=r'naturalness parameter $\epsilon$',ylabel=r'$|\delta A_T|$',title='Planck-suppressed response'); ax.legend(fontsize=8,ncol=2); fig.tight_layout(); fig.savefig(out,dpi=220); plt.close(fig)
