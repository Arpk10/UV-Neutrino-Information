"""Transparent numerical reconstructions of the curves shown in the manuscript figures.
The manuscript gives benchmark endpoints/ranges rather than every raw plotting array.
These arrays therefore reproduce the documented trends and scales, not an unreleased
original solver's bit-for-bit output.
"""
import numpy as np
rg_mu=np.logspace(13,np.log10(91.1876),180); rg_x=np.log10(rg_mu); t=(13-rg_x)/(13-np.log10(91.1876))
rg_ee=1e-3*(1+0.51*t); rg_mumu=1e-2*(1+0.51*t); rg_tautau=1e-2*(1+0.51*t)
shift23=-2.6e-3*t; shift13=-1.1e-3*t; shift12=-0.2e-3*t; shiftcp=-0.5e-3*t
imz=np.linspace(-2,2,240); yukawa=0.130+0.012*(np.abs(imz)/2)**1.7; cpinv=-3.5e-6*np.tanh(1.4*imz); masses=[0.05,0.0086,0.050]
eps=np.logspace(-4,4,240); slopes=np.array([1.0,.72,1.25,.92,.58,.82]); norms=1e-8*slopes[:,None]*eps[None,:]
L=np.linspace(0,3000,3001); A3=9e-4*np.sin(L/730)*np.exp(-L/8000); A4=A3-2e-4*(L/3000)**1.1-1e-4*np.sin(2*np.pi*L/23)
sterile_labels=["B1","B2","B3","B4","B5","B6","B7","B8"]; sterile_ratios=np.array([.16,-.42,1.8,4.1,7.5,-12,22,42.5])
MRlog=np.linspace(6,16,120); imz_grid=np.linspace(-5,5,121); MM,ZZ=np.meshgrid(MRlog,imz_grid); logdelta=-7.35+.25*(1-(MM-6)/10)-.03*ZZ**2; edge=5-.55*np.maximum(MM-12,0); logdelta=np.ma.array(logdelta,mask=np.abs(ZZ)>edge)
eps_cp=np.logspace(-2,3,300); dACP=3.2e-7*eps_cp
