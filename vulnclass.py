##
#Import Section
import vulners
##

##
#Vulerability Search method using Vulners Database
def vulncls(cpe_info,product,product_version):

    """This method has the role of searching the database for possible vulnerabilities"""
    vulners_api = vulners.Vulners(api_key="<Add your API KEY HERE>")
    vuln_results = " "
    vuln_found  = False
  

    #Searches for Vulnerabilities based on the CPE
    cpe_results = vulners_api.cpeVulnerabilities(cpe_info)
    cpe_exploit_list = cpe_results.get('exploit')
    cpe_vulnerabilities_list = [cpe_results.get(key) for key in cpe_results if key not in ['info', 'blog', 'bugbounty']]

    #The Module is not perfect and sometimes returns a blank object so a check is needed in case nothing has been found
    vuln_cpetitle = "  CPE Based vulnerabilities "  + "\n"
    if cpe_vulnerabilities_list:
          vuln_results = vuln_cpetitle +"  " + cpe_vulnerabilities_list + "\n"
          vuln_found = True
    else:
        vuln_results = vuln_cpetitle + "  No Vulnerabilties have been found." + "\n"

    #Searches for Software vulnerabilties based on the Products 
    results = vulners_api.softwareVulnerabilities(product,product_version)
    exploit_list2 = results.get('exploit')
    vulnerabilities_list2 = [results.get(key) for key in results if key not in ['info', 'blog', 'bugbounty']]

    #The Module is not perfect and sometimes returns a blank object so a check is needed in case nothing has been found
    vuln_softwaretitle = "  Product based vulnerabilities " + "\n"
    if vulnerabilities_list2:
        vuln_results = vuln_results + "\n"+ vuln_softwaretitle +"  " + vulnerabilities_list2
        vuln_found = True
    else:
        vuln_results = vuln_results + "\n" + vuln_softwaretitle + "  No Vulnerabilities have been found."
        

    return vuln_results , vuln_found
##
