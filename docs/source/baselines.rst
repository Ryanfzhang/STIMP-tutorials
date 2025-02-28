=====
Train baselines 
=====

Imputation Methods
----------------

We provide the script for training the baselines, including ``DINEOF`` :cite:`alvera2007multivariate,ma2021two`, ``CSDI`` :cite:`tashiro2021csdi`, ``ImputeFormter`` :cite:`nie2024imputeformer`, ``Inpainter`` :cite:`yun2023imputation`,
``Lin-itp``, ``MaskedAE`` :cite:`he2022masked`, ``Slide window`` and ``TRMF`` :cite:`yu2016temporal`. 
To assess the performance of STIMP, we randomly selected nine different rates of missing data, ranging from 10% to 90%, for choosing observed data as imputation targets.
The experiments in the four coastal ocean regions, including Pearl River Estuary, Northern Gulf of Mexico, Chesapeake Bay and Yangtze River Estuary, can be conducted using the following script.

.. code-block:: bash

   for area in {"PRE","MEXICO","Chesapeake","Yangtze"}
   do
      for i in {0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9}
      do
         python imputation/train_stimp.py --missing_ratio $i --area $area
         python imputation/train_csdi.py --missing_ratio $i --area $area
         python imputation/train_dineof.py --missing_ratio $i --area $area
         python imputation/train_imputeformer.py --missing_ratio $i --area $area
         python imputation/train_inpainter.py --missing_ratio $i --area $area
         python imputation/train_lin_itp.py --missing_ratio $i --area $area
         python imputation/train_mae.py --missing_ratio $i --area $area
         python imputation/train_mean.py --missing_ratio $i --area $area
         python imputation/train_trmf.py --missing_ratio $i --area $area
      done
   done
.. bibliography::
   :filter: {"baselines"} & docnames
