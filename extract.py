from pypdf import PdfReader
import pymupdf4llm
import pathlib
from pandas import DataFrame

# Reads pdf file using basic library
def basicPDFRead():
    reader = PdfReader("Roble.pdf")

    page = reader.pages[0]

    text = page.extract_text()
    hospitals = text.split("DEPARTMENT:NAME:STOP")
    for i in range(len(hospitals)-1):
        print("\n\n\n******")
        print("Hospital {}: ".format(i))
        print(hospitals[i])

# Extracts and converts to md file
def fromPDFToMD():
    md_text = pymupdf4llm.to_markdown("Roble.pdf")

    # now work with the markdown text, e.g. store as a UTF8-encoded file
    pathlib.Path("output.md").write_bytes(md_text.encode())


# Places to store mailAddresses and cityStates
mailAddresses = []
cityStates = []

# Reading markdown file and extracting relevant information from each hospital
with open("output.md", "r") as f:
    s = f.read()
    hospitals = s.split("NAME: DEPARTMENT: STOP STAR COMMENTS")

    # Looping through each hosptial to extract its address
    for hospital in hospitals:
        mailAddressStart = hospital.find("MAIL ADD:")
        mailAddressEnd = mailAddressStart + hospital[mailAddressStart:].find("\n")

        mailAddress = hospital[mailAddressStart:mailAddressEnd].replace("MAIL ADD:", "").strip()

        cityStateStart = hospital.find("CITY/STATE: **")
        cityLength = len("CITY/STATE: **")
        cityStateEnd = cityStateStart + cityLength + hospital[cityStateStart+cityLength:].find("**")
        
        cityState = hospital[cityStateStart:cityStateEnd].replace("CITY/STATE: **", "").strip()

        mailAddresses.append(mailAddress)
        cityStates.append(cityState)
      
        break

# Using pandas to write to excel file
df = DataFrame({"Mail Address":mailAddresses, "City/State":cityStates})
df.to_excel('test.xlsx', sheet_name='sheet1', index=False)