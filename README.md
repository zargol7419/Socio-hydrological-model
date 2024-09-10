# A Distributed Socio-Hydrological Framework
This model integrates two different software, MODFLOW and NetLogo, through Python as an intermediary platform.
This framework enables a high spatiotemporal resolution in the Socio-hydrological model. The hydrological component of this model is MODFLOW-2000, which simulates an unconfined aquifer. The social component or decision-making model is the NetLogo model, in which farmers make decisions regarding their cultivation patterns according to their psychological features.
A Python-based interface can help users implement both sub-models sequentially, which can reduce the complexity of coupled Socio-hydrological models.
A makefile is not available for MODFLOW-2000 source files. However, the build order for the source files is listed below.


1.Borkhar 4202

2.Year1

3.MODFLOW-Q1

4.Year2

5.MODFLOW-Q2

6.Year3

7.MODFLOW-Q3

8.Year4

9.MODFLOW-Q4

10.Fitness function

11. Genetic-historical-calibration

In the files, there are several path files through which the model reads initial data or prints the output due to the limitation of publishing these data. A short report has been referred to in our last manuscript.

**Contact**:

For more information please contact me : Sampad7419@gmail.com
The Netlogo model of this project can be found at CoMSES.net at :(https://www.comses.net/codebases/f4630400-d48b-4634-b0d7-c22467a4d3a5/)
