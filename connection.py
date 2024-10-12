import mysql.connector
import Student
import Queries

# Establishing a database connection2

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
    name_len = email_len = 0
    for i in data:
        name_len = max(name_len,len(i[1]))
        email_len = max(email_len,len(i[-1]))
    print("="*(40+name_len+email_len))
    all_len = [3,name_len,5,12,email_len]
    print("| Id  || Name" + " "*(name_len-4) + " || Year  || Mobile No    || Email" + " "*(email_len-5)+" |")
    for i in data:
        for j in range(len(i)):
            print("| " + str(i[j]) + " "*(all_len[j]-len(str(i[j]))),end=" |")
        print()
    print("="*(40+email_len+name_len))

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
    while True:
        try:
            i = int(input())
            break
        except Exception:
            print("Enter Integer: ")
    if i in (1,2,3,4,5):
        j = input(f"{col_print[i-1]} equal to: ")
        ins = query_all.update_query(col[a-1],up,col[i-1],j)
        mycur.execute(ins)
        mydb.commit()
        print("Data updated successfully...")

def search(a,b):
    col = ["id","Name","Year","mob","email"][a-1]
    ins = f"SELECT * FROM trail WHERE {col} LIKE %s;"
    mycur.execute(ins,("%"+b+"%",))
    data = mycur.fetchall()
    display_all(data)

try:
    with mydb.cursor() as mycur:
        mycur.execute("set sql_safe_updates=0")
        while True:
            print("1.Add data\n2.Display all data\n3.Delete Data\n4.Update Data\n5.Search Data\n6.Self Query\n7.Exit")
            while True:
                try:
                    c = int(input())
                    break
                except Exception:
                    print("Enter Integer: ")
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
                while True:
                    try:
                        dlt = int(input())
                        if dlt not in [1,2,3,4,5,6]:
                            print("Enter correct choice.\nRe-enter choice...")
                            continue
                        break
                    except Exception:
                        print("Enter Integer: ")
                if dlt in [1,2,3,4,5]:
                    delete(dlt)
            elif c==4:
                print("Update: \n1.Id\n2.Name\n3.Year\n4.Mobile No.\n5.Email\n6.Back")
                while True:
                    try:
                        sea = int(input())
                        if sea in [1,2,3,4,5,6]:
                            break
                        else:
                            print("Enter correct choice.\nRe-enter choice...")
                    except Exception:
                        print("Enter Integer: ")
                if sea!=6:
                    update(sea)
            elif c==5:
                print("Search by: \n1.Id\n2.Name\n3.Year\n4.Mobile No.\n5.Email\n6.Back")
                while True:
                    try:
                        sea = int(input())
                        if sea in [1,2,3,4,5,6]:
                            break
                        else:
                            print("Enter correct choice.\nRe-enter choice...")
                    except Exception:
                        print("Enter Integer: ")
                while sea in [1,2,3,4,5]:
                    s1 = input("Enter data to search: ")
                    if len(s1)<3:
                        print("For search enter minimum 3 character!!!")
                        continue
                    else:
                        break
                search(sea,s1)
            elif c==6:
                try:
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
                except Exception:
                    print("Invalid Query...")
            elif c==7:
                mycur.execute("set sql_safe_updates=1")
                break
            else:
                print("Enter correct choice.\nRe-enter the choice...")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    mydb.close()
