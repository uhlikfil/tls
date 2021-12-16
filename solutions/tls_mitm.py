##############################
########### Task 5 ###########
##############################

from solutions.tls_agent import Agent


class MITM:
    def __init__(self) -> None:
        self.msg = None
        self.current_target: Agent = Agent()
        self.other_target: Agent = Agent()

    def receive_public_data(self, p, g):
        self.__swap_current_target()  # other receives, because he's going to send it to that side
        self.current_target.receive_public_data(p, g)

    def send_public_data(self):
        return self.current_target.send_public_data()

    def receive_public_key(self, key):
        self.current_target.receive_public_key(key)

    def send_public_key(self):
        self.__swap_current_target()
        return self.current_target.send_public_key()

    def intercept_message(self, msg):
        """intercept message from target1 to target2"""
        self.current_target.receive_message(msg)
        self.msg = self.current_target.msg
        self.other_target.msg = self.msg
        self.__swap_current_target()  # he's probably going to reply
        return self.current_target.send_message()

    def __swap_current_target(self):
        self.current_target, self.other_target = self.other_target, self.current_target
