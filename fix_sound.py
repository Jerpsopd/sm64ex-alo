import json
import os
import glob

def update_sound_field(json_file):
    # Load the JSON data
    with open(json_file, 'r') as file:
        data = json.load(file)
    print(json_file)

    # Construct the sound folder path from the sample_bank key
    sample_bank = data.get("sample_bank", "")
    sound_folder = os.path.join("./sound/samples/", sample_bank)

    # Iterate over the instruments
    for instrument_key, instrument in data.get("instruments", {}).items():
        for sss in ["sound", "sound_lo", "sound_hi", "percussion"]:
            for a in range(2):
                try:
                    if a == 0:
                        sound_prefix = instrument.get(sss)
                    else:
                        sound_prefix = instrument.get(sss).get("sample")
                    if instrument_key == "Hi-Hat":
                        print("Hi-Hat")
                        print(instrument.get("sound"))
                    if sound_prefix == "3B":
                        print(sound_prefix)
                    
                    # Skip if no sound prefix is present
                    if not sound_prefix:
                        continue

                    # Find a matching file in the specified folder
                    matching_files = [
                        f for f in os.listdir(sound_folder)
                        if f.startswith(f"{sound_prefix}_")
                    ]

                    if matching_files:
                        # Use the first matching file (if multiple found) without the extension
                        if a == 0:
                            instrument[sss] = os.path.splitext(matching_files[0])[0]
                            print(p)
                        else:
                            instrument[sss]["sample"] = os.path.splitext(matching_files[0])[0]
                except:
                    pass
            
            if "percussion" == instrument_key:
                print("precussion")
                
                
                for p in instrument:
                    try:
                        sound_prefix = p.get("sound").get("sample")

                        # Skip if no sound prefix is present
                        if not sound_prefix:
                            continue

                        # Find a matching file in the specified folder
                        matching_files = [
                            f for f in os.listdir(sound_folder)
                            if f.startswith(f"{sound_prefix}_")
                        ]

                        if matching_files:
                            # Use the first matching file (if multiple found) without the extension
                            p["sound"]["sample"] = os.path.splitext(matching_files[0])[0]
                    except:
                        sound_prefix = p.get("sound")

                        # Skip if no sound prefix is present
                        if not sound_prefix:
                            continue

                        # Find a matching file in the specified folder
                        matching_files = [
                            f for f in os.listdir(sound_folder)
                            if f.startswith(f"{sound_prefix}_")
                        ]

                        if matching_files:
                            # Use the first matching file (if multiple found) without the extension
                            p["sound"] = os.path.splitext(matching_files[0])[0]

    # Save the updated JSON back to the file
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

# Example usage
json_file_path = glob.glob(os.path.join("./sound/sound_banks", "*.json"))

for a in json_file_path:
    try:
        update_sound_field(a)
    except:
        pass
