import os
import shutil
import json
import json_source_map
from pathlib import Path

class SeverityEvaluetor:
    """
    Manage the logic for evaluating the severity of a rule based on predefined key
    
    """

  #Set of keywords that indicate a specific severity High/Medium/Low 
    high_severity = {"open", "public", "*", "0.0.0.0", "ssh", "rdp", "internet", "admin",
                    "fromport", "toport", "master", "password", "protection"}

    medium_severity = {"encryption", "unencrypted", "policy", "role", "privilege",
                    "logging", "audit", "kms", "encrypted", "group", "az", "property", "policies"}

    low_severity = {"naming", "tag", "versioning", "backup", "idle", "default", "description",
                "engine", "0", "1", "2", "listelement"}
      
    #function to evaluate the severity of the rule
    def severity_evaluation(rule):
        """
        Evaluates the severity of a control rule based on keywords
        present in the rule text.
    
        Args: 
            rule (strg): The string text of the rule to analize

        Return:
            stg: The assigned severity ("High", "Medium", "Low") or None

        """ 
        rule_lower = rule.lower()

        #check for high severity keywords
        if any(keyword in rule_lower for keyword in self.high_severity):
            return "High"
        #check for medium severity keywords
        if any(keyword in rule_lower for keyword in self.medium_severity):
            return "Medium"
        #check for low severity keywords
        if any(keyword in rule_lower for keyword in self.low_severity):
            return "Low"
        #return None in case there is no match
        return None 



#function to create a folder if not exist and put inside the json file to be parsed to lint
def save_file(raw_data):
    """
    Make the directory "user_data" if not exist and save the raw data inside

    Args: raw_data (strg): The string of data form the Json to write on the file

    """
    os.makedirs("user_data", exist_ok=True)

    #define the path for the file
    second_file_name = os.path.join("user_data", "line_mapping.json")

    try:
        with open(second_file_name, "w")as secondfile:
            secondfile.write(raw_data)

    except Exception as e:
        print("Exception occurred while writing the file")


#function to delete the created folder once utilized
def delete_folder():
    """
    Delete recursive the temporaney work-directory ("user_data")

    """
    folder_path = "./user_data"

    try:
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
    except Exception:
        print("Something get wrong while deleting the folder")

#function to calculate the line of the issue in the json
def find_line(data, match_path): 
    """
    Use an element's JSONPath to find its exact position (row:column) in the JSON file.
    
    Args: 
        data(strg): The path of JSON file to analize
        match_path(strg): The JSONPath 

    Return:
        strg: the coordinate as "line/column" or "not found" for an error 
    """
    #convert the path string into a Path Object
    file_path = Path(data)
    #open the file_path with error handeling 
    try:
        with open(file_path, "r") as f:
            the_json = f.read()
    except Exception as e:
        print("Exception while open the file path")
    try:
        source_map = json_source_map.calculate(the_json)

        line = source_map[match_path].value_start.line
        column = source_map[match_path].value_start.column

        return f"{line + 1}:{column}"
    except Exception:
        return "not found"


def create_path_for_coordinate_resources(matches):
    """
    Take a list of nodes and joins them to form a valid JSONPath, required by the json_source_map

    Args:
        matches (list): A list of sting that rappresent the nodes in the Path Json 

    Returns:
        strg: the formatted JSONPath
    """
    string_matches = [str(item) for item in matches]
    final_result = '/' + '/'.join(string_matches)

    return final_result
