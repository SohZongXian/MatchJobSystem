from flask import Flask, render_template, request, flash
from flask_mysqldb import MySQL
from flask_paginate import Pagination
from sumSimilarity import Sum
from model import calculateSim
#from preprocessingParagraph import preProcessing

app=Flask(__name__)       

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'project'
app.config['SECRET_KEY'] = 'something only you know'
 
mysql = MySQL()
mysql.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/job', methods = ['POST', 'GET'])
def search():
    if request.method == 'GET':
        terms = request.args.get('term')
        term = terms.split()
        print(term)
        conn = mysql.connection
        cursor = conn.cursor()

        if terms == 'all' or len(terms)==0: 
            cursor.execute("SELECT ID, NAME, COMPANY, DESCRIPTION from job")
            conn.commit()
            data = cursor.fetchall()
            #cursor.close()
            return render_template("job.html", data=data, terms=terms)

        for r in range (len(term)):
            cursor.execute("SELECT ID, NAME, COMPANY, DESCRIPTION from job WHERE CATEGORY LIKE %s OR NAME LIKE %s OR DESCRIPTION LIKE %s", (("%" + term[r] + "%",),("%" + term[r] + "%",),("%" + term[r] + "%",)))
            conn.commit()
            data1 = cursor.fetchall()
            data = data1 + data1

        if len(data) == 0 :
            flash('No related job found. Please try again.')
            return render_template("job.html", terms=terms)
    return render_template("job.html", data=data, terms=terms)

@app.route('/job/match/<id>')
def match(id):
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT DESCRIPTION from job WHERE ID = %s",[id])
    conn.commit()
    description = cursor.fetchall()
    description = description[0]
    descriptionj = ''.join([str(x) for t in description for x in t])
    de = descriptionj
    print(de)

    cursor.execute("SELECT NAME from job WHERE ID = %s",[id])
    conn.commit()
    jobnamea = cursor.fetchall()
    jobnamea = jobnamea[0]
    jobnamej = ''.join([str(x) for t in jobnamea for x in t])
    jobname = jobnamej

    cursor.execute("SELECT LINK from job WHERE ID = %s",[id])
    conn.commit()
    joblinka = cursor.fetchall()
    joblinka = joblinka[0]
    joblinkj = ''.join([str(x) for t in joblinka for x in t])
    joblink = joblinkj

    cursor.execute("SELECT ABSTRACT from user_1")
    conn.commit()
    abstract = cursor.fetchall()

    cursor.execute("SELECT NAME from user_1")
    conn.commit()
    user = cursor.fetchall()

    cursor.execute("SELECT LINK from user_1")
    conn.commit()
    scopuslink = cursor.fetchall()

    cursor.execute("SELECT USERNAME,SIMILARITY,SCOPUSLINK,JOBID from result WHERE JOBID= %s ORDER BY SIMILARITY DESC",[id])
    conn.commit()
    final_result = cursor.fetchall()

    if len(final_result) == 0:
        #result = calculateSim(de,abstract)
        
        #for r in range(len(result)):
        #    cursor.execute("""INSERT INTO result(JOBID,USERNAME,SIMILARITY,SCOPUSLINK) VALUES (%s,%s,%s,%s)""",(id,user[r],result[r],scopuslink[r]))
        #    conn.commit()

        #cursor.execute("SELECT USERNAME,SIMILARITY,SCOPUSLINK,JOBID from test_1 WHERE JOBID= %s ORDER BY SIMILARITY DESC",[id])
        #conn.commit()
        #result1 = cursor.fetchall()

        #cursor.execute("SELECT USERNAME,SIMILARITY,SCOPUSLINK,JOBID from test_2 WHERE JOBID= %s ORDER BY SIMILARITY DESC",[id])
        #conn.commit()
        #result2 = cursor.fetchall()

        #lastresult = Sum(result1,result2)

        #for r in range (len(lastresult)):
        #    cursor.execute("""INSERT INTO result(JOBID,USERNAME,SIMILARITY,SCOPUSLINK) VALUES (%s,%s,%s,%s)""",(lastresult[r][3],lastresult[r][0],lastresult[r][1],lastresult[r][2]))
        #    conn.commit()

        cursor.execute("SELECT USERNAME,SIMILARITY,SCOPUSLINK,JOBID from result WHERE JOBID= %s ORDER BY SIMILARITY DESC",[id])
        conn.commit()
        final_result = cursor.fetchall()

    #cursor.execute("INSERT INTO test (USERNAME,SIMILARITY) %r;" % (tuple(final_result),))

    return render_template("match.html",id=id,jobname=jobname,joblink=joblink,user=user,final_result=final_result)

@app.route('/job/match/<id>/show-in-pagination',methods = ['POST', 'GET'])

def show(id):
    entries = 5
    limit = 5
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT NAME from job WHERE ID = %s",[id])
    conn.commit()
    jobnamea = cursor.fetchall()
    jobnamea = jobnamea[0]
    jobnamej = ''.join([str(x) for t in jobnamea for x in t])
    jobname = jobnamej

    cursor.execute("SELECT LINK from job WHERE ID = %s",[id])
    conn.commit()
    joblinka = cursor.fetchall()
    joblinka = joblinka[0]
    joblinkj = ''.join([str(x) for t in joblinka for x in t])
    joblink = joblinkj

    cursor.execute("SELECT NAME from user_1")
    conn.commit()
    user = cursor.fetchall()

    cursor.execute("SELECT DESCRIPTION from job WHERE ID = %s",[id])
    conn.commit()
    description = cursor.fetchall()
    description = description[0]
    descriptionj = ''.join([str(x) for t in description for x in t])
    de = descriptionj

    cursor.execute("SELECT ABSTRACT from user_1")
    conn.commit()
    abstract = cursor.fetchall()

    cursor.execute("SELECT LINK from user_1")
    conn.commit()
    scopuslink = cursor.fetchall()

    if request.method == 'GET':
        entries = request.args.get('entries')
        conn = mysql.connection
        cursor = conn.cursor()

        if entries== '5':
            limit = 5

        if entries == '10':
            limit = 10

        if entries == '25':
            limit = 25

        if entries == '50':
            limit = 50

        if entries == 'all':
            limit = 66

        cursor.execute("SELECT USERNAME,SIMILARITY,SCOPUSLINK from result WHERE JOBID= %s ORDER BY SIMILARITY DESC",[id])
        conn.commit()
        final_result = cursor.fetchall()

        if len(final_result) == 0:
            result = calculateSim(de,abstract)
        
            for r in range(len(result)):
                cursor.execute("""INSERT INTO result(JOBID,USERNAME,SIMILARITY,SCOPUSLINK) VALUES (%s,%s,%s,%s)""",(id,user[r],result[r],scopuslink[r]))
                conn.commit()

            cursor.execute("SELECT USERNAME,SIMILARITY,SCOPUSLINK,JOBID from test_1 WHERE JOBID= %s ORDER BY SIMILARITY DESC",[id])
            conn.commit()
            result1 = cursor.fetchall()

            cursor.execute("SELECT USERNAME,SIMILARITY,SCOPUSLINK,JOBID from test_2 WHERE JOBID= %s ORDER BY SIMILARITY DESC",[id])
            conn.commit()
            result2 = cursor.fetchall()

            lastresult = Sum(result1,result2)

            for r in range (len(lastresult)):
                cursor.execute("""INSERT INTO result(JOBID,USERNAME,SIMILARITY,SCOPUSLINK) VALUES (%s,%s,%s,%s)""",(lastresult[r][3],lastresult[r][0],lastresult[r][1],lastresult[r][2]))
                conn.commit()

            cursor.execute("SELECT USERNAME,SIMILARITY,SCOPUSLINK,JOBID from result WHERE JOBID= %s ORDER BY SIMILARITY DESC",[id])
            conn.commit()
            final_result = cursor.fetchall()

        total = len(final_result)

        page = request.args.get('page', 1, type=int)
        offset = page*limit - limit

        cursor.execute("SELECT USERNAME,SIMILARITY,SCOPUSLINK from result WHERE JOBID= %s ORDER BY USERNAME LIMIT %s OFFSET %s",(id,limit, offset))
        conn.commit()
        dataa = cursor.fetchall()

        pagination = Pagination(page=page, per_page=limit, offset=offset, total=total, record_name='user',css_framework='bootstrap3')
        return render_template("try.html",entries=entries,jobname=jobname,joblink=joblink,user=user,id=id,dataa=dataa,pagination=pagination)
    


if __name__=="__main__":
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug = True)
