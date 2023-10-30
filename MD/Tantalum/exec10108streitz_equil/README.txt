This is a directory with the necessary files to create a Tantalum oxidation simulation.
Order of files to be run:
maketalayer.in -> Creates Tantalum substrate, up to user to decide dimensions. Creates tantalum_20208.data for example.
setup.in -> Adds O2 molecules in room temperature / approx atmospheric density, creates TaOxidation_init.data
simulate.in -> Runs files.
NAMING SCHEME:
Initial input for simulate.in is TaOxidation_init.data. For readability in future, should add which runs are being performed to this section.
so inputs would go TaOxidation_0_1000.data, then TaOxidation_1000_10000.data, etc.
