import gpt2.interactive_conditional_samples as ics
#import gpt2.generate_unconditional_samples as gus 


def make_story(input_text = '', randomness = 1, text_diversity = 40):
    return ics.generate_story(raw_text = input_text, temperature = randomness, top_k = text_diversity)

