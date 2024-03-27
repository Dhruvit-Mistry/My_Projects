# from openai import OpenAI
# import pyaudio
# import wave
# import keyboard
# from flask import Flask, render_template
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# def record_audio(file_name, sample_rate=44100, chunk_size=1024):
#     """
#     Record audio from the microphone until the user presses a key and save it to a WAV file.
#
#     Args:
#     - file_name (str): Name of the output WAV file.
#     - sample_rate (int): Sampling rate of the audio (default is 44100 Hz).
#     - chunk_size (int): Size of each audio chunk processed during recording (default is 1024 samples).
#     """
#     audio = pyaudio.PyAudio()
#
#     # Open a new audio stream for recording
#     stream = audio.open(format=pyaudio.paInt16,
#                         channels=1,
#                         rate=sample_rate,
#                         input=True,
#                         frames_per_buffer=chunk_size)
#
#     print("Recording... Press 'q' to stop.")
#
#     frames = []
#
#     # Record audio data in chunks until 'q' is pressed
#     while True:
#         if keyboard.is_pressed('q'):
#             break
#         data = stream.read(chunk_size)
#         frames.append(data)
#
#     print("Finished recording.")
#
#     # Stop and close the audio stream
#     stream.stop_stream()
#     stream.close()
#     audio.terminate()
#
#     # Save the recorded audio to a WAV file
#     with wave.open(file_name, 'wb') as wf:
#         wf.setnchannels(1)
#         wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
#         wf.setframerate(sample_rate)
#         wf.writeframes(b''.join(frames))
#
# @app.route('/record')
# def start_recording():
#     file_name = "recorded_audio.wav"
#     record_audio(file_name)
#     return f"Audio recording saved to {file_name}"
#
# @app.route('/transcribe')
# def transcribe():
#     file_name = "recorded_audio.wav"
#     client = OpenAI(api_key="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")
#     audio_file = open(file_name, "rb")
#     transcription = client.audio.transcriptions.create(
#         response_format="text",
#         model="whisper-1",
#         file=audio_file,
#         language='en'
#     )
#     return transcription.text
#     return render_template('result.html', transcription_text=transcription_text)
#
#
#
# if __name__ == "__main__":
#     app.run(debug=True)


#### 2

# from openai import OpenAI
# import pyaudio
# import wave
# import keyboard
# from flask import Flask, render_template, request
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# def record_audio(file_name, sample_rate=44100, chunk_size=1024):
#     """
#     Record audio from the microphone until the user presses a key and save it to a WAV file.
#
#     Args:
#     - file_name (str): Name of the output WAV file.
#     - sample_rate (int): Sampling rate of the audio (default is 44100 Hz).
#     - chunk_size (int): Size of each audio chunk processed during recording (default is 1024 samples).
#     """
#     audio = pyaudio.PyAudio()
#
#     # Open a new audio stream for recording
#     stream = audio.open(format=pyaudio.paInt16,
#                         channels=1,
#                         rate=sample_rate,
#                         input=True,
#                         frames_per_buffer=chunk_size)
#
#     print("Recording... Press 'q' to stop.")
#
#     frames = []
#
#     # Record audio data in chunks until 'q' is pressed
#     while True:
#         if keyboard.is_pressed('q'):
#             break
#         data = stream.read(chunk_size)
#         frames.append(data)
#
#     print("Finished recording.")
#
#     # Stop and close the audio stream
#     stream.stop_stream()
#     stream.close()
#     audio.terminate()
#
#     # Save the recorded audio to a WAV file
#     with wave.open(file_name, 'wb') as wf:
#         wf.setnchannels(1)
#         wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
#         wf.setframerate(sample_rate)
#         wf.writeframes(b''.join(frames))
#
# @app.route('/record')
# def start_recording():
#     file_name = "recorded_audio.wav"
#     record_audio(file_name)
#     return f"Audio recording saved to {file_name}"
#
#
#
# @app.route('/transcribe', methods=['POST', 'GET'])
# def transcribe():
#     if request.method == 'GET':
#         return "Please submit the audio file for transcription."
#
#     # Handle POST request to transcribe the audio file
#     file_name = "recorded_audio.wav"
#     client = OpenAI(api_key="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")
#     audio_file = open(file_name, "rb")
#     transcription = client.audio.transcriptions.create(
#         response_format="text",
#         model="whisper-1",
#         file=audio_file,
#         language='en'
#     )
#     transcription_text = transcription.text
#     return render_template('result.html', transcription_text=transcription_text)
#
# if __name__ == "__main__":
#     app.run(debug=True)

#### 3

from openai import OpenAI
import pyaudio
import wave
import keyboard
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# def record_audio_until_q(sample_rate=44100):
#     """
#     Record audio from the default input device until the 'Q' key is pressed.
#
#     Args:
#     - sample_rate (int): Sampling rate of the audio (default is 44100 Hz).
#
#     Returns:
#     - audio_data (numpy.ndarray): Recorded audio data as a NumPy array.
#     """
#     print("Recording... Press 'Q' to stop.")
#
#     audio_data = []
#
#     # Start recording audio until 'Q' key is pressed
#     while True:
#         if keyboard.is_pressed('q'):
#             print("Stopping recording...")
#             import webbrowser
#             webbrowser.open('http://127.0.0.1:5000/transcribe')
#             break
#
#         # Record a chunk of audio
#         chunk = sd.rec(int(sample_rate), samplerate=sample_rate, channels=1, dtype=np.float32)
#         audio_data.append(chunk)
#         sd.wait()
#
#     # Concatenate recorded chunks into a single array
#     audio_data = np.concatenate(audio_data, axis=0)
#
#     return audio_data
def record_audio(file_name, sample_rate=44100, chunk_size=1024):
    """
    Record audio from the microphone until the user presses a key and save it to a WAV file.

    Args:
    - file_name (str): Name of the output WAV file.
    - sample_rate (int): Sampling rate of the audio (default is 44100 Hz).
    - chunk_size (int): Size of each audio chunk processed during recording (default is 1024 samples).
    """
    audio = pyaudio.PyAudio()

    # Open a new audio stream for recording
    stream = audio.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=chunk_size)

    print("Recording... Press 'q' to stop.")

    frames = []

    # Record audio data in chunks until 'q' is pressed
    while True:
        if keyboard.is_pressed('q'):
            #return render_template('result.html', transcription_text = transcription)
            #return redirect("/transcribe")
            import webbrowser
            webbrowser.open('http://127.0.0.1:5000/transcribe')
            break
        data = stream.read(chunk_size)
        frames.append(data)

    print("Finished recording.")

    # Stop and close the audio stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio to a WAV file
    with wave.open(file_name, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

# @app.route('/check')
# def check():
#     print('check')

@app.route('/transcribe', methods=['POST', 'GET'])
def transcribe():
    print("Request method:", request.method)

    # Handle POST request to transcribe the audio file
    file_name = "recorded_audio.wav"
    client = OpenAI(api_key="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")
    audio_file = open(file_name, "rb")
    transcription = client.audio.transcriptions.create(
        response_format="text",
        model="whisper-1",
        file=audio_file,
        language='en'
    )
    print(transcription)
    #transcription_text = transcription.text
    return render_template('result.html', transcription_text = transcription)

@app.route('/record',methods = ['POST'])
def start_recording():
    #print("hello")
    file_name = "recorded_audio.wav"
    record_audio(file_name)
    return f"Audio recording saved to {file_name}"



if __name__ == "__main__":
    app.run(debug=True)
