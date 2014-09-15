import random
import willie.module


# TODO: Make this a config option?
HOPE = 0.05


def divergence_value():
    if HOPE > random.random():
        return "This world line has Divergence Value of %.6f YA FOUND IT!" % (1 + random.random() / 10)
    else:
        return "This world line has Divergence Value of %.6f" % random.random()


@willie.module.commands('wl')
@willie.module.example('.wl', 'This world line has Divergence Value of 0.512616')
def worldline(bot, trigger):
    bot.reply(divergence_value())


if __name__ == "__main__":
    print(divergence_value())
