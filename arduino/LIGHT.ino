void setup() {
    serial.begin(9600);
    pinMode(LED_BULITIN, OUTPUT);
}



void loop() { //loop runs over again 
    
    
    if(serial.available()) {
        char c = serial.read();
        if (c =='1') {
            digitalwrite(LED_BULITIN, HIGH); 
            //turns the led light on high as this is the voltage level.
            
            serial.println("LED LIGHT ON <3");
        }
        
        
        if (c == '0'){
            digitalwrite(LED_BUILTIN, LOW);
            //turns the led light off and on low as this responds to the voltage level (LOW).
            
            serial.println("LED LIGHT OFF <3");
        }
        }


}