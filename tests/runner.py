# Example command
# cd to orangeHRMPython>
# python tests/runner.py --test_dir=tests --run_allure=true
# python tests/runner.py --test_dir=tests --run_allure=true --behave_options="-k -t tcId001"
import logging
import subprocess
import argparse
from datetime import datetime
import os
import pathlib
import platform

def add_drivers_to_path():

    print("Adding webdrivers to path.")
    curr_file_path = pathlib.Path(__file__).parent.absolute()

    if platform.system() == 'Mac':
        webdriver_path = os.path.join(curr_file_path, 'webdrivers', 'mac')
    elif platform.system() == 'Windows':
        webdriver_path = os.path.join(curr_file_path, 'webdrivers', 'wimdows')
    elif platform.system() == 'Linux':
        webdriver_path = os.path.join(curr_file_path, 'webdrivers', 'linux')
    else:
        raise Exception("Unknown platform. Unable to add webdrivers to path.")

    current_path = os.environ.get['PATH']
    new_path = webdriver_path + ':' + current_path
    os.environ['PATH'] = new_path

def get_unique_run_id():

    if os.environ.get("BUILD_NUMBER"):
        unique_run_id = os.environ.get("BUILD_NUMBER")
    elif os.environ.get("CUSTOM_BUILD_NUMBER"):
        unique_run_id = os.environ.get("CUSTOM_BUILD_NUMBER")
    else:
        unique_run_id = datetime.now().strftime("%Y%m%d%H%M%S")

    os.environ['UNIQUE_RUN_ID'] = unique_run_id

    return unique_run_id

def create_output_directory(prefix='results_', report_path='reports'):

    global run_id
    if not run_id:
        raise Exception("Variable 'run_id' is not set. Unable to create output directory")

    curr_file_path = pathlib.Path(__file__).parent.absolute() / report_path
    dir_to_create = os.path.join(curr_file_path, prefix + str(run_id))
    os.mkdir(dir_to_create)

    print(f"Created output directory: {dir_to_create}")

    return dir_to_create

if __name__ == '__main__':
    rs = subprocess.run('behave', shell =True)
    # if rs.returncode != 0:
    #     raise Exception("E")

    run_id = get_unique_run_id()

    parser = argparse.ArgumentParser()
    parser.add_argument('--test_dir', required=True, help="Location of test file.")
    parser.add_argument('--behave_options', type=str, required=False,
                        help="String of behave options. For Example tags like '-t <tag name>'")
    parser.add_argument('--run_allure', choices=['true', 'True', 'false', 'False'], required=False,
                        help="To run allure report server at the end of the test run or not.")
    args = parser.parse_args()
    test_dir = args.test_dir
    run_allure = args.run_allure
    behave_options = '' if not args.behave_options else args.behave_options

    output_dir = create_output_directory()
    json_out_dir = os.path.join(output_dir, 'json_report_out.json')
    junit_out_dir = os.path.join(output_dir, 'junit_report_out')
    allure_out_dir = os.path.join(output_dir, 'allure_report_out')

    command = f'behave -k --logging-level INFO --summary -f json.pretty -o "{json_out_dir}" ' \
              f'--junit --junit-directory "{junit_out_dir}" ' \
              f'-f allure_behave.formatter:AllureFormatter -o {allure_out_dir} ' \
              f'{behave_options} ' \
              f'{test_dir} '

    print(f"Running command: {command}")
    logging.info(f"Running command: {command}")

    rs = subprocess.run(command, shell=True)

    print(f"JSON Report directory: {json_out_dir}")
    print(f"JUNIT Report directory: {junit_out_dir}")
    print(f"Allure Report directory: {allure_out_dir}")

    if run_allure and run_allure.upper() == 'TRUE':
        subprocess.run(f'allure serve {allure_out_dir}', shell=True)
