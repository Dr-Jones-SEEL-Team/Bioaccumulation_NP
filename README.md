""" 


For those pointed here by the paper, "Heterogenous biofilm mass-transport model replicates periphery sequestration of antibiotics in Pseudomonas aeruginosa
PAO1 microcolonies" (doi: 10.1073/pnas.2312995120), the data/scripts are in the following locations:

    Figure_1:
        
	Model Solver Script folder: N15 
            Open the python script 'N15-Main Code'. Change parameters as neccesary to run model. Can run script for multiple parameter combination by entering multiple values for a parameter of interest. Ensure all other scripts in the directory are copied over. Results are saved in an exported word document, with directory destination specified through the string-variable "direct_export_path". Cocnentration and parameter values for each run are saved as .csv files. Requires a .txt file with the current run # to be saved in the same directory as the 'N15-Main Code' file. N15 is the equilibrium solver for the Heterogenous Biofilm Model, as opposed to N12, which solves the governing equation dynamically.
        
	Solver results folder: Figure_1
            Parameter and concentration data for each run of simulation used in Phase-space plot contained in the directory.
        
	Script for Figure generation: Figure_1/phase_diagram_figure_generator


    Figure_2:
        
	Model Solver Scripts folder: N12 (Heterogenous Biofilm Model and Heterogenous Porosity Model), N13 (Heterogenous Attachment Site Model), N14 (Homogenous Biofilm Model)
            Open the python script 'N12/3/4-Main Code' corresponding to the model of interest. Change parameters as neccesary to run model. Can run script for multiple parameter combinations by entering multiple values for a parameter of interest. Ensure all other scripts in the directory are copied over. Results are saved in an exported word document, with directory destination specified through the string-variable "direct_export_path". Cocnentration and parameter values for each run are saved as .csv files. Requires a .txt file with the current run # to be saved in the same directory as the 'N12/3/4-Main Code' file.
        
	Solver results: Figure_2
            The model data used in the plots are included in the directory under the labels: "N1X_[Run #]Tsengfit[cirpo/tobra]_[model used]". The first column in the dataset is the time, 2nd is position, third is experimental data, fourth are model fits. The corresponding solver word document output (includes parameter values, underlying plots) is in the sub-directory "Original_solver_results". The underlying model outputs of attached (bound) and mobile (unbound) dimensionless antibiotic concentrations are incldued as .csv files in the sub-directory "Original_solver_results", where the data is in matrix format, with the first column representing position values (thus different rows represent different position) and the first row representing time values (this difference columns represent different time-points). "collateddata" files should be copies of the "N1X_[Run #]Tsengfit[cirpo/tobra]_[model used]" files (making missing N14 collated data files redundant). 
        
	Script for Figure Generation: Figure_2/subplot_collator_figure1
        
	The experimental data used: Figure_2
            The Tseng data extracted from their figure is included in the directory as "tseng_fits_Fig2B_Cyt5tob_incubation" and "tseng_fits_Fig2B_Cy5cipro_incubation". First column has time data, second column is position in microns, third column is Cy5 fluorescence intensity in AU (absorbance units, probably). 


Python (v3.11.4) Packages Installed in Anaconda enviornment for running scripts (not all packages neccesary, but all should be sufficient):

Package                       Version
----------------------------- -----------
aicsimageio                   4.12.1
aicspylibczi                  3.1.2
aiobotocore                   2.5.4
aiohttp                       3.8.5
aioitertools                  0.11.0
aiosignal                     1.3.1
alabaster                     0.7.13
annotated-types               0.5.0
arrow                         1.2.3
asciitree                     0.3.3
asteval                       0.9.31
astroid                       2.15.6
asttokens                     2.2.1
async-timeout                 4.0.3
atomicwrites                  1.4.1
attrs                         23.1.0
autopep8                      2.0.2
Babel                         2.12.1
backcall                      0.2.0
backports.functools-lru-cache 1.6.5
bcrypt                        3.2.2
beautifulsoup4                4.12.2
binaryornot                   0.4.4
bioformats-jar                2020.5.27
black                         23.7.0
bleach                        6.0.0
botocore                      1.31.17
Brotli                        1.0.9
certifi                       2023.7.22
cffi                          1.15.1
chardet                       5.1.0
charset-normalizer            3.2.0
click                         8.1.6
cloudpickle                   2.2.1
colorama                      0.4.6
comm                          0.1.4
contourpy                     1.1.0
cookiecutter                  2.3.0
cryptography                  41.0.2
cycler                        0.11.0
Cython                        3.0.0
dabest                        2023.2.14
dask                          2023.5.0
debugpy                       1.6.8
decorator                     5.1.1
defusedxml                    0.7.1
diff-match-patch              20230430
dill                          0.3.7
distributed                   2023.5.0
docstring-to-markdown         0.12
docutils                      0.20.1
elementpath                   4.1.5
entrypoints                   0.4
executing                     1.2.0
fasteners                     0.19
fastjsonschema                2.18.0
flake8                        6.0.0
fonttools                     4.42.0
frozenlist                    1.4.0
fsspec                        2023.9.2
future                        0.18.3
idna                          3.4
imagecodecs                   2023.9.18
imageio                       2.31.1
imagesize                     1.4.1
importlib-metadata            6.8.0
importlib-resources           6.0.0
inflection                    0.5.1
intervaltree                  3.1.0
ipykernel                     6.25.0
ipython                       8.14.0
ipython-genutils              0.2.0
isort                         5.12.0
jaraco.classes                3.3.0
jedi                          0.18.2
jellyfish                     1.0.0
jgo                           1.0.5
Jinja2                        3.1.2
jmespath                      1.0.1
JPype1                        1.4.1
jsonschema                    4.18.6
jsonschema-specifications     2023.7.1
jupyter_client                8.3.0
jupyter_core                  5.3.1
jupyterlab-pygments           0.2.2
keyring                       24.2.0
kiwisolver                    1.4.4
lazy_loader                   0.3
lazy-object-proxy             1.9.0
lmfit                         1.2.2
locket                        1.0.0
lqrt                          0.3.3
lxml                          4.9.3
markdown-it-py                3.0.0
MarkupSafe                    2.1.3
matplotlib                    3.7.2
matplotlib-inline             0.1.6
mccabe                        0.7.0
mdurl                         0.1.0
mistune                       3.0.0
more-itertools                10.1.0
mpmath                        1.3.0
msgpack                       1.0.6
multidict                     6.0.4
munkres                       1.1.4
mypy-extensions               1.0.0
nbclient                      0.8.0
nbconvert                     7.7.3
nbformat                      5.9.2
nest-asyncio                  1.5.6
networkx                      3.1
numcodecs                     0.11.0
numpy                         1.26.0
numpydoc                      1.5.0
ome-types                     0.4.2
ome-zarr                      0.8.1
packaging                     23.1
pandas                        1.5.3
pandocfilters                 1.5.0
paramiko                      3.3.1
parso                         0.8.3
partd                         1.4.0
pathspec                      0.11.2
patsy                         0.5.3
pexpect                       4.8.0
pickleshare                   0.7.5
Pillow                        10.0.0
pip                           23.2.1
pkgutil_resolve_name          1.3.10
platformdirs                  3.10.0
pluggy                        1.2.0
ply                           3.11
pooch                         1.7.0
prompt-toolkit                3.0.39
psutil                        5.9.5
ptyprocess                    0.7.0
pure-eval                     0.2.2
pycodestyle                   2.10.0
pycparser                     2.21
pydantic                      2.4.0
pydantic_core                 2.10.0
pydocstyle                    6.3.0
pyflakes                      3.0.1
Pygments                      2.15.1
pylint                        2.17.5
pylint-venv                   3.0.2
pyls-spyder                   0.4.0
PyNaCl                        1.5.0
pyparsing                     3.0.9
PyQt5                         5.15.9
PyQt5-sip                     12.12.2
PyQtWebEngine                 5.15.4
PySocks                       1.7.1
python-dateutil               2.8.2
python-docx                   1.0.1
python-lsp-black              1.3.0
python-lsp-jsonrpc            1.0.0
python-lsp-server             1.7.4
python-slugify                8.0.1
pytoolconfig                  1.2.5
pytz                          2023.3
PyWavelets                    1.4.1
pywin32                       304
pywin32-ctypes                0.2.2
PyYAML                        6.0
pyzmq                         25.1.0
QDarkStyle                    3.1
qstylizer                     0.2.2
QtAwesome                     1.2.3
qtconsole                     5.4.3
QtPy                          2.3.1
referencing                   0.30.1
requests                      2.31.0
resource-backed-dask-array    0.1.0
rich                          13.5.1
rope                          1.9.0
rpds-py                       0.9.2
Rtree                         1.0.1
s3fs                          2023.9.2
scikit-image                  0.21.0
scipy                         1.11.1
scyjava                       1.9.1
seaborn                       0.12.2
setuptools                    68.0.0
sip                           6.7.11
six                           1.16.0
snowballstemmer               2.2.0
sortedcontainers              2.4.0
soupsieve                     2.3.2.post1
Sphinx                        7.1.2
sphinxcontrib-applehelp       1.0.4
sphinxcontrib-devhelp         1.0.2
sphinxcontrib-htmlhelp        2.0.1
sphinxcontrib-jsmath          1.0.1
sphinxcontrib-qthelp          1.0.3
sphinxcontrib-serializinghtml 1.1.5
spyder                        5.4.4
spyder-kernels                2.4.4
stack-data                    0.6.2
statsmodels                   0.14.0
sympy                         1.12
tblib                         2.0.0
text-unidecode                1.3
textdistance                  4.5.0
three-merge                   0.1.1
tifffile                      2023.7.18
tinycss2                      1.2.1
toml                          0.10.2
tomli                         2.0.1
tomlkit                       0.12.1
toolz                         0.12.0
tornado                       6.3.2
tqdm                          4.66.1
traitlets                     5.9.0
typing_extensions             4.7.1
tzdata                        2023.3
ujson                         5.7.0
uncertainties                 3.1.7
Unidecode                     1.3.6
urllib3                       1.26.16
watchdog                      3.0.0
wcwidth                       0.2.6
webencodings                  0.5.1
whatthepatch                  1.0.5
wheel                         0.41.0
win-inet-pton                 1.1.0
wrapt                         1.15.0
xarray                        2023.1.0
xmlschema                     2.5.0
xsdata                        23.8
yapf                          0.40.1
yarl                          1.9.2
zarr                          2.16.1
zict                          3.0.0
zipp                          3.16.2

"""
