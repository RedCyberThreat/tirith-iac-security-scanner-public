import json as j
from rule_engine import (
    S3Checker,
    EC2Checker,
    IAMChecker,
    RDSChecker, 
)

Gravity_Order ={
    'High' : 1,
    'Medium' : 2,
    'Low' : 3
}

def sort_findings_by_severity(findings_dict):
    """
    Sort a Dict of result in base of the gravity (High, Medium, Low)
    Complexity: O(n log n)
    """
    sorted_list = sorted(
        findings_dict.items(),
        key = lambda item: Gravity_Order.get(item[1], 99) 
        )

    return sorted_list

#list of s3 rules  
s3_public_access_rules = ['BlockPublicAcls', 'IgnorePublicAcls', 'BlockPublicPolicy', 'RestrictPublicBuckets']
#list of SecurityGroup rules
list_of_securityGroup_rules = ['FromPort', 'ToPort']
#list for IAM rules
list_of_iam_rules = ['Action']
#list of RDS rules
list_of_rds_rules = ['StorageEncrypted']
def append_result(result, type_name, all_findings):
    if len(result) > 0:
        if type_name not in all_findings:
            all_findings[type_name] = []
        all_findings[type_name].append(result)

def threat_check(data):
    all_findings = {}
    #loop in the uploded json to check for threats
    try:
        reseurces = data['Resources']
    except KeyError:
        reseurces = data['Resource']
    for key, value in reseurces.items():

        #checking for S3 threaths
        if 'S3' in value.get('Type', '') and 'S3::Bucket' in value.get('Type', ''):
            s3_checker = S3Checker()
            result1 = s3_checker.check_public_access(s3_public_access_rules, value)
            result2 = s3_checker.check_encryption(value)

            for result in [result1, result2]:
                type_name = 'AWS::S3::Bucket'
                append_result(result, type_name, all_findings)
            
        #checking for EC2 threats
        if 'EC2' in value.get('Type', '') and 'EC2::SecurityGroup' in value.get('Type', ''):

            ec2_checker = EC2Checker()
            for i, _ in enumerate(value['Properties'].get('SecurityGroupIngress', [])):
                ec2_checker.check_securitygroups(list_of_securityGroup_rules, i, value)

            result = ec2_checker.get_findings()
            type_name = 'AWS::EC2::SecurityGroup'
            append_result(result, type_name, all_findings)
                
        #checking for IAM threats
        if 'IAM' in value.get('Type', '') and 'IAM::Role' in value.get('Type', ''):
                
                iam_checker = IAMChecker()
                iam_checker.check_role(list_of_iam_rules, value)
                result = iam_checker.get_findings()

                type_name = 'AWS::IAM::Role'
                append_result(result, type_name, all_findings)

        #checking for RDS threats
        if 'RDS' in value.get('Type', '') and 'RDS::DBInstance' in value.get('Type', ''):
                
                rds_checker = RDSChecker()
                rds_checker.check_dbinstance(list_of_rds_rules,value)
                result = rds_checker.get_findings()
        
                type_name = 'AWS::RDS::DBInstance'
                append_result(result, type_name, all_findings)
    
    sorted_findings = {}

    for type_name, list_of_results in all_findings.items():

        combined_result = {}
        for result_dict in list_of_results:
            combined_result.update(result_dict)

        sorted_result_list = sort_findings_by_severity(combined_result)

        sorted_findings[type_name] = sorted_result_list

    return j.dumps(sorted_findings, indent=2)

