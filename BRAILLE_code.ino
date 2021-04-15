

    
int len;
int i=0;

String str;
//========OUTPUT PIN======

int D1 = 2;
int D2 = 3;
int D3 = 4;
int D4 = 5;
int D5 = 6;
int D6 = 7;

void setup() 
{
  
  pinMode(D1, OUTPUT);
  pinMode(D2, OUTPUT);
  pinMode(D3, OUTPUT);
  pinMode(D4, OUTPUT);
  pinMode(D5, OUTPUT);
  pinMode(D6, OUTPUT);
  
  Serial.begin(9600);

}


void loop() 
{


    while(Serial.available()== 0)
    {
    }
        str = Serial.readString();
  
      str.toUpperCase();
      
    for(;i<str.length();i++)
     {
      Serial.println(str[i]);
  
 //============================================
  switch (str[i]) 
  {
      case 'A': letterPrint(1,0,0,0,0,0);break;
      case 'B': letterPrint(1,0,1,0,0,0);break;
      
      case 'C': letterPrint(1,1,0,0,0,0);break;
      
      case 'D': letterPrint(1,1,0,1,0,0); break;
      
      case 'E': letterPrint(1,0,0,1,0,0); break;
      
      case 'F': letterPrint(1,1,1,0,0,0); break;
      
      case 'G': letterPrint(1,1,1,1,0,0); break;
      
      case 'H': letterPrint(1,0,1,1,0,0); break;
      
      case 'I': letterPrint(0,1,1,0,0,0); break;
      
      case 'J':  letterPrint(0,1,1,1,0,0); break;
      
      case 'K':  letterPrint(1,0,0,0,1,0); break;
      
      case 'L':  letterPrint(1,0,1,0,1,0);break;
      
      case 'M':  letterPrint(1,1,0,0,1,0);break;
      
      case 'N':  letterPrint(1,1,0,1,1,0);break;
      
      case 'O':  letterPrint(1,0,0,1,1,0);break;
      
      case 'P':  letterPrint(1,1,1,0,1,0);break;
      
      case 'Q':  letterPrint(1,1,1,1,1,0);break;
      
      case 'R':  letterPrint(1,0,1,1,1,0);break;
      
      case 'S':  letterPrint(0,1,1,0,1,0);break;
      
      case 'T':  letterPrint(0,1,1,1,1,0);break;
      
      case 'U':  letterPrint(1,0,0,0,1,1);break;
      
      case 'V':  letterPrint(1,0,1,0,1,1);break;
      
      case 'W':  letterPrint(0,1,1,1,0,1);break;
      
      case 'X':  letterPrint(1,1,0,0,1,1);break;
      
      case 'Y':  letterPrint(1,1,0,1,1,1);break;
      
      case 'Z':  letterPrint(1,0,0,1,1,1);break;
      
      default:
        Serial.println("SORRY");
       
        }
 letterPrint(0,0,0,0,0,0);
     }
     Serial.end();  

 //=================STOP============================
 
  //================================================
 
}
  
//===============================================
void letterPrint(int d1sta,int d2sta,int d3sta,int d4sta,int d5sta,int d6sta) {
  
    digitalWrite(D1, d1sta);
  
    digitalWrite(D2, d2sta);
  
    digitalWrite(D3, d3sta);
  
    digitalWrite(D4, d4sta);
  
    digitalWrite(D5, d5sta);

    digitalWrite(D6, d6sta);
    delay(2000);
}

