Introduction:
The following code defines a PyQt5 QWidget-based class named `SHOT_CREATOR`. This class is designed as a template to retrieve data from ShotGrid and handle specific actions when data is received. 
You are tasked with creating a structure based on a dictionary that includes the keys 'code' and 'sg_sequence'. 
Example: {'code' : 'DEV_0010A_0010', 'sg_sequence' : {'type': 'Sequence', 'code' : '0010A'}}

The structure should follow a specific pattern using the given example, such as "040_SOURCES/{shot}/010_PLATES". 
If the shot contains sequence it contain a sequence folder.
Examples:
040_SOURCES/0010A/DEV_0010A_0010/010_PLATES  # if sequence exists and is not Nonetype
040_SOURCES/DEV_0010A_0010/010_PLATES  # if sequence does not exist / or is Nonetype

Your Task:
- Use the provided dictionary data to build a directory structure.
- Use the `code` and `sg_sequence` values from the dictionary to populate the structure.
- Use the structure from provided CONF file.

Below are detailed comments explaining the various parts of the code.


Notes:
CWD (Current Working Directory) points to main NL Hub directory. Please note that loading files will work under ./plugins/<plugin_folder>/<file>
