import socketio
import pickle

emotinal_state_ecg = 0
sio = socketio.Client() # Create a SocketIO client instance

@sio.on('connect')
def on_connect():
    print('Connected to server')

@sio.on('disconnect')
def on_disconnect():
    print('Disconnected from server')

@sio.on('new_heart_rate')
def on_new_heart_rate(data):
    emotinal_state_ecg = get_emotion_prediction(data)
    print('Received new heart rate:', data)

def get_emotion_prediction(data):
    ecg_heart_rate = float(data)
    prediction = 1
    #filename = 'finalized_model.pickle' #'TEST.pickle' 
    #loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
    #prediction=loaded_model.predict([[ecg_heart_rate]]) # predictions using the loaded model file
    print('ECG prediction is', prediction)
    return prediction 
    
# Establishing a SocketIO connection to Aquarela server
sio.connect('http://localhost:3000')

# Emit the "heart_rate" event with a heart rate value
heart_rate_value_prediction = 1 # Feliz
sio.emit('prediction_heart_rate', heart_rate_value_prediction)

# Function ECG to send the Flag of emotional state in HeartRate
def sendValue(emotinal_state_ecg):
    sio.emit('prediction_heart_rate', emotinal_state_ecg)

# Wait for a moment to allow the event to be sent
sio.sleep(2)

# Disconnect from the server
sio.disconnect()



heart_rate = {80,79,78,75,75,80,86,75,86,81,80,84,82,83,81,84,86,82,81}

def get_prediction():
    ecg_heart_rate = float(heart_rate)
    prediction = 1
    #filename = 'finalized_model.pickle' #'TEST.pickle' 
    #loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
    #prediction=loaded_model.predict([[ecg_heart_rate]]) # predictions using the loaded model file
    print('ECG prediction is', prediction)

if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app