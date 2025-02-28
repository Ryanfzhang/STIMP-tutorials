=====
Usage
=====


Pipeline overview
------------

STIMP is a deep learning-based method that accurately imputes and predicts Chl\_a in the coastal oceans. The inputs for STIMP include observations of Chl\_a from coastal oceans, denoted as  $\bfX^{ob}$, and a spatial graph, $\bfG$, that contains the geographic coordinates of the observations. STIMP simultaneously outputs a complete Chl\_a dataset, $\bfX$, and accurately predicts Chl\_a, $\Tilde{\bfY}$, based on $\bfX$. STIMP and is formulated as:

:math:`\LaTeX`
   p(\tilde{\mathbf{Y}}|\mathbf{X}^{ob})=\int_{\mathbf{X}}p_\Phi(\tilde{\mathbf{Y}}|\mathbf{X})p_\theta(\mathbf{X}|\mathbf{X}^{ob})d\mathbf{X}.

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