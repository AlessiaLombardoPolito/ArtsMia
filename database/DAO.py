from database.DB_connect import DBConnect
from model.artObject import ArtObject
from model.connessioni import Connessione


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getPeso(self, v1, v2):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT count(*) 
                    FROM exhibition_objects eo1, exhibition_objects eo2
                    WHERE eo1.exhibition_id = eo2.exhibition_id
                    and eo1.object_id < eo2.object_id
                    and eo1.object_id = %s
                    and eo2.object_id = %s"""

        cursor.execute(query, (v1.object_id, v2.object_id,))

        for row in cursor:
            result.append((row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnesioni(idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT eo1.object_id as o1, eo2.object_id as o2, count(*) as peso 
                    FROM exhibition_objects eo1, exhibition_objects eo2
                    WHERE eo1.exhibition_id = eo2.exhibition_id
                    and eo1.object_id < eo2.object_id
                    group by eo1.object_id, eo2.object_id
                    order by peso desc"""

        cursor.execute(query)

        for row in cursor:
            result.append(Connessione(idMap[row["o1"]],
                                      idMap[row["o2"]],
                                      row["peso"]))

        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getAllObjects():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM objects o"""

        cursor.execute(query)

        for row in cursor:
            result.append(ArtObject(**row)) #solo se nomi della dataclass sono gli stessi della tabella e sto usando dictionary

        cursor.close()
        conn.close()
        return result

