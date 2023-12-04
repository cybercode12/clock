#תוכנית שמכניסה למשתמש אפשרות לשנות את השנייה של השעון לעלות את השניות\ דקות שעות \ לכתוב שעה ,
#אני יכול לתת את השעה ההתחלתית של השעון ואם לא נתתי זה 00:00


class Clock():

    def __init__(self, hours = 00, minutes = 0, seconds = 0):

        self.hours = 00
        self.minutes = 0
        self.seconds = 0



    def get_time(self):
        '''
        take all the variables and join them into a sting - 00:00
        :return: hours : minutes seconds
        '''
        time = str(self.hours) + ":" + str(self.minutes) + str(self.seconds)
        return time

