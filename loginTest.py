import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import HtmlTestRunner
import time
import random

def login(self):
        user = "jda136"
        password = "Nnahoj2310"
        elem = self.driver.find_element_by_id("username")
        elem.send_keys(user)
        elem = self.driver.find_element_by_id("password")
        elem.send_keys(password)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
def login_test(self):
    user = "ft131"
    password = "test21test#"
    elem = self.driver.find_element_by_id("username")
    elem.send_keys(user)
    elem = self.driver.find_element_by_id("password")
    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)
    time.sleep(2)


def addInstructor(self):
        instructor_list = self.driver.find_element_by_xpath("//*[@id='instructor-list']/a")
        instructor_list.click()
        self.driver.implicitly_wait(3)
        add_new_instructor = self.driver.find_element_by_xpath("//*[@id='example_wrapper']/div[1]/div/button")
        add_new_instructor.click()
        netid = self.driver.find_element_by_id("NetID")
        netid.send_keys("ft131")
        time.sleep(1)
        department = Select(self.driver.find_element_by_id("Department"))
        department.select_by_visible_text("01:160 - Chemistry")
        campus = Select(self.driver.find_element_by_id("Campus"))
        campus.select_by_visible_text("New Brunswick")
        status = Select(self.driver.find_element_by_id("FT/PT"))
        status.select_by_visible_text("Full Time")
        wait = WebDriverWait(self.driver, 10)
        add_instructor = wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='addNewInstructor']/div/div/form/div[2]/button[2]")))
        time.sleep(3)
        ActionChains(self.driver).move_to_element(add_instructor).click().perform()
        check = self.driver.find_element_by_xpath("//*[@id='maincontent']/div/div/div/div[1]/div/div/p")
        check_string = check.get_attribute("innerHTML")


def removeAccess(self):
        filter_users = self.driver.find_element_by_xpath("//div[@id='example_filter']/label/input")
        filter_users.send_keys("ft131")
      
        while(True):    
            row_count = len(self.driver.find_elements_by_xpath("//table[@id='example']/tbody/tr"))    
            if (row_count == 1):
                list_check = self.driver.find_element_by_xpath("//*[@id='example']/tbody/tr/td")
                string_list = list_check.get_attribute("innerText")
                if (string_list == "No matching records found"):
                    self.assertTrue 
                    break           
            delete = self.driver.find_element_by_xpath("//*[@id='example']/tbody/tr[1]/td[6]/a[2]/i")
            ActionChains(self.driver).move_to_element(delete).click().perform()
            delete_user = self.driver.find_element_by_xpath("//button[@class='btn btn-danger btn-ok']")
            time.sleep(5)
            ActionChains(self.driver).move_to_element(delete_user).click().perform()
            time.sleep(5)
            filter_users = self.driver.find_element_by_xpath("//div[@id='example_filter']/label/input")
            ActionChains(self.driver).move_to_element(filter_users).click().send_keys("ft131").perform()

def removeInstructor(self):
        instructor_list = self.driver.find_element_by_xpath("//*[@id='instructor-list']/a")
        instructor_list.click()
        self.driver.implicitly_wait(3)
        while(True): 
            filter_users = self.driver.find_element_by_id("instructor_search_netid")
            filter_users.send_keys("ft131")
            filter_users.send_keys(Keys.RETURN)
            time.sleep(3)   
            row_count = len(self.driver.find_elements_by_xpath("//*[@id='example']/tbody"))    
            if (row_count == 1):
                print("inside row_count")
                list_check = self.driver.find_element_by_xpath("//*[@id='example']/tbody/tr/td")
                string_list = list_check.get_attribute("innerText")
                print(string_list)
                if (string_list == "No data available in table"):
                    print("true")
                    self.assertTrue 
                    break

            try:               
                delete = self.driver.find_element_by_xpath("//*[@id='example']/tbody/tr[1]/td[7]/a[3]/i") 
            except NoSuchElementException:
                delete = self.driver.find_element_by_xpath("//*[@id='example']/tbody/tr/td[7]/a[2]/i")
            ActionChains(self.driver).move_to_element(delete).click().perform()
            delete_user = self.driver.find_element_by_xpath("//button[@class='btn btn-danger btn-ok']")
            time.sleep(5)
            ActionChains(self.driver).move_to_element(delete_user).click().perform()
            time.sleep(5)
            filter_users = self.driver.find_element_by_xpath("//div[@id='example_filter']/label/input")
            ActionChains(self.driver).move_to_element(filter_users).click().send_keys("ft131").perform()
def addSchOff(self):
        schoolOfficial = self.driver.find_element_by_xpath("//*[@id='enter-school-official']/a")
        schoolOfficial.click()
     
        self.driver.implicitly_wait(15)
        add = self.driver.find_element_by_xpath("//*[@id='example_wrapper']/div[1]/div/button")
        add.click()
        netid = self.driver.find_element_by_xpath("//*[@id='add_netid2']")
        netid.send_keys("jda136")
        school = Select(self.driver.find_element_by_id("add_school2"))
        school.select_by_visible_text("01 - School of Arts & Sciences")
        try:
            element = WebDriverWait(self.driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//*[@id='addNewUser']/div/div/form/div[2]/button[2]"))
        )
        except:
            print("timeoutError")
        time.sleep(5)
        add = self.driver.find_element_by_xpath("//*[@id='addNewUser']/div/div/form/div[2]/button[2]")
        ActionChains(self.driver).move_to_element(add).click().perform()
        time.sleep(2)
def delSO(self):
    time.sleep(1)
    schoolOfficial = self.driver.find_element_by_xpath("//*[@id='enter-school-official']/a")
    schoolOfficial.click()
    filter = self.driver.find_element_by_xpath("//*[@id='example_filter']/label/input")
    filter.send_keys("jda136")
    list_check = self.driver.find_element_by_xpath("//*[@id='example']/tbody/tr/td")
    string_list = list_check.get_attribute("innerText")
    if (string_list != "No matching records found"):
        delete = self.driver.find_element_by_xpath("//*[@id='example']/tbody/tr/td[5]/a[2]/i")
        delete.click()
        confirm = self.driver.find_element_by_xpath("//*[@id='deleteUserModal']/div/div/form/div/button[2]")
        confirm.click()
def addDep(self):
    schoolOfficial = self.driver.find_element_by_xpath("//*[@id='enter-school-official']/a")
    ActionChains(self.driver).move_to_element(schoolOfficial).click().perform()
    add_department = self.driver.find_element_by_xpath("//*[@id='example_wrapper']/div[1]/div/button")
    add_department.click()
    deptCode= self.driver.find_element_by_xpath("//*[@id='departmentcode2']")
    deptCode.send_keys("01:000")
    deptName = self.driver.find_element_by_xpath("//*[@id='departmentname2']")
    deptName.send_keys("test")
    time.sleep(4)
    add_department = self.driver.find_element_by_xpath("//*[@id='addNewUser']/div/div/form/div[2]/button[2]")
    ActionChains(self.driver).move_to_element(add_department).click().perform()

def delDep(self):
    department = self.driver.find_element_by_xpath("//*[@id='example']/tbody/tr[1]/td[2]")
    department_name = department.get_attribute("innerHTML")
    print("end of deldep")
    if (department_name == "test"):
        self.driver.implicitly_wait(30)
        delete = self.driver.find_element_by_xpath("//*[@id='example']/tbody/tr[1]/td[3]/a[2]/i")
        ActionChains(self.driver).move_to_element(delete).click().perform()
        time.sleep(2)
        delete2 = self.driver.find_element_by_xpath("//*[@id='deleteUserModal']/div/div/form/div/button[2]")
        delete2.click()
def fill_grid(self):
    #time.sleep(2)
        #time.sleep(2)
    for _ in range(random.randint(25,50)):
        
        row = random.randint(1,26)
        column = (random.randint(2,6))
        
        select = self.driver.find_element_by_xpath("//*[@id='form2']/table/tbody/tr[{}]/td[{}]/label".format(row,column))
        self.driver.execute_script("arguments[0].scrollIntoView(false);", select)
        time.sleep(0.5)
        ActionChains(self.driver).move_to_element(select).click(select).perform()
    #time.sleep(1)    
    save = self.driver.find_element_by_xpath("//*[@id='form2']/div/a")
    #time.sleep(.5)
    save.click()
def add_DA(self, name):
    time.sleep(1)
    user_access = self.driver.find_element_by_xpath("//*[@id='user-access']/a")
    user_access.click()
    add_user = self.driver.find_element_by_xpath("//button[@class='add-new-button w3-mobile w3-margin-left']")
    add_user.click()
    netid = self.driver.find_element_by_id("add_netid2")
    netid.send_keys(name)
    permission = Select(self.driver.find_element_by_id("add_permission2"))
    permission.select_by_visible_text("Departmental Approver")
    department = Select(self.driver.find_element_by_id("add_department2"))
    department.select_by_visible_text("01:160 - Chemistry")
    add_user = self.driver.find_element_by_xpath("//div[@id='addNewUser']//button[@class='btn btn-primary']")
    add_user.click()
def del_DA(self):
    time.sleep(1)
    user_access = self.driver.find_element_by_xpath("//*[@id='user-access']/a")
    user_access.click()
    filter = self.driver.find_element_by_xpath("//*[@id='example_filter']/label/input")
    filter.send_keys("jda136")
    garbage = self.driver.find_element_by_xpath("//*[@id='example']/tbody/tr[2]/td[6]/a[2]/i")
    garbage.click()
    delete = self.driver.find_element_by_xpath("//*[@id='deleteUserModal']/div/div/form/div/button[2]")
    delete.click()
        

class Login(unittest.TestCase):
    @classmethod
    def setUp(inst):
        # create a new sesson
        inst.driver = webdriver.Chrome()
        inst.driver.implicitly_wait(3)
        inst.driver.maximize_window()
        inst.driver.get("https://test-sis.rutgers.edu/instructor")
    
  

    def test_login(self):
        self.driver.get("https://test-sis.rutgers.edu/instructor")
        user = "jda136"
        password = "Nnahoj2310"
        elem = self.driver.find_element_by_id("username")
        elem.send_keys(user)
        elem = self.driver.find_element_by_id("password")
        elem.send_keys(password)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        with self.assertRaises(NoSuchElementException):
            element=self.driver.find_element_by_xpath("//*[@id='status']")
        
    @classmethod
    def tearDown(inst):
        # close the browser window
        inst.driver.quit()


class userAccess(unittest.TestCase):   
    @classmethod
    def setUp(self):
        # create a new sesson
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://test-sis.rutgers.edu/instructor")
        login(self)
        user_access = self.driver.find_element_by_xpath("//li[@id='user-access']/a")
        user_access.click()
        removeAccess(self)
    def test_administratorAccessA(self):
        add_user = self.driver.find_element_by_xpath("//button[@class='add-new-button w3-mobile w3-margin-left']")
        add_user.click()
        netid = self.driver.find_element_by_id("add_netid2")
        netid.send_keys("ft131")
        permission = Select(self.driver.find_element_by_id("add_permission2"))
        permission.select_by_visible_text("Administrator")
        #department = Select(self.driver.find_element_by_id("add_department2"))
        #department.select_by_visible_text("Chemistry")
        add_user = self.driver.find_element_by_xpath("//div[@id='addNewUser']//button[@class='btn btn-primary']")
        add_user.click()
        filter_users = self.driver.find_element_by_xpath("//div[@id='example_filter']/label/input")
        filter_users.send_keys("ft131")
        check = self.driver.find_element_by_xpath("//tbody/tr[@class='odd']/td[3]")
        self.assertEqual('ft131',check.get_attribute("innerHTML"))
     
    def test_administratorAccessDS(self):
        add_user = self.driver.find_element_by_xpath("//button[@class='add-new-button w3-mobile w3-margin-left']")
        add_user.click()
        netid = self.driver.find_element_by_id("add_netid2")
        netid.send_keys("ft131")
        permission = Select(self.driver.find_element_by_id("add_permission2"))
        permission.select_by_visible_text("Departmental Scheduler")
        department = Select(self.driver.find_element_by_id("add_department2"))
        department.select_by_visible_text("01:160 - Chemistry")
        add_user = self.driver.find_element_by_xpath("//div[@id='addNewUser']//button[@class='btn btn-primary']")
        add_user.click()
        filter_users = self.driver.find_element_by_xpath("//div[@id='example_filter']/label/input")
        filter_users.send_keys("ft131")
        check = self.driver.find_element_by_xpath("//tbody/tr[@class='odd']/td[3]")
        self.assertEqual('ft131',check.get_attribute("innerHTML"))
    def test_administratorAccessDA(self):
        add_DA(self,"ft131")
        filter_users = self.driver.find_element_by_xpath("//div[@id='example_filter']/label/input")
        filter_users.send_keys("ft131")
        check = self.driver.find_element_by_xpath("//tbody/tr[@class='odd']/td[3]")
        self.assertEqual('ft131',check.get_attribute("innerHTML"))

    def test_delete(self):
        removeAccess(self)
    @classmethod
    def tearDown(self):
        removeAccess(self)
        # close the browser window
        self.driver.quit()
class instructorList(unittest.TestCase):   
    @classmethod
    def setUp(self):
        # create a new sesson
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://test-sis.rutgers.edu/instructor")
        login(self)
        removeInstructor(self)
        
    def test_addNewInstructor(self):
        self.driver.implicitly_wait(3)
        for x in range(3):
            add_new_instructor = self.driver.find_element_by_xpath("//*[@id='example_wrapper']/div[1]/div/button")
            add_new_instructor.click()
            netid = self.driver.find_element_by_id("NetID")
            netid.send_keys("ft131")
            department = Select(self.driver.find_element_by_id("Department"))
            department.select_by_visible_text("01:160 - Chemistry")
            campus = Select(self.driver.find_element_by_id("Campus"))
            campus.select_by_index(x)
            status = Select(self.driver.find_element_by_id("FT/PT"))
            status.select_by_visible_text("Full Time")
            wait = WebDriverWait(self.driver, 10)
            add_instructor = wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='addNewInstructor']/div/div/form/div[2]/button[2]")))
            time.sleep(3)
            ActionChains(self.driver).move_to_element(add_instructor).click().perform()
            check = self.driver.find_element_by_xpath("//*[@id='maincontent']/div/div/div/div[1]/div/div/p")
            check_string = check.get_attribute("innerHTML")
            self.assertEqual("Successfully added Instructor [ ft131 - 01:160 ].", check_string," INSTRUCTOR NOT CREATED")
        
    @classmethod
    def tearDown(self):
        removeInstructor(self)
        # close the browser window
        self.driver.quit()


class instructorPreferences(unittest.TestCase):
    @classmethod
    def setUp(self):
        # create a new sesson
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get("https://test-sis.rutgers.edu/instructor")
        login(self)
        removeInstructor(self)
        addInstructor(self)
        instructorPreferences = self.driver.find_element_by_xpath("//*[@id='instructor-preference']/a")
        instructorPreferences.click()
        search = self.driver.find_element_by_xpath("//*[@id='instructor_search_netid']")
        search.send_keys("ft131")
        try:
            element = WebDriverWait(self.driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//*[@id='instructor_search']/fieldset/div[4]/input"))
        )
        except:
            print("timeoutError")

        search = self.driver.find_element_by_xpath("//*[@id='instructor_search']/fieldset/div[4]/input")
        ActionChains(self.driver).move_to_element(search).click().perform()
    
        preference = self.driver.find_element_by_xpath("//*[@id='example']/tbody/tr/td[7]/span/a")
        ActionChains(self.driver).move_to_element(preference).click().perform()
    #Make sure that preferences is set to no preferences or else test will brake
    def test_optionA(self):
        optionA= self.driver.find_element_by_xpath("//*[@id='maincontent']/div/div/div/div/div[3]/div/fieldset/div/div/nav/ul/li[1]/label")
        ActionChains(self.driver).move_to_element(optionA).click().perform()
        for _ in range(1,7):
            
            list_item = self.driver.find_element_by_xpath("//*[@id='period-option-a{}']".format(_))
            class_status = list_item.get_attribute("class") 
            print("click status", class_status)
           
            if (class_status == "checka checka1 highlight-selecta" ):
                print("condition satisfied")
                list_item = self.driver.find_element_by_xpath("//*[@id='frmOptionA']/ul/li[{}]/label".format(_))
                list_item.click()
  
            
        list_item = self.driver.find_element_by_xpath("//*[@id='frmOptionA']/ul/li[1]/label")
        list_item.click()



        submit = self.driver.find_element_by_xpath("//*[@id='submitOptionA']")
        submit.click()
        time.sleep(3)
        check_elem = self.driver.find_element_by_xpath("//*[@id='maincontent']/div/div/div/div[1]/div/div/p")
        check_string = check_elem.get_attribute("innerHTML")
        self.assertIn("Successfully updated instructor", check_string)
    def test_optionB(self):
        optionB = self.driver.find_element_by_xpath("//*[@id='maincontent']/div/div/div/div/div[3]/div/fieldset/div/div/nav/ul/li[2]/label")
        ActionChains(self.driver).move_to_element(optionB).click().perform()
        for _ in range(10):
            
            for x in range(1,random.randint(9,20)):
                column = random.randint(1,2)
                if column ==1:
                    row = random.randint(1,9)
                else:
                    row = random.randint(1,10)
                if column == 2:
                    check_index = 10+row-1
                else:
                    check_index = row
                print(column)
                print(row)

                list_item = self.driver.find_element_by_xpath("//*[@id='frmOptionC']/div[{}]/ul/li[{}]/label".format(column, row))
                selection_status = self.driver.find_element_by_xpath("//*[@id='period-option-c{}']".format(check_index))
                selection_status = selection_status.get_attribute("class")
                if (selection_status == "checkc checkc1 highlight-selectc"):
                    ActionChains(self.driver).move_to_element(list_item).click().perform()
                else:
                    x = x-1
            save = self.driver.find_element_by_xpath("//*[@id='submitOptionC']")
            self.driver.implicitly_wait(15)
            ActionChains(self.driver).move_to_element(save).click().perform()
            self.driver.implicitly_wait(15)
            check = self.driver.find_element_by_xpath("//*[@id='maincontent']/div/div/div/div[1]/div/div/p")
            self.assertEqual("Successfully updated instructor [ ft131 - FACULTY TEST21 ]",check.get_attribute("innerHTML"))
    @classmethod
    def tearDown(self):
        removeInstructor(self)
        # close the browser window
        self.driver.quit()

class schoolOfficial(unittest.TestCase):
    @classmethod
    def setUp(self):
        #create a new sesson
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get("https://test-sis.rutgers.edu/instructor")
        login(self)
        delSO(self)
    def test_addSO(self):
        addSchOff(self)
        check = self.driver.find_element_by_xpath("//*[@id='maincontent']/div/div/div/div[1]/div/div/p")
        self.assertEqual("Successfully added School Official [jda136 / 01].",check.get_attribute("innerHTML"))
    def test_delSO(self):
        addSchOff(self)
        delSO(self)
        check = self.driver.find_element_by_xpath("//*[@id='maincontent']/div/div/div/div[1]/div/div/p")
        self.assertEqual("Successfully deleted School Official [jda136 / 01].",check.get_attribute("innerHTML"))
    
    @classmethod
    def tearDown(self): 
        delSO(self)
        # close the browser window
        time.sleep(5)
        self.driver.quit()
class departmentList(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get("https://test-sis.rutgers.edu/instructor")
        login(self)
        dl = self.driver.find_element_by_xpath("//*[@id='department-list']/a")
        ActionChains(self.driver).move_to_element(dl).click().perform()
    def test_addD(self):
        addDep(self)
        check = self.driver.find_element_by_xpath("//*[@id='maincontent']/div/div/div/div[1]/div/div/p")
        check_string = check.get_attribute("innerHTML")
        self.assertEqual(check_string, "Successfully added new Department [01:000 - test].")
        delDep(self)
    def test_delD(self):
        addDep(self)
        delDep(self)
        check = self.driver.find_element_by_xpath("//*[@id='maincontent']/div/div/div/div[1]/div/div/p")
        check_string = check.get_attribute("innerHTML")
        self.assertEqual(check_string, "Successfully deleted Department [01:000].")
    @classmethod
    def tearDown(self): 
        # close the browser window
        self.driver.quit()
class systemSettings(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get("https://test-sis.rutgers.edu/instructor")
        login(self)
        systemSettings = self.driver.find_element_by_xpath("//*[@id='system-settings']/a")
        systemSettings.click()
    def test_semesterChange(self):
        currentSemester = Select(self.driver.find_element_by_id("semester-yearterm"))
        currentSemester.select_by_visible_text("Fall 2020")
        time.sleep(3)
        save = self.driver.find_element_by_xpath("//*[@id='settings-form']/fieldset/div[7]/input")
        save.click()
        time.sleep(1)
        check = self.driver.find_element_by_xpath("//*[@id='maincontent']/div/div/div/div[1]/div/div/p")
        self.assertEqual("Successfully updated system settings.", check.get_attribute("innerHTML"))
        currentSemester = Select(self.driver.find_element_by_id("semester-yearterm"))
        currentSemester.select_by_visible_text("Spring 2020")
        time.sleep(3)
        save = self.driver.find_element_by_xpath("//*[@id='settings-form']/fieldset/div[7]/input")
        save.click()
    def test_semesterDates(self):
        semesterDates = self.driver.find_element_by_id("semester-date")
        semesterDates.send_keys("01/20/2020 - 04/21/2020")
        save = self.driver.find_element_by_xpath("//*[@id='settings-form']/fieldset/div[7]/input")
        save.click()
        check = self.driver.find_element_by_xpath("//*[@id='maincontent']/div/div/div/div[1]/div/div/p")
        self.assertEqual("Successfully updated system settings.", check.get_attribute("innerHTML"))
        semesterDates = self.driver.find_element_by_id("semester-date")
        semesterDates.send_keys("01/20/2020 - 05/21/2020")
        save = self.driver.find_element_by_xpath("//*[@id='settings-form']/fieldset/div[7]/input")
        save.click()

    def test_instructorDates(self):
        instructorDates = self.driver.find_element_by_id("in-date")
        instructorDates.send_keys("03/01/2019 - 03/30/2019")
        save = self.driver.find_element_by_xpath("//*[@id='settings-form']/fieldset/div[7]/input")
        save.click()
        instructorDates = self.driver.find_element_by_id("in-date")
        instructorDates.send_keys("03/01/2019 - 04/30/2019")
        save = self.driver.find_element_by_xpath("//*[@id='settings-form']/fieldset/div[7]/input")
        save.click()
    def test_depSchedDates(self):
        depSchedDates = self.driver.find_element_by_id("ds-date")
        depSchedDates.send_keys("03/01/2019 - 03/30/2019")
        save = self.driver.find_element_by_xpath("//*[@id='settings-form']/fieldset/div[7]/input")
        save.click()
        depSchedDates = self.driver.find_element_by_id("ds-date")
        depSchedDates.send_keys("03/01/2019 - 04/30/2019")
        save = self.driver.find_element_by_xpath("//*[@id='settings-form']/fieldset/div[7]/input")
        save.click()
    def test_depAppDates(self):
        depAppDates = self.driver.find_element_by_id("da-date")
        depAppDates.send_keys("03/01/2019 - 03/30/2019")
        save = self.driver.find_element_by_xpath("//*[@id='settings-form']/fieldset/div[7]/input")
        save.click()
        depAppDates = self.driver.find_element_by_id("da-date")
        depAppDates.send_keys("03/01/2019 - 04/30/2019")
        save = self.driver.find_element_by_xpath("//*[@id='settings-form']/fieldset/div[7]/input")
        save.click()
    
    def test_SODates(self):
        depSchedDates = self.driver.find_element_by_id("so-date")
        depSchedDates.send_keys("03/01/2019 - 03/30/2019")
        save = self.driver.find_element_by_xpath("//*[@id='settings-form']/fieldset/div[7]/input")
        save.click()
        depSchedDates = self.driver.find_element_by_id("so-date")
        depSchedDates.send_keys("03/01/2019 - 04/30/2019")
        save = self.driver.find_element_by_xpath("//*[@id='settings-form']/fieldset/div[7]/input")
        save.click()
    @classmethod
    def tearDown(self):
        self.driver.close() 
        # close the browser window
class MedRelObligations(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get("https://test-sis.rutgers.edu/instructor")
        login(self)
        addSchOff(self)
        addInstructor(self)
    def test_MedRelObl(self):
        MedRelObl = self.driver.find_element_by_xpath("//*[@id='instructor-accommodation']/a")
        MedRelObl.click()
        netid = self.driver.find_element_by_xpath("//*[@id='instructor_search_netid']")
        netid.send_keys("ft131")
        search = self.driver.find_element_by_xpath("//*[@id='instructor_search']/fieldset/div[4]/input")
        search.click()
        accomodation = self.driver.find_element_by_xpath("//*[@id='example']/tbody/tr/td[7]/span[2]/a")
        accomodation.click()
        fill_grid(self)
        check = self.driver.find_element_by_xpath("//*[@id='maincontent']/div/div/div/div[1]/div/div/p")
        self.assertEqual("Successfully updated Instructor Accommodation [ft131 - NB].", check.get_attribute("innerHTML"))
    def tearDown(self):
        delSO(self)
        removeInstructor(self)
        self.driver.quit()
class DepObligations(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get("https://test-sis.rutgers.edu/instructor")
        login(self)
        add_DA(self, "jda136")
        addInstructor(self)
    def test_DepObl(self):
        page = self.driver.find_element_by_xpath("//*[@id='instructor-obligation']/a")
        time.sleep(1)
        page.click()
        netid = self.driver.find_element_by_xpath("//*[@id='instructor_search_netid']")
        netid.send_keys("ft131")
        search = self.driver.find_element_by_xpath("//*[@id='instructor_search']/fieldset/div[4]/input")
        search.click()
        obligation = self.driver.find_element_by_xpath("//*[@id='example']/tbody/tr/td[7]/span[2]/a")
        obligation.click()
        fill_grid(self)
        check = self.driver.find_element_by_xpath("//*[@id='maincontent']/div/div/div/div/div/div[1]/p/text()")
        self.assertEqual("Successfully updated instructor", check.get_attribute("innerHTML"))
    def tearDown(self):
        del_DA(self)
        removeInstructor(self)
        self.driver.quit()

        



html_report_dir = './html_report' 
if __name__ == '__main__':
  unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=html_report_dir))

