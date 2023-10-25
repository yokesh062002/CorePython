from pickle import *
name=open("varun.txt","wb")
studentdata=[501,"varun","tpt","mech"]
collegedata={"name":"varun","college":"tpt","rollno":501}
myfrndsname=("yokesh","gowtham")
dump(studentdata,name)
dump(collegedata,name)
dump(myfrndsname,name)
name.close()