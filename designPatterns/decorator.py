
def add_footer(function):

    def decorator():
        ret = function()

        return "{} \n subject to copyright".format(ret)
    return decorator

@add_footer
def best_song():
    return "And I cant stop falling in love with you"


print(best_song())