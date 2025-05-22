# iot_engine.py




def handle_iot_control(user_input, entities=None):
    return "💡 Done."

def handle_control_lights(user_input, entities=None):
    if "off" in user_input.lower():
        return "💡 Turning off the lights."
    return "💡 Turning on the lights."

def handle_turn_off_lights(user_input, entities=None):
    return "💡 Turning off the lights."

def handle_control_temperature(user_input, entities=None):
    return "🌡️ Adjusting the thermostat to your preferred setting."

def handle_sensor_status(user_input, entities=None):
    return "📟 Checking sensor status... All sensors are operating normally."

def handle_device_status(user_input, entities=None):
    return "🔌 Devices connected and operational."

def handle_control_appliance(user_input, entities=None):
    return "🧺 Appliance has been turned on/off as requested."

def handle_control_lock(user_input, entities=None):
    return "🔒 Locking the doors now."

def handle_control_thermostat(user_input, entities=None):
    return "🌬️ Thermostat set to a comfortable temperature."

def iot_engine_dispatcher(intent, user_input, entities=None):
    if intent in ["turn_on_lights", "control_lights"]:
        return handle_control_lights(user_input, entities)
    elif intent == "turn_off_lights":
        return handle_turn_off_lights(user_input, entities)
    elif intent == "control_temperature":
        return handle_control_temperature(user_input, entities)
    elif intent == "sensor_status":
        return handle_sensor_status(user_input, entities)
    elif intent in ["device_connection", "device_integration", "get_device_status"]:
        return handle_device_status(user_input, entities)
    elif intent == "control_appliance":
        return handle_control_appliance(user_input, entities)
    elif intent == "control_lock":
        return handle_control_lock(user_input, entities)
    elif intent == "control_thermostat":
        return handle_control_thermostat(user_input, entities)
    else:
        return "🤖 I’m still learning how to handle that smart home request."
