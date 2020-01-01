def create_test_item(problem:str, options:[str], tags:[str], answers:[str], description:str):
    return {
        'problem': problem,
        'options': options,
        'tags': tags,
        'answers': answers,
        'description': description
    }

TEST_LIST = [
    create_test_item(
        'What is fault-tolerance?',
        [   
            'A block of code designed to perform a particular task',
            'Used to perform arithmetic on numbers (literals or variables)',
            'A special variable, which can hold more than one value at a time',
            'The ability for a system to remain in operation even if some of the components used to build the system fail',
        ],
        ['concept', 'fault-tolerance'],
        ['4'],
        ''
    ),
    create_test_item(
        'Amazon Web Services is responsible for protecting the global infrastructure that runs all of the services offered in the AWS cloud. This infrastructure is comprised of: ',
        [
            'The hardware, operational software, networking, and facilities that run AWS services.',
            'The facilities that run AWS services.',
            'The hardware and operational software',
            'The network and facilities that run AWS services.'
        ],
        ['concept', 'security'],
        ['1'],
        ''
    ),
    create_test_item(
        'AWS Key Management Service supports two kinds of keys.  Which of the following are the keys supported by AWS Key Management Service? ',
        [
            'Security keys and Network keys',
            'Master keys and data keys',
            'Memory keys and data keys',
            'Encrypt keys and decrypt keys'
        ],
        ['security', 'KMS'],
        ['2'],
        ''
    ),
    create_test_item(
        'By default, how many Amazon RDS DB instances can a customer have running?',
        [
            '20',
            '30',
            '40',
            '100'
        ],
        ['datbase', 'RDS'],
        ['3'],
        'By default, customers are allowed to have up to a total of 40 Amazon RDS DB instances. Of those 40, up to 10 can be Oracle or SQL Server DB Instances under the License Included model. All 40 can be used for Amazon Aurora, MySQL, MariaDB, Oracle, SQL Server, or PostgreSQL under the BYOL model.'
    )
]
