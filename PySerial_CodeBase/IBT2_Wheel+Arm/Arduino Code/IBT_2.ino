/*
 * IBT_2 MOTOR DRIVER INTERFACING WITH PYTHON
 * Developed By : Sihab Sahariar
 * Date of Creation : 11 January 2021
 * Functionalities : Arm & Wheel
*/


//------------------------------PIN ASSIGN------------------------------ 
//Motor 1(Left Side of Rover)
int RPWM1=5;
int LPWM1=6;
//Motor 2 (Right Side of Rover)
int RPWM2=4;
int LPWM2=3;
//Act 1 
int RPWM_act1 = 5; // UP
int LPWM_act1 = 6; // DOWN
//Act 2 
int RPWM_act2 = 7; // UP
int LPWM_act2 = 8; // DOWN
//Act 3 
int RPWM_act3 = 9; // UP
int LPWM_act3 = 10; // DOWN
//Claw 
int RPWM_claw = 11; // OPEN
int LPWM_claw = 12; // CLOSE
//Base 
int RPWM_base = 13; // CLOCKWISE
int LPWM_base = 14; // ANTICLOCKWISE
//Wrist 
int RPWM_wrist = 15;// CLOCKWISE
int LPWM_wrist = 16;// ANTICLOCKWISE

//--------------------------PIN SETUP-----------------------------------
void setup(){
  pinMode(RPWM1, OUTPUT);
  pinMode(LPWM1, OUTPUT);
  pinMode(RPWM2, OUTPUT);
  pinMode(LPWM2, OUTPUT);
  pinMode(RPWM_act1,OUTPUT);
  pinMode(LPWM_act1,OUTPUT);
  pinMode(RPWM_act2,OUTPUT);
  pinMode(LPWM_act2,OUTPUT);
  pinMode(RPWM_act3,OUTPUT);
  pinMode(LPWM_act3,OUTPUT);
  pinMode(RPWM_act4,OUTPUT);
  pinMode(LPWM_act4,OUTPUT);
  pinMode(RPWM_base,OUTPUT);
  pinMode(LPWM_base,OUTPUT);
  pinMode(RPWM_wrist,OUTPUT);
  pinMode(LPWM_wrist,OUTPUT);
  pinMode(RPWM_claw,OUTPUT);
  pinMode(LPWM_claw,OUTPUT);
}
//-----------------------FUNCTIONALITIES--------------------------------
void stop_all(){
  analogWrite(RPWM1, 0);
  analogWrite(LPWM1, 0);
  analogWrite(RPWM2, 0);
  analogWrite(LPWM2, 0);
  analogWrite(RPWM_act1,0);
  analogWrite(LPWM_act1,0);
  analogWrite(RPWM_act2,0);
  analogWrite(LPWM_act2,0);
  analogWrite(RPWM_act3,0);
  analogWrite(LPWM_act3,0);
  analogWrite(RPWM_act4,0);
  analogWrite(LPWM_act4,0);
  analogWrite(RPWM_base,0);
  analogWrite(LPWM_base,0);
  analogWrite(RPWM_wrist,0);
  analogWrite(LPWM_wrist,0);
  analogWrite(RPWM_claw,0);
  analogWrite(LPWM_claw,0);
}
void forward(){
	 analogWrite(RPWM1,255);
	 analogWrite(LPWM1,0);
	 analogWrite(RPWM2,255);
	 analogWrite(LPWM2,0); 
}	 
void left(){
	 analogWrite(RPWM1,0);
	 analogWrite(LPWM1,255);
	 analogWrite(RPWM2,255);
	 analogWrite(LPWM2,0); 
}
void right(){
	 analogWrite(RPWM1,255);
	 analogWrite(LPWM1,0);
	 analogWrite(RPWM2,0);
	 analogWrite(LPWM2,255); 
}
void backward(){
	 analogWrite(RPWM1,0);
	 analogWrite(LPWM1,255);
	 analogWrite(RPWM2,0);
	 analogWrite(LPWM2,255); 
}
void act1_up(){
	 analogWrite(RPWM_act1,255);
	 analogWrite(LPWM_act1,0);
}
void act1_down(){
	 analogWrite(RPWM_act1,0);
	 analogWrite(LPWM_act1,255);
}
void act2_up(){
	 analogWrite(RPWM_act2,255);
	 analogWrite(LPWM_act2,0);
}
void act2_down(){
	 analogWrite(RPWM_act2,0);
	 analogWrite(LPWM_act2,255);
}
void act3_up(){
	 analogWrite(RPWM_act3,255);
	 analogWrite(LPWM_act3,0);
}
void act3_down(){
	 analogWrite(RPWM_act3,0);
	 analogWrite(LPWM_act3,255);
}
void claw_open(){
	 analogWrite(RPWM_claw,255);
	 analogWrite(LPWM_claw,0);
}
void claw_close(){
	 analogWrite(RPWM_claw,0);
	 analogWrite(LPWM_claw,255);
}
void wrist_clockwise(){
	 analogWrite(RPWM_wrist,255);
	 analogWrite(LPWM_wrist,0);
}
void wrist_anticlockwise(){
	 analogWrite(RPWM_wrist,0);
	 analogWrite(LPWM_wrist,255);
}
void base_clockwise(){
	 analogWrite(RPWM_base,255);
	 analogWrite(LPWM_base,0);
}
void base_anticlockwise(){
	 analogWrite(RPWM_base,0);
	 analogWrite(LPWM_base,255);
}
//-----------------------------MAIN-------------------------------------
void loop()
{
    if (Serial.available() > 0){
      inByte = Serial.read();
      if(inByte == 'x')
      {
		  stop_all();
	  }
      
	  /*      Wheel Control      */
      if(inByte == 'w')
      {
        forward();
      }
      else if (inByte == 'a')
      {
		left();
      }
      else if (inByte == 'd')
      {
		right();
      }
      else if (inByte == 's')
      {
		backward();
      }
      
       /*      Arm Control      */
       
      if (inByte == 'r')
      {       
		arm1_up();
      }
      else if (inByte == 'f'){ 
		arm1_down();
      }     
      if (inByte == 't'){       
		arm2_up();
      }
      else if (inByte == 'g')
      {  
		arm2_down();
      }   
      if (inByte == 'y')
      {       
		arm3_up();
      }
      else if (inByte == 'h')
      { 
		arm3_down();
      }   
      if (inByte == 'o')
      {
		claw_open();
      }
      else if (inByte == 'p')
      {
		claw_close();
      }   
      if (inByte == 'm')
      {
		wrist_clockwise();
      }
      else if (inByte == 'n')
      {
		wrist_anticlockwise();
      }   
      if (inByte == 'v')
      {
		  base_clockwise();
      }
      else if (inByte == 'b')
      {
		base_anticlockwise();
      }        
         
    }
}
