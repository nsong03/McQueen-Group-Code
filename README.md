# McQueen-Group-Code
A key problem in transmon qubit formation is their usable lifetime. 'Noise' effects from fluctuating external EM fields, disturbances from the sapphire substrate commonly used in transmon circuits, and the oxide growth on the current record-holders (Tantalum and Niobium) are the chief culprits that limit transmon usefulness at the moment. This work focuses on the last factor of the oxide layer. The presence of an oxide layer may be limiting transmon performance due to the presence of unmatched spin pairs, ireggularities in the multi-layered oxides that form, or some other factors. 
This repository has my work with the McQueen group for the 2023 PARADIM summer REU program. The main results can be separated into two parts.
1. Developing a predictive model for oxidation properties based off of the Materials Project and SuperCon datasets.
These results include the prediction of formation energies for ~170k entries in datasets that are realized and unrealized, the melting points of these materials with a model from ASU's Hong group, and the main result of an expanded oxide metric based off of a previous REU student's work (1).
This expanded metric used the weighted formation energies of a material's input and output state to approximate the likelihood of said material to form an oxide.
Overall, three metrics of importance have emerged. The oxidation metric of the material, the melting point, and the critical temperature. Each of these are either known or predicted for a subset of the datapoints used here, and a full dataset csv can be provided on request (It was too large to publish on github, but running the code here should reproduce results).
2. An attempt to create a molecular dynamics simulation of Tantalum oxidation. I was not able to successfully perform these simulations, but for future work some references are listed here.
a. YS Lin's work on a Tantalum PINN potential, used for amorphous oxide simulation.  https://arxiv.org/abs/2101.06540
b. K. Sasikumar's work on a CTIP potential for Tantalum oxides https://www.osti.gov/servlets/purl/1372401 . 
Attempts to recreate both works are in the MD folder in this code, along with references I relied on in the Papers folder. These attempts, thus far, have not been successful as the oxygen atoms disobey logic.


(1). Carson Koppel, 'Machine-guided Design of Oxidation Resistant Superconductors for Quantum Information Applications'
