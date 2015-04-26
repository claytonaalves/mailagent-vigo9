#!/usr/bin/python
import sys
import MySQLdb
import logging
logging.basicConfig(filename='/tmp/mailagent.log',level=logging.CRITICAL)

remote_connection = MySQLdb.connect('mail_server', 'user', 'password', 'dbispconfig')

def insert_mail_account(email, password, quota):
    logging.info("Inserindo %s" % (email,))
    username = email.split('@')[0]
    maildir  = '/var/vmail/valesat.com/' + username
    # password                 : $1$HCE0myRy$A5otAiwEAwh6al6EpFNr30
    logging.info("%s %s" % (username, maildir,))

    query = """
        INSERT INTO mail_user (sys_userid, sys_perm_user, sys_perm_group, server_id, email, login, password, name, maildir, quota, homedir)
        VALUES (1, 'riud', 'riud', 1, %s, %s, %s, %s, %s, %s, '/var/vmail')
    """
    cursor = remote_connection.cursor()
    cursor.execute(query, (email, email, password, username, maildir, quota))

def update_mail_account(email, password, quota):
    username = email.split('@')[0]
    maildir  = '/var/vmail/valesat.com/' + username

    query = """
        UPDATE mail_user SET
           email=%s,
           login=%s,
           password=%s,
           name=%s,
           maildir=%s,
           quota=%s
        WHERE email=%s
    """
    cursor = remote_connection.cursor()
    cursor.execute(query, (email, email, password, username, maildir, quota, email))

def remove_mail_account(email):
    cursor = remote_connection.cursor()
    cursor.execute("DELETE FROM mail_user WHERE login=%s", (email, ))

param = sys.argv[1]
email = sys.argv[2]
password = sys.argv[3]
quota = sys.argv[4]

logging.info("%s %s" % (param, email))

if param=='ins':
    insert_mail_account(email, password, quota)
elif param=='upd':
    update_mail_account(email, password, quota)
elif param=='del':
    remove_mail_account(email)

remote_connection.commit()

