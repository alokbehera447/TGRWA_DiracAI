import os

App1="Vchat"
App2="EMail"
App3="Ticket"

redirapp1="chat"
redirapp2="email"
redirapp3="ticket"




#create app2 files first
mkfile1 = "cp basefiles/App2.js %s.js"%(App2)
os.system(mkfile1)
refile1="sed -i 's/App2/%s/g' %s.js"%(App2,App2)
os.system(refile1)


mkfile2 = "cp basefiles/TopInfoBarApp2.js TopInfoBar%s.js"%(App2) 
os.system(mkfile2)
refile2="sed -i 's/App2/%s/g' TopInfoBar%s.js"%(App2,App2)
os.system(refile2)
refile2_1="sed -i 's/App1/%s/g' TopInfoBar%s.js"%(App1,App2)
os.system(refile2_1)
refile2_3="sed -i 's/App3/%s/g' TopInfoBar%s.js"%(App3,App2)
os.system(refile2_3)

refile2_1rd="sed -i 's/app1/%s/g' TopInfoBar%s.js"%(redirapp1,App2)
os.system(refile2_1rd)

refile2_3rd="sed -i 's/app3/%s/g' TopInfoBar%s.js"%(redirapp3,App2)
os.system(refile2_3rd)



mkfile3 = "cp basefiles/App2ContentDiv.js %sContentDiv.js"%(App2)
os.system(mkfile3)
refile3="sed -i 's/App2/%s/g' %sContentDiv.js"%(App2,App2)
os.system(refile3)


mkfile4 = "cp basefiles/App2ContentDiv.module.css %sContentDiv.module.css"%(App2)
os.system(mkfile4)

makeDir="mkdir %s"%(App2)
os.system(makeDir)

moveToDirJS="mv ./*.js %s"%(App2)
os.system(moveToDirJS)

moveToDirCSS="mv ./*.css %s"%(App2)
os.system(moveToDirCSS)





#Create App1 files now

mkfile1 = "cp basefiles/App2.js %s.js"%(App1)
os.system(mkfile1)
refile1="sed -i 's/App2/%s/g' %s.js"%(App1,App1)
os.system(refile1)



mkfile2 = "cp basefiles/TopInfoBarApp1.js TopInfoBar%s.js"%(App1)
os.system(mkfile2)
refile2="sed -i 's/App1/%s/g' TopInfoBar%s.js"%(App1,App1)
os.system(refile2)
refile2_1="sed -i 's/App2/%s/g' TopInfoBar%s.js"%(App2,App1)
os.system(refile2_1)
refile2_3="sed -i 's/App3/%s/g' TopInfoBar%s.js"%(App3,App1)
os.system(refile2_3)

refile2_1rd="sed -i 's/app2/%s/g' TopInfoBar%s.js"%(redirapp2,App1)
os.system(refile2_1rd)

refile2_3rd="sed -i 's/app3/%s/g' TopInfoBar%s.js"%(redirapp3,App1)
os.system(refile2_3rd)


mkfile3 = "cp basefiles/App2ContentDiv.js %sContentDiv.js"%(App1)
os.system(mkfile3)
refile3="sed -i 's/App2/%s/g' %sContentDiv.js"%(App1,App1)
os.system(refile3)

mkfile4 = "cp basefiles/App2ContentDiv.module.css %sContentDiv.module.css"%(App1)
os.system(mkfile4)


makeDir="mkdir %s"%(App1)
os.system(makeDir)

moveToDirJS="mv ./*.js %s"%(App1)
os.system(moveToDirJS)

moveToDirCSS="mv ./*.css %s"%(App1)
os.system(moveToDirCSS)






#Create app3 first
mkfile1 = "cp basefiles/App2.js %s.js"%(App3)
os.system(mkfile1)
refile1="sed -i 's/App2/%s/g' %s.js"%(App3,App3)
os.system(refile1)

mkfile2 = "cp basefiles/TopInfoBarApp3.js TopInfoBar%s.js"%(App3)
os.system(mkfile2)
refile2="sed -i 's/App1/%s/g' TopInfoBar%s.js"%(App1,App3)
os.system(refile2)
refile2_1="sed -i 's/App2/%s/g' TopInfoBar%s.js"%(App2,App3)
os.system(refile2_1)
refile2_3="sed -i 's/App3/%s/g' TopInfoBar%s.js"%(App3,App3)
os.system(refile2_3)

refile2_1rd="sed -i 's/app1/%s/g' TopInfoBar%s.js"%(redirapp1,App3)
os.system(refile2_1rd)

refile2_3rd="sed -i 's/app2/%s/g' TopInfoBar%s.js"%(redirapp2,App3)
os.system(refile2_3rd)


mkfile3 = "cp basefiles/App2ContentDiv.js %sContentDiv.js"%(App3)
os.system(mkfile3)
refile3="sed -i 's/App2/%s/g' %sContentDiv.js"%(App3,App3)
os.system(refile3)

mkfile4 = "cp basefiles/App2ContentDiv.module.css %sContentDiv.module.css"%(App3)
os.system(mkfile4)



makeDir="mkdir %s"%(App3)
os.system(makeDir)

moveToDirJS="mv ./*.js %s"%(App3)
os.system(moveToDirJS)

moveToDirCSS="mv ./*.css %s"%(App3)
os.system(moveToDirCSS)








