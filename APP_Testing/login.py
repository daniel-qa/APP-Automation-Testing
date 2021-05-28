#!/usr/bin/python
# -*- coding: utf-8 -*-

#=== APP Unit Test ===
# Date    : 2021.05.28
# Program : login
# Author  : Habook daniel
#===========================

from time import sleep
from appium import webdriver
import unittest

#==============================
# function :login_function
# Parameter :	
#	driver->must given
def login_function(driver,wait_time=5,user_id="ac001",password="ac001"):
	ex=""
	try:
		#1/0  # for debug Error Case
		# Get Web Driver
		sleep(2)		
	
		# Login	
		if(1):
			# 輸入帳號
			id = user_id
			#id="qa001"
			appelement = driver.find_element_by_id('com.xxxx.xxxx:id/login_id_edit')
			appelement.send_keys(id)		
			# 輸入密碼
			pwd = password
			#pwd="qa001"
			appelement = driver.find_element_by_id('com.xxxx.xxxx:id/login_pwd_edit')
			appelement.send_keys(pwd)
			# 登入
			appelement = driver.find_element_by_id('com.xxxx.xxxx:id/login')
			appelement.click()
			sleep(wait_time)
		
			ret="OK"
	except Exception,ex:
		#print(Exception,":",ex)	
		ret="Fail"

	return ret,ex

	
#==============================
# function :get_driver_info
# Parameter : deviceName
#	retunr desired_caps[]
def get_driver_info(deviceName="LC57GYF00340"):
	ex=""
	
	try:	
		""" Default Device """
		""" HTC 820 """
		# 初始化資料
		desired_caps = {}
		# platformName
		desired_caps['platformName'] = 'Android'
		# platformVersion 系統版本
		desired_caps['platformVersion'] = '5.0.2'
		# deviceName 裝置名稱
		#desired_caps['deviceName'] = 'Android Emulator'
		desired_caps['deviceName'] = 'LC57GYF00340'
		# appPackage
		desired_caps['appPackage'] = 'com.xxxx.xxxx'
		#appActivity
		desired_caps['appActivity'] = 'SplashActivity'
		
		""" Other Device """
		""" IPHONE """
		if(deviceName=="IPHONE"):
			print "IPHONE"
			
		ret="OK"
	except Exception,ex:
		print(Exception,":",ex)	
		
	return desired_caps

if __name__== "__main__":
	print ("This is main function called")
	
	#if(0):
	#	# 初始化資料	
	#	desired_caps = {}
	#	# platformName
	#	desired_caps['platformName'] = 'Android'
	#	# platformVersion 系統版本
	#	desired_caps['platformVersion'] = '5.0.2'
	#	# deviceName 裝置名稱
	#	#desired_caps['deviceName'] = 'Android Emulator'
	#	desired_caps['deviceName'] = 'LC57GYF00340'
	#	# appPackage
	#	desired_caps['appPackage'] = 'com.xxxx.xxxx'
	#	#appActivity
	#	desired_caps['appActivity'] = 'SplashActivity'		
	#	driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)	

	if(1):		
		# WebDriver
		# 取得裝置資訊
		desired_caps = {}
		desired_caps = get_driver_info()
	
		driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		
		id ="qa001"
		pwd ="qa001"
		ret=login_function(driver=driver, user_id=id, password=pwd)	
		print("login_function : " + ret[0]+ "  " + str(ret[1]) )
		sleep(5)
		
