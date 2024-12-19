# HelenaPDFExtractor
This repository contains the code used to extract hosptial address information from a 100+ page PDF document consisting of over 300 hospitals. It uses pymupdf4llm, pathlib, and pandas in order to convert the PDF document into a parsable MD file, extract the information, and ouput the results into an excel file organized into the corresponding columns. 

---

## Project Features

- **PDF File Conversion to MD:** Takes the PDF document and uses pymupdf4llm to convert the document into an acceptable MD format
- **Hosptial Address Extraction:** Splits the MD file into chunks corresponding to each hosptial and extracts the relevant address information
- **Excel file output:** Takes the collected addresses and outputs them into an excel file for later use

---

This project was for a specific use case designed to extract 300+ hospitals' address information from a 100+ page PDF document, but the general format could be used to extract information from various different PDF sources. If you're using it for a personal project or have any questions, please feel free to reach out at loganrichards.dev@gmail.com. 