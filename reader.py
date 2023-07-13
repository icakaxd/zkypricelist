import os

# Files
old_pricelist_path = "pricelist.txt"
new_pricelist_path = "new_pricelist.txt"

# Check if the new pricelist file exists
if os.path.exists(new_pricelist_path):
    with open(new_pricelist_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        if lines:
            # Get the last item
            last_item = lines[-1].split(",")[0]
        else:
            last_item = None
else:
    last_item = None
    # Create new pricelist file if it doesn't exist
    open(new_pricelist_path, 'a', encoding="utf-8").close()

# Read the old pricelist and add items to the new one
with open(old_pricelist_path, "r", encoding="utf-8") as old_file, open(new_pricelist_path, "a", encoding="utf-8") as new_file:
    skip = True if last_item else False
    for line in old_file:
        id = line.split(",")[0]
        name = line.rsplit(",", 1)[0][len(id) + 1:]
        price = line.rsplit(",", 1)[1].strip()
        if skip:
            if id == last_item:
                skip = False
            continue
        print(f"Product: {name}, Price: {price}.")
        print("Press Enter to add this item or input any character to skip.")
        user_input = input().strip()
        if not user_input:
            new_file.write(line)
