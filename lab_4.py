import os

#stage= os.environ["STAGE"].upper()
#unset STAGE and then echo $STAGE 
stage = os.getenv("STAGE", "dev").upper() #sets dev as the default value

output = f"We're running in {stage}"

if stage.startswith("PROD"):
        output = "DANGER!!! - " + output
        
print (output)