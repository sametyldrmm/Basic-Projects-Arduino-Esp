#define fanSwitchPin 6
#define buttonPin 3
#define echoPin 2 
#define trigPin 3 
int fanOn = 0;
long distance;
long duration;

int getFanBtnState(){
    if(digitalRead(buttonPin) == HIGH)
        fanOn++;
    return fanOn;
}

void runFan(){
    digitalWrite(fanSwitchPin, HIGH);
    delay(10000);
    digitalWrite(fanSwitchPin, LOW);
}

void setup() {
    pinMode(buttonPin, INPUT_PULLUP);
    pinMode(fanSwitchPin, OUTPUT);
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
    digitalWrite(fanSwitchPin, LOW);
}

int mesafeSensor(long distance)
{
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);

    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    duration = pulseIn(echoPin, HIGH);

    distance = duration * 0.034 / 2;
}

void loop() {
    fanOn = getFanBtnState(); 
    if(fanOn % 2 == 1)
    {
        runFan();
    }
    else if(fanOn % 2 == 0)
    {
        fanOn = getFanBtnState();
        while ()
        {
            
        }
    }
}