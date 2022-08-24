#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe

	
@frappe.whitelist(allow_guest=True)
def read_acc22():
	import csv
	with open('/home/slnee/bench/apps/erpnext/erpnext/roya/royaa.csv', 'r') as csvfile:
		spamreader = csv.reader(csvfile)
		index=0
		for row in spamreader:
			if row[1]:
				parent_account=None
				#is_group = 0
				root_type=""
				#par=None
				#index+=1
				print (row[1])
				print (row[1][0])
				print ("**********")
				if(row[2]=="Asset"):
					root_type="Asset"
				if(row[2]=="Liability"):
					root_type="Liability"
				if(row[2]=="Owner's Equity"):
					root_type="Equity"
				if(row[2]=="Revenue"):
					root_type="Income"
				if(row[2]=="Expense"):
					root_type="Expense"
				#print row[0][0]
				print (root_type)
				print (index)
				index +=1
				exi=frappe.get_all("Account" , ['name'],filters={"account_name":(row[0].strip()).decode('utf-8'),"company":"مصنع رويا للمنتجات الغذائية"})
				if exi:
					print("Exi")
					continue

				
				parent=frappe.get_all("Account" , ['name'],filters={"account_name":(row[1].strip()).decode('utf-8'),"company":"مصنع رويا للمنتجات الغذائية"})
				if parent:
					print (parent[0].name)
					parent_account = parent[0].name
				dd = frappe.get_doc({"doctype":"Account",
						"account_name":(row[0].strip()).decode('utf-8'),
						 "is_group ":  0,
						 "account_serial" : 0,
						 "root_type": root_type,
						 "parent_account" : parent_account,
						 "company" :"مصنع رويا للمنتجات الغذائية"
						 })
				dd.flags.ignore_mandatory = True
				dd.ignore_validate = True
				dd.save(ignore_permissions = True)
				frappe.db.sql(""" update  `tabAccount` set is_group ='{0}' where name = '{1}'""".format(1,dd.name))
			 	frappe.db.commit()
