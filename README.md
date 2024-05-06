# Final Project Links

- [Final Deployment](http://gullapallimonica.pythonanywhere.com/usignup/)
- [Final Github Repo](https://github.com/CSCI-5828-S24/Fse-finalproject-Group20.git)
- [Final User Stories](https://trello.com/b/DeGjB8FM/fseportfoliopulse)
- [Final Overview Page](https://github.com/coloradocollective/5828_S24/wiki/Team-20:-PortfolioPulse)
- [Final PPT](https://docs.google.com/presentation/d/14DMFWzqRrVgIF8F3mQoO-nuW8QUgIT5BpIQsqe7xXz8/edit?usp=sharing)

# Rubric Items

| Topic | Links to the Code | Comments |
|:-----|:----------------:|:---------:|
| Web application basic form, reporting | [Link](https://github.com/CSCI-5828-S24/Fse-finalproject-Group20/tree/main/fin_app/templates) | Includes SignUp, login, create Stock investments form, create crypto investments form etc |
| Data collection | [Link](https://github.com/CSCI-5828-S24/Fse-finalproject-Group20/tree/main/collector_app) | Fetches data from the API in accordance with data entered by user in fin_app |
| Data analyzer | [Link](https://github.com/CSCI-5828-S24/Fse-finalproject-Group20/tree/main/analyzer_app) | Performs visualization on updating data in the database from collector app functions along with entered data in fin_app using matplotlib |
| Unit tests | [Link](https://github.com/CSCI-5828-S24/Fse-finalproject-Group20/blob/main/fin_app/tests.py) | Test_usignup_view, test_ulogin_view, test_ulogout_view, test_home_view, test_create_view, test_view_view, test_create_crypto_view and more |
| Data persistence any data store | [Link 1](http://gullapallimonica.pythonanywhere.com/admin/login/?next=/admin/) and [Link 2](https://github.com/CSCI-5828-S24/Fse-finalproject-Group20/blob/main/db.sqlite3) | Efficient to view using /admin in Django apps |
| Rest collaboration internal or API endpoint | [Link](https://github.com/CSCI-5828-S24/Fse-finalproject-Group20/blob/main/collector_app/templatetags/yfinance_tags.py) | Used yfinance API or Yahoo Finance API to fetch close_price of stock |
| Product environment | [Link](http://gullapallimonica.pythonanywhere.com/usignup/) | PythonAnywhere is our deployment platform |
| Integration tests | [Link](https://github.com/CSCI-5828-S24/Fse-finalproject-Group20/blob/main/analyzer_app/tests.py) | Test_stock_graph_no_stocks, test_invalid_stock_data and more |
| Using mock objects or any test doubles | [Link](https://github.com/CSCI-5828-S24/Fse-finalproject-Group20/blob/main/fin_app/tests.py) | Line 301 to 318 |
| Continuous integration | [Link]([(https://blog.pythonanywhere.com/87/)]) | Created a bare repo while deployment in pythonanywhere, wont show on github actions so attached link to the process followed |
| Production monitoring instrumenting | [Link](https://www.pythonanywhere.com/user/GullapalliMonica/webapps/#tab_id_gullapallimonica_pythonanywhere_com) | URL only accessible to developer, but images have been included in presentation for proof |
| Acceptance tests | [Link](https://github.com/CSCI-5828-S24/Fse-finalproject-Group20/blob/main/acceptance_tests/acc_tests.py) | Test_user_signup, test_user_login, test_user_logout using selenium |
| Event collaboration messaging | [Link](https://github.com/CSCI-5828-S24/Fse-finalproject-Group20/blob/main/financial_project/settings.py) | From line number 139-147 |
| Continuous delivery | [Link]([(https://blog.pythonanywhere.com/87/)]) | Created a bare repo while deployment in pythonanywhere, wont show on github actions so attached link to the process followed |
