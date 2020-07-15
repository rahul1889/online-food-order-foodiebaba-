# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class ActionHelloWorld(FormAction):
    def name(self) -> Text:
        return "order_form"


    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["item", "quantifier", "quantity"]
        
    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:
#
       dispatcher.utter_message(template="utter_submit", item=tracker.get_slot('item'),
                                quantifier=tracker.get_slot('quantifier'), quantity=tracker.get_slot('quantity'))

       return []




    def slot_mappings(self):
        #-> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        return {
            "item": [self.from_entity(entity="item", intent='order'),self.from_text()],
            "quantifier": [self.from_entity(entity="quantifier", intent="item_quantifier"),self.from_text()],
            "quantity": [self.from_entity(entity="quantity", intent="item_quantityr"),self.from_text()]
        }
