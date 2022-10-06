from django.dispatch import Signal

mqtt_connect = Signal(["client"])
mqtt_pre_publish = Signal(["client", "topic", "payload", "qos", "retain"])
mqtt_publish = Signal(["client", "userdata", "mid"])
mqtt_disconnect = Signal(["client", "userdata", "rc"])
