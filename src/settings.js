let DEBUG = true;
let HOST_URL = "http://djangochat-4280.rostiapp.cz";
let SOCKET_URL = "ws://djangochat-4280.rostiapp.cz";
if (DEBUG) {
  // HOST_URL = "http://localhost:8000";
  // SOCKET_URL = "ws://localhost:8000";
  HOST_URL = "http://147.230.155.90:8000";
  SOCKET_URL = "ws://147.230.155.90:8000";
}

export { HOST_URL, SOCKET_URL, DEBUG };
