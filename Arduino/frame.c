const int sensorMin = 0;   
const int sensorMax = 1024;

void setup()   
{
    Serial.begin(9600);   
}

void loop() 
{
    int sensorReading = analogRead(A0);
    int range = map(sensorReading,   sensorMin, sensorMax, 0, 3);
    switch (range) 
    {
        case 0:
            Serial.println("close fire");
            break;
        case 1:
            Serial.println("distant fire");
            break;
        case 2:
            Serial.println("no fire");
            break;
    }
    delay(1); 
}