/*recebe tres char pela serial e acende os leds de acordo com a ordem de chegada.
 * Se chegar a ordem 110, os dois primeiros leds se acendem. Se chegar a ordem 101
 * apenas o primeiro e o terceiro led se acendem.
 */

char dado[3];
int LEDS[3]={10,11,12};
int b=0;
int i=0;
  
void setup() {
  Serial.begin(9600); // abre a porta serial, configura a taxa de transferência para 9600 bps
}

void loop() {

  if(Serial.available()>0){  
    i=0;
    while(Serial.available()>0){    //Serial.available() mostra quantos bytes tem no
      dado[i]=Serial.read();        //buffer de recepção serial
      delay(50); 
      Serial.print(dado[i]);
      i++; 
      b=0;
    }
  }    
  roda();
}

void acende(int num){
  pinMode(num, OUTPUT);
  digitalWrite(num, HIGH);
}

void apaga(int num){
  digitalWrite(num, LOW);
}

void exec1(int num){
  if(dado[num]=='1'){
    acende(LEDS[num]);
    delay(10);
  }else if(dado[num]=='0'){
    apaga(LEDS[num]);
    delay(10);
  }
}

void roda(){
  for(i=0; i<3 && b==0; i++){
    Serial.print("LED ");
    Serial.print(i+1);
    Serial.print(": ");
    Serial.print(dado[i]);
    Serial.print("\n");
    exec1(i);
    delay(10);
  }
  b=1;
}



