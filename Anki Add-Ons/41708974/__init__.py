from aqt import mw
from PyQt5.QtWidgets import QAction, QMenu
from aqt.qt import *
from aqt.utils import showInfo, showWarning, tooltip, askUser

from os.path import dirname, join, realpath
import webbrowser
import requests
from bs4 import BeautifulSoup
import datetime
import hashlib
import json

from .Leaderboard import start_main
from .Setup import start_setup
from .Stats import Stats
from .config_manager import write_config
from .lb_on_homescreen import leaderboard_on_deck_browser
from .version import version
from .api_connect import connectToAPI

def Main():
	create_token()
	config = mw.addonManager.getConfig(__name__)
	if config["username"] == "":
		invoke_setup()
	else:
		mw.leaderboard = start_main(season_start, season_end, current_season)
		mw.leaderboard.show()
		mw.leaderboard.raise_()
		mw.leaderboard.activateWindow()

def invoke_setup():
	mw.lb_setup = start_setup(season_start, season_end)
	mw.lb_setup.show()
	mw.lb_setup.raise_()
	mw.lb_setup.activateWindow()

def config_setup():
	s = start_setup(season_start, season_end)
	if s.exec():
		pass

def github():
	webbrowser.open('https://github.com/ThoreBor/Anki_Leaderboard/issues')

def create_token():
	config = mw.addonManager.getConfig(__name__)
	if config["token"] == None:
		token = str(mw.col.db.list("SELECT id FROM revlog LIMIT 1"))
		token = hashlib.sha1(token.encode('utf-8')).hexdigest().upper()
		write_config("token", token)
	if "Leaderboard_Token_v3" not in mw.col.conf:
		mw.col.conf['Leaderboard_Token_v3'] = config["token"]

def check_info():
	config = mw.addonManager.getConfig(__name__)
	try:
		url = 'https://ankileaderboardinfo.netlify.app'
		page = requests.get(url, timeout=30)
		soup = BeautifulSoup(page.content, 'html.parser')
		if soup.find(id='show_message').get_text() == "True":
			info = soup.find("div", id="Message")
			notification_id = soup.find("div", id="id").get_text()
			if config["notification_id"] != notification_id:
				showInfo(str(info), title="Leaderboard")
				write_config("notification_id", notification_id)
	except:
		showWarning("Timeout error [check_info] - No internet connection, or server response took too long.", title="Leaderboard error")

def add_username_to_friendlist():
	config = mw.addonManager.getConfig(__name__)
	if config['username'] != "" and config['username'] not in config['friends']:
		friends = config["friends"]
		friends.append(config['username'])
		write_config("friends", friends)

def background_sync():
	create_token()
	config = mw.addonManager.getConfig(__name__)
	token = config["token"]
	streak, cards, time, cards_past_30_days, retention, league_reviews, league_time, league_retention, league_days_percent = Stats(season_start, season_end)

	if datetime.datetime.now() < season_end:
		data = {'Username': config['username'], "Streak": streak, "Cards": cards, "Time": time, "Sync_Date": datetime.datetime.now(),
		"Month": cards_past_30_days, "Country": config['country'].replace(" ", ""), "Retention": retention,
		"league_reviews": league_reviews, "league_time": league_time, "league_retention": league_retention, "league_days_percent": league_days_percent,
		"Token_v3": config["token"], "Version": version}
	else:
		data = {'Username': config['username'], "Streak": streak, "Cards": cards, "Time": time, "Sync_Date": datetime.datetime.now(),
		"Month": cards_past_30_days, "Country": config['country'].replace(" ", ""), "Retention": retention, "Update_League": False,
		"Token_v3": config["token"], "Version": version}

	x = connectToAPI("sync/", False, data, "Done!", "background_sync")
	if x.text == "Done!":
		tooltip("Synced leaderboard successfully.")
	
	if config["homescreen"] == True:
		write_config("homescreen_data", [])
		leaderboard_on_deck_browser()

def season():
	url = 'https://ankileaderboard.pythonanywhere.com/season/'
	try:
		season = requests.get(url, timeout=30).json()
		global season_start
		season_start = season[0]
		season_start = datetime.datetime(season_start[0],season_start[1],season_start[2],season_start[3],season_start[4],season_start[5])
		global season_end
		season_end = season[1]
		season_end = datetime.datetime(season_end[0],season_end[1],season_end[2],season_end[3],season_end[4],season_end[5])
		global current_season
		current_season = season[2]
	except:
		season_start = datetime.datetime.now()
		season_end = datetime.datetime.now()
		current_season = ""
		showWarning("Timeout error [season] - No internet connection, or server response took too long.", title="Leaderboard error")

def profileHook():
	check_info()
	config = mw.addonManager.getConfig(__name__)
	if config["autosync"] == True:
		gui_hooks.reviewer_will_end.append(background_sync)
	if config["homescreen"] == True:
		leaderboard_on_deck_browser()

def deleteHook(dialog, ids):
	config = mw.addonManager.getConfig(__name__)
	askUserDeleteAccount = """<h3>Deleting Leaderboard Account</h3>
	Keep in mind that deleting the add-on only removes the local files. Do you also want to delete your account (username, league history)?
	"""
	askUserCreateMetaBackup = """<h3>Leaderboard Configuration Backup</h3>
	If you want to reinstall this add-on in the future, creating a backup of the configurations is recommended. Do you want to create a backup?
	"""
	if "41708974" in ids or "Anki_Leaderboard" in ids:
		if askUser(askUserDeleteAccount):
			data = {'Username': config["username"], "Token_v3": config["token"]}
			x = connectToAPI("delete/", False, data, "Deleted", "deleteHook")
			if x.text == "Deleted":
				write_config("username", "")
				tooltip("Successfully deleted account.")
				write_config("token", None)
		if askUser(askUserCreateMetaBackup):
			config = mw.addonManager.getConfig(__name__)
			meta_backup = open(join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "leaderboard_meta_backup.json"), "w", encoding="utf-8")
			meta_backup.write(json.dumps({"config": config}))
			meta_backup.close()
			tooltip("Successfully created a backup")

def checkBackup():
	askUserRestoreFromBackup = """<h3>Leaderboard configuration backup found</h3>
	Do you want to restore your configurations?
	"""
	backup_path = join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "leaderboard_meta_backup.json")
	if os.path.exists(backup_path):
		meta_backup = open(backup_path, "r", encoding="utf-8")
		if askUser(askUserRestoreFromBackup):
			new_meta = open(join(dirname(realpath(__file__)), "meta.json"), "w", encoding="utf-8") 
			new_meta.write(json.dumps(json.loads(meta_backup.read())))
			new_meta.close()
			meta_backup.close()
		os.remove(backup_path)

def add_menu(Name, Button, exe, *sc):
	action = QAction(Button, mw)
	action.triggered.connect(exe)
	if not hasattr(mw, 'menu'):
		mw.menu = {}
	if Name not in mw.menu:
		add = QMenu(Name, mw)
		mw.menu[Name] = add
		mw.form.menubar.insertMenu(mw.form.menuTools.menuAction(), add)
	mw.menu[Name].addAction(action)
	for i in sc:
		action.setShortcut(QKeySequence(i))

try:
	from aqt import gui_hooks
	gui_hooks.profile_did_open.append(profileHook)
	try:
		# this hook will be implemented in Anki 2.1.45
		gui_hooks.addons_dialog_will_delete_addons.append(deleteHook)
	except:
		print("addons_dialog_will_delete_addon is not a hook yet")
except:
	config = mw.addonManager.getConfig(__name__)
	if config["import_error"] == True:
		showInfo("Because you're using an older Anki version some features of the Leaderboard add-on can't be used.", title="Leaderboard")
		write_config("import_error", False)

checkBackup()	
write_config("achievement", True)
write_config("homescreen_data", [])
add_username_to_friendlist()
season()

add_menu('&Leaderboard',"&Leaderboard", Main, 'Shift+L')
add_menu('&Leaderboard',"&Sync and update the home screen leaderboard", background_sync, "Shift+S")
add_menu('&Leaderboard',"&Config", invoke_setup, "Alt+C")
add_menu('&Leaderboard',"&Make a feature request or report a bug", github)
mw.addonManager.setConfigAction(__name__, config_setup)