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
        ' Amazon Web Services is responsible for protecting the global infrastructure that runs all of the services offered in the AWS cloud. This infrastructure is comprised of: ',
        [
            'The hardware, operational software, networking, and facilities that run AWS services.',
            'The facilities that run AWS services.',
            'The hardware and operational software',
            'The network and facilities that run AWS services.'
        ],
        ['concept', 'security'],
        ['1'],
        ''
    )
]
