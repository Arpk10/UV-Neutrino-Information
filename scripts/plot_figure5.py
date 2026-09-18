from pathlib import Path
import sys, matplotlib.pyplot as plt
R=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(R/'data')); from figure_data import *
out=R/'figs/generated/figure5.png'; fig,ax=plt.subplots(1,2,figsize=(10,3.5)); ax[0].plot(L,A3,label='3-flavor'); ax[0].plot(L,A4,label='3+1 benchmark'); ax[0].set(xlabel='baseline [km]',ylabel=r'$A_T$',title='Baseline dependence'); ax[0].legend(fontsize=8); ax[1].bar(range(8),sterile_ratios); ax[1].axhline(0,lw=1); ax[1].set_xticks(range(8),sterile_labels); ax[1].set(xlabel='sterile benchmark',ylabel=r'$\delta A_T^{(4f)}/\delta A_T^{(3f)}$',title='Finite benchmark response'); fig.suptitle('Sterile-Neutrino Effects on the T-Asymmetry'); fig.tight_layout(); fig.savefig(out,dpi=220); plt.close(fig)
