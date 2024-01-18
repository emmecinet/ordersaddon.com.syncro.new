def buttonSubCategories():
    sub_categories = Query.selectData("SELECT TBLCM_CODICE2, TBLCM_DESCRIZIONE1 FROM TBLCM ORDER BY TBLCM_DESCRIZIONE1 ASC")
    

def buttonItems():
    items = Query.selectData("SELECT ART_CODICE, ART_DESCRIZIONE1, ART_CODICE_UM, ART_CODICE_IV_VEN, ART_CODICE_CM, ART_CODICE_ME FROM ART ORDER BY ART_CODICE ASC")
    

def buttonQuantity():
    quantity = Query.selectData("SELECT ART_CODICE, ART_DESCRIZIONE1, ART_CODICE_UM, ART_CODICE_IV_VEN, ART_CODICE_CM, ART_CODICE_ME FROM ART ORDER BY ART_CODICE ASC")
    

def buttonPriceLists():
    price_list = Query.selectData("SELECT LIS_CODICE_ART, LIS_CODICE_LI, LIS_PREZZO_01, LIS_AA, LIS_MM, LIS_GG, LIS_DATA_FINE_VLD FROM LIS ORDER BY LIS_CODICE_ART ASC")
    

def buttonCustomers():
    customer = Query.selectData("SELECT CLI_CODICE, CLI_DESCRIZIONE1, CLI_CODICE_AG, CLI_CODICE_LI FROM CLI ORDER BY CLI_DESCRIZIONE1 ASC")
    

def buttonCustomersDestination():
    destination = Query.selectData("SELECT * FROM DES") 
    


