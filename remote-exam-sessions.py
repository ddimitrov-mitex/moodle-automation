#!/usr/bin/python3

# installation:
# install geckodriver
# pip3 install -r requirements.txt

import time
import os
import datetime
import csv
from selenium.webdriver.support.ui import Select

from selenium import webdriver
driver = webdriver.Firefox()


# parameters
moodle_course_id = "5927"
week_number = 15
exam_title = "Контролно"


if os.path.exists("geckodriver.log"):
	os.remove("geckodriver.log")


# open moodle and sign in
driver.get("https://learn.fmi.uni-sofia.bg/")
driver.find_element_by_link_text("Вход").click()
time.sleep(12) # just manually enter the credentials and press Enter
driver.get("https://learn.fmi.uni-sofia.bg/course/view.php?id=" + moodle_course_id)
driver.find_element_by_xpath('//button[normalize-space()="Включи редактирането"]').click()
with open('remote-exam-students.csv', newline='') as f: # CSV with two columns: name and f.n., without header row
	reader = csv.reader(f)
	for row in reader:
		time.sleep(1.5)
		student_name = row[0]
		fn = row[1]
		print(str(fn) + " " + student_name)
		driver.find_elements_by_class_name("addresourcemodchooser")[week_number - 1].find_element_by_tag_name("a").click() # TODO frequent crashes
		driver.find_element_by_id("item_bigbluebuttonbn").click()
		driver.find_element_by_name("submitbutton").click()
		driver.find_element_by_id("id_name").send_keys(exam_title + " - " + str(fn))
		# TODO description
		# driver.find_element_by_link_text("Показване повече...").click()
		driver.find_element_by_link_text("Participants").click()
		userTypes = Select(driver.find_element_by_id("bigbluebuttonbn_participant_selection_type"))
		driver.find_element_by_link_text("Participants").click() # ???
		userTypes.select_by_visible_text("User")
		users = Select(driver.find_element_by_id("bigbluebuttonbn_participant_selection"))
		time.sleep(0.5)
		users.select_by_visible_text(student_name) # TODO duplicate students names; TODO non-existing names
		driver.find_element_by_id("id_addselectionid").click()
		driver.find_element_by_css_selector("#participant_list_tr_all-all .fa-trash").click()
		driver.find_element_by_link_text("Ограничаване на достъпа").click()
		driver.find_element_by_xpath('//button[normalize-space()="Добавяне на ограничение..."]').click()
		driver.find_element_by_xpath('//button[normalize-space()="Потребителски профил"]').click()
		restrictions = Select(driver.find_element_by_name("field"))
		restrictions.select_by_visible_text("Факултетен номер")
		driver.find_element_by_css_selector("input[title='Value to compare against']").send_keys(str(fn))
		driver.find_element_by_css_selector('input[value="Запазване и връщане в курса"]').click()

