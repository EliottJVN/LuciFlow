import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

def run_model(audio_path:str, model_id="openai/whisper-large-v3-turbo"):
    """
    audio_path : path to your audio file.
    model_id : the model you wanna use.
    return the text detected
    """
    # Select the available device.
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
    )
    model.to(device)
 
    processor = AutoProcessor.from_pretrained(model_id)

    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        torch_dtype=torch_dtype,
        device=device,
        return_timestamps=True
    )

    return pipe(audio_path)["text"]

if __name__ == '__main__':
    my_audio = "uploads/test.mp3"
    result = run_model(my_audio)
    print(result)
