## SELENIUM PYTHON BEHAVE
1. Setup project then create file setup.py
   - install setup.py
     - open CMD, terminal or etc and execute "python setup.py install"
     - and "python setup.py develop"

2. Create common class as config, function, steps etc
3. Create feature file
4. Create step
    - Call step in other step
   
                    @given("user logged in") 
                    def user_logged_in(context):
                        context.execute_steps(u""""
                        Given user go to 'login' page
                        When user enters the username
                        And user enters the password
                        And user click login button
                        """)

5. Generate report menggunakan allure framework
	- install allure https://docs.qameta.io/allure/
	- install allure "pip install allure-behave" python https://pypi.org/project/allure-behave/ 

6. Run behave test
	- behave .\tests\ (execute all feature)
	- behave .\tests\ -tags=tcId01 (execute specific scenario)
	- behave .\tests\ --logging-level=LOGGING_LEVEL (execute specific scenario)
    - behave .\tests\ -e login.feature (execute all exclude specific feature file)
	- behave .\tests\ -f allure_behave.formatter:AllureFormatter -o .\tests\reports  (execute all feature and generate allure report with name "report")
    - allure serve .\tests\reports (Convert and open allure report automatically in your browser)

6. Run python runner
	- python .\tests\runner.py --test_dir=tests --run_allure=true (generate allure report)
    - python .\tests\runner.py --test_dir=tests --run_allure=true --behave_options="-k -t tcId001" (run with tags)
    - python .\tests\runner.py --test_dir=tests --run_allure=false --behave_options="-k -D browser=firefox"  (run with specific browser)