##
#Import Section
from reportlab.pdfgen import canvas 
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.utils import ImageReader
from textwrap import wrap
##

#Report Method, Formats and generates the PDF
def report_class(hostname,cvereport,vulnerabilityres,mitresearch):

    ####
    #File Details
    filename = "Report.pdf"
    docTitle = "Full Scan Report"

    #Titles
    MainTitle = "The report for "+ hostname

    #Subtitles
    SubtitlePgOne = "Quick Scan Findings"
    SubtitlePgTwo = "Vulnerabilities Search"
    SubtitlePgThree = "Results for the Top 15 CVE Check"
    SubtitlePgFour = "CyberBot Scan & Intepretation"
    SubtitlePgFive = "MITRE ATT&CK Techniques Search"
    SubtitlePgSix = "Full Nmap Scan"
    SubtitlePgSeven = "MITRE ATT&CK Visual Representation"

    #Context added for each page 
    ContextPgOne = "\n" + "\n" +"Tool Details:"+"\n"+"\n"+ "The Network Scan was performed using NMAP, a network mapper and discovery tool used to to :" + "\n" +"1.Find live hosts on a network"+ "\n" + "2.Perform port scanning"+ "\n" + "3.Ping sweeps" + "\n" +"4.OS detection"+ "\n" + "5.Version detection"+ "\n"+"\n"+"For more information about the tool, visit: " + 'https://nmap.org/'
    ContextPgTwo = "\n" + "\n" +"Tool Details:"+"\n"+"\n"+ "The Scan was performed using VulnSearch, one of the biggest Vulnerability Database available." + "\n" + "The search was performed using the products found in the Network Scans and their versions." + "\n" +"\n"+ "For more information about the tool, visit: "+ 'https://vulners.com/'
    ContextPgThree = "\n" + "\n" +"Tool Details:"+"\n"+"\n"+"The Top 15 CVE Check was made based on the Products found. "+ "\n" + "The CVE's selected are based on the information found on the CISA website and NIST Database. " + "\n"+"\n"+ "For more information about the tool, visit: "+"\n"+"CISA: "+'https://us-cert.cisa.gov/ncas/alerts/aa20-133a' + "\n" + "NIST: " +'https://nvd.nist.gov/'
    ContextPgFour = "\n" + "\n" +"Tool Details:"+"\n"+"\n"+ "The Deep Learning Neural Network interpretation was done using Keras."+ "\n" + "Using the Natural Language Toolkit(NLTK), the neural network detected and categorised any cpe's found. "+"\n"+"\n"+"For more information about the tool, visit: "+ "\n" +"Keras- "+'https://keras.io/' + "\n" + "NlTK- " + 'https://www.nltk.org/' + "\n" + "Tensorflow- "+ 'https://www.tensorflow.org/'
    ContextPgFive = "\n" + "\n" +"Tool Details:"+"\n"+"\n"+ "The MITRE ATT&CK Framework was used to find possible techniques/sub-techniques and mitigations."+ "\n" + "The PyAttck module was used to retrieve techniques and its details." +"\n"+ "MITRE ATT&CK is a globally-accessible knowledge base of adversary tactics and techniques based on"+"\n"+"real-world observations of cyber security threats." + "\n"+"\n"+ "For more information about the tool, visit: "+ 'https://attack.mitre.org/'

    #Deep learning Results
    cyber_scan = open("cyberbotreport.txt", "r")
    cyber_res = cyber_scan.read()

    #Scan Results in a Formatted Way
    textLines = open("FormattedScan.txt", "r")
    formatted_res = textLines.read()

    #Raw Nmap Scan results
    nmapscan = open("NmapScan.txt", "r")
    nmap_raw = nmapscan.read()

    #Retrieving the image
    img = open("mitre_visualization.jpeg", "rb")
    mitre_graph = ImageReader(img)
    ####

    #####
    #Creating the document
    pdf = canvas.Canvas(filename)
    pdf.setTitle(docTitle)
    ####

    ####
    #Setting the Title for the First Page
    pdf.setFont('Times-Roman',30)
    pdf.drawCentredString(300,770, MainTitle)
    #####

    #####
    #Setting the Subtitle for Page 1 
    pdf.setFont('Times-Roman', 22)
    pdf.drawCentredString(290,720, SubtitlePgOne) 
    #Draw a line of separation
    pdf.line(30,710,550,710)
    ####

    ####
    #Add the context for Page 1
    pdf.setFont('Times-Roman', 13)
    pdf.drawString(40, 685, "Quick NMAP Scan Results:")
    pdf.setFont('Times-Roman', 11)
    p1 = pdf.beginText()
    p1.setTextOrigin(50, 665)
    p1.textLines(formatted_res+ContextPgOne)
    pdf.drawText(p1)
    #pdf.drawString(50, 665, formatted_res)
    #Showpage ends the current page
    pdf.showPage()
    ####

    ####
    #Setting the Subtitle for Page 2 
    pdf.setFont('Times-Roman', 22)
    pdf.drawCentredString(290,770, SubtitlePgTwo) 
    #Draw a line of separation
    pdf.line(30,760,550,760)
    ####

    ####
    #Add the context for Page 2
    pdf.setFont('Times-Roman', 13)
    pdf.drawString(40, 685, "The following Vulnerabilities have been found: ")
    pdf.setFont('Times-Roman', 11)
    p6 = pdf.beginText()
    p6.setTextOrigin(50, 665)
    p6.textLines(vulnerabilityres+ContextPgTwo)
    pdf.drawText(p6)
    #Showpage ends the current page
    pdf.showPage()
    ####


    ####
    #Setting the Subtitle for Page 3
    pdf.setFont('Times-Roman', 22)
    pdf.drawCentredString(290,770, SubtitlePgThree) 
    #Draw a line of separation
    pdf.line(30,760,550,760)
    ####

    ####
    #Add the context for Page 3
    pdf.setFont('Times-Roman', 13)
    pdf.drawString(40, 685, "CVE check results:")
    pdf.setFont('Times-Roman', 11)
    p2 = pdf.beginText()
    p2.setTextOrigin(50, 665)
    p2.textLines(cvereport + ContextPgThree)
    pdf.drawText(p2)
    #Showpage ends the current page
    pdf.showPage()
    ####


    ####
    #Setting the Subtitle for Page 4
    pdf.setFont('Times-Roman', 22)
    pdf.drawCentredString(290,770, SubtitlePgFour) 
    #Draw a line of separation
    pdf.line(30,760,550,760)
    ####

    ####
    #Add the context for Page 4
    pdf.setFont('Times-Roman', 13)
    pdf.drawString(40, 685, "Deep Learning Scan Interpretation:")
    pdf.setFont('Times-Roman', 11)
    p3 = pdf.beginText()
    p3.setTextOrigin(50, 665)
    p3.textLines(cyber_res + ContextPgFour)
    pdf.drawText(p3)
    #Showpage ends the current page
    pdf.showPage()
    ####


    ####
    #Setting the Subtitle for Page 5
    pdf.setFont('Times-Roman', 22)
    pdf.drawCentredString(290,770, SubtitlePgFive) 
    #Draw a line of separation
    pdf.line(30,760,550,760)
    ####

    ####
    #Add the context for Page 5
    pdf.setFont('Times-Roman', 13)
    pdf.drawString(40, 685, "MITRE ATT&CK Framework techniques found")
    pdf.setFont('Times-Roman', 11)
    p4 = pdf.beginText()
    p4.setTextOrigin(50, 665)
    p4.textLines(mitresearch + ContextPgFive)
    pdf.drawText(p4)
    #Showpage ends the current page
    pdf.showPage()
    ####


    ####
    #Setting the Subtitle for Page 7
    pdf.setFont('Times-Roman', 22)
    pdf.drawCentredString(290,770, SubtitlePgSeven) 
    #Draw a line of separation
    pdf.line(30,760,550,760)
    ####

    ####
    #Add the subtitle and image for Page 7
    pdf.setFont('Times-Roman', 11)
    pdf.drawString(40, 685, "Techniques and Subtechniques represented as a Star Graph")
    pdf.drawImage(mitre_graph,x=20,y=165,width=550,height=500,preserveAspectRatio = True,showBoundary = True)
    #Showpage ends the current page
    pdf.showPage()
    ####


    ####
    #Setting the Subtitle for Page 6
    pdf.setFont('Times-Roman', 22)
    pdf.drawCentredString(290,770, SubtitlePgSix) 
    #Draw a line of separation
    pdf.line(30,760,550,760)
    ####

    ####
    #Add the context for Page 6
    pdf.setFont('Times-Roman', 13)
    pdf.drawString(40, 685, "Raw Nmap Scan Results: ")
    pdf.setFont('Times-Roman', 11)
    p5 = pdf.beginText()
    p5.setTextOrigin(50, 665)
    wrapped_text = "\n".join(wrap(nmap_raw,105))
    p5.textLines(wrapped_text)
    pdf.drawText(p5)
    #Showpage ends the current page
    pdf.showPage()
    ####


    ####
    #Saving and closing of the PDF
    pdf.save()
    ####