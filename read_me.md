# SkySim

This project was created to simulate positions of sources (star/galaxy/others) over an area of sky.

The initial requirements are as follows:
* Stars should have randomized sky positions around the Andromeda galaxy.
* Positions should fall within 1 degree of the central location
* Each star should have a unique ID
* The star ID and position should be saved in a csv file to be analyzed by other programs.

This program is intended to be used by the developer and their research group which includes people who are not proficient python programmers. It is intended that the software will grow in capability and complexity only as needed to support a current research project.

## Installing
This project relies only on Python built-ins and the numpy library. Use `pip install -r requirements.txt` if you don't yet meet these requirements.

The sky_sim.py file is a program which simulates a catalogue of foreground stars in the direction of the Andromeda galaxy.

## Usage
The main entry point for this project is `sim_catalog`:

`./sim_catalog -- help
usage: sim [-h] [--ref_ra REF_RA] [--ref_dec REF_DEC] [--radius RADIUS] [--n NSOURCES] [--out OUTFILE]

optional arguments:
    -h, --help          show this help message and exit

    --ref_ra REF_RA     Central/reference RA position HH:MM:SS.S format
    --ref_dec REF_DEC   Central/reference Dec position DD:MM:SS.S format
    --radius RADIUS     radius within which the new positions are generated (deg)
    --n NSOURCES        Number of positions to generate
    --out OUTFILE       Filename for saving output (csv format)

## Documentation
Documentation is currently just this file, and associated Python docstrings.

## Author / Contribution
This project is developed by Joshua Ong. If you want to contribute to this project please create a fork and issue pull requests for new features or bug fixes.




