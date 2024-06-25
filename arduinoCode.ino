#include <Ethernet.h>
#include <EthernetUdp.h>
#define green 11 
#define blue 12 

byte mac[] = {
  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED
};
IPAddress ip(192, 168, 137, 3);

unsigned int localPort = 8080;      
char packetBuffer[70];  
char ReplyBuffer[] = "acknowledged";        
EthernetUDP Udp;

void setup() {
  pinMode(green,OUTPUT);
  pinMode(blue,OUTPUT);
  Ethernet.init(10);  
  Ethernet.begin(mac, ip);
  Serial.begin(9600);
  Serial.println("Hello:");
  while (!Serial) {
    Serial.println("Hello:"); 
  }

  if (Ethernet.hardwareStatus() == EthernetNoHardware) {
    Serial.println("Ethernet shield was not found.  Sorry, can't run without hardware. :(");
    while (true) {
      delay(1); 
    }
  }
  if (Ethernet.linkStatus() == LinkOFF) {
    Serial.println("Ethernet cable is not connected.");
  }

  // start UDP
  Udp.begin(localPort);
}

void loop() {
  int packetSize = Udp.parsePacket();
  if (packetSize) {
    Serial.print("Received packet of size ");
    Serial.println(packetSize);
    Serial.print("From ");
    IPAddress remote = Udp.remoteIP();
    for (int i=0; i < 4; i++) {
      Serial.print(remote[i], DEC);
      if (i < 3) {
        Serial.print(".");
      }
    }
    Serial.print(", port ");
    Serial.println(Udp.remotePort());

    Udp.read(packetBuffer, 70);
    Serial.println("Contents:");
    Serial.println(packetBuffer);
    
    String sub1=packetBuffer;
    int index2 = sub1.indexOf('(');
    int index3 = sub1.indexOf(')');
    String sub_S = sub1.substring(index2+1,index3);
    int numOfAxis = getElements(sub_S,',');
    
    Serial.println("Number Of Data = ");
    Serial.println(numOfAxis);
    for(int i=0;i<=numOfAxis;i++)
    {
      String data = getValue(sub_S,',',i);
      Serial.print("data number ");
      Serial.print(i);
      Serial.print(" = ");
      Serial.println(data);
    }
    
    String but1=getValue(sub_S,',',4);
    Serial.println(but1.toInt());
    
//    if(but1.toInt()==1)
//    {
//      digitalWrite(green,LOW);
//      digitalWrite(blue,HIGH);
//      
//    }
//     else if(but1.toInt()==0)
//    {
//      digitalWrite(green,HIGH);
//      digitalWrite(blue,LOW);
//      
//    }
    
    Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());
    Udp.write(ReplyBuffer);
    Udp.endPacket();
    memset(packetBuffer, 0, 70);
  }
  delay(10);
}

int getElements(String data, char separator)
{
  int index = data.length()-1;
  int counter=0;
  for(int i=0;i<=index;i++)
  {
    if(data.charAt(i)==separator)
    {
      counter++;
    }
    
   }
   return counter;
}



String getValue(String data, char separator,int number )
{ 
  int sepCounter = 0;
  int subArray[] = {0, -1};
  int maxIndex = data.length()-1;

  for(int i=0; i<=maxIndex && sepCounter<=number; i++){
    if(data.charAt(i)==separator || i==maxIndex){
        sepCounter++;
        subArray[0] = subArray[1]+1;
        subArray[1] = (i == maxIndex) ? i+1 : i;
    }
  }

  return sepCounter>number ? data.substring(subArray[0], subArray[1]) : "";
}
