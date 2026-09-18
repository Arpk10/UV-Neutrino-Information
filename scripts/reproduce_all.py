from pathlib import Path
import subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
for i in range(1,8): subprocess.run([sys.executable,str(ROOT/'scripts'/f'plot_figure{i}.py')],cwd=ROOT,check=True)
print('Generated figs/generated/figure1.png ... figure7.png')
