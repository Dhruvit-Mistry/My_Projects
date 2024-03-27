from pvrecorder import PvRecorder
import wave
import struct

# Create a PvRecorder instance with the desired frame_length
frame_length = 512  # You can adjust this value as needed
recorder = PvRecorder(frame_length=frame_length)

# Start recording
recorder.start()

# Record audio for a specific duration (e.g., 5 seconds)
duration_seconds = 5
audio_frames = []
for _ in range(int(recorder.sample_rate * duration_seconds / recorder.frame_length)):
    frame = recorder.read()
    audio_frames.extend(frame)

# Stop recording
recorder.stop()

# Save recorded audio to a WAV file
path = 'recorded_audio.wav'
with wave.open(path, 'wb') as f:
    f.setnchannels(1)  # Mono audio
    f.setsampwidth(2)  # 2 bytes per sample (16-bit)
    f.setframerate(recorder.sample_rate)
    f.writeframes(struct.pack('h' * len(audio_frames), *audio_frames))

print(f"Audio recorded and saved to {path}")
