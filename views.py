# import logging, os, time, uuid, tempfile
# from flask import Blueprint, Flask, render_template, request, flash, redirect, url_for
# from wtforms import SubmitField
# from flask_wtf import FlaskForm
# from flask_wtf.file import FileField, FileRequired, FileAllowed
# from flask_uploads import UploadSet, configure_uploads, AUDIO
# from whisper_jax import FlaxWhisperPipline
# from werkzeug.utils import secure_filename
# from werkzeug.datastructures import FileStorage
# from requests.exceptions import RequestException
# from pydub import AudioSegment
# from pydub.silence import split_on_silence

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# app = Flask(__name__)
# pipeline = FlaxWhisperPipline("openai/whisper-small")

# flask_logger = logging.getLogger('werkzeug')
# flask_logger.setLevel(logging.INFO)

# if not os.path.exists('uploaded_audio'):
#     os.makedirs('uploaded_audio')

# custom_audio_extensions = AUDIO + ('m4', 'm4a')
# audio_files = UploadSet('audio', custom_audio_extensions)
# app.config['UPLOADED_AUDIO_DEST'] = 'uploaded_audio'
# configure_uploads(app, audio_files)
# # rate_limiter = RateLimiter(max_calls=50, period=60)


# class AudioForm(FlaskForm):
#     file = FileField('Audio File', validators=[
#         FileRequired(), FileAllowed(audio_files, 'Audio only!')])
#     submit = SubmitField('Submit')


# def transcribe_chunk(audio_chunk):
#     MAX_RETRIES = 5
#     INITIAL_DELAY = 1.0  # seconds
    
#     # Create a temporary file to store the audio_chunk_data
#     with tempfile.NamedTemporaryFile(suffix=".wav") as temp_audio_file:
#         audio_chunk.export(temp_audio_file.name, format="wav")
#         temp_audio_file.flush()

#         # Limit the max retries
#         retries = 0
#         while retries < MAX_RETRIES:
#             try:
#                 response = pipeline(temp_audio_file, task="transcribe", return_timestamps=True)
#                 return response
#             except RequestException as e:
#                 error_message = e.args[0].get("error", {}).get("message", "")
#                 if "Rate limit" in error_message:
#                     wait_time = INITIAL_DELAY * (2 ** retries)
#                     time.sleep(wait_time)
#                     retries += 1
#                 else:
#                     raise ValueError(f"Failed to transcribe audio: {e}")
#             except Exception as e:
#                 raise ValueError(f"Failed to transcribe audio: {e}")

#             # If all retries fail, raise an error
#         raise ValueError(
#             "Failed to transcribe audio: Rate limit reached after all retries.")


# # def transcribe_audio(file_path):
# #     start_time = time.time()
# #     try:
# #         audio = AudioSegment.from_file(file_path)
# #         audio = audio.set_channels(1)  # Convert to mono
# #         sample_rate = audio.frame_rate
# #     except Exception as e:
# #         raise ValueError(f"Failed to read audio file: {e}")

    
    

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     form = AudioForm()
#     if form.validate_on_submit():
#         logger.info("File submitted")
#         filename = secure_filename(form.file.data.filename)
#         audio_path = os.path.join(app.config['UPLOADED_AUDIO_DEST'], filename)
#         form.file.data.save(audio_path)
#         logger.info(f"File saved to: {audio_path}")
#         try:
#             logger.info("Transcribing audio")
#             transcript, transcription_time = transcribe_audio(audio_path)
#             logger.info("Generating summary and title")
#             title, summary, summary_time = generate_summary_and_title(
#                 transcript)
#         except ValueError as e:
#             logger.error(f"Error: {e}")
#             flash(str(e), 'error')
#             return redirect(url_for('demo'))
#         logger.info("Rendering summary")
#         # return render_template('summary.html', title=title, summary=summary, transcript=transcript, transcription_time=transcription_time, summary_time=summary_time)
#     return render_template('demo.html', form=form)

# @app.route('/start_ASR')
# def start():
#     fileRecord = RecordDemo()

# @app.route('/recorded-audio', methods=['POST'])
# def recorded_audio():
#     audio_data = request.files['file']
#     unique_id = str(uuid.uuid4())
#     filename = f"{unique_id}.wav"
#     audio_path = os.path.join(app.config['UPLOADED_AUDIO_DEST'], filename)
#     audio_data.save(audio_path)
#     return {'id': unique_id}

