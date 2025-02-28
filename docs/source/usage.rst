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

Imputation
------------

Prediction
------------