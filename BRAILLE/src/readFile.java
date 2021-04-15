
import java.io.*;
import javax.swing.JFileChooser;



public class readFile
{
  
    
    
    public String readFile1(String st)throws Exception 
    {
      String line;
      String skills="";
    //-------------------------------------------------------------------------  
        
        //===============================================================================            
            BufferedReader input = new BufferedReader(new FileReader(st));

        int co=0,srt=0,ed=0;


        while ((line = input.readLine()) != null) 
        {
	      
            skills=skills+line;
        }

             return skills;

    }
	  


}