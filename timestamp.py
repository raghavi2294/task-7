
import datetime 
  
filename = datetime.datetime.now()
      
def create_file(): 
 
    with open(filename.strftime("%d %B %Y")+".txt", "w") as file: 
     file.write("13 May 2024")
    
create_file() 
