from pathlib import Path
import sys, matplotlib.pyplot as plt
R=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(R/'data')); from figure_data import *
out=R/'figs/generated/figure6.png'; fig,ax=plt.subplots(figsize=(6.7,4.4)); im=ax.pcolormesh(MM,ZZ,logdelta,shading='auto'); fig.colorbar(im,ax=ax,label=r'$\log_{10}|\delta A_T|$'); ax.set(xlabel=r'$\log_{10}(M_{R,3}/\mathrm{GeV})$',ylabel=r'Im$(z_{12})$',title='Constrained scan of $|\delta A_T|$ at $\epsilon=1$'); fig.tight_layout(); fig.savefig(out,dpi=220); plt.close(fig)
