## Training Journey

I started with understanding of Transformer library of Hugging Face

https://huggingface.co/docs/transformers/en/quicktour


## Dataset 

https://huggingface.co/blog/tegridydev/llm-dataset-formats-101-hugging-face


## Finetuning

https://huggingface.co/docs/autotrain/en/tasks/llm_finetuning


We will start with following format for preparing training dataset:


{
  "prompt": "The sentence below may contain one error in punctuation or capitalisation, or it may be error-free.\nSelect the group of words that contains the mistake, or choose 'No mistake' if the sentence is correct. \n On Tuesday afternoons, Sarah practises her violin in the schools music room.\n A) On Tuesday afternoons,  B) Sarah practises her violin  C) in the schools music room  D) No mistake",
  "response": "C. Explanation: The correct sentence is 'The error is in \"schools music room\" - it should be \"school's music room\" as his is a possessive (the music room belongs to the school). The sentence needs an apostrophe before the 's' to show possession.'"
}


## Fine tuning template script:

https://gitlab.com/CeADARIreland_Public/llm-resources/-/blob/main/fine_tuning_template_script.py?ref_type=heads

## Anther format is mentioned in the below template example

https://gitlab.com/CeADARIreland_Public/llm-resources/-/blob/main/fine_tuning_template_script.py?ref_type=heads


## Fine tuning tutorial (Using QLora):

https://dassum.medium.com/fine-tune-large-language-model-llm-on-a-custom-dataset-with-qlora-fb60abdeba07


## Alpaca Model Training Process

Explain the process of using dataset schema
instruction:
input:
output:

https://github.com/tatsu-lab/stanford_alpaca



## Whitepapers Finetuning

https://arxiv.org/pdf/2408.13296

https://arxiv.org/pdf/2409.03444





