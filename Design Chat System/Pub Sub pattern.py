# 1786. Pub Sub Pattern
# 中文English
# Pub/Sub pattern is a wide used pattern in system design. In this problem, you need to implement a pub/sub pattern to support user subscribes on a specific channel and get notification messages from subscribed channels.

# There are 3 methods you need to implement:

# subscribe(channel, user_id): Subscribe the given user to the given channel.
# unsubscribe(channel, user_id): Unsubscribe the given user from the given channel.
# publish(channel, message): You need to publish the message to the channel so that everyone subscribed on the channel will receive this message. Call PushNotification.notify(user_id, message) to push the message to the user.
# Example
# subscribe("group1",  1)
# publish("group1", "hello")
# >> user 1 received "Hello"
# subscribe("group1", 2)
# publish("group1", "thank you")
# >> user 1 received "thank you"
# >> user 2 received "thank you"
# unsubscribe("group2", 3)
# >> user 3 is not in group2, do nothing
# unsubscribe("group1", 1)
# publish("group1", "thank you very much")
# >> user 2 received "thank you very much"
# publish("group2", "are you ok?")
# >> # you don't need to push this message to anyone
# If there are more than 1 user subscribed on the same channel, it doesn't matter the order of time users receiving the message. It's ok if you push the message to user 2 before user 1.

# subscribe("group1", 1)
# subscribe("group1", 2)
# publish("group1", "thank you")
# unsubscribe("group2", 3)
# unsubscribe("group1", 1)
# publish("group1", "thank you very much")
# publish("group2", "are you ok?")

'''
Definition of PushNotification
class PushNotification:
    @classmethod
    def notify(user_id, message):
'''
from collections import defaultdict
class PubSubPattern:
    def __init__(self):
    # do intialization if necessary 
        self.subs = defaultdict(set)

    """
    @param: channel: a channel name
    @param: user_id: a user id
    @return: nothing
    """
    def subscribe(self, channel, user_id):
        # write your code here
        self.subs[channel].add(user_id)

    """
    @param: channel: a channel name
    @param: user_id: a user id
    @return: nothing
    """
    def unsubscribe(self, channel, user_id):
    	# write your code here
    	if user_id in self.subs[channel]:
    	    self.subs[channel].remove(user_id)
        
    """
    @param: channel: a channel name
    @param: message: need send message
    @return: nothing
    """
    def publish(self, channel, message):
		# write your code here
        for user in self.subs[channel]:
            PushNotification.notify(user, message)