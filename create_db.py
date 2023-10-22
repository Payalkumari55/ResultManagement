import sqlite3
def create_db():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(id INT PRIMSRY KEY AUTO_INCREMENT, name varchar,duration text,charges text,city text,description text)")
    con.commit()


    # cur.execute("CREATE TABLE IF NOT EXISTS student(roll INT PRIMARY KEY , name varchar,email text,gender text,dob text,contact text,session text,course text,state text,city text,pin text,address text)")
    # con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS result(id INT PRIMSRY KEY AUTO_INCREMENT, roll text ,first_name text,last_name text,course text,marks_obt text,full_marks text,percentage text,remarks text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS subject(id INT PRIMSRY KEY AUTO_INCREMENT, Branch text ,Department text,Semester text,year text,subject text)")
    con.commit()

    con.close()
    
create_db()
