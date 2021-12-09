##
#Import Section
import nmap
from vulnclass import vulncls
from cvecheck import cvechecks
import json
##

#Nmap scan method
def nmapScan(ipentry,vulners_enabled):
    ##
    #instantiate nmap.PortScanner object
    nm = nmap.PortScanner()

    #scans for the top 10.000 ports 
    scan = nm.scan(ipentry,'1-10000', '-v -sS -sV -sC -A -O')
    
    # Get nmap scan informations
    scaninfor = nm.scanstats()

    # Gets all hosts that were scanned
    hosts = nm.all_hosts() 

    # Gets the host status
    ipstatus = nm[ipentry].state() 

    # Finds protocols found tcp/udp 
    scanprotocols = nm[ipentry].all_protocols() 
    prot = 'tcp'

    # Finds open ports
    openports = nm[ipentry][prot].keys()

    # Finds the details and outputs in CSV version 
    portsdetails = nm.csv() 
    ##

    ##
    #Formats the results into a readable format 
    openportsinfo = ' '
    vuln_results = " "
    products_found = False
    cveres = ""
    vuln_found = ""
    for port in openports:
        #Scans each port for detailed information ( Name, product, state(open/closed) )
       products =  nm[ipentry][prot][port]['product']
       portsinfo = 'Port : %s \n State : %s     Name: %s     Product: %s     CPE: %s' % (port, nm[ipentry][prot][port]['state'], nm[ipentry][prot][port]['name'], products , nm[ipentry][prot][port]['cpe'])

       #Checks if any products found for the MITRE Framework
       if products:
           products_found =True 

       #Creates a string with the ports, to be displayed on the GUI
       openportsinfo = openportsinfo + '\n' + '\n' + portsinfo
       vuln_return = " "
       #passes the cpe to the vuln search and searches based on cpe/version and product/version for vulnerabilities and makes sure the module is enabled
       if nm[ipentry][prot][port]['version'] and vulners_enabled == True:
            try:
                 #formats the products and version into a format accepted by vulnsearch
                 software_prod = products
                 software_version = nm[ipentry][prot][port]['version']
                 vulnvar = nm[ipentry][prot][port]['cpe'] + ":" + software_version

                 #Parses to the actual class and waits for results
                 vuln_return,vuln_found = vulncls(str(vulnvar),software_prod,software_version)

            except:
                 print("An error has occured while searching for the Vulnerability")
       else:
            vuln_return = "The search for vulnerabilities is not possible for this port as the product does not have the version specified."

       #creates a string for vulnerabilities only if the vulners has been configured. Otherwise, it returns a generic response. 
       if vulners_enabled == True:
            #Creates the final string for the Vuln search that can be added to the report
            vuln_results = vuln_results + "\n" + "\n" + "Search for Port: " + str(port) +"\n"+ str(vuln_return) + "\n"
       else:
            vuln_results = "Vulners Module is not enabled. No data available. "
            vuln_found = False

       #This checks for the top 15 known vulnerabilities 
       try:
           #parses the products found and checks for the top 15 CVE's
           cveres = cveres + "\n" + "CVE Check for "+ str(products) + "\n \n"+ str(cvechecks(products)) + "\n"
       except:
           print("CVE Call has failed..")
    ##
    
    #Formats the result into a more readable format
    display_str = 'Hosts Found: %s \n \n Hosts Information: %s \n \n Host Status: %s \n \n Protocols found: %s \n \n Open Ports: %s \n \n Ports Details: \n %s ' % (hosts,scaninfor,ipstatus,scanprotocols,openports,portsdetails)
    
    #Modifies the Json object to a string so that it can be processed by the Deep learning Class 
    rawscanres = json.dumps(scan)

    #Returns the results to the Main Class
    return openportsinfo , display_str , cveres , rawscanres , vuln_results , vuln_found , products_found
