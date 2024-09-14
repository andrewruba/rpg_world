
def simple_change(x):
    def anon(**kwargs):
        return x
    return anon

def multi_effect_target_example(**kwargs):
    target = kwargs.get("target")
    return -(50 + (target.stats.get("focus") * 0.5)) * (1 - (target.stats.get("armor") / 100.0))

def multi_effect_recipient_example(**kwargs):
    recipient = kwargs.get("recipient")
    return -(50 + (recipient.stats.get("focus") * 0.1)) * (1 - (recipient.stats.get("armor") / 100.0))

