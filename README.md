<img width="1018" height="388" alt="image" src="https://github.com/user-attachments/assets/b6d6022f-0e52-4421-a2d9-5652d84437a8" />

## A Distributed Socio-hydrological Framework
This model integrates two different software systems, **MODFLOW** and **NetLogo**, through **Python** as an intermediary platform. The framework enables a high spatiotemporal resolution in the Socio-hydrological modelling.

## Hydrological Component
The hydrological component of this model is **MODFLOW-2000**, which simulates an unconfined aquifer. The case study of this project is Isfahan-Borkhar aquifer. The model is designed to simulate groundwater flow over multiple years. For the hydrogeological section, please note that the groundwater model in this project was developed independently using the GMS software based on the data from the case study. Therefore, working with the model files is done using the flopy library and executing the model’s ASCII files (with the .mfn extension). At the beginning of each year of model execution, the contents of the text files related to pumping rates of wells (files with the .wel extension) are updated based on the computational pumping rates in the social model. Then, by executing the code in the MODFLOW-Qi files for each year, the groundwater model’s executable files (with the .mfn extension) are run, updating the groundwater levels, which are then saved as output in the csv files. This way, by replacing and modifying the model data according to the data for each study area, the model can be executed for other study areas as well.

## Social Component
The social component, or decision-making model, is implemented using **NetLogo**, where farmers make decisions about their cultivation patterns based on psychological features and environmental factors. This model has been independently developed within the NetLogo 6.2.2 environment and is invoked using the Pynetlogo library. Accordingly, the commands generated in the NetLogo model are executed sequentially by the Borkhar4202 file code, allowing farmers to select crop patterns and calculate the water pumping rate.

## Model Workflow

The workflow integrates both sub-models sequentially through a Python-based interface provided by the central file, **Borkhar4202.py** using the Python subprocess.run command. This file manages the interaction between the MODFLOW and NetLogo models. It first updates the input data for MODFLOW, runs the simulation, and then transfers the results to the NetLogo model for decision-making. By running this single Python script, users can execute the entire socio-hydrological model. The files are executed in a time-sequenced order, as described below:

**1.** Year1 to Year4: These files modify the pumping rates of wells for each year and are crucial for adjusting the hydrological model. After adjusting these rates, the corresponding MODFLOW-Q1 to MODFLOW-Q4 files are used to rerun the model with the updated pumping rates.

**2.** MODFLOW-Q1 to MODFLOW-Q4: These files run the MODFLOW model for each year with the adjusted pumping rates and simulate the flow in the unconfined aquifer. These files are called sequentially after each year’s pumping rate adjustment.

**3.** Fitness function and Genetic-historical-calibration: These two files are used separately for model calibration after the main model (Borkhar4202) has been fully executed and developed. These steps are focused on optimizing the parameters and ensuring the model fits the observed data.

**4.** The remaining commands in the Borkhar4202 file are used for calling the NetLogo model via the Python interface. The Python-based interface facilitates communication between the MODFLOW and NetLogo models, enabling the simulation of the socio-hydrological processes where farmers make decisions based on psychological features. The relevant commands for invoking and running NetLogo are located in the main script borkhar4202.py.

Each file in this sequence plays a role in either modifying the model inputs (e.g., pumping rates), running the hydrological model (MODFLOW), or invoking the socio-economic model (NetLogo). The files are executed one after another to simulate the interactions between hydrological and social processes, ensuring the models are coupled effectively.

## Installation Instructions

1. **Install dependencies**:

    The project uses Python, so install the required dependencies via `pip`. This project benefits from two main libraries including Flopy & Pynetlogo:
   **Installation**: Available with the pip package manager:
   pip install pynetlogo
   pip install flopy
  FloPy requires Python 3.10+ with:
numpy >=1.20.3
matplotlib >=1.4.0
pandas >=2.0.0
Additionally pynetlogo requires packages including: JPype , NumPy, SciPy , pandas

Make sure you have the following external software installed:

   - **GMS 10.6** (for MODFLOW model)
   - **NetLogo 6.2.2** (for social decision-making model)

2. **Running the model**:

    To run the full simulation, execute the following command in your terminal:

    ```bash
    python Borkhar4202.py
    ```

   This will execute the Python interface, which coordinates the MODFLOW and NetLogo models.
   
3. **Input Data**:

Make sure the necessary input files are in place:

**4202-borkhar.mfn**: Groundwater model input file.

**farmers behavior.nlogo**: NetLogo model file with farmers' decision-making rules.

These files should be placed in the directory specified by the code (you can adjust file paths if needed).

4. **Outputs**:

    The model will generate output files in the as csv files, including simulation results and then transfer them from modflow to netlogo and vice versa.

## Data Availability

 The input and output data used for this model are not publicly available due to restrictions on data sharing. Additional data supporting the findings are available from the first author, Zahra Soleimanzadeh (**z.soleimanzadeh98@gmail.com**) upon reasonable request.

## Related Links
- **NetLogo model**: [Link to the model on CoMSES.net](https://www.comses.net/codebase-release/7651242e-876b-4c64-9faf-3b5f1e68ec5e/)

## License

This project is licensed under the MIT License.

## Software/Code Citation:

Soleimanzadeh, Z. (2026). Socio-hydrological-model: A distributed socio-hydrological model (v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.18734546

The DOI for this repository is:
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18734546.svg)](https://doi.org/10.5281/zenodo.18734546)


**Contact**:

The Netlogo model of this project can be found at CoMSES.net at :(https://www.comses.net/codebases/f4630400-d48b-4634-b0d7-c22467a4d3a5/)
