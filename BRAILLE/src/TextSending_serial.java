
import static java.lang.Thread.sleep;
import jssc.SerialPort;
import jssc.SerialPortException;


public class TextSending_serial 
{
    
    
    void Senddata1(String sdt) throws InterruptedException
    {
       
        SerialPort serialPort = new SerialPort("COM6");
        
       
        try 
        {
          
    serialPort.openPort();
serialPort.setParams(SerialPort.BAUDRATE_9600,SerialPort.DATABITS_8,SerialPort.STOPBITS_1,SerialPort.PARITY_NONE);
          
sleep(2000);
System.out.print(sdt);
serialPort.writeString(sdt);

 serialPort.closePort();



        }
     
        catch (SerialPortException ex)
        
        {
            //ex.printStackTrace();
            System.out.println(ex);
        }
    }  
    
   

public static void main(String[] args) throws InterruptedException 
    {
        
      // TextSending_serial obj=new TextSending_serial();
       // obj.Senddata1("ABC");
      
    }

}