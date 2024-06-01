//#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266WebServer.h>
#include <SoftwareSerial.h>

#define SERIAL_BAUD 9600

SoftwareSerial espSerial(5, 16); // RX, TX

ESP8266WiFiMulti wifiMulti;     // Create an instance of the ESP8266WiFiMulti class, called 'wifiMulti'

ESP8266WebServer server(80);    // Create a webserver object that listens for HTTP request on port 80

const char *html =
  "<form action=\"/LED1\" method=\"POST\"><input type=\"submit\" value=\"Toggle LED1\"></form>"
  "<form action=\"/LED2\" method=\"POST\"><input type=\"submit\" value=\"Toggle LED2\"></form>"
  "<p></p>";

const int GPIO_1 = D1;
const int GPIO_2 = D2;

void handleRoot();              // function prototypes for HTTP handlers
void handleLED_1();
void handleLED_2();
void handleNotFound();

void setup(void){
  Serial.begin(115200);         // Start the Serial communication to send messages to the computer
  espSerial.begin(SERIAL_BAUD);
  Serial.println('\n');

  pinMode(GPIO_1, OUTPUT);
  pinMode(GPIO_2, OUTPUT);

  wifiMulti.addAP("dlink-M961-2.4G-6fa6", "csffb76673");   // add Wi-Fi networks you want to connect to
  //wifiMulti.addAP("Hashem_EXT", "csffb76673");   // add Wi-Fi networks you want to connect to

  Serial.println("Connecting ...");
  int i = 0;
  while (wifiMulti.run() != WL_CONNECTED) { // Wait for the Wi-Fi to connect: scan for Wi-Fi networks, and connect to the strongest of the networks above
    delay(250);
    Serial.print('.');
    digitalWrite(GPIO_1, 1);
    delay(100);
    digitalWrite(GPIO_1, 0);
    delay(100);
  }
  Serial.println('\n');
  Serial.print("Connected to ");
  Serial.println(WiFi.SSID());              // Tell us what network we're connected to
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());           // Send the IP address of the ESP8266 to the computer

  server.on("/", HTTP_GET, handleRoot);     // Call the 'handleRoot' function when a client requests URI "/"
  server.on("/LED1", HTTP_POST, handleLED_1);  // Call the 'handleLED_1' function when a POST request is made to URI "/LED1"
  server.on("/LED2", HTTP_POST, handleLED_2);  // Call the 'handleLED_2' function when a POST request is made to URI "/LED2"
  //server.on("/test", HTTP_GET)
  server.onNotFound(handleNotFound);        // When a client requests an unknown URI (i.e. something other than "/"), call function "handleNotFound"

  server.begin();                           // Actually start the server
  Serial.println("HTTP server started");
}

void loop(void){
  server.handleClient();                    // Listen for HTTP requests from clients
}

void handleRoot() {                         // When URI / is requested, send a web page with a button to toggle the LED
  server.send(200, "text/html", html);
}

void handleLED_1() {                          // If a POST request is made to URI /LED
  espSerial.println(String("13"));
  server.sendHeader("Location","/");        // Add a header to respond with a new location for the browser to go to the home page again
  server.send(303);                         // Send it back to the browser with an HTTP status 303 (See Other) to redirect
}

void handleLED_2(){
  espSerial.println(String("12"));      // Change the state of the LED
  server.sendHeader("Location","/");        // Add a header to respond with a new location for the browser to go to the home page again
  server.send(303);                         // Send it back to the browser with an HTTP status 303 (See Other) to redirect
}

void handleNotFound(){
  server.send(404, "text/plain", "404: Not found"); // Send HTTP status 404 (Not Found) when there's no handler for the URI in the request
}
