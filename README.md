# controli2c 
[link to the youtube video](https://youtu.be/6xu8heEp08c?list=PLTywNZ-LJF2MVMe4GCK71t0w0yWfOh3kK)

# Arduino code:
You can find below the code c used for the Arduino to initialize I2C and use data sent by the Raspberry Pi.

    #include <Wire.h>
    
    #define SLAVE_ADDRESS 0x12
    int dataReceived = 0;
    const int led1 = 2;
    const int led2 = 3;
    const int led3 = 4;
    const int led4 = 5;
    const int led5 = 6;
    
    void setup() {
        Wire.begin(SLAVE_ADDRESS);
        Wire.onReceive(receiveData);
        Wire.onRequest(sendData);
    
        pinMode(led1, OUTPUT);
        pinMode(led2, OUTPUT);
        pinMode(led3, OUTPUT);
        pinMode(led4, OUTPUT);
        pinMode(led5, OUTPUT);
    }

    void loop() {
        digitalWrite(led1, LOW);
        digitalWrite(led2, LOW);
        digitalWrite(led3, LOW);
        digitalWrite(led4, LOW);
        digitalWrite(led5, LOW);
      
        if(dataReceived & (1 << 0) ){
            digitalWrite(led1, HIGH);
        }
      
        if(dataReceived & (1 << 1) ){
            digitalWrite(led2, HIGH);
        }
      
        if(dataReceived & (1 << 2) ){
            digitalWrite(led3, HIGH);
        }
      
        if(dataReceived & (1 << 3) ){
            digitalWrite(led4, HIGH);
        }
      
        if(dataReceived & (1 << 4) ){
            digitalWrite(led5, HIGH);
        }
    }

    void receiveData(int byteCount){
        while(Wire.available()) {
            dataReceived = Wire.read();
        }
    }

    void sendData(){
        int envoi = 1;
        Wire.write(envoi);
    }
