from classQuery import Query

class Categories:

    query_select = "SELECT TBLME_CODICE2, TBLME_DESCRIZIONE1 FROM TBLME ORDER BY TBLME_DESCRIZIONE1 ASC"

    def get():
        data = Query.selectData(Categories.query_select)
        return data

    