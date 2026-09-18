"""Compact reference implementation of the neutrino-oscillation equations used in the paper."""
from __future__ import annotations
import numpy as np
from scipy.linalg import expm
HBARC_GEV_KM = 5.0677307e18

def rot(i, j, theta, delta=0.0, n=3):
    U = np.eye(n, dtype=complex); c, s = np.cos(theta), np.sin(theta)
    U[i,i]=U[j,j]=c; U[i,j]=s*np.exp(-1j*delta); U[j,i]=-s*np.exp(1j*delta)
    return U

def pmns(theta12, theta13, theta23, delta):
    return rot(1,2,theta23) @ rot(0,2,theta13,delta) @ rot(0,1,theta12)

def mixing_3plus1(theta12,theta13,theta23,delta,theta14=0,theta24=0,theta34=0,delta14=0,delta24=0,delta34=0):
    U=np.eye(4,dtype=complex); U[:3,:3]=pmns(theta12,theta13,theta23,delta)
    U=rot(2,3,theta34,delta34,4)@U; U=rot(1,3,theta24,delta24,4)@U; U=rot(0,3,theta14,delta14,4)@U
    return U

def casas_ibarra_Y(MR,masses_GeV,U3,R=None,v=246.0):
    MR=np.asarray(MR,float); masses_GeV=np.asarray(masses_GeV,float)
    if R is None: R=np.eye(3,dtype=complex)
    return 1j*np.sqrt(2)/v*np.diag(np.sqrt(MR))@R@np.diag(np.sqrt(masses_GeV))@U3.conj().T

def planck_basis():
    mats=[]
    for i in range(3):
        B=np.zeros((3,3),complex); B[i,i]=1; mats.append(B)
    for i,j in ((0,1),(0,2),(1,2)):
        B=np.zeros((3,3),complex); B[i,j]=B[j,i]=1; mats.append(B)
    return mats

def matter_potential_GeV(rho_gcm3=2.8,ye=0.5): return 7.56e-23*rho_gcm3*ye

def hamiltonian(U,masses_eV,E_GeV,rho_gcm3=2.8,ye=0.5,antinu=False):
    m2=(np.asarray(masses_eV)*1e-9)**2
    H=U@np.diag(m2)@U.conj().T/(2*E_GeV)
    V=np.zeros_like(H); V[0,0]=matter_potential_GeV(rho_gcm3,ye)
    if antinu: H=H.conj(); V=-V
    return H+V

def propagate(H,L_km): return expm(-1j*H*(L_km*HBARC_GEV_KM))
def probability(S,alpha,beta): return float(abs(S[beta,alpha])**2)

def asymmetries(U,masses_eV,E_GeV,L_km,rho_gcm3=2.8,ye=0.5):
    H=hamiltonian(U,masses_eV,E_GeV,rho_gcm3,ye,False)
    Hb=hamiltonian(U,masses_eV,E_GeV,rho_gcm3,ye,True)
    S=propagate(H,L_km); Sb=propagate(Hb,L_km)
    AT=probability(S,1,0)-probability(S,0,1)
    ACP=probability(S,1,0)-probability(Sb,1,0)
    return AT,ACP
