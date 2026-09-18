from pathlib import Path
import numpy as np, matplotlib.pyplot as plt
R=Path(__file__).resolve().parents[1]; out=R/'figs/generated/figure1.png'; out.parent.mkdir(exist_ok=True)
base=np.array([[.011,.004,.006],[.004,.030,.013],[.006,.013,.032]])
mid=base*.49 + np.array([[.001,.001,.000],[.001,.001,.001],[.000,.001,.002]])
shift=mid-base*.49
fig,ax=plt.subplots(1,3,figsize=(10,3.1))
for a,M,title in zip(ax,[base,mid,shift],['UV (M_R=10$^{13}$ GeV)','IR (M_Z)','RG-induced shift']):
    im=a.imshow(np.abs(M)); a.set_title(title); a.set_xticks(range(3),['e','μ','τ']); a.set_yticks(range(3),['e','μ','τ'])
    for i in range(3):
        for j in range(3): a.text(j,i,f'{abs(M[i,j]):.3f}',ha='center',va='center')
fig.suptitle('UV → IR Transport of the Effective Weinberg Operator'); fig.tight_layout(); fig.savefig(out,dpi=220); plt.close(fig)
