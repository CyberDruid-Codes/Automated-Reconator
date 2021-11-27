##
def cvechecks(product):
   #checks each known CVE based on the parsed product
   cvevulncheck = 0
   cvestr = "Your System is vulnerable to the following CVE's: " + "\n"
   negativecve = "This part of the System is not vulnerable to the Top 15 CVE's."+ "\n" +"After the check, no signs of:"+"\n"+"CVE_2017_11882, CVE_2017_0199, CVE_2017_5638, CVE_2012_0158, CVE_2019_0604, CVE_2017_0143," + "\n" + "CVE_2018_4878, CVE_2017_8759, CVE_2015_1641, CVE_2018_7600 and CVE_2019_19781 has been found."+ "\n " + "Check the link below for more details about the CVE's"
   CVE_2017_11882(product)
   CVE_2017_0199(product)
   CVE_2017_5638(product)
   CVE_2012_0158(product)
   CVE_2019_0604(product)
   CVE_2017_0143(product)
   CVE_2018_4878(product)
   CVE_2017_8759(product)
   CVE_2015_1641(product)
   CVE_2018_7600(product)
   CVE_2019_19781(product)

   if cvevulncheck != 0:
       return cvestr
   else: 
       return negativecve
##

##
#Checks the environment for possible CVE's based on the Product and hints to possible solutions
def CVE_2017_11882(product):
    if product == "Microsoft Office 2007 SP3" or product == "Microsoft Office 2010 SP2" or product == "Microsoft Office 2013 SP1" or product == "Microsoft Office 2016":
        
        cvename = "CVE-2017-11882"
        cvevulncheck +=1
        cvestr += cvestr + " " + cvename + "\n"
    else:
        pass 

def CVE_2017_0199(product):
    if product == "Microsoft Office 2007 SP3" or product == "Microsoft Office 2010 SP2" or product == "Microsoft Office 2013 SP1" or product == "Microsoft Office 2016" or product == "Windows 8.1" or product == "Windows 7 SP1" or product == "Windows Server 2008 SP2" or product == " Microsoft Windows Vista SP2":
        
        cvename = "CVE-2017-0199"
        cvevulncheck +=1
        cvestr += cvestr + " " + cvename + "\n"
    else:
         
        pass

def CVE_2017_5638(product):
   
   if product == "Apache Struts 2" or product.find("Apache Struts 2") == True:
        
        cvename = "CVE-2017-5638"
        cvevulncheck +=1
        cvestr += cvestr + " " + cvename + "\n"
   else:
       pass
        

def CVE_2012_0158(product):
   if product == "Microsoft Office 2003 SP3" or product == "Microsoft Office 2007 SP2" or product == "Microsoft Office 2007 SP3" or product == "Microsoft Office 2010 Gold" or product == "Microsoft Office 2003 Web Components SP3" or product == "SQL Server 2000 SP4" or product == "SQL Server 2005 SP4" or product == "SQL Server 2008 SP2" or product == "SQL Server 2008 SP3" or product == "SQL Server 2000 R2" or product == "BizTalk Server 2002 SP1" or product == "Commerce Server 2002 SP4" or product == "Commerce Server 2007 SP2" or product == "Commerce Server 2009 Gold" or product == "Commerce Server 2009 R2" or product == "Visual FoxPro 8.0 SP1" or product == "Visual FoxPro 9.0 SP2" or product == "Visual Basic 6.0":
        
        cvename = "CVE-2012-0158"
        cvevulncheck +=1
        cvestr += cvestr + " " + cvename + "\n"
   else:
        pass
        

def CVE_2019_0604(product):
    if product == "Microsoft SharePoint":
        #print(product + " "+ "is possibly vulnerable to CVE-2019-0604")
        cvename = "CVE-2019-0604"
        cvevulncheck +=1
        cvestr += cvestr + " " + cvename + "\n"
    else:
        pass
        

def CVE_2017_0143(product):
  if product == "Microsoft Windows Vista SP2" or product == "Windows Server 2008 SP2" or product == "Windows Server 2008 R2 SP1" or product == "Windows 7 SP1" or product == "Windows 8.1" or product == "Windows Server 2012 Gold" or product == "Windows Server 2012 Gold R2" or product == "Windows RT 8.1" or product == "Windows 10 Gold 1511" or product == "Windows 10 Gold 1607" or product == "Windows Server 2016":
        
        cvename = "CVE-2017-0143"
        cvevulncheck +=1
        cvestr += cvestr + " " + cvename + "\n"
  else:
      pass
      

def CVE_2018_4878(product):
     #add a version check for this
    if product == "Adobe Flash Player":
       
        cvename = "CVE-2018-4878"
        cvevulncheck +=1
        cvestr += cvestr + " " + cvename + "\n"
    else:
        pass
        

def CVE_2017_8759(product):
   if product == "Microsoft .NET Framework 2.0" or product == "Microsoft .NET Framework 3.5" or product == "Microsoft .NET Framework 3.5.1" or product == "Microsoft .NET Framework 4.5.2" or product == "Microsoft .NET Framework 4.6" or product == "Microsoft .NET Framework 4.6.1" or product == "Microsoft .NET Framework 4.6.2" or product == "Microsoft .NET Framework 4.7":
        
        cvename = "CVE-2017-8759"
        cvevulncheck +=1
        cvestr += cvestr + " " + cvename + "\n"
   else:
       pass
         

def CVE_2015_1641(product):
    if product == "Microsoft Word 2007 SP3" or product == "Office 2010 SP2" or product == "Microsoft Word 2010 SP2" or product == "Microsoft Word 2013 SP1" or product == "Microsoft Word 2013 RT SP1" or product == "Microsoft Word for Mac 2011" or product == "Microsoft Office Compatibility Pack SP3" or product == "Word Automation Services"  or product == "Microsoft Office Web Apps Server 2010 SP2" or product == "Microsoft Office Web Apps Server 2013 SP1":
        
        cvename = "CVE-2015-1641"
        cvevulncheck +=1
        cvestr += cvestr + " " + cvename + "\n"
    else:
        pass
        

def CVE_2018_7600(product):
   if product == "Drupal" or product.find("Drupal") == True:
        
        cvename = "CVE-2018-7600"
        cvevulncheck +=1
        cvestr += cvestr + " " + cvename + "\n"
   else:
       pass
       
def CVE_2019_19781(product):
     if product == "Citrix Application Delivery Controller" or product == "Citrix Gateway" or product == "Citrix SDWAN WANOP":
        
        cvename = "CVE-2019-19781"
        cvevulncheck +=1
        cvestr += cvestr + " " + cvename + "\n"
     else:
         pass

##