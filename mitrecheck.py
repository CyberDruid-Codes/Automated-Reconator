##
#Importing Section
from pyattck import Attck
##

##
#Global Variables and Objects Declaration
attack = Attck()
techniq_count = 0
report_string = ""
techniques_id = []
subtechnique_id =[]
##

#Takes the boolean values (indicating the possible vulnerable objects are found) and searches for MITRE Techniques/ Sub-Techniques
def mitre(vulnerabilities, network_scan, products, hardware):
    
    global report_string, techniq_count

    #Checking if the requirements for the specified techniques exist
    def techniquescheck():
        global techniques_id

        if vulnerabilities:
            techniques_id.append('T1595')
            techniques_id.append('T1587')
            techniques_id.append('T1588')
        elif network_scan:
             techniques_id.append('T1595')
        if products or hardware: 
             techniques_id.append('T1592')

    #Iterates trough the Mitre matrix and based on the findings, returns the specific techniques and mitigations
    def MITREcheck():
        global techniq_count, techniques_id ,report_string ,subtechnique_id

        for technique in attack.enterprise.techniques:
            if 'PRE' in technique.platforms:
                if technique.id in techniques_id:
                    techniq_count +=1
                    report_string = report_string + str(techniq_count)+ ".Technique" + "\n" + "ID: " + technique.id + " - " + technique.name + "\n" + "For More Information: " + technique.wiki + "\n \n" + "•Mitigation(s)"+ "\n"
                    for mitigation in technique.mitigations:
                        report_string = report_string + "•ID: " + mitigation.id +  " - " + mitigation.name  + "\n" + "•For More Information: " + mitigation.wiki + "\n \n" + "•Subtechnique(s)"+ "\n"
                    

                    for subtechnique in technique.subtechniques:

                        #Active Scanning Subtechnique 1
                        if subtechnique.id == "T1595.001":
                            if network_scan:
                                report_string = report_string + "•ID: " + subtechnique.id +  " - " + subtechnique.name + "\n" + "•For More Information: " + subtechnique.wiki + "\n \n"
                                subtechnique_id.append('T1595.001')
                               
                        #Active Scanning/Obtain Capabilities/Develop Capabilties Subtechnique 2-5
                        elif subtechnique.id in ('T1595.002', 'T1587.004', 'T1588.006', 'T1588.005'): 
                            if vulnerabilities:
                                report_string = report_string + "•ID: " + subtechnique.id +  " - " + subtechnique.name + "\n" + "•For More Information: " + subtechnique.wiki + "\n \n"
                                subtechnique_id.append('T1595.002')
                                subtechnique_id.append('T1587.004')
                                subtechnique_id.append('T1588.006')
                                subtechnique_id.append('T1588.005')

                        #Gather Victim Host Information Subtechnique 1
                        elif subtechnique.id == "T1592.001": 
                            if hardware:
                                report_string = report_string + "•ID: " + subtechnique.id +  " - " + subtechnique.name + "\n" + "•For More Information: " + subtechnique.wiki + "\n \n"
                                subtechnique_id.append('T1592.001')

                        #Gather Victim Host Information Subtechnique 2
                        elif subtechnique.id == "T1592.002": 
                            if products:
                                report_string = report_string + "•ID: " + subtechnique.id +  " - " + subtechnique.name + "\n" + "•For More Information: " + subtechnique.wiki + "\n \n"
                                subtechnique_id.append('T1592.002')



    #calls the methods 
    techniquescheck()
    MITREcheck()
    
    #formats the results for the report, into one string  
    report_string = report_string + "\n" + "The number of techniques found is " + str(techniq_count) + " out of 4" + "\n" +"(This tool searches for specific techniques, as the other are out of scope)"

    #Adding one more node, which is named Network, the central node
    techniques_id.insert(0,"Network")

    return report_string , techniques_id , subtechnique_id
    


