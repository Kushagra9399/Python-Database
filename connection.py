import mysql.connector
import Student
import Queries

# Establishing a database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kush",
    database="kp"
)
query_all = Queries.Queries()

def insert():
    st = Student.Student()
    id = count(mycur)
    ins = query_all.insert_query
    values = (id+1, st.name, st.year, st.mob, st.email)
    mycur.execute(ins, values)
    mydb.commit()

def count(mycur):
    mycur.execute("SELECT COUNT(*) FROM TRAIL")
    id = mycur.fetchone()[0]
    return id

def display_all(data=""):
    if data=="":
        ins = query_all.select_all
        mycur.execute(ins)
        data = mycur.fetchall()
    print("="*70)
    print("| Id | Name           | Year | Mobile No   | Email")
    for i in data:
        print("| " + str(i[0]) + " "*(3-len(str(i[0]))),end="")
        print("| " + i[1] + " "*(15-len(str(i[1]))),end="")
        print("| " + str(i[2]) + " "*(5-len(str(i[2]))),end="")
        print("| " + i[3] + " "*(12-len(str(i[3]))),end="")
        print("| " + i[4] + " "*(30-len(str(i[4]))))
    print("="*70)

def delete(a):
    col = ["id","Name","Year","mob","email"]
    col_print = ["Id","Name","Year","Mobile Number","Email"]
    dlt = input(f"{col_print[a-1]} equals to: ")
    print("Are you sure?(y or n)")
    sure = input()
    if sure=="y" or sure == "Y":
        ins = query_all.delete_query(col[a-1],dlt)
        mycur.execute(ins)
        mydb.commit()
        print("Data Deleted Successfully...")
        mycur.execute("SET @new_id = 0;")
        mycur.execute("UPDATE trail SET id = (@new_id := @new_id + 1);")
        mydb.commit()
    else:
        print("Deletion Cancelled...")

def update(a):
    col = ["id","Name","Year","mob","email"]
    col_print = ["Id","Name","Year","Mobile Number","Email"]
    print("Update data to: ")
    up = input()
    print("Update data by condition:\n1.Id\n2.Name\n3.Year\n4.Mobile No.\n5.Email\n6.Back")
    i = int(input())
    if i in (1,2,3,4,5):
        j = input(f"{col_print[i-1]} equal to: ")
        ins = query_all.update_query(col[a-1],up,col[i-1],j)
        mycur.execute(ins)
        mydb.commit()
        print("Data updated successfully...")

def search(a,b):
    col = ["id","Name","Year","mob","email"][a-1]
    ins = f"SELECT * FROM trail WHERE {col} = %s;"
    mycur.execute(ins,(b,))
    data = mycur.fetchall()
    display_all(data)

try:
    with mydb.cursor() as mycur:
        mycur.execute("set sql_safe_updates=0")
        while True:
            print("1.Add data\n2.Display all data\n3.Delete Data\n4.Update Data\n5.Search Data\n6.Self Query\n7.Exit")
            c = int(input())
            if c==1:
                insert()
            elif c==2:
                if count(mycur)==0:
                    print("No data present...\nPlease enter data...")
                else:
                    display_all()
            elif c==3:
                print("Enter one data to delete row:")
                print("1.Id\n2.Name\n3.Year\n4.Mobile No.\n5.Email\n6.Back")
                dlt = int(input())
                if dlt in [1,2,3,4,5]:
                    delete(dlt)
            elif c==4:
                print("Update: \n1.Id\n2.Name\n3.Year\n4.Mobile No.\n5.Email\n6.Back")
                sea = int(input())
                if sea in [1,2,3,4,5]:
                    update(sea)
            elif c==5:
                print("Search by: \n1.Id\n2.Name\n3.Year\n4.Mobile No.\n5.Email\n6.Back")
                sea = int(input())
                if sea in [1,2,3,4,5]:
                    s1 = input("Enter data to search: ")
                    search(sea,s1)
            elif c==6:
                print("Write query: ")
                ins = input()
                a = ins.split()
                if a[0]=="SELECT" or a[0]=="select":
                    mycur.execute(ins)
                    data = mycur.fetchall()
                    for i in data:
                        print(i)
                else:
                    mycur.execute(ins)
                    mydb.commit()
            else:
                mycur.execute("set sql_safe_updates=1")
                break

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    mydb.close()
