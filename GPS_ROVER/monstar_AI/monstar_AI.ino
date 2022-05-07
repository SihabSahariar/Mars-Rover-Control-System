//Sihab Sahariar - Control & Software
int Motor1_Forward = 7;
int Motor1_Backward = 8;
int Motor2_Forward = 4;
int Motor2_Backward = 9;
int Motor1_PWM = 5;
int Motor2_PWM = 6;
int Speed = 170;



void setup() {
  pinMode(Motor1_Forward, OUTPUT);
  pinMode(Motor2_Forward, OUTPUT);
  pinMode(Motor1_Backward, OUTPUT);
  pinMode(Motor2_Backward, OUTPUT);
  pinMode(Motor1_PWM, OUTPUT);
  pinMode(Motor2_PWM, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  while(Serial.available()>0)
  {
    char val= Serial.read();
    if (val=='d') //Right
    {
      digitalWrite(Motor1_Forward,HIGH);
      digitalWrite(Motor2_Forward,HIGH);
      digitalWrite(Motor1_Backward,LOW);
      digitalWrite(Motor2_Backward,LOW);
      digitalWrite(Motor1_PWM,Speed);
      digitalWrite(Motor2_PWM,Speed);

      
    }
    else if(val== 'a') //Left
    {
      digitalWrite(Motor1_Forward,LOW);
      digitalWrite(Motor2_Forward,LOW);
      digitalWrite(Motor1_Backward,HIGH);
      digitalWrite(Motor2_Backward,HIGH);
      digitalWrite(Motor1_PWM,Speed);
      digitalWrite(Motor2_PWM,Speed);
      
    }
   else if(val== 's')  //Backward
   {
      digitalWrite(Motor1_Forward,LOW);
      digitalWrite(Motor2_Forward,HIGH);
      digitalWrite(Motor1_Backward,HIGH);
      digitalWrite(Motor2_Backward,LOW);
      digitalWrite(Motor1_PWM,Speed);
      digitalWrite(Motor2_PWM,Speed);
   }
   else if(val== 'w') //Forward
   {
      digitalWrite(Motor1_Forward,HIGH);
      digitalWrite(Motor2_Forward,LOW);
      digitalWrite(Motor1_Backward,LOW);
      digitalWrite(Motor2_Backward,HIGH);
      digitalWrite(Motor1_PWM,Speed);
      digitalWrite(Motor2_PWM,Speed);
   }
    else if(val== 'x')
   {
      digitalWrite(Motor1_Forward,LOW);
      digitalWrite(Motor2_Forward,LOW);
      digitalWrite(Motor1_Backward,LOW);
      digitalWrite(Motor2_Backward,LOW);
      digitalWrite(Motor1_PWM,0);
      digitalWrite(Motor2_PWM,0);
   }
  }
  

}
