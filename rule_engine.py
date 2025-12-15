from utilities import severity_evaluation

def get_nested_values(data,path):
    """
    Navigate a nested data structure (dictionary or list) using a list of keys/indexes as the 'path'
    
    Args:
        data (dict|list): the structure of datas to Navigate
        path(list): list of key (strg) or indexes (strg) that define the path

    Return:
        the found value or None if the path doesn't exist
    """
    current = data 
    
    for key in path:
        if isinstance(current, list):
            if not isinstance(key, int):
                return None
            try:
                current = current[key]
            except IndexError:
                return None

        elif isinstance(current, dict):
            current = current.get(key)
            if current is None:
                return None

        else:
            return None
    return current


class BaseChecker:
    def __init__ (self):
        self.dangerous_rules = { }

    def add_finding(self, rule_name, rule_text=None):
        text_to_evaluate = rule_text if rule_text else rule_name
        self.dangerous_rules[rule_name] = severity_evaluation(text_to_evaluate)

    def get_findings(self):
        return self.dangerous_rules

class S3Checker(BaseChecker):

    def check_public_access(self, list_of_s3_rules, value):

        path_base = ['Properties', 'PublicAccessBlockConfiguration']

        for rule_name in list_of_s3_rules: 
            config_value = get_nested_values(value, path_base + [rule_name])

            if config_value is False:
               self.add_finding(rule_name)

        return self.get_findings()

    def check_encryption(self, value):

        path_list = ['Properties', 'BucketEncryption', 'ServerSideEncryptionConfiguration', 0, 'ServerSideEncryptionByDefault']

        algorithm = get_nested_values(value, path_list + ['SSEAlgorithm'])
        kms_id = get_nested_values(value, path_list + ['KMSMasterKeyID'])

        is_safe = (algorithm == "AES256") or (algorithm == 'aws:kms' and kms_id)

        if not is_safe:

            self.add_finding('ServerSideEncryption', 'ServerSideEncryptionConfiguration')

        return self.get_findings()

class EC2Checker(BaseChecker):

    dangerous_port = ["22", "3389"]

    def check_securitygroups (self, list_of_securityGroup_rules, iter_index, value):

        for rule_name in list_of_securityGroup_rules:
            path_cidr = ['Properties', 'SecurityGroupIngress', iter_index, "CidrIP"]
            path_port = ['Properties', 'SecurityGroupIngress', iter_index, rule_name]

            cidr_ip = get_nested_values(value, path_cidr)
            port_value = get_nested_values(value, path_port)

            is_public_cdir = cidr_ip == "0.0.0.0/0"
            is_dangerous_port = str(port_value) in self.dangerous_port

            if is_dangerous_port and is_public_cdir:
                self.add_finding(rule_name)

        return self.get_findings()

class IAMChecker(BaseChecker):

    def check_role(self, list_of_iam_rules, value):

        for rule_name in list_of_iam_rules:

            path_role = ['Properties', 'AssumeRolePolicyDocument', 'Statement', 0, rule_name]
            role_value = get_nested_values(value, path_role)

            path_policy = ['Properties', 'Policies', 0, 'PolicyDocument', 'Statement', 0, rule_name]
            policy_value = get_nested_values(value, path_policy)

            if role_value == '*' or policy_value == '*':

                self.add_finding('Actions', rule_text = '*')

                break

        return self.get_findings()

class RDSChecker(BaseChecker):

    def check_dbinstance(self, list_of_rds_rules, value):

        for rule_name in list_of_rds_rules:

            config_value = get_nested_values(value, ['Properties',rule_name])

            if config_value is False:
                self.add_finding(rule_name)

        return self.get_findings()
