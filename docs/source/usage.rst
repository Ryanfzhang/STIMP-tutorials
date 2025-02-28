=====
Usage
=====


Pipeline overview
------------

STIMP is a deep learning-based method that accurately imputes and predicts Chl_a in the coastal oceans. The inputs for STIMP include observations of Chl_a from coastal oceans, denoted as  :math:`\mathbf{X}^{ob}`, 
and a spatial graph, :math:`\mathbf{G}`, that contains the geographic coordinates of the observations. STIMP simultaneously outputs a complete Chl_a dataset, 
:math:`\mathbf{X}`, and accurately predicts Chl_a, :math:`\tilde{\mathbf{Y}}`, based on :math:`\mathbf{X}`. STIMP and is formulated as:

.. math:: p(\tilde{\mathbf{Y}}|\mathbf{X}^{ob})=\int_{\mathbf{X}}p_\Phi(\tilde{\mathbf{Y}}|\mathbf{X})p_\theta(\mathbf{X}|\mathbf{X}^{ob})d\mathbf{X}.

.. figure:: figures/architecture.png
   :width: 720px
   :align: center
   :alt: Pipeline

Prepare data
------------
All data used in this work are publicly available through online sources. The chlorophyll-a observation datasets were 8-day averaged Level 3 mapped products from Moderate Resolution Imaging Spectroradiometer (MODIS) Aqua projects with a spatial resolution of 4 km 
`MODIS <https://search.earthdata.nasa.gov/search?q=10.5067/AQUA/MODIS/L3M/CHL/2022>`_. You can select the data with **\*.8D.\*.4km.nc** as filter. 

We also uploaded the datasets on Zenodo at https://doi.org/10.5281/zenodo.14724760. Then, 

.. code-block:: bash

   mv data.zip /path/to/STIMP/
   unzip e data.zip

`Prepare the dataset from the raw data <https://github.com/YangLabHKUST/STIMP/blob/release/tutorials/01-preprocess_chla_data.ipynb>`_ We generate the 4 datasets, including Pearl River Estuary, the Northern of Mexico, Chesapeake Bay and Yangtze River Estuary, following this tutorials. 
The generated datasets are also included in the data.zip

Imputation
------------
The imputation step intends to reconstruct multiple potential complete spatiotemporal Chl_a distributions from partial observations. Due to the collected remote sensing Chl_a data
does not contain ground truth for unobserved data, we can ramdomly select part of observation as imputation target to train the imputation function :math:`p_\theta(\mathbf{X}|\mathbf{X}^{ob})`.

.. code-block:: bash

   python imputation/train_stimp.py --missing_ratio A --area B # :math:`A\in (0, 0.9)


Prediction
------------