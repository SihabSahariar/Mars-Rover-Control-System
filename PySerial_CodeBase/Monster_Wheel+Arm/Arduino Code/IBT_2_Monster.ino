/*
 * IBT_2 AND MONSTER MOTOR DRIVER INTERFACING WITH PYTHON
 * Developed By : Sihab Sahariar
 * Date of Creation : 11 January 2021
 * Functionalities : Arm & Wheel
 * Monster 1 - Base & Act 1 
 * Monster 2 - Act 2 & Act 3 
 * Monster 3 - Act 4(Claw) & Wrist 
*/


//------------------------------PIN ASSIGN------------------------------ 
//Motor 1(Left Side of Rover)
int RPWM1=5;
int LPWM1=6;
//Motor 2 (Right Side of Rover)
int RPWM2=4;
int LPWM2=3;
//Act 1 
int act1_cw =  5;
int act1_ccw = 6;
int act1_pwm = 7;
//Act 2 
int act2_cw =  8;
int act2_ccw = 9;
int act2_pwm = 10;
//Act 3 
int act3_cw =  11;
int act3_ccw = 12;
int act3_pwm = 13;
//Claw 
int act_claw_cw =  14;
int act_claw_ccw = 15;
int act_claw_pwm =  16;
//Base 
int act_base_cw =  17;
int act_base_ccw = 18;
int act_base_pwm = 19;
//Wrist 
int act_wrist_cw =  20;
int act_wrist_ccw = 21;
int act_wrist_pwm = 22;

//--------------------------PIN SETUP-----------------------------------
void setup(){
	pinMode(RPWM1, OUTPUT);
	pinMode(LPWM1, OUTPUT);
	pinMode(RPWM2, OUTPUT);
	pinMode(LPWM2, OUTPUT);
	pinMode(act1_cw ,OUTPUT);
	pinMode(act1_ccw ,OUTPUT);
	pinMode(act1_pwm ,OUTPUT);
	pinMode(act2_cw ,OUTPUT);
	pinMode(act2_ccw ,OUTPUT);
	pinMode(act2_pwm ,OUTPUT);
	pinMode(act3_cw ,OUTPUT);
	pinMode(act3_ccw ,OUTPUT);
	pinMode(act3_pwm ,OUTPUT);
	pinMode(act_claw_cw ,OUTPUT);
	pinMode(act_claw_ccw ,OUTPUT);
	pinMode(act_claw_pwm ,OUTPUT);
	pinMode(act_base_cw ,OUTPUT);
	pinMode(act_base_ccw ,OUTPUT);
	pinMode(act_base_pwm ,OUTPUT);
	pinMode(act_wrist_cw ,OUTPUT);
	pinMode(act_wrist_ccw ,OUTPUT);
	pinMode(act_wrist_pwm ,OUTPUT);
}
//-----------------------FUNCTIONALITIES--------------------------------
void stop_all(){
	analogWrite(RPWM1, 0);
	analogWrite(LPWM1, 0);
	analogWrite(RPWM2, 0);
	analogWrite(LPWM2, 0);
	analogWrite(act1_cw ,0);
	analogWrite(act1_ccw ,0);
	analogWrite(act1_pwm ,0);
	analogWrite(act2_cw ,0);
	analogWrite(act2_ccw ,0);
	analogWrite(act2_pwm ,0);
	analogWrite(act3_cw ,0);
	analogWrite(act3_ccw ,0);
	analogWrite(act3_pwm ,0);
	analogWrite(act_claw_cw ,0);
	analogWrite(act_claw_ccw ,0);
	analogWrite(act_claw_pwm ,0);
	analogWrite(act_base_cw ,0);
	analogWrite(act_base_ccw ,0);
	analogWrite(act_base_pwm ,0);
	analogWrite(act_wrist_cw ,0);
	analogWrite(act_wrist_ccw ,0);
	analogWrite(act_wrist_pwm ,0);
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
	analogWrite(act1_cw ,255);
	analogWrite(act1_ccw ,0);
	analogWrite(act1_pwm ,255);
}
void act1_down(){
	analogWrite(act1_cw ,0);
	analogWrite(act1_ccw ,255);
	analogWrite(act1_pwm ,255);
}
void act2_up(){
	analogWrite(act1_cw ,255);
	analogWrite(act1_ccw ,0);
	analogWrite(act1_pwm ,255);
}
void act2_down(){
	analogWrite(act2_cw ,0);
	analogWrite(act2_ccw ,255);
	analogWrite(act2_pwm ,255);
}
void act3_up(){
	analogWrite(act2_cw ,255);
	analogWrite(act2_ccw ,0);
	analogWrite(act2_pwm ,255);
}
void act3_down(){
	analogWrite(act3_cw ,0);
	analogWrite(act3_ccw ,255);
	analogWrite(act3_pwm ,255);
}
void claw_open(){
	analogWrite(act_claw_cw ,255);
	analogWrite(act1_claw_ccw ,0);
	analogWrite(act_claw_pwm ,255);
}
void claw_close(){
	analogWrite(act_claw_cw ,0);
	analogWrite(act_claw_ccw ,255);
	analogWrite(act_claw_pwm ,255);
}
void wrist_clockwise(){
	analogWrite(act_wrist_cw ,255);
	analogWrite(act_wrist_ccw ,0);
	analogWrite(act_wrist_pwm ,255);
}
void wrist_anticlockwise(){
	analogWrite(act_wrist_cw ,0);
	analogWrite(act_wrist_ccw ,255);
	analogWrite(act_wrist_pwm ,255);
}
void base_clockwise(){
	analogWrite(act_base_cw ,255);
	analogWrite(act_base_ccw ,0);
	analogWrite(act_base_pwm ,255);
}
void base_anticlockwise(){
	analogWrite(act_base_cw ,0);
	analogWrite(act_base_ccw ,255);
	analogWrite(act_base_pwm ,255);
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
