from difflib import SequenceMatcher
from peace_snippets import daily_exercises, emotion_responses
from email import utils


class Content:
    def __init__(self, message, request):
        self.message = message

    def intro_message():
        return '''
        Hi, I'm Peace Pal.
        Together- we're going to find more inner peace.
        Every day- I'll send you an exercise to help you manage the feelings that are limiting your peace. 
        Feel free to message me whenever you're not feeling at peace, and I'll do my best to share something helpful.
        \n\n\n 
        ______
        If you're confused at any time, just reply 'help'
        '''

    def handle_reply(self):
        #TODO: stop logic to call PDK
        if 'help' in self.message.message.lower():
            return '''
            Every day I'll send you an exercise that's meant to help improve your peace. 
            At any time, you can reply with 'stop' to stop receiving these daily messages.
            You can also send a me a new message detailing something that's preventing you from feeling at peace and I'll do my best to send a rely that will help.
            '''
        else:
            print('Unhandled reply')
            pass
    

    def similar(self, str_a, str_b):
        similarity = SequenceMatcher(None, str_a, str_b).ratio()
        return True if similarity > .9 else False

    def emotion_response(self, emotion_label):
        matched_responses = [er for er in emotion_responses if er['emotion'] == emotion_label]
        if len(matched_responses) > 0:
            res = matched_responses[0]['response']
        else:
            res = "I'm still learning. Check back soon."
        return res
            
    def pick_scheduled_exercise(self, prev_messages):
        #TODO: use similarity search to allow for some 
        #changes in exercises text
        unsent_exercises = list(set(daily_exercises) - set(prev_messages))
        print("\n EXERCISE TO SEND", unsent_exercises[0])
        
        return unsent_exercises[0]

