import pyodbc
from ClassOrdersAddonSyncro import OrdersAddonSyncro

class Query:
    def __init__(self, dns):
        self.dns = ""

    def builderQuery(type_query,table,fields,values=[],conditions=[],orders={}):   
        
        if type_query == "INSERT":

            # sql = "INSERT INTO " + table + " ("

            # count_fields = 1
            # tot_fields = len(fields)
            # for field in fields:
            #     if count_fields < tot_fields:
            #         sql += field + ","
            #     else:
            #         sql += field + ""

            #     count_fields = count_fields + 1
            
            # sql += ") VALUES ( "

            # count_values = 1
            # tot_values = len(values)
            # for value in values:
            #     if count_values < tot_values:
            #         sql += "'" + value + "',"
            #     else:
            #         sql += "'" + value + "'"

            #     count_values = count_values + 1

            # sql += ")"

            return sql
        
        elif type_query == "SELECT":

            sql = "SELECT "

            count_field = 1
            tot_fields = len(fields)
            for field in fields:
                if count_field < tot_fields:
                    sql += field + ", "
                else:
                    sql += field + " "

                count_field = count_field + 1

            sql += "FROM " + table + " "

            count_conditions = 1
            tot_conditions = len(conditions)
            if tot_conditions > 1:
                sql += "WHERE "
                for condition in conditions:
                    if count_conditions < tot_conditions:
                        sql += " (" + condition + ") AND "
                    else:
                        sql += " (" + condition + ") "

                tot_conditions = tot_conditions + 1

            count_orders = 1
            tot_orders = len(orders)
            if tot_orders > 0:
                sql += "ORDER BY "
                for order_key in orders.keys(): 
                    if count_orders < tot_orders:
                        sql += order_key + " " + orders[order_key] + ","
                    else:
                        sql += order_key + " " + orders[order_key] + ""

                    count_orders = count_orders + 1
            
            return sql

        elif type_query == "UPDATE":
            return "Update"
        
        elif type_query == "REPLACE":
            return "Replace"

        elif type_query == "DELETE":
            return "Delete"

                   
    def exQueryData(sql):
        conn = pyodbc.connect('DSN='+OrdersAddonSyncro.get_configuration().get('connection','conn_dns')+';')
        cursor = conn.cursor()
        rows = cursor.execute(sql)
        data = rows.fetchall()
        #data = [data[0] for data in rows.fetchall()]
        conn.close

        return data

    def exQueryNonData(sql):
        result = bool
        conn = pyodbc.connect('DSN='+OrdersAddonSyncro.get_configuration().get('connection','conn_dns')+';')
        cursor = conn.cursor()
        cursor.execute(sql)

        if(cursor.commit()): result = True
        else : result = False

        conn.close

        return result

    