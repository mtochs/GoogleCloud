from __future__ import print_function
from config import *
from google.cloud import texttospeech

def synthesize_text(text, output_file='output.mp3'):
	"""Synthesizes speech from the input string of text."""
	client = texttospeech.TextToSpeechClient()
	#print(client.list_voices())

	input_text = texttospeech.types.SynthesisInput(text=text)

	# Note: the voice can also be specified by name.
	# Names of voices can be retrieved with client.list_voices().
	voice = texttospeech.types.VoiceSelectionParams(
		language_code='en-US',
		name='en-US-Wavenet-D',
		ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)
	
	audio_config = texttospeech.types.AudioConfig(
		audio_encoding=texttospeech.enums.AudioEncoding.MP3)

	response = client.synthesize_speech(input_text, voice, audio_config)

	# The response's audio_content is binary.
	with open(output_file, 'wb') as out:
		out.write(response.audio_content)
		print('Audio content written to file:', output_file)
	

if __name__ == "__main__":
	#'''
	synthesize_text('Investors adopt many different approaches that offer little or no real prospect of long-term '
		'success and considerable chance of substantial economic loss. Many are not coherent investment '
		'programs at all but instead resemble speculation or outright gambling. Investors are frequently '
		'lured by the prospect of quick and easy gain and fall victim to the many fads of Wall Street. My '
		'goals in writing this book are twofold. In the first section I identify many of the pitfalls that face '
		'investors. By highlighting where so many go wrong, I hope to help investors learn to avoid these '
		'losing strategies.')
	#'''
	