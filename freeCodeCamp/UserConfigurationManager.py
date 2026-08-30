def add_setting(settings_dictionary, setting_tuple):
    new_key = setting_tuple[0].lower()
    new_value = setting_tuple[1].lower()

    if new_key not in settings_dictionary: #ja e O(1)
        settings_dictionary[new_key] = new_value
        return f"Setting '{new_key}' added with value '{new_value}' successfully!"
    else:
        return f"Setting '{new_key}' already exists! Cannot add a new setting with this name."
    

def update_setting(settings_dictionary, setting_tuple):
    new_key = setting_tuple[0].lower()
    new_value = setting_tuple[1].lower()
    
    if new_key in settings_dictionary: 
        settings_dictionary[new_key] = new_value
        return f"Setting '{new_key}' updated to '{new_value}' successfully!"
    else:
        return f"Setting '{new_key}' does not exist! Cannot update a non-existing setting."
def delete_setting(settings_dictionary, key):
    new_key = key.lower()
    if new_key in settings_dictionary: 
        settings_dictionary.pop(new_key)
        return f"Setting '{new_key}' deleted successfully!"
    else:
        return "Setting not found!"
def view_settings(settings_dictionary):
    if not settings_dictionary:
        return "No settings available."
    else:
        linhas = [f"{key.capitalize()}: {value}" for key, value in settings_dictionary.items()]
    return "Current User Settings:\n" + "\n".join(linhas) + "\n"
    
test_settings = {
    "theme": "dark",
    'notifications': 'enabled', 
    'volume': 'high'
}