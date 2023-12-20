import os

# To install allure run: npm install -g allure-commandline --save-dev

allure_dir = os.path.join(".", 'allure')

print("Running tests...")
os.system(f"pytest.exe test --alluredir {allure_dir}")

print("Generating report...")
os.system(f"allure serve {allure_dir}")
