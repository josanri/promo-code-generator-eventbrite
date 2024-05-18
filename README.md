# promo-code-generator-eventbrite
Generate promo codes for Eventbrite events and save them to a file.
## Install
```bash
pip install -r requirements.txt
```
## Requirements
To use the tool you can have a file containing the different names for the promo codes. This file should be a text file with one name per line. 
## Usage
By typing:
```bash
python src/main.py [OPTIONS] --filename <FILENAME>
```
The tool will generate promo codes for each name in the file and save them to a file. The tool also has the option to save QR codes for each promo code generated with ``--qr` flag.
```
code-generator [-h]
    --filename FILENAME
    [-c COUNT]
    [--custom-name CUSTOM_NAME]
    [--domain {at,be,ca,ch,cl,co,com,com.ar,com.au,com.br,com.mx,com.ng,com.pe,co.nz,co.uk,co.za,de,dk,es,fi,fr,hk,ie,in,it,my,nl,ph,pt,se,sg}]
    [-o OUTPUT_FILE]
    [--qr]
    [--id EVENT_ID]
    [--output-dir QR_DIRECTORY]

Optional Arguments
-h, --help: Show this help message and exit.
-c COUNT, --count COUNT: Number of promo codes to generate.
--filename FILENAME: File containing names of the attendees.
--custom-name CUSTOM_NAME: Custom name as prefix to every promo code.
--domain {at,be,ca,ch,cl,co,com,com.ar,com.au,com.br,com.mx,com.ng,com.pe,co.nz,co.uk,co.za,de,dk,es,fi,fr,hk,ie,in,it,my,nl,ph,pt,se,sg}: Domain for the promo codes.
-o OUTPUT_FILE, --output-file OUTPUT_FILE: Directory to save the uuids generated.
--qr, --save_qr: Flag to save QR codes for every promo code.
--id EVENT_ID, --event EVENT_ID: Event ID.
--output-dir QR_DIRECTORY: Directory to save the QR codes for every promo code.

*COUNT is limited to 500, the current limit to bulk csv promo codes
```