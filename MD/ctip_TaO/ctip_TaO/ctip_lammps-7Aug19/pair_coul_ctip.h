/* ----------------------------------------------------------------------
   LAMMPS - Large-scale Atomic/Molecular Massively Parallel Simulator
   http://lammps.sandia.gov, Sandia National Laboratories
   Steve Plimpton, sjplimp@sandia.gov

   Copyright (2003) Sandia Corporation.  Under the terms of Contract
   DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains
   certain rights in this software.  This software is distributed under
   the GNU General Public License.

   See the README file in the top-level LAMMPS directory.
------------------------------------------------------------------------- */

#ifdef PAIR_CLASS

PairStyle(coul/ctip,PairCoulCtip)

#else

#ifndef LMP_PAIR_COUL_Ctip_H
#define LMP_PAIR_COUL_Ctip_H

#include "pair.h"

namespace LAMMPS_NS {

class PairCoulCtip : public Pair {
 public:
  PairCoulCtip(class LAMMPS *);
  virtual ~PairCoulCtip();
  virtual void compute(int, int);
  void settings(int, char **);
  void coeff(int, char **);
  void init_style();
  double init_one(int, int);
  double memory_usage();
  virtual void *extract(const char *, int &);

 private:
  struct Param {
    double chi, eta, gamma, zeta, zcore, qmin, qmax;
    int ielement;
  };

  int nmax;
  int nelements;                // # of unique elements
  char **elements;              // names of unique elements
  int *elem2param;            // mapping from element triplets to parameters
  int *map;                     // mapping from atom types to elements
  int nparams;                  // # of stored parameter sets
  int maxparam;                 // max # of parameter sets
  double precision;
  Param *params;                // parameter set for an I-J-K interaction

  // Kspace parameters
  int kspacetype;
  double cut_coul, cut_coulsq;
  double *cut_respa;
  double **scale;

  // ctip correction
  double ctip_omega; // penalty to gain/lose electrons

  // Wolf
  double g_wolf, woself, dwoself;

  // Ewald
  double g_ewald;

  // QEq
  double *qeq_x, *qeq_j, *qeq_g, *qeq_z, *qeq_c;
  double *qeq_qmin, *qeq_qmax;

  void allocate();
  virtual void read_file(char *);
  void setup_params();
  double self(Param *, double);
  void coulomb_integral_wolf(double, double, double, double &, double &,
        double &, double &);
  void wolf_sum(double, double, double, double, double, double, double,
		  double, double &, double &);
  void coulomb_integral_ewald(double, double, double, double &, double &,
        double &, double &);
  void ewald_sum(double, double, double, double, double, double, double,
		  double, double &, double &, double);

};

}

#endif
#endif

/* ERROR/WARNING messages:

E: Illegal ... command

Self-explanatory.  Check the input script syntax and compare to the
documentation for the command.  You can use -echo screen as a
command-line option when running LAMMPS to see the offending line.

E: Incorrect args for pair coefficients

Self-explanatory.  Check the input script or data file.

E: Pair style coul/ctip requires atom attribute q

Self-explanatory.

E: Pair style requires a KSpace style

No kspace style is defined.

E: All pair coeffs are not set

All pair coefficients must be set in the data file or by the
pair_coeff command before running a simulation.

E: Cannot open coul/ctip potential file %s

The specified coul/ctip potential file cannot be opened.  Check
that the path and name are correct.

E: Incorrect format in coul/ctip potential file

Incorrect number of words per line in the potential file.

E: Illegal coul/ctip parameter

One or more of the coefficients defined in the potential file is
invalid.

E: Potential file has duplicate entry

The potential file has more than one entry for the same element.

E: Potential file is missing an entry

The potential file does not have a needed entry.

*/
