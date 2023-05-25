import requests
from difflib import SequenceMatcher
from peace_snippets import daily_exercises, emotion_responses
from email import utils


class Content:
    def __init__(self, message, request):
        self.message = message
        self.pdk_url = request.headers['PDK-URL']

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
    def schedule_message(self, date_time, payload):
        formatted_dt = utils.format_datetime(date_time)
        schedule_url = self.pdk_url + "/schedule"
        payload = {
            "dateTime": formatted_dt,
            "msg": payload
        }
        res = requests.post(schedule_url, json=payload)
        return 'OK'

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
    
    def req_message_data(self):
        # The inbound message on self.message is to
        # our app, and we want outbound messages to
        # see what we've sent
        q_str = "/messages?recipient=" + self.message.recipient
        res = requests.get(self.pdk_url + q_str)
        return res.json()

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
            
    def pick_scheduled_exercise(self):
        prev_msg_data = self.req_message_data()
        prev_sent_msgs = [m['message'] for m in prev_msg_data]
        print("PREV SENT MSGS: ", prev_sent_msgs)
        #TODO: use similarity search to allow for some 
        #changes in exercises text
        unsent_exercises = list(set(daily_exercises) - set(prev_sent_msgs))
        print("\n UNSENT EXERCISES", unsent_exercises)
        
        return unsent_exercises[0]

