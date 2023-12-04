#תוכנית שמכניסה למשתמש אפשרות לשנות את השנייה של השעון לעלות את השניות\ דקות שעות \ לכתוב שעה ,
#אני יכול לתת את השעה ההתחלתית של השעון ואם לא נתתי זה 00:00


class Clock():

    def __init__(self, hours = 00, minutes = 00, seconds = 00):

        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

        self.time = str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)

    def get_time(self):
        '''
        take all the variables and join them into a sting - 00:00
        :return: hours : minutes seconds
        '''
        self.time = str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)
        return



    def set_time(self,value_type, new_value):
        '''
        will receive from the client what would he like to change(hours/minutes/seconds) and what value to change to
        :param value_type: hours/minutes/seconds
        :type new_value: int
        :return: None
        '''

        #setting the new value
        if value_type == "hours":
            self.hours = new_value

        elif value_type == "minutes":
            self.minutes = new_value

        elif value_type == "hours":
            self.seconds = new_value
        else:
            print("please follow the given instractions...")

        #changing the time

       # get_time()

        return

    def add_time(self, value_type, new_value):
        '''

        :param value_type:
        :param new_value:
        :return:
        '''

        
