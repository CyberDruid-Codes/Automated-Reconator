```html
       d8888          888                                   888                 888      8888888b.                                             888                    
      d88888          888                                   888                 888      888   Y88b                                            888                    
     d88P888          888                                   888                 888      888    888                                            888                    
    d88P 888 888  888 888888 .d88b.  88888b.d88b.   8888b.  888888 .d88b.   .d88888      888   d88P .d88b.   .d8888b .d88b.  88888b.   8888b.  888888 .d88b.  888d888 
   d88P  888 888  888 888   d88""88b 888 "888 "88b     "88b 888   d8P  Y8b d88" 888      8888888P" d8P  Y8b d88P"   d88""88b 888 "88b     "88b 888   d88""88b 888P"   
  d88P   888 888  888 888   888  888 888  888  888 .d888888 888   88888888 888  888      888 T88b  88888888 888     888  888 888  888 .d888888 888   888  888 888     
 d8888888888 Y88b 888 Y88b. Y88..88P 888  888  888 888  888 Y88b. Y8b.     Y88b 888      888  T88b Y8b.     Y88b.   Y88..88P 888  888 888  888 Y88b. Y88..88P 888     
d88P     888  "Y88888  "Y888 "Y88P"  888  888  888 "Y888888  "Y888 "Y8888   "Y88888      888   T88b "Y8888   "Y8888P "Y88P"  888  888 "Y888888  "Y888 "Y88P"  888     
```                                                                                                                                                                     
                  

           
           
#### ----Description---- ####

The Automated Agent-Based Model for Penetration Testing is a tool that tackles one main problem, it cuts the complexity of the First Step in the Penetration Testing Process 
(Reconnaissance) and interpretation of the results, by utilizing Deep Neural Networks.

#### ----Why use the Automated Reconator?---- ####

The tool's Aim is to Scan the Network (Recon) and check for possible vulnerabilities / CVE’s, interpret the scan results using a Deep Learning model and generate a detailed Report which is visible, easy to read and understand.        
This will help the cybersecurity experts to spend less on this first step (Reconnaissance), without missing any information, the report being easy to present, as by gathering the results and automatically generating a detailed PDF file. 

#### ----Python modules used---- ####

The Following Python modules(as the guidelines or foundations for the components): Tkinter for the GUI, Nmap for the network scan, VulnSearch for the vulnerability search, ReportLab for 
the automated PDF Generation, tf.keras for the deep neural network model, Pyattck for the MITRE ATT&CK Framework and Networkx for the techniques/sub-techniques Graph Generator.

#### ----Prerequisites---- ####
                                                                                                                                                                      
The script requires Python 3.8 installed, as a minimum requirement.          
For the script to run fully, Python 3.7 needs to be installed too. This is for the optional deep learning module to run, as it utilizes tf.keras.

The optional vulnerability check module requires an api key added on line 11 of the "vulnclass.py" file. 
The API key can be requested from here, for free! -> https://vulners.com/ (General API Key) 

The following python modules need to be installed: 

-For Python 3.8: 
https://pypi.org/project/vulners/
https://pypi.org/project/python-nmap/
https://pypi.org/project/pyattck/
https://pypi.org/project/reportlab/3.5.59/
https://pypi.org/project/networkx/2.5/
https://pypi.org/project/matplotlib/

-For Python 3.7:
https://pypi.org/project/nltk/
https://pypi.org/project/numpy/
https://pypi.org/project/tensorflow/

To install them on different versions, you can do: python3.x -m pip install <package name> 
(Note: some of these modules might be on python by default. It will notify you if the module is already installed) 

#### ----Prerequisites / Extra Setup ---- ####
The following modules need to be edited: cyberbotcall.py and vulncls.py. 

The cyberbotcall.py has to have the path of the two scripts (i.e. cyberbot and learning.py). You can easily add that once you have the scripts locally.
The Vulncls has to have your API key at the top of the script. 

Here is an explanation on how to have 2 python versions running on the same machine(For the deep learning module): 
https://towardsdatascience.com/installing-multiple-alternative-versions-of-python-on-ubuntu-20-04-237be5177474

#### ----How to use---- ####

Step 1: Download/clone the scripts locally                             
Step 2: Check the Prerequisites                     
Step 3: Run the Pentestertool.py (double click or through any CLI)                           
Step 4: Select the appropriate values for the 2 optional components (Have they been configured? No -> Press False)            
Step 5: Input the IP and Press Submit (Make sure the host is reachable from your machine)             
Step 6: Wait for the scripts to run              
Step 7: Press on the "Generate Report" button (This and the individual files will be generated at the location of the script)                  
       
Note - Make sure the script has the permission to run on your machine and that the host is reachable from your machine     


#### ----Demo---- ####
You can watch my youtube video to see the script in action!        
Link:          
https://www.youtube.com/watch?v=GYNTDR-vtng&t=5s&ab_channel=CyberDruid
