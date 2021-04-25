import random 


text = [
    'I know this is an older question and that the original question needed the div to have a fixed height, but I thought I would share that this can also be accomplished without a fixed pixel height for those looking for that kind of answer.', 
    'This method works better for fluid layouts that need to adapt to the height of the screen they are being viewed on and also works for the overflow-x property.'
    ]

def make_story():
    return random.choice(text)
