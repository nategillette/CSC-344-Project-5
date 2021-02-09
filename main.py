import os
import re
import subprocess
import tarfile

cFile, cSetlist, cLineCounter = "", "", ""
cljFile, cLjSetlist, cLjLineCounter = "", "", ""
scalaFile, scalaSetlist, ScalaLineCounter = "", "", ""
plFile, plSetlist, plLineCounter = "", "", ""
pyFile, pySetlist, pyLineCounter = "", "", ""

files = ["main.c","core.clj","Main.scala","main.pl","main.py"]
basepath = input("Enter Directory:")
src = basepath
for entry in os.listdir(basepath):
    if entry in files:
                counterList = []
                sorted_list = []
                File = open(entry, "r+")
                lineCounter = subprocess.Popen(["wc", entry],
                                               stdout=subprocess.PIPE)
                (lineCount, err) = lineCounter.communicate()
                counterList.append(lineCount.split()[0])
                List = re.findall("[a-zA-Z0-9]*", File.read())
                for x in List:
                    if not (x in sorted_list) and (len(x) >= 3):
                        sorted_list.append(x)
                sorted_list.sort()

                if entry == 'main.c':
                    cFile = entry
                    cLineCounter = lineCount.split()[0]
                    for x in sorted_list:
                        tableRow = "<tr> | " + x + " </tr>"
                        cSetlist = cSetlist + tableRow
                    cColor = "#DAA520"
                    chtml = open('C_assignment.html', 'w')
                    message = "<body bgcolor="+cColor+"><link><br><a href=" + cFile \
                              + ">C Assignment</a></br></link><h4>Line count is : " + str(cLineCounter) + \
                              " </h4><h4> Identifiers are: <h4><p>" + cSetlist + "<p><body><h3>" \
                                "To go back to assignments page</h3><a href=""index.html"">Back to Assignments</a></body>"
                    chtml.write(message)
                    chtml.close()

                if entry == 'core.clj':
                    cljFile = entry
                    cLjLineCounter = lineCount.split()[0]
                    for x in sorted_list:
                        tableRow = "<tr> | " + x + " </tr>"
                        cLjSetlist = cLjSetlist + tableRow
                    cljColor = "#ADFF2F"
                    cljhtml = open('Clojure_assignment.html', 'w')
                    message = "<body bgcolor="+cljColor+"><link><br><a href=" + cljFile \
                              + ">Clojure Assignment</a></br></link><h4>Line count is : " + str(cLjLineCounter) + \
                              " </h4><h4> Identifiers are: <h4><p>" + cLjSetlist + "<p><body><h3>" \
                                "To go back to assignments page</h3><a href=""index.html"">Back to Assignments</a></body>"
                    cljhtml.write(message)
                    cljhtml.close()


                if entry == 'Main.scala':
                    scalaFile = entry
                    ScalaLineCounter = lineCount.split()[0]
                    for x in sorted_list:
                        tableRow = "<tr> | " + x + " </tr>"
                        scalaSetlist = scalaSetlist + tableRow
                    scaColor = "#FFC0CB"
                    scalahtml = open('Scala_assignment.html', 'w')
                    message = "<body bgcolor="+scaColor+"><link><br><a href=" + scalaFile \
                              + ">Scala Assignment</a></br></link><h4>Line count is : " + str(ScalaLineCounter) + \
                              " </h4><h4> Identifiers are: <h4><p>" + scalaSetlist + "<p><body><h3>" \
                                "To go back to assignments page</h3><a href=""index.html"">Back to Assignments</a></body>"
                    scalahtml.write(message)
                    scalahtml.close()

                if entry == 'main.pl':
                    plFile = entry
                    plLineCounter = lineCount.split()[0]
                    for x in sorted_list:
                        tableRow = "<tr> | " + x + " </tr>"
                        plSetlist = plSetlist + tableRow
                    plColor = "#40E0D0"
                    plhtml = open('Prolog_assignment.html', 'w')
                    message = "<body bgcolor="+plColor+"><link><br><a href=" + plFile \
                              + ">Prolog Assignment</a></br></link><h4>Line count is : " + str(plLineCounter) + \
                              " </h4><h4> Identifiers are: <h4><p>" + plSetlist + "<p><body><h3>" \
                                "To go back to assignments page</h3><a href=""index.html"">Back to Assignments</a></body>"
                    plhtml.write(message)
                    plhtml.close()

                if entry == 'main.py':
                    pyFile = entry
                    pyLineCounter = lineCount.split()[0]
                    pyColor = "#BA55D3"
                    for x in sorted_list:
                        tableRow = "<tr> | " + x + " </tr>"
                        pySetlist = pySetlist + tableRow
                    pyhtml = open('Python_assignment.html', 'w')
                    message = "<body bgcolor="+pyColor+"><link><br><a href=" + pyFile \
                              + ">Python Assignment</a></br></link><h4>Line count is : " + str(pyLineCounter) + \
                              "</h4><h4> Identifiers are: <h4><p>" + pySetlist + "<p><body><h3>" \
                                "To go back to assignments page</h3><a href=""index.html"">Back to Assignments</a>"
                    pyhtml.write(message)
                    pyhtml.close()

html = open('index.html', 'w')
message = """<!DOCTYPE html>
<html>
   <head><meta charset="UTF-8"><title>CSC 344</title></head><body>
                <h1>CSC 344 - Programming Languages</h1><h3>
                This is a collection of Nathan Gillette's CSC 344 assignments</h3>
                <p>Click on the link below to look through my assignments</p>

   <body bgcolor="lightgrey">
      <ul><li><a href="C_assignment.html">C assignment</a>     
     <br><li><a href="Clojure_assignment.html">Clojure Assignment</a>    
      <br><li><a href="Scala_assignment.html">Scala Assignment</a>   
      <br><li><a href="Prolog_assignment.html">Prolog Assignment</a>    
     <br><li><a href="Python_assignment.html">Python Assignment</a>
   </body>
</html>"""

html.write(message)
html.close()

tarName = 'csc344.tar.gz'
tar = tarfile.open(tarName, 'w:gz')
tar.add("./", arcname='csc344')
tar.close()

sendTo = input("Type the email you want to send it to, and press enter: ")
print("You sent the email to " + sendTo)
email = subprocess.Popen('mutt -s "Csc 344 Python Email by Nathan Gillette" ' + sendTo + ' -a ' + tarName + ' ',
                         shell=True)
email.communicate()
