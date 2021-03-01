class Date:

    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def to_int(cls, str_date):
        try:
            date = str_date.split('-', 3)
            cls.d = int(date[0])
            cls.m = int(date[1])
            cls.y = int(date[2])
        except:
            raise TypeError
        return None

    @staticmethod
    def validation(str_date):
        ret = 0
        # очень простые проверки.
        try:
            date = str_date.split('-', 3)
            if (0 < int(date[0]) < 32 and 0 < int(date[1]) < 13 and 999 < int(date[2]) < 9999):
                ret = 1
        except:
            pass

        return ret

if not Date.validation("22-12-1999"):
    print("дата некорректная")
Date.to_int("22-12-1999")
