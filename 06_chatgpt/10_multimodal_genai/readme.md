# Multimodal Generative AI

https://openai.com/blog/chatgpt-can-now-see-hear-and-speak

https://www.marketsandmarkets.com/ResearchInsight/multimodal-ai-market.asp

Image Generation:

https://platform.openai.com/docs/guides/images?context=node

Vision:

https://platform.openai.com/docs/guides/vision

https://platform.openai.com/docs/api-reference/images

Text to Speech:

https://platform.openai.com/docs/guides/text-to-speech

Speech to Text:

https://platform.openai.com/docs/guides/speech-to-text


Audio:

https://platform.openai.com/docs/api-reference/audio





https://medium.com/data-science/using-generative-ai-to-automatically-create-a-video-talk-from-an-article-6381c44c5fe0


https://github.com/lakshmanok/lakblogs/blob/main/genai_seminar/create_lecture.ipynb

This is used for generation of videos using AI in a notebook. This article takes an article or paper and turns it into powerpoint slides and audio and connects them.

- uses Google Gemini Flash
- I used Python to download the article as a PDF, and upload it to a temporary storage location that Gemini can read
- 
    class Slide(BaseModel):
        title: str
        key_points: List[str]
        lecture_notes: str

    class Lecture(BaseModel):
        slides: List[Slide]
        lecture_title: str
        based_on_article_by: str

- Now, invoke the model, passing in the PDF file and asking it to populate the desired structure. The result is JSON, so extract it into a Python object
- For example, this is what the 3rd slide looks like:

            {'key_points': [
                'Silver layer cleans, structures, and prepares data for self-service analytics.',
                'Data is denormalized and organized for easier use.',
                'Type 2 slowly changing dimensions are handled in this layer.',
                'Governance responsibility lies with the source team.'
            ],
            'lecture_notes': 'The silver layer takes data from the bronze layer and transforms it into a usable format for self-service analytics. This involves cleaning, structuring, and organizing the data. Type 2 slowly changing dimensions, which track changes over time, are also handled in this layer. The governance of the silver layer rests with the source team, which is typically the data engineering team responsible for the source system.',
            'title': 'The Silver Layer: Data Transformation and Preparation'
            }

- We can use the Python package pptx to create a Presentation with notes and bullet points
- The code to create a slide looks like this:

        for slidejson in lecture['slides']:
            slide = presentation.slides.add_slide(presentation.slide_layouts[1])
            title = slide.shapes.title
            title.text = slidejson['title']
            # bullets
            textframe = slide.placeholders[1].text_frame
            for key_point in slidejson['key_points']:
                p = textframe.add_paragraph()
                p.text = key_point
                p.level = 1
            # notes
            notes_frame = slide.notes_slide.notes_text_frame
            notes_frame.text = slidejson['lecture_notes']



- Here’s the code to take some text, and have an AI voice read it out. We save the resulting audio into an mp3 file:

            from google.cloud import texttospeech

            def convert_text_audio(text, audio_mp3file):
                """Synthesizes speech from the input string of text."""
                tts_client = texttospeech.TextToSpeechClient()    
                input_text = texttospeech.SynthesisInput(text=text)
                
                voice = texttospeech.VoiceSelectionParams(
                    language_code="en-US",
                    name="en-US-Standard-C",
                    ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
                )
                audio_config = texttospeech.AudioConfig(
                    audio_encoding=texttospeech.AudioEncoding.MP3
                )

                response = tts_client.synthesize_speech(
                    request={"input": input_text, "voice": voice, "audio_config": audio_config}
                )

                # The response's audio_content is binary.
                with open(audio_mp3file, "wb") as out:
                    out.write(response.audio_content)
                    print(f"{audio_mp3file} written.")

- Now, create audio by iterating through the slides, and passing in the lecture notes:

            for slideno, slide in enumerate(lecture['slides']):
                    text = f"On to {slide['title']} \n"
                    text += slide['lecture_notes'] + "\n\n"
                    filename = os.path.join(outdir, f"audio_{slideno+1:02}.mp3")
                    convert_text_audio(text, filename)
                    filenames.append(filename)

- The result is a bunch of audio files. You can concatenate them if you wish using pydub:

            combined = pydub.AudioSegment.empty()
            for audio_file in audio_files:
                audio = pydub.AudioSegment.from_file(audio_file)
                combined += audio
                # pause for 4 seconds
                silence = pydub.AudioSegment.silent(duration=4000)
                combined += silence
            combined.export("lecture.wav", format="wav")



- Rather annoyingly, there’s no easy way to render PowerPoint slides as images using Python. You need a machine with Office software installed to do that — not the kind of thing that’s easily automatable.

- Now that we have a set of audio files and a set of image files, we can use a Python package moviepy to create a video clip:



