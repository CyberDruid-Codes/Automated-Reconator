##
#Import Section
import os
##

##
#Method calls for the Deep Learning Algorithm using Command Prompt (locally) or trains it (based on the boolean variable)
#This is needed as the main codebase runs on python 3.8 and tf.keras can only run on python 3.7
def callortrain(call):
    if call == True:
        os.system('python3.7 <Path to the script>\\cyberbot.py')

    else:
        os.system('python3.7 <Path to the script>\\learningAlg.py')
##
