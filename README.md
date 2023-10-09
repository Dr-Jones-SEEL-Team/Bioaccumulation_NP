# Bioaccumulation_NP
"""
Project Folder for Finite Difference Mass Transport Models for Bioaccumulation of species in biofilms (project initially started attempting to understand effect of nanoparticle surface charge on transport in biofilms).

For those pointed here by the paper, "", the data/scripts are in the following locations:

- Figure_1:
  - Model Solver Script: Bioaccumulation_NP/N12
    - Open the python script 'N12-Main Code'. Change parameters as neccesary to run model. Can run script for multiple parameter combination by entering multiple values for a parameter of interest. Ensure all other scripts in the directory are copied over. Results are saved in an exported word document, with directory destination specified through the string-variable "direct_export_path". Cocnentration and parameter values for each run are saved as .csv files. Requires a .txt file with the current run # to be saved in the same directory as the 'N12-Main Code' file. 
  - Solver results: Bioaccumulation_NP/Results/Figure_1
    - Parameter and concentration data for each run of simulation used in Phase-space plot contained in the directory.
  - Script for Figure generation: Bioaccumulation_NP/Results/Figure_1/phase_diagram_figure_generator
- Figure_2:   
  - Model Solver Scripts: Bioaccumulation_NP/N12 (Heterogenous Biofilm Model and Heterogenous Porosity Model), Bioaccumulation_NP/N13 (Heterogenous Attachment Site Model), Bioaccumulation_NP/N14 (Homogenous Biofilm Model)
    - Open the python script 'N12/3/4-Main Code' corresponding to the model of interest. Change parameters as neccesary to run model. Can run script for multiple parameter combinations by entering multiple values for a parameter of interest. Ensure all other scripts in the directory are copied over. Results are saved in an exported word document, with directory destination specified through the string-variable "direct_export_path". Cocnentration and parameter values for each run are saved as .csv files. Requires a .txt file with the current run # to be saved in the same directory as the 'N12/3/4-Main Code' file. 
  - Solver results: Bioaccumulation_NP/Results/Figure_2
    - The data used in the plots are included in the directory under the labels: "N1X_[Run #]_Tsengfit_[cirpo/tobra]_[model used]". The first column in the dataset is the time, 2nd is position, third is experimental data, fourth are model fits. The corresponding solver word document output (includes parameter values, underlying plots) is in the sub-directory "Original_solver_results".
  - Script for Figure Generation: Bioaccumulation_NP/Results/Figure_2/subplot_collator_figure1

"""
