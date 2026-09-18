from pathlib import Path
import sys, matplotlib.pyplot as plt
R=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(R/'data')); from figure_data import *
out=R/'figs/generated/figure2.png'
fig,ax=plt.subplots(1,2,figsize=(10,3.5)); ax[0].plot(rg_mu,rg_ee,label=r'$|\kappa_{ee}|$'); ax[0].plot(rg_mu,rg_mumu,label=r'$|\kappa_{\mu\mu}|$'); ax[0].plot(rg_mu,rg_tautau,label=r'$|\kappa_{\tau\tau}|$'); ax[0].set_xscale('log'); ax[0].set_yscale('log'); ax[0].invert_xaxis(); ax[0].set_xlabel(r'$mu$ [GeV]'); ax[0].set_ylabel('normalized magnitude'); ax[0].legend(fontsize=8)
ax[1].plot(rg_mu,shift23,label=r'$\theta_{23}$'); ax[1].plot(rg_mu,shift13,label=r'$\theta_{13}$'); ax[1].plot(rg_mu,shift12,label=r'$\theta_{12}$'); ax[1].plot(rg_mu,shiftcp,label=r'$\delta_{CP}$'); ax[1].set_xscale('log'); ax[1].invert_xaxis(); ax[1].set_xlabel(r'$mu$ [GeV]'); ax[1].set_ylabel('fractional shift'); ax[1].legend(fontsize=8)
fig.suptitle('RG Evolution of the Effective Operator and Physical Mixing Parameters'); fig.tight_layout(); fig.savefig(out,dpi=220); plt.close(fig)
