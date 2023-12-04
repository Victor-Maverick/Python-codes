print("--MAIN MENU--\n1. Phonebook\n2. Messages\n3. Chat\n4. Call register\n5. Tones\n6. Settings\n7. Call divert\n8. Games\n9. Calculator\n10. Reminders\n11. Clock\n12. Profiles\n13. SIM sevices\n");

selector = int(input('Select an option from 1-13: '))

match selector:
	case 1:
		print("Phone book\n1. Search\n2. Service Nos.\n3. Add name\n4. Erase\n5. Edit\n6. Assign tone\n7. Send b'card\n8. Options\n9. Speed dials\n10. Voice tags\n")
		phone = int(input("Enter a number from 1-10 to select an option"))
		match phone:
			case 1: 
				print("Search")
			case 2: 
				print("Service Nos")
			case 3: 
				print("Add name")
			case 4: 
				print("Erase")
			case 5: 
				print("Edit")
			case 6: 
				print("Assign tone")
			case 7: 
				print("Send b'card")
			case 8: 
				print("Options\n  1. Type of view\n  2. Memory status")
				options = int(input('select from options 1 and 2'))
				match options:
					case 1: 
						print('Type of view')
					case 2: 
						print('Memory status')
			case 9: 
				print('Speed dials')
			case 10:
				print('Voice tags')
	case 2:
		print("Messages\n1. Write messages\n2. Inbox\n3. Outbox\n4. Picture messages\n5. Templates\n6. Smileys\n7. Message settings\n8. Info Service\n9. Voice mailbox number\n10. Service command editor\n")
		messsage_selector = int(input('pick an option from 1 -10 to select '))
		match messsage_selector:
			case 1: 
				print("Write messages")
			case 2: 
				print("Inbox")
			case 3: 
				print("Outbox")
			case 4: 
				print("Picture messages")
			case 5: 
				print("Templates")
			case 6:
				print("Smileys")
			case 7:
				print("Message settings\n 1. Set\n2. Common\n")
				message_settings_selector=int(input("Enter 1 or 2 to select between the options: "))
				match message_settings_selector:
					case 1:
						print("Set\n 1. Message centre number\n 2. Message sent as\n3. Message validity");
						message_centre = int(input("choose from options 1-3: "))
						match message_centre:
							case 1:
								print('message center number')
							case 2: 
								print("Message sent as")
							case 3:
								print("Message validity")
				
					case 2:
						print("Coomon\n 1. Delivery reports\n 2. Reply via same centre\n 3. Character support\n")
						delivery_report = print("choose from options 1-3: ")
						match delivery_report:
							case 1:
								print("Delivery reports")
							case 2:
								print("Reply via same centre")
							case 3: 
								print("Character support")
			case 8:
				print("Info service")
			case 9:
				print("Voice mailbox number")
			case 10:
				print("Service command editor")
	case 3: 
		print("Chat")
	case 4:
		print("Call register\n 1.Missed calls\n 2.Received calls\n 3.Dialled numbers\n 4.Erase recent call lists\n 5.Show call duration\n 6.Show call costs\n 7.Call cost settings\n 8.Prepaid credit")
		call_register = int(input('Select an option from 1-8'))
		match call_register:
			case 1:
				print('Missed calls')
			case 2:
				print('Received calls')
			case 3:
				print('Dialled numbers')
			case 4:
				print('Erase recent call lists')
			case 5:
				print("Show call duration\n 1.Last call duration\n 2.All calls' duration\n 3.Received calls' duration\n 4.Dialled calls' duration\n 5.Clear timers\n")
				call_duration = int(input('pick an option from 1-5: '))
				match call_duration:
					case 1:
						print('Last call duration')
					case 2:
						print("All calls' duration")
					case 3:												print('Received calls\'s duration')
					case 4:
						print("Dialled calls' duration")
					case 5:
						print('Clear timers')
			case 6:
				print("Show call costs\n 1.Last call cost\n 2.All calls' cost\n 3.Clear counters")
				call_cost = int(input('pick an option from 1-3: '))
				match call_cost:
					case 1:
						print('Last call cost')
					case 2:
						print("All calls' cost")
					case 3:
						print("Clear counters")
			case 7:
				print('Call cost settings\n 1.Call cost limit\n 2.Show costs in\n')
				cost_settings = int(input('pick an option from 1-2: '))
				match cost_settings:
					case 1:
						print('Call cost limit')
					case 2:
						print("Show costs in")
			case 8:
				print('Prepaid credit')

	case 5:
		print("Tones\n 1.Ringing tone\n 2. Ringing volume\n 3.Incoming call alert\n 4.Composer\n 5.Message alert tone\n 6.Keypad tones\n 7.Warning and game tones\n 8.Vibrating alert\n 9.Screen saver\n")
		tones = int(input('pick an option from 1-9: '))
		match tones:
			case 1:
				print('Ringing tone')
			case 2:
				print("Ringing volume")		
			case 3:
				print("Incoming call alert")
			case 4:
				print("Composer")
			case 5:
				print('Message alert tone')
			case 6:
				print('Keypad tones')
			case 7:
				print("Warning and game tones")		
			case 8:
				print("Vibrating alert")
			case 9:
				print("Screen saver")
	case 6:
		print("Settings\n 1.Call settings\n 2.Phone settings\n 3.Security settings\n 4. Restore factory settings\n")
		settings = int(input('pick an option from 1-4: '))
		match settings:
			case 1:
				print('Call settings\n 1.Automatic redial\n 2.Speed dialling\n 3.Call waiting options\n 4.Own number sending\n 5.Phone line in use\n 6.Automatic answer\n')
				call_settings = int(input('pick an option from 1-6: '))
				match call_settings:
					case 1:
						print('Automatic redial')
					case 2:
						print("Speed dialling")		
					case 3:
						print("Call waiting options")
					case 4:
						print("Own number sending")
					case 5:
						print('Phone line in use')
					case 6:
						print('Automatic answer')
			case 2:
				print('Phone settings\n 1.Language\n 2.Cell info display\n 3.Welcome info display\n 4.Network selection\n 5.Lights\n 6.Confirm SIM service actions\n')
				phone_settings = int(input('select an option from 1-6: '))
				match phone_settings:
					case 1:
						print('Language')
					case 2:
						print("Cell info display")		
					case 3:
						print("Welcome info display")
					case 4:
						print("Network selection")
					case 5:
						print('Lights')
					case 6:
						print('Confirm SIM service actions')
			case 3:
				print('Security settings\n 1.PIN code request\n 2.Call barring service\n 3.Fixed dialling\n 4.Closed user group\n 5.Phone security\n 6.Change access codes\n')
				phone_settings = int(input('select an option from 1-6: '))
				match phone_settings:
					case 1:
						print('PIN code request')
					case 2:
						print("Call barring service")		
					case 3:
						print("Fixed dialling")
					case 4:
						print("Closed user group")
					case 5:
						print('Phone security')
					case 6:
						print('Change access codes')
			case 4:
				print("Restore factory settings")
	
	case 7:
		print('Call divert')
	case 8:
		print('Games')
	case 9:
		print('Calculator')
	case 10:
		print('Reminders')
	case 11:
		print('Clock\n 1.Alarm clock\n 2.Clock settings\n 3.Date settings\n Stopwatch\n Countdown timer\n 6.Auto update of date and time\n')
		clock_selector = int(input('Select an option from 1-6: '))
		match clock_selector:
			case 1:
				print('Alarm clock')
			case 2:
				print('Clock settings')
			case 3:
				print('Date settings')
			case 4: 
				print('Stopwatch')
			case 5:
				print('Countdown timer')
			case 6:
				print('Auto update date and time')
	case 12:
		print('Profiles')
	case 13:
		print('SIM services')				