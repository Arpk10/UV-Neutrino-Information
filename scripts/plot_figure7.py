from pathlib import Path
import sys, matplotlib.pyplot as plt
R=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(R/'data')); from figure_data import *
out=R/'figs/generated/figure7.png'; fig,ax=plt.subplots(figsize=(6.7,4.2)); ax.loglog(eps_cp,dACP,label=r'$|\delta A_{CP}|$'); ax.axhline(6e-5,ls='--',label='optimistic scale'); ax.axhline(1.2e-4,ls='--',label='typical scale'); ax.axvline(1,ls=':',label=r'$\epsilon=1$'); ax.set(xlabel=r'naturalness parameter $\epsilon$',ylabel=r'$|\delta A_{CP}|$',title='Planck-induced CP-asymmetry correction'); ax.legend(fontsize=8); fig.tight_layout(); fig.savefig(out,dpi=220); plt.close(fig)
