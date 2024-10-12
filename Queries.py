class Queries:
    insert_query = "INSERT INTO trail (id, name, year, mob, email) VALUES (%s, %s, %s, %s, %s)"
    select_all = "SELECT * FROM trail"
    count = "SELECT COUNT(*) FROM trail"

    def delete_query(self,a,b):
        if type(b)==str:
            self.delete = f"DELETE FROM trail WHERE {a}='{b}'"
        else:
            self.delete = f"DELETE FROM trail WHERE {a}={b}"
        return self.delete

    def update_query(self,a,b,c=0,d=0):
        if c==0:
            if type(b)==int and type(d)==int:
                self.update = f"UPDATE trail SET {a} = {b} WHERE {c}={d}"
            elif type(b)==str and type(d)==str:
                self.update = f"UPDATE trail SET {a} = '{b}' WHERE {c}='{d}'"
            elif type(b)==str and type(d)==int:
                self.update = f"UPDATE trail SET {a} = '{b}' WHERE {c}={d}"
            else:
                self.update = f"UPDATE trail SET {a} = {b} WHERE {c}='{d}'"
        else:
            if type(b)==int:
                self.update = f"UPDATE trail SET {a}={b}"
            else:
                self.update = f"UPDATE trail SET {a}='{b}'"
        return self.update