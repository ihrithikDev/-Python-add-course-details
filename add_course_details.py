import sqlite3 



class DatabaseManager():
        
        def __init__(self):
            global con
             
            try:
                con = sqlite3.connect('courses.db')
                with con:
                    cur = con.cursor()
                    cur.execute("CREATE TABLE IF NOT EXISTS course(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price INTEGER, is_private BOOLEAN NOT NULL DEFAULT 1 ) ")
            except Exception:
                print("Unable to create a Database..")


        def insert_data(self, data):
            try:
                with con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO course(name, description, price, is_private) VALUES(?,?,?,?)", data)
                    return True
                    
            except Exception:
                return False

        # Read Data
        def fetch_data(self):
            try:
                with con:
                    cur  = con.cursor()
                    cur.execute("SELECT * FROM course")
                    return cur.fetchall()
            except Exception:
                return False
        # DElete Data
        def delete_data(self, id):
            try:
                with con:
                    cur = con.cursor()
                    sql = "DELETE FROM course WHERE id = ?"
                    cur.execute(sql,[id])
                    return True
            except Exception:
                return False

# interface

def main():
    
    
    db = DatabaseManager()

    
    print("\n ==== ::  COURSE MANAGEMENT : USER MANUAL :: ====\n")
    

    print("\tPress 1. Insert a new Course.")
    print("\tPress 2. Show all Courses")
    print("\tPress 3. Delete a course(NEED ID OF COURSE)")

    

    choice = input("\n\tEnter a Choice: ")

    if choice == "1":
        print("\n\tPls Provide some Instruction.")
        print("\t-------------------------------")
        name = input("\n\tEnter a Course name : ")
        description = input("\tEnter a Course description : ")
        price = input("\tEnter a Course price : ")
        private = input("\tIs course is private ? (1/0) ")

        if db.insert_data([name, description, price, private]):
            print("\n\tCourse was inserted sucessfully.")
        else:
            print("OPPS! SomeThing gone wrong.")
    elif choice == "2":
        print("\n\t ---- :: Course List :: ----")

        for index,item in enumerate(db.fetch_data()):
            print("\n\tSl no : " + str(index+1))
            print("\tCourse ID : " + str(item[0]))
            print("\tCourse Name : " + str(item[1]))
            print("\tCourse Description : " + str(item[2]))
            print("\tCourse Price : " + str(item[3]))
            private = 'Yes' if item[4] else 'No'

            print("\n")

    elif choice == "3":
        record_id = input("\n\tEnter the course ID : ")
        
        if db.delete_data(record_id):
            print("\n\tCouse was deleted successfully.")
        else:
            print("\n\tOOP! SOMETHING GONE WRONG")
    else:
        print("\n\tBAD Choice")

if __name__ == "__main__":

        main()
        more = input("\n\tDo want To Explore more option ? (yes/No) : ")
        if more == "yes":
                main()
        else:
            print("\n\tHave a Nice Day! \n\tThank You")
            quit()
                   
            






