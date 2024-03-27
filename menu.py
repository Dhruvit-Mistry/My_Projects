# from pvrecorder import PvRecorder
# import wave, struct
#
# recorder = PvRecorder(device_index=2, frame_length=512) #(32 milliseconds of 16 kHz audio)
# audio = []
# path = 'audio_recording.wav'
#
# try:
#     recorder.start()
#
#
#     while True:
#         frame = recorder.read()
#         audio.extend(frame)
# except KeyboardInterrupt:
#     recorder.stop()
#     with wave.open(path, 'w') as f:
#         f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
#         f.writeframes(struct.pack("h" * len(audio), *audio))
# finally:
#     recorder.delete()

# import wave
# import struct
# from threading import Thread
# from pvrecorder import PvRecorder
#
# def record_audio_with_interrupt():
#     recorder = PvRecorder(device_index=2, frame_length=512) #(32 milliseconds of 16 kHz audio)
#     audio = []
#     path = 'audio_recording.wav'
#     recording = True
#
#     def stop_recording():
#         nonlocal recording
#         recording = False
#
#     def record():
#         nonlocal recording
#         try:
#             recorder.start()
#             while recording:
#                 frame = recorder.read()
#                 audio.extend(frame)
#         except KeyboardInterrupt:
#             pass
#         finally:
#             recorder.stop()
#             with wave.open(path, 'w') as f:
#                 f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
#                 f.writeframes(struct.pack("h" * len(audio), *audio))
#             recorder.delete()
#
#     record_thread = Thread(target=record)
#     record_thread.start()
#
#     print("Press 'Q' to stop recording.")
#
#     while recording:
#         user_input = input().strip().lower()
#         if user_input == 'q':
#             stop_recording()
#
#     record_thread.join()
#
# record_audio_with_interrupt()


# import wave
# import struct
# from threading import Thread
# from pvrecorder import PvRecorder
# import keyboard
#
# def record_audio_with_interrupt():
#     recorder = PvRecorder(device_index=2, frame_length=512) #(32 milliseconds of 16 kHz audio)
#     audio = []
#     path = 'audio_recording.wav'
#     recording = True
#
#     def stop_recording():
#         nonlocal recording
#         recording = False
#
#     def record():
#         nonlocal recording
#         try:
#             recorder.start()
#             while recording:
#                 frame = recorder.read()
#                 audio.extend(frame)
#         except KeyboardInterrupt:
#             pass
#         finally:
#             recorder.stop()
#             with wave.open(path, 'w') as f:
#                 f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
#                 f.writeframes(struct.pack("h" * len(audio), *audio))
#             recorder.delete()
#
#     record_thread = Thread(target=record)
#     record_thread.start()
#
#     print("Press 'Q' to stop recording.")
#
#     keyboard.add_hotkey('q', stop_recording)
#
#     record_thread.join()
#
# record_audio_with_interrupt()

#---------------------------------------------------------------------------------------------------#

from openai import OpenAI
import wave
from flask import Flask, render_template, request
import struct
from threading import Thread
from pvrecorder import PvRecorder
import keyboard

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def record_audio_with_interrupt():
    recorder = PvRecorder(device_index=1, frame_length=512) #(32 milliseconds of 16 kHz audio)
    audio = []
    path = 'recorded_audio.wav'
    recording = True

    def stop_recording():
        nonlocal recording
        recording = False

    def record():
        nonlocal recording
        try:
            recorder.start()
            while recording:
                frame = recorder.read()
                audio.extend(frame)
        except KeyboardInterrupt:
            pass
        finally:
            recorder.stop()
            with wave.open(path, 'wb') as f:
                f.setnchannels(1)  # Mono audio
                f.setsampwidth(2)  # 2 bytes per sample (16-bit)
                f.setframerate(16000)  # Sample rate of 16 kHz
                f.writeframes(struct.pack('h' * len(audio), *audio))
            recorder.delete()

    record_thread = Thread(target=record)
    record_thread.start()

    print("Recording audio... Press 'Q' to stop recording.")

    keyboard.add_hotkey('q', stop_recording)

@app.route('/transcribe', methods=['POST'])
def transcribe():
    file_name = "recorded_audio.wav"
    client = OpenAI(api_key="your_openai_api_key_here")
    audio_file = open(file_name, "rb")
    transcription = client.audio.transcriptions.create(
        response_format="text",
        model="whisper-1",
        file=audio_file,
        language='en'
    )
    transcription_text = transcription.text
    return render_template('result.html', transcription_text=transcription_text)

@app.route('/record', methods=['POST'])
def start_recording():
    record_audio_with_interrupt()
    return "Recording started..."

if __name__ == "__main__":
    app.run(debug=True)
