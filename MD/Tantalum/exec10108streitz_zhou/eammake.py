#! /usr/bin/env python

import math

from atsim.potentials import EAMPotential, Potential
from atsim.potentials.eam_tabulation import SetFL_EAMTabulation


def makeFunc(a, b, r_e, c):
    # Creates functions of the form used for density function.
    # Functional form also forms components of pair potential.
    def func(r):
        return (a * math.exp(-b*(r/r_e - 1)))/(1+(r/r_e - c)**20.0)
    return func


def makePairPotAA(A, gamma, r_e, kappa,
                  B, omega, lamda):
    # Function factory that returns functions parameterised for homogeneous pair interactions
    f1 = makeFunc(A, gamma, r_e, kappa)
    f2 = makeFunc(B, omega, r_e, lamda)

    def func(r):
        return f1(r) - f2(r)
    return func


def makePairPotAB(dens_a, phi_aa, dens_b, phi_bb):
    # Function factory that returns functions parameterised for heterogeneous pair interactions
    def func(r):
        return 0.5 * ((dens_b(r)/dens_a(r) * phi_aa(r)) + (dens_a(r)/dens_b(r) * phi_bb(r)))
    return func


def makeEmbed(rho_e, rho_s, F_ni, F_i, F_e, eta):
    # Function factory returning parameterised embedding function.
    rho_n = 0.85*rho_e
    rho_0 = 10000000.0*rho_e

    def e1(rho):
        return sum([F_ni[i] * (rho/rho_n - 1)**float(i) for i in range(4)])

    def e2(rho):
        return sum([F_i[i] * (rho/rho_e - 1)**float(i) for i in range(4)])

    def e3(rho):
        return F_e * (1.0 - eta*math.log(rho/rho_s)) * (rho/rho_s)**eta

    def func(rho):
        if rho < rho_n:
            return e1(rho)
        elif rho_n <= rho < rho_0:
            return e2(rho)
        return 0.00
    return func


def makePotentialObjects():
    # Potential parameters
    r_eO = 3.668766
    f_eO = 1.888839
    gamma_O = 5.931086
    omega_O = 4.104248
    a_O = 0.415946
    b_O = 0.706278
    kappa_O = 0.240129
    lambda_O = 0.754356

    rho_e_O = 74.860644
    rho_s_O = 100
    F_ni_O = [-1.576011, -1.757687, 1.212659, 1.394335]
    F_i_O = [-1.866573, -1.806293, 0.871914, 0.0000]
    eta_O = 0 # Does not matter
    F_e_O = -2

    # Define the density functions
    dens_O = makeFunc(f_eO, omega_O, r_eO, lambda_O)

    # Finally, define embedding functions for each species
    embed_O = makeEmbed(rho_e_O, rho_s_O, F_ni_O, F_i_O, F_e_O, eta_O)

    # Wrap them in EAMPotential objects
    eam_potentials = [
        EAMPotential("O", 8, 15.99, embed_O, dens_O)]

    # Define pair functions
    pair_OO = makePairPotAA(a_O, gamma_O, r_eO, kappa_O,
                              b_O, omega_O, lambda_O)


    # Wrap them in Potential objects
    pair_potentials = [
        Potential('O', 'O', pair_OO)]

    return eam_potentials, pair_potentials


def main():
    eam_potentials, pair_potentials = makePotentialObjects()

    # Perform tabulation
    # Make tabulation
    cutoff_rho = 100.0
    nrho = 2000

    cutoff = 6.0
    nr = 2000

    tabulation = SetFL_EAMTabulation(
        pair_potentials,
        eam_potentials,
        cutoff, nr,
        cutoff_rho, nrho
    )

    with open("Zhou_OO.eam.alloy", 'w') as outfile:
        tabulation.write(outfile)


if __name__ == '__main__':
    main()