from pyscf.scf import rohf
import numpy as np

class GVB(rohf.ROHF):

    def __init__(self, _hf):
        self._hf = _hf
        
        self.npair = 0
        self.nmo = _hf.mo_coeff.shape[-1]
        if hasattr(_hf, 'nelec'):
            self.nelec = _hf.nelec
            na, nb = self.nelec
        elif hasattr(_hf.mol, 'nelectron'):
            nocc = _hf.mol.nelectron // 2
            self.nelec = nocc, nocc
            na = nocc
            nb = nocc
        else:
            raise AttributeError('_hf has no nelec/nelectron')
        self.nopen = na - nb        
        self.ci = None

    def build(self):
        na, nb = self.nelec
        ncore = nb - self.npair
        if self.ci is None:
            self.ci = init_ci(self.npair)
        mo_occ, mo_occ2 = get_occ(self.ci, ncore, self.nopen, self.nmo)
        print(mo_occ)

def init_ci(npair):
    ci = np.ones(npair, dtype=float)*0.9
    return ci

def get_occ(ci, ncore, nopen, nmo):
    npair = len(ci)
    mo_occ = np.zeros(nmo)
    mo_occ[:ncore] = 1.0
    mo_occ[ncore:ncore+npair] = ci**2  
    mo_occ[ncore+npair:ncore+npair+nopen] = 0.5
    iupper = ncore+npair+nopen+npair
    mo_occ[iupper-npair:iupper] = 1-np.flip(ci)**2
    return mo_occ, 0     
