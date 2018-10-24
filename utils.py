#!/usr/bin/env python3

import sqlite3

db = sqlite3.connect('hibp.db')

def friendlyView(data, email):
    print("******************************************")
    print("Have I Been Pwned Report for %s:" % email)
    for item in data:
        print("Name of Breach: %s" % item['Name'])
        print("Title: %s" % item["Title"])
        print("Domain: %s" % item["Domain"])
        print("Breach Date: %s" % item["BreachDate"])
        print("Added Date: %s" % item["AddedDate"])
        print("Modified Date: %s" % item["ModifiedDate"])
        print("PwnCount: %s" % item["PwnCount"])
        print("Description: %s" % item["Description"])
        for lines in item["DataClasses"]:
            print("Data Includes: %s" % lines)
        print("Verified? " + str(item["IsVerified"]))
        print("Fabricated? " + str(item["IsFabricated"]))
        print("Sensitive? " + str(item["IsSensitive"]))
        print("Retired? " + str(item["IsRetired"]))
        print("Spam List? " + str(item["IsSpamList"]))
        print("----------------------------------")
    print("****************************************")

def friendlyBreachView(data, name):
    print("******************************************")
    print("Have I Been Pwned Report for %s:" % name)
    print("Name of Breach: %s" % data['Name'])
    print("Title: %s" % data["Title"])
    print("Domain: %s" % data["Domain"])
    print("Breach Date: %s" % data["BreachDate"])
    print("Added Date: %s" % data["AddedDate"])
    print("Modified Date: %s" % data["ModifiedDate"])
    print("PwnCount: %s" % data["PwnCount"])
    print("Description: %s" % data["Description"])
    for lines in data["DataClasses"]:
        print("Data Includes: %s" % lines)
    print("Verified? " + str(data["IsVerified"]))
    print("Fabricated? " + str(data["IsFabricated"]))
    print("Sensitive? " + str(data["IsSensitive"]))
    print("Retired? " + str(data["IsRetired"]))
    print("Spam List? " + str(data["IsSpamList"]))
    print("----------------------------------")
    print("****************************************")

def setupDatabase():
    c = db.cursor()
    c.execute('''CREATE TABLE breaches (name text, title text, domain text, breachDate text, addedDate text, modifiedDate text, pwnCount integer, description text, dataClasses text, verified numeric, fabricated numeric, sensitive numeric, retired numeric, spamList numeric)
    ''')
    c.execute('''CREATE TABLE users (id text, firstName text, lastName text, email text, company text, active numeric)
    ''')
    c.execute('''CREATE TABLE findings (id text, email text, breach text)
    ''')
    db.commit()

def addCustomerInfo(id, first, last, email, company, active):
    c = db.cursor()
    c.execute("INSERT INTO users VALUES (%s, %s, %s, %s, %s, %i)" % (id, first, last, email, company, active))
    db.commit()

def addFindingRecord(id, email, breach):
    c = db.cursor()
    c.execute("INSERT INTO findings VALUES (%s, %s, %s) " % (id, email, breach))
    db.commit()

def addBreach(name, title, domain, breachDate, addedDate, modifiedDate, pwnCount, description, dataClasses, verified, fabricated, sensitive, retired, spamList):
    c = db.cursor()
    c.execute("INSERT INTO breaches VALUES(%s, %s, %s, %s, %s, %s, %i, %s, %s, %i, %i, %i, %i, %i)" % (name, title, domain, breachDate, addedDate, modifiedDate, pwnCount, description, dataClasses, verified, fabricated, sensitive, retired, spamList))
    db.commit()

def customerByName(first, last):
    c = db.cursor()
    dbObject = c.execute("SELECT email FROM users WHERE firstName='%s' AND lastName='%s'" % (first, last))
    data = dbObject.fetchall()
    return data

def customersByCompany(company):
    c = db.cursor()
    dbObject = c.execute("SELECT email FROM users WHERE company='%s'" % company)
    data = dbObject.fetchall()
    return data

def allCustomers():
    c = db.cursor()
    dbObject = c.execute("SELECT email FROM users WHERE active='1'")
    data = dbObject.fetchall()
    # the fetchall returns a tuple full of email addresses
    return data

def checkBreachesByUser():
    c = db.cursor()
    dbObject = c.execute("SELECT * FROM breaches")
    data = dbObject.fetchall()
    return data

def friendlyViewBreachesByUser(data):
    pass
