goog.provide('Blockly.Blocks.divers');

goog.require('Blockly.Blocks');


Blockly.Arduino['base_delayms'] = function(block) {
  var delay_time = Blockly.Arduino.valueToCode(block, 'DELAY_TIME', Blockly.Arduino.ORDER_ATOMIC) || '1000';
  var code = 'delay(' + delay_time + ');\n';
  return code;
};

Blockly.Arduino['grove_temporature_sensor'] = function(block) {
  var dropdown_pin = this.getFieldValue('PIN');
  /*
	a=analogRead(0);
	  resistance=(float)(1023-a)*10000/a;
	  temperature=1/(log(resistance/10000)/B+1/298.15)-273.15;
  */
  var code = 'round('+'(1/(log((float)(1023-analogRead('+dropdown_pin+'))*10000/analogRead('+dropdown_pin+'))/10000)/3975+1/298.15)-273.15'+')';
  return [code, Blockly.Arduino.ORDER_ATOMIC];
};

Blockly.Arduino['grove_ultrasonic_ranger'] = function(block) {
    var PIN_TRIG = this.getFieldValue('PIN_TRIG'); 
    var PIN_ECHO = this.getFieldValue('PIN_ECHO');
    Blockly.Arduino.setups_['setup_output_'+'A0'] = 'pinMode(A0, OUTPUT);';
    Blockly.Arduino.setups_['setup_input_'+'A5'] = 'pinMode('+'A5'+', INPUT);';
    Blockly.Arduino.definitions_['var_ultrasonic'+'A0'] = 'long ultra_distance() {\n'+
        '   long duration, distance;\n'+
        '   digitalWrite(A0,LOW);\n'+
        '   delayMicroseconds(2);\n'+
        '   digitalWrite(A0, HIGH);'+
        '   delayMicroseconds(10);\n'+
        '   digitalWrite(A0, LOW);\n'+
        '   duration = pulseIn(A5, HIGH);\n'+
        '   distance = duration * 340 / (2 * 10000);\n'+
        '   return distance;\n'+
        '}\n';;
    var code;
    code = 'ultra_distance()';
  return [code, Blockly.Arduino.ORDER_ATOMIC];
};

Blockly.Arduino['grove_motor_shield'] = function(block) {
  var dropdown_type = '#include';
  var varName='<AFMotor.h>';
  var motorpin='AF_DCMotor motor_L(1); \nAF_DCMotor motor_R(4);';
  Blockly.Arduino.definitions_['variables'+varName] = dropdown_type + '  ' + varName+'\n\n'+motorpin  ;
	
  var dropdown_direction = this.getFieldValue('DIRECTION');
  var speed = Blockly.Arduino.valueToCode(this, 'SPEED', Blockly.Arduino.ORDER_ATOMIC) || '150';
  Blockly.Arduino.setups_["setup_motor"] =  " motor_L.setSpeed("+speed+");\n"+
  "   motor_L.run(RELEASE);\n"+
  "   motor_R.setSpeed("+speed+");\n"+
  "   motor_R.run(RELEASE);\n";
  var code = "";
  if(dropdown_direction==="forward"){
    Blockly.Arduino.definitions_['define_forward'] = "void forward()\n"+
"{\n"+
     "   motor_L.run(FORWARD);\n"+
     "   motor_R.run(FORWARD);\n"+
"}\n";
    code="forward();\n";
  } else if (dropdown_direction==="left") {
    Blockly.Arduino.definitions_['define_right'] = "void right()\n"+
"{\n"+
     "   motor_L.run(RELEASE);\n"+
     "   motor_R.run(FORWARD);\n"+
     "   delay(1000);\n"+
"}\n\n";
    code="right();\n";
  } else if (dropdown_direction==="right") {
    Blockly.Arduino.definitions_['define_left'] = "void left()\n"+
"{\n"+
     "   motor_L.run(FORWARD);\n"+
     "   motor_R.run(RELEASE);\n"+
     "   delay(1000);\n"+
"}\n\n";
    code="left();\n";
  } else if (dropdown_direction==="backward"){
    Blockly.Arduino.definitions_['define_backward'] = "void backward()\n"+
"{\n"+
     "   motor_L.run(BACKWARD);\n"+
     "   motor_R.run(BACKWARD);\n"+
"}\n\n";
    code="backward();\n";
  } else if (dropdown_direction==="stop"){
    Blockly.Arduino.definitions_['define_stop'] = "void stop()\n"+
"{\n"+
     "   motor_L.run(RELEASE);\n"+
     "   motor_R.run(RELEASE);\n"+
     "   delay(1000);\n"+
"}\n\n";
    code="stop();\n";
  }
  return code;
};


Blockly.Arduino['millis'] = function(block) {
  var code = 'millis()';
  return [code, Blockly.Arduino.ORDER_ATOMIC];
};

Blockly.Arduino['var_random'] = function(block) {
  var value_rand_min = Blockly.Arduino.valueToCode(this, 'rand_min', Blockly.Arduino.ORDER_ATOMIC);
  var value_rand_max = Blockly.Arduino.valueToCode(this, 'rand_max', Blockly.Arduino.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'random('+value_rand_min+','+value_rand_max+')';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Arduino.ORDER_NONE];
};


Blockly.Arduino['various_constrain'] = function(block) {
  var value_x = Blockly.Arduino.valueToCode(this, 'x', Blockly.Arduino.ORDER_ATOMIC);
  var value_a = Blockly.Arduino.valueToCode(this, 'a', Blockly.Arduino.ORDER_ATOMIC);
  var value_b = Blockly.Arduino.valueToCode(this, 'b', Blockly.Arduino.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'constrain('+value_x+','+value_a+','+value_b+')';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Arduino.ORDER_NONE];
};
